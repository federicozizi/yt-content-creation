"""Lobste.rs: feed RSS pubblico (community curata, ottimo segnale tech)."""
import re
import requests
import xml.etree.ElementTree as ET
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "lobsters"
URL = "https://lobste.rs/rss"
TAG_RE = re.compile(r"<[^>]+>")


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc_raw = item.findtext("description") or ""
        desc = TAG_RE.sub("", desc_raw).strip()
        if not title:
            continue
        out.append(normalize(title=title, url=link, source=PLATFORM, snippet=desc))
        if len(out) >= 10:
            break
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
