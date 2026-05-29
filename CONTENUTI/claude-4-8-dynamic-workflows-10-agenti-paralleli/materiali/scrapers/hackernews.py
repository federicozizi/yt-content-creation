"""Hacker News: top stories via Firebase API (nessuna chiave necessaria)."""
import requests
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "hackernews"
TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
HN_LINK = "https://news.ycombinator.com/item?id={}"


def fetch_trends() -> list[dict]:
    ids = requests.get(TOP_URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT).json()[:15]
    out = []
    for hid in ids:
        try:
            it = requests.get(ITEM_URL.format(hid), headers=DEFAULT_HEADERS, timeout=TIMEOUT).json()
            if not it or it.get("type") != "story":
                continue
            out.append(normalize(
                title=it.get("title"),
                url=it.get("url") or HN_LINK.format(hid),
                source=PLATFORM,
                score=str(it.get("score", "")),
                snippet=f"{it.get('descendants', 0)} commenti",
            ))
        except Exception:
            continue
        if len(out) >= 10:
            break
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
