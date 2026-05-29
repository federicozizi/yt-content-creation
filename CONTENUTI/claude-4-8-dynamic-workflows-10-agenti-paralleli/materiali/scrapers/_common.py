"""Helpers condivisi dai 10 scraper. Nessuna dipendenza esterna oltre a requests/bs4 (vedi requirements.txt)."""
import json
import sys
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36 yt-content-creation-demo"

DEFAULT_HEADERS = {"User-Agent": UA, "Accept-Language": "it-IT,it;q=0.9,en;q=0.8"}

TIMEOUT = 12


def save(platform: str, items: list[dict]) -> Path:
    path = OUTPUT_DIR / f"{platform}.json"
    payload = {"platform": platform, "count": len(items), "items": items}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def normalize(title: str | None, url: str | None, source: str, score: str = "", snippet: str = "") -> dict:
    return {
        "title": (title or "").strip(),
        "url": (url or "").strip(),
        "source": source,
        "score": str(score),
        "snippet": (snippet or "").strip()[:280],
    }


def run_and_save(platform: str, fetch_fn) -> int:
    """Wrapper standard: chiama fetch_fn(), salva su disco, ritorna count. Stampa info per i sub-agenti."""
    try:
        items = fetch_fn()
    except Exception as exc:
        items = []
        print(f"[{platform}] ERRORE: {exc}", file=sys.stderr)
    out = save(platform, items)
    print(f"[{platform}] {len(items)} item salvati in {out}")
    return len(items)
