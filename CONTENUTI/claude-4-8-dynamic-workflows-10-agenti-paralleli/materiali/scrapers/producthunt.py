"""Product Hunt: feed Atom pubblico (no API key)."""
import re
import requests
import xml.etree.ElementTree as ET
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "producthunt"
URL = "https://www.producthunt.com/feed"
NS = {"atom": "http://www.w3.org/2005/Atom"}
TAG_RE = re.compile(r"<[^>]+>")


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = []
    for entry in root.findall("atom:entry", NS)[:12]:
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip()
        link_el = entry.find("atom:link", NS)
        link = link_el.get("href") if link_el is not None else ""
        content = entry.findtext("atom:content", default="", namespaces=NS) or ""
        summary = entry.findtext("atom:summary", default="", namespaces=NS) or ""
        snippet = TAG_RE.sub(" ", content or summary).strip()
        if not title:
            continue
        out.append(normalize(title=title, url=link, source=PLATFORM, snippet=snippet))
        if len(out) >= 10:
            break
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
