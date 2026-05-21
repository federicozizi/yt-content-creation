"""
team_agenti.py — Team di agenti AI competitor-intel

Lancia 3 watcher in parallelo (pricing, features, social) usando asyncio.gather,
poi un synthesizer che aggrega i risultati e produce un brief markdown.
Ogni watcher usa Playwright per scrapare le pagine competitor, poi passa
il contenuto reale a Claude per l'analisi.
Salva il brief in briefs/YYYY-MM-DD.md e lo invia via email.

Uso: python team_agenti.py

Dipendenze: anthropic, python-dotenv, playwright (vedi requirements.txt)
Credenziali: file .env con ANTHROPIC_API_KEY, GMAIL_USER, GMAIL_APP_PASSWORD, BRIEF_RECIPIENT
"""

import asyncio
import json
import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from anthropic import AsyncAnthropic
from dotenv import load_dotenv
from playwright.async_api import async_playwright

# ---- Setup ----
load_dotenv(override=True)
ROOT = Path(__file__).resolve().parent
BRIEFS_DIR = ROOT / "briefs"
PROMPTS_DIR = ROOT / "prompts"
CONFIG_PATH = ROOT / "competitors.json"

ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
GMAIL_USER = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
BRIEF_RECIPIENT = os.environ["BRIEF_RECIPIENT"]

client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

ROLE_URL_FIELDS = {
    "pricing": ["pricing_url", "website"],
    "features": ["blog_url"],
    "social": ["linkedin_url", "blog_url"],
}

STEALTH_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)


# ---- Helpers ----
def log(role: str, msg: str) -> None:
    from datetime import datetime
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {role:12s} -> {msg}", flush=True)


def load_config() -> dict:
    competitors = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))["competitors"]
    prompts = {}
    for role in ("pricing", "features", "social", "synthesizer"):
        prompts[role] = (PROMPTS_DIR / f"{role}.txt").read_text(encoding="utf-8")
    return {"competitors": competitors, "prompts": prompts}


# ---- Scraping con Playwright ----
async def create_stealth_context(browser):
    """Crea un browser context con user-agent e impostazioni realistiche."""
    return await browser.new_context(
        user_agent=STEALTH_USER_AGENT,
        viewport={"width": 1920, "height": 1080},
        locale="it-IT",
        timezone_id="Europe/Rome",
        extra_http_headers={
            "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        },
    )


async def scrape_page(context, url: str, timeout_ms: int = 30000) -> str:
    """Apre una pagina con Playwright, aspetta il caricamento, restituisce il testo visibile."""
    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
        await page.wait_for_timeout(3000)
        text = await page.inner_text("body")
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        truncated = "\n".join(lines[:300])
        return truncated
    except Exception as e:
        return f"[ERRORE SCRAPING: {e}]"
    finally:
        await page.close()


def is_usable_content(text: str, url: str = "") -> bool:
    """Controlla che il contenuto scraped sia utilizzabile (non login wall, CAPTCHA, ecc.)."""
    if not text or text.startswith("[ERRORE SCRAPING"):
        return False
    low = text.lower()
    login_signals = ["sign in", "log in", "forgot password", "join now", "captcha"]
    hits = sum(1 for s in login_signals if s in low)
    if hits >= 2:
        return False
    if "linkedin.com" in url and "posted this" not in low and "reactions" not in low:
        return False
    return True


async def scrape_with_fallback(context, competitor: dict, url_fields: list) -> tuple:
    """Prova gli URL in ordine, restituisce (contenuto, url_usato, fonte)."""
    for field in url_fields:
        url = competitor.get(field, "")
        if not url:
            continue
        content = await scrape_page(context, url)
        if is_usable_content(content, url):
            return content, url, field
    return "[NESSUN CONTENUTO DISPONIBILE]", "", "nessuna"


async def scrape_competitors(context, role: str, competitors: list) -> dict:
    url_fields = ROLE_URL_FIELDS[role]
    tasks = [scrape_with_fallback(context, comp, url_fields) for comp in competitors]
    results = await asyncio.gather(*tasks)
    out = {}
    for comp, (content, url, source) in zip(competitors, results):
        out[comp["name"]] = {"content": content, "url": url, "source": source}
    return out


NO_HALLUCINATION_RULE = (
    "\n\n## REGOLA CRITICA — ZERO ALLUCINAZIONI\n"
    "Basa la tua analisi ESCLUSIVAMENTE sul testo scraped fornito sopra.\n"
    "- Se il contenuto e' '[NESSUN CONTENUTO DISPONIBILE]', scrivi '[dati non disponibili]'.\n"
    "- Se il contenuto non contiene informazioni pertinenti al tuo ruolo, scrivi '[dati non disponibili]'.\n"
    "- NON INVENTARE MAI: prezzi, nomi di piani, titoli di post, date di pubblicazione, "
    "numeri di reazioni/like, metriche finanziarie (revenue, GMV, utenti), o qualsiasi altro dato numerico.\n"
    "- Se la fonte e' un blog (non LinkedIn), NON riportare conteggi di reazioni o engagement.\n"
    "- Ogni fatto che riporti DEVE essere rintracciabile nel testo scraped sopra. "
    "Se non lo trovi li', non lo scrivi.\n"
    "- Un report con 3 righe vere vale piu' di un report pieno di dati inventati."
)


# ---- Watcher (scraping + chiamata Claude) ----
async def watcher(context, role: str, system_prompt: str, competitors: list) -> str:
    log(role, f"scraping {len(competitors)} competitor...")
    scraped = await scrape_competitors(context, role, competitors)

    scraped_block = ""
    for name, data in scraped.items():
        source_label = f" (fonte: {data['url']})" if data['url'] else ""
        if data['source'] != ROLE_URL_FIELDS[role][0] and data['url']:
            source_label += f" [fallback da {data['source']}]"
        scraped_block += f"\n### {name}{source_label}\n{data['content']}\n"

    log(role, f"scraping OK -> analisi con Claude...")
    user_message = (
        "Ecco la lista dei competitor da analizzare in formato JSON:\n\n"
        f"{json.dumps(competitors, ensure_ascii=False, indent=2)}\n\n"
        "Ed ecco il contenuto reale delle loro pagine web, estratto oggi:\n"
        f"{scraped_block}"
        f"{NO_HALLUCINATION_RULE}\n\n"
        "Analizza il contenuto reale estratto e procedi seguendo le istruzioni del tuo system prompt."
    )
    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    findings = response.content[0].text
    log(role, f"{len(competitors)} competitor processati OK")
    return findings


# ---- Synthesizer (chiamata Claude finale che aggrega i findings) ----
async def synthesizer(system_prompt: str, findings: dict) -> str:
    log("synthesizer", "in elaborazione...")
    today = date.today().strftime("%-d %B %Y") if os.name != "nt" else date.today().strftime("%#d %B %Y")
    user_message = (
        f"Data di oggi: {today}\n\n"
        "Ti passo i 3 findings dei watcher. Produci il brief unificato seguendo le istruzioni del tuo system prompt.\n\n"
        "## FINDINGS — pricing\n"
        f"{findings['pricing']}\n\n"
        "## FINDINGS — features\n"
        f"{findings['features']}\n\n"
        "## FINDINGS — social\n"
        f"{findings['social']}\n"
    )
    response = await client.messages.create(
        model="claude-opus-4-7",
        max_tokens=2048,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    brief = response.content[0].text
    today_iso = date.today().isoformat()
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    brief_path = BRIEFS_DIR / f"{today_iso}.md"
    brief_path.write_text(brief, encoding="utf-8")
    log("synthesizer", f"brief scritto in briefs/{today_iso}.md OK")
    return brief


# ---- Invio email via SMTP Gmail ----
def send_email(brief: str) -> None:
    log("email", f"invio a {BRIEF_RECIPIENT}...")
    today = date.today().strftime("%d/%m/%Y")
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Brief competitor {today}"
    msg["From"] = GMAIL_USER
    msg["To"] = BRIEF_RECIPIENT
    msg.attach(MIMEText(brief, "plain", "utf-8"))
    msg.attach(MIMEText(f"<pre>{brief}</pre>", "html", "utf-8"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
    log("email", f"inviata a {BRIEF_RECIPIENT} OK")


# ---- Main async ----
async def main() -> None:
    cfg = load_config()
    competitors = cfg["competitors"]
    prompts = cfg["prompts"]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await create_stealth_context(browser)

        # ===== Fan-out parallelo =====
        pricing_md, features_md, social_md = await asyncio.gather(
            watcher(context, "pricing", prompts["pricing"], competitors),
            watcher(context, "features", prompts["features"], competitors),
            watcher(context, "social", prompts["social"], competitors),
        )

        await context.close()
        await browser.close()

    findings = {
        "pricing": pricing_md,
        "features": features_md,
        "social": social_md,
    }

    # ===== Synthesizer (sequenziale, dopo i 3 watcher) =====
    brief = await synthesizer(prompts["synthesizer"], findings)

    # ===== Invio email =====
    send_email(brief)


if __name__ == "__main__":
    asyncio.run(main())
