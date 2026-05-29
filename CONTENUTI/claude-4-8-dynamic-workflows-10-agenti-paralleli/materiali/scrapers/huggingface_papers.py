"""Hugging Face Papers (trending research AI). Sostituisce Bluesky che ha bloccato l'API pubblica.

Nome del file mantenuto come bluesky.py per compatibilita' con orchestrator,
ma PLATFORM esposto e' 'huggingface_papers' (nome corretto per la dashboard).
"""
import requests
from bs4 import BeautifulSoup
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "huggingface_papers"
URL = "https://huggingface.co/papers"


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    seen = set()
    # I paper trending sono link verso /papers/<arxiv-id>
    for a in soup.select("a[href^='/papers/']"):
        href = a.get("href", "")
        # esclude link di filtraggio (?date=...) e di paginazione
        if "?" in href or href.count("/") != 2:
            continue
        title = a.get_text(strip=True)
        if not title or len(title) < 10 or href in seen:
            continue
        seen.add(href)
        out.append(normalize(
            title=title,
            url=f"https://huggingface.co{href}",
            source=PLATFORM,
            snippet="Paper di ricerca AI in trending",
        ))
        if len(out) >= 10:
            break
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)
