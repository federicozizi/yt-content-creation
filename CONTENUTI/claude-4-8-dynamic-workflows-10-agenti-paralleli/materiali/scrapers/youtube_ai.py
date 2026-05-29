"""YouTube: feed RSS ufficiale dei video di un canale (nessuna API key).

Canale di default: Matt Wolfe (@mreflow) - uno dei piu' seguiti su AI tools.
Per cambiare canale: estrai il channel_id da youtube.com/@nome (View Source -> 'channelId').
"""
import re
import requests
import xml.etree.ElementTree as ET
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "youtube_ai"
CHANNEL_ID = "UChpleBmo18P08aKCIgti38g"  # Matt Wolfe
URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

NS = {"atom": "http://www.w3.org/2005/Atom", "media": "http://search.yahoo.com/mrss/"}
TAG_RE = re.compile(r"<[^>]+>")


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = []
    for entry in root.findall("atom:entry", NS)[:10]:
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip()
        link_el = entry.find("atom:link", NS)
        link = link_el.get("href") if link_el is not None else ""
        desc = ""
        group = entry.find("media:group", NS)
        if group is not None:
            d = group.findtext("media:description", default="", namespaces=NS)
            desc = TAG_RE.sub("", d or "").strip()
        out.append(normalize(title=title, url=link, source=PLATFORM, snippet=desc))
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
