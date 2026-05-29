"""
Orchestrator del calendario editoriale.

Cosa fa:
1. Esegue i 10 scraper in parallelo (ThreadPoolExecutor)
2. Aggrega i risultati in dashboard.html
3. Apre la dashboard nel browser di default

Uso:
    python orchestrator.py

Questo script funziona da SOLO (senza Claude / senza API key) e produce una
dashboard con tutti i trend grezzi.

Per la versione "Dynamic Workflows" con sintesi AI (10 sub-agenti Claude
in parallelo, ognuno che sintetizza idee video dalla propria piattaforma):
vedi CLAUDE.md e ROUTINE.md. La routine schedulata di Claude esegue quel ciclo.
"""
import json
import subprocess
import sys
import webbrowser
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRAPERS_DIR = ROOT / "scrapers"
OUTPUT_DIR = ROOT / "output"
DASHBOARD = ROOT / "dashboard.html"

SCRAPERS = [
    ("hackernews", "Hacker News"),
    ("reddit", "Reddit r/artificial"),
    ("devto", "Dev.to"),
    ("producthunt", "Product Hunt"),
    ("medium", "Medium"),
    ("github_trending", "GitHub Trending"),
    ("lobsters", "Lobste.rs"),
    ("youtube_ai", "YouTube (AI channels)"),
    ("google_news", "Google News IT"),
    ("huggingface_papers", "Hugging Face Papers"),
]


def run_scraper(name: str) -> tuple[str, int, str]:
    script = SCRAPERS_DIR / f"{name}.py"
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(SCRAPERS_DIR),
            capture_output=True,
            text=True,
            timeout=45,
        )
        out = (proc.stdout + proc.stderr).strip().splitlines()
        last = out[-1] if out else ""
        # ottieni count dal file JSON appena scritto
        json_path = OUTPUT_DIR / f"{name}.json"
        if json_path.exists():
            count = json.loads(json_path.read_text(encoding="utf-8")).get("count", 0)
        else:
            count = 0
        return name, count, last
    except Exception as exc:
        return name, 0, f"ERRORE: {exc}"


def load_all() -> list[dict]:
    blocks = []
    for slug, label in SCRAPERS:
        json_path = OUTPUT_DIR / f"{slug}.json"
        if not json_path.exists():
            blocks.append({"slug": slug, "label": label, "items": [], "count": 0})
            continue
        data = json.loads(json_path.read_text(encoding="utf-8"))
        blocks.append({
            "slug": slug,
            "label": label,
            "items": data.get("items", []),
            "count": data.get("count", 0),
        })
    return blocks


def render_dashboard(blocks: list[dict], synthesis_path: Path | None = None) -> str:
    now = datetime.now().strftime("%d/%m/%Y - %H:%M")
    total = sum(b["count"] for b in blocks)
    ok_count = sum(1 for b in blocks if b["count"] > 0)

    synthesis_html = ""
    if synthesis_path and synthesis_path.exists():
        synthesis_html = synthesis_path.read_text(encoding="utf-8")

    cards = []
    for b in blocks:
        items_html = ""
        if b["items"]:
            for it in b["items"]:
                title = (it.get("title") or "").replace("<", "&lt;").replace(">", "&gt;")
                url = it.get("url") or "#"
                score = it.get("score") or ""
                snippet = (it.get("snippet") or "").replace("<", "&lt;").replace(">", "&gt;")
                score_html = f'<span class="score">{score}</span>' if score else ""
                items_html += f"""
                <li>
                    <a href="{url}" target="_blank" rel="noopener">{title}</a>
                    {score_html}
                    {f'<p class="snippet">{snippet[:200]}</p>' if snippet else ''}
                </li>"""
            status = "ok"
            status_text = f"{b['count']} trend"
        else:
            items_html = '<li class="empty">Nessun dato (scraper fallito o vuoto)</li>'
            status = "err"
            status_text = "vuoto"
        cards.append(f"""
        <article class="card status-{status}">
            <header>
                <h2>{b['label']}</h2>
                <span class="badge">{status_text}</span>
            </header>
            <ul>{items_html}</ul>
        </article>""")

    cards_html = "\n".join(cards)

    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Calendario editoriale - {now}</title>
<style>
  :root {{
    --bg: #0f1115;
    --surface: #181b22;
    --surface-2: #1f232c;
    --ink: #e8e8ea;
    --ink-soft: #9aa0aa;
    --accent: #f59e0b;
    --green: #22c55e;
    --red: #ef4444;
    --line: #2a2f3a;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, sans-serif;
    background: var(--bg);
    color: var(--ink);
    margin: 0;
    padding: 0;
    line-height: 1.5;
  }}
  header.main {{
    background: linear-gradient(135deg, #1a1d28 0%, #0f1115 100%);
    border-bottom: 1px solid var(--line);
    padding: 28px 40px 24px;
    position: sticky;
    top: 0;
    z-index: 10;
    backdrop-filter: blur(8px);
  }}
  header.main h1 {{
    margin: 0;
    font-size: 26px;
    letter-spacing: -0.02em;
  }}
  header.main h1 .pill {{
    background: var(--accent);
    color: #1a1a1a;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-left: 10px;
    vertical-align: middle;
  }}
  .meta {{
    color: var(--ink-soft);
    font-size: 14px;
    margin-top: 6px;
  }}
  .meta strong {{ color: var(--ink); }}
  section.synthesis {{
    background: linear-gradient(180deg, rgba(245,158,11,0.08) 0%, transparent 100%);
    border-bottom: 1px solid var(--line);
    padding: 24px 40px 32px;
  }}
  section.synthesis h2 {{
    font-size: 18px;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin: 0 0 14px;
  }}
  main {{
    padding: 32px 40px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
    gap: 22px;
  }}
  .card {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.15s, border-color 0.15s;
  }}
  .card:hover {{ transform: translateY(-2px); border-color: var(--accent); }}
  .card header {{
    padding: 14px 18px;
    background: var(--surface-2);
    border-bottom: 1px solid var(--line);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .card header h2 {{
    margin: 0;
    font-size: 16px;
    font-weight: 700;
  }}
  .badge {{
    background: var(--green);
    color: #0a0a0a;
    padding: 3px 9px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }}
  .status-err .badge {{ background: var(--red); color: white; }}
  .card ul {{
    list-style: none;
    margin: 0;
    padding: 8px 0;
    max-height: 480px;
    overflow-y: auto;
  }}
  .card li {{
    padding: 10px 18px;
    border-bottom: 1px solid var(--line);
  }}
  .card li:last-child {{ border-bottom: none; }}
  .card li a {{
    color: var(--ink);
    text-decoration: none;
    font-weight: 500;
    font-size: 14.5px;
    line-height: 1.4;
    display: block;
  }}
  .card li a:hover {{ color: var(--accent); }}
  .score {{
    display: inline-block;
    background: var(--surface-2);
    color: var(--ink-soft);
    padding: 1px 7px;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 600;
    margin-top: 4px;
  }}
  .snippet {{
    color: var(--ink-soft);
    font-size: 12.5px;
    margin: 4px 0 0;
    line-height: 1.4;
  }}
  .empty {{
    color: var(--red);
    font-style: italic;
    font-size: 13px;
  }}
  footer {{
    text-align: center;
    padding: 24px;
    color: var(--ink-soft);
    font-size: 13px;
    border-top: 1px solid var(--line);
  }}
</style>
</head>
<body>
<header class="main">
  <h1>Calendario editoriale - trend in tempo reale <span class="pill">Live</span></h1>
  <div class="meta">
    Generato il <strong>{now}</strong> -
    <strong>{ok_count}/10</strong> piattaforme attive -
    <strong>{total}</strong> trend totali raccolti
  </div>
</header>

{f'<section class="synthesis"><h2>Idee video sintetizzate dai 10 agenti</h2>{synthesis_html}</section>' if synthesis_html else ''}

<main>
{cards_html}
</main>

<footer>
  Generato da orchestrator.py - 10 scraper in parallelo, output JSON in <code>output/</code>.
  Per la sintesi AI: routine Claude (Opus 4.8) che esegue il ciclo di <code>CLAUDE.md</code>.
</footer>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    no_open = "--no-open" in argv          # non aprire il browser (utile per routine schedulate)
    skip_scrape = "--skip-scrape" in argv  # non rilanciare gli scraper: rigenera solo la dashboard dai JSON

    if skip_scrape:
        print("\n[ORCHESTRATOR] --skip-scrape: rigenero la dashboard dai JSON esistenti.\n")
        ok = sum(1 for slug, _ in SCRAPERS if (OUTPUT_DIR / f"{slug}.json").exists())
    else:
        print(f"\n[ORCHESTRATOR] Lancio {len(SCRAPERS)} scraper in parallelo...\n")
        results = []
        with ThreadPoolExecutor(max_workers=len(SCRAPERS)) as pool:
            futures = {pool.submit(run_scraper, slug): label for slug, label in SCRAPERS}
            for fut in as_completed(futures):
                label = futures[fut]
                name, count, msg = fut.result()
                mark = "OK " if count > 0 else "X  "
                print(f"  {mark} {label:30s} -> {count} trend")
                results.append((name, count, msg))
        ok = sum(1 for _, c, _ in results if c > 0)
        print(f"\n[ORCHESTRATOR] {ok}/{len(SCRAPERS)} piattaforme con dati validi.")

    blocks = load_all()
    synthesis_path = OUTPUT_DIR / "synthesis.html"
    DASHBOARD.write_text(render_dashboard(blocks, synthesis_path), encoding="utf-8")
    print(f"[ORCHESTRATOR] Dashboard scritta: {DASHBOARD}")

    if no_open:
        print("[ORCHESTRATOR] --no-open: salto l'apertura del browser.")
    else:
        print("[ORCHESTRATOR] Apertura nel browser...")
        webbrowser.open(DASHBOARD.as_uri())
    print("[ORCHESTRATOR] Fatto.\n")
    return 0 if ok >= 8 else 1


if __name__ == "__main__":
    sys.exit(main())
