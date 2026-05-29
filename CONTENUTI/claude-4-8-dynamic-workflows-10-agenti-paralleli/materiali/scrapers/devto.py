"""Dev.to: API REST pubblica (nessuna chiave). Articoli top tag 'ai' nella settimana."""
import requests
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "devto"
URL = "https://dev.to/api/articles?per_page=10&top=7&tag=ai"


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    arts = r.json()
    out = []
    for a in arts:
        out.append(normalize(
            title=a.get("title"),
            url=a.get("url"),
            source=PLATFORM,
            score=str(a.get("positive_reactions_count", "")),
            snippet=a.get("description", ""),
        ))
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
