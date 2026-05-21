"""
Newsletter AI personale — Variante 2 (Anthropic API + parsing HTML/RSS)

Scarica HTML/RSS delle fonti, estrae articoli con BeautifulSoup/feedparser,
manda a Claude API solo il testo pulito per il riassunto, salva il markdown.

Uso:
    python newsletter.py

Schedulazione: vedi scheduling/crontab-example.txt
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import feedparser
import requests
from anthropic import Anthropic
from bs4 import BeautifulSoup
from dotenv import load_dotenv


ROOT = Path(__file__).parent
NEWSLETTER_DIR = ROOT / "newsletter"
TIMEOUT = 15
MAX_TEXT_CHARS = 8000
ARTICLE_DATE_WINDOW_HOURS = 48

EMOJI_BY_CATEGORY = {
    "product": "🚀",
    "research": "📄",
    "changelog": "🔧",
    "tech": "🆕",
}


def extract_articles(fonte: dict) -> list[dict]:
    """Ritorna una lista di {title, url, category} per la fonte data."""
    if fonte["tipo"] == "rss":
        feed = feedparser.parse(fonte["url"])
        return [
            {"title": e.title, "url": e.link, "category": fonte["categoria"]}
            for e in feed.entries[:20]
        ]

    if fonte["tipo"] == "html":
        html = requests.get(fonte["url"], timeout=TIMEOUT).text
        soup = BeautifulSoup(html, "html.parser")
        seen = set()
        out = []
        for a in soup.select(fonte["selettore_articolo"]):
            href = a.get("href")
            if not href or href in seen:
                continue
            seen.add(href)
            full_url = urljoin(fonte["url"], href)
            out.append({"title": a.get_text(strip=True), "url": full_url, "category": fonte["categoria"]})
            if len(out) >= 20:
                break
        return out

    return []


def summarize_article(client: Anthropic, articolo: dict, system_prompt: str, model: str) -> str | None:
    """Scarica il full text dell'articolo e chiede a Claude di riassumere. Ritorna i bullet markdown o None se SKIP."""
    try:
        html = requests.get(articolo["url"], timeout=TIMEOUT).text
    except requests.RequestException as e:
        print(f"   ⚠️  fetch fallito per {articolo['url']}: {e}", file=sys.stderr)
        return None

    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)[:MAX_TEXT_CHARS]
    if not text.strip():
        return None

    msg = client.messages.create(
        model=model,
        max_tokens=400,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Titolo: {articolo['title']}\n\nContenuto:\n{text}",
            }
        ],
    )
    body = msg.content[0].text.strip()
    if body.upper().startswith("SKIP"):
        return None
    return body


def compose_newsletter(today: str, summaries: list[dict]) -> str:
    """Compone il markdown finale della newsletter."""
    nice_date = datetime.now().strftime("%A %d %B %Y")
    if not summaries:
        return (
            f"# 🧠 La tua AI Brief — {nice_date}\n\n"
            f"Nessuna novità rilevante oggi.\n"
        )

    parts = [f"# 🧠 La tua AI Brief — {nice_date}\n", f"## {len(summaries)} novità di oggi\n"]
    for s in summaries:
        emoji = EMOJI_BY_CATEGORY.get(s["category"], "🆕")
        parts.append(f"### {emoji} {s['title']}\n{s['summary']}\n- 🔗 {s['url']}\n")
    return "\n".join(parts)


def main() -> int:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or "XXXX" in api_key:
        print("❌ ANTHROPIC_API_KEY non configurata in .env", file=sys.stderr)
        return 1

    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-7")
    client = Anthropic(api_key=api_key)

    fonti = json.loads((ROOT / "fonti.json").read_text(encoding="utf-8"))["fonti"]
    state = json.loads((ROOT / "state.json").read_text(encoding="utf-8"))
    system_prompt = (ROOT / "prompt.txt").read_text(encoding="utf-8")
    visti = set(state.get("articoli_visti", []))

    NEWSLETTER_DIR.mkdir(exist_ok=True)
    oggi = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    inizio = time.time()
    print(f"🚀 Avvio newsletter per {oggi}")

    summaries: list[dict] = []
    processati: list[str] = []
    scartati = 0

    for fonte in fonti:
        print(f"📖 {fonte['nome']}...")
        articoli = extract_articles(fonte)
        nuovi = [a for a in articoli if a["url"] not in visti]
        for art in nuovi[:5]:  # cap a 5 articoli/fonte per non esagerare con i token
            processati.append(art["url"])
            summary = summarize_article(client, art, system_prompt, model)
            if summary:
                summaries.append({**art, "summary": summary})
            else:
                scartati += 1

    output = compose_newsletter(oggi, summaries)
    out_path = NEWSLETTER_DIR / f"{oggi}.md"
    out_path.write_text(output, encoding="utf-8")

    state["articoli_visti"] = list(visti | set(processati))
    state["ultimo_run"] = datetime.now(timezone.utc).isoformat()
    (ROOT / "state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    durata = time.time() - inizio
    print(f"\n✅ Newsletter generata: {out_path}")
    print(f"   - {len(fonti)} fonti consultate")
    print(f"   - {len(processati)} articoli letti")
    print(f"   - {len(summaries)} articoli inclusi")
    print(f"   - {scartati} articoli scartati")
    print(f"   - {durata:.1f} secondi totali")

    return 0


if __name__ == "__main__":
    sys.exit(main())
