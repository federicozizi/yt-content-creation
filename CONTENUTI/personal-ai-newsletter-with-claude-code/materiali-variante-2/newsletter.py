"""
Personal AI Newsletter — Variant 2 (Anthropic API + HTML/RSS parsing)

Downloads HTML/RSS of the sources, extracts articles with BeautifulSoup/feedparser,
sends Claude API only the clean text for summarization, saves the markdown.

Usage:
    python newsletter.py

Scheduling: see scheduling/crontab-example.txt
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

EMOJI_BY_CATEGORY = {
    "product": "🚀",
    "research": "📄",
    "changelog": "🔧",
    "tech": "🆕",
}


def extract_articles(source: dict) -> list[dict]:
    """Returns a list of {title, url, category} for the given source."""
    if source["type"] == "rss":
        feed = feedparser.parse(source["url"])
        return [
            {"title": e.title, "url": e.link, "category": source["category"]}
            for e in feed.entries[:20]
        ]

    if source["type"] == "html":
        html = requests.get(source["url"], timeout=TIMEOUT).text
        soup = BeautifulSoup(html, "html.parser")
        seen = set()
        out = []
        for a in soup.select(source["article_selector"]):
            href = a.get("href")
            if not href or href in seen:
                continue
            seen.add(href)
            full_url = urljoin(source["url"], href)
            out.append({"title": a.get_text(strip=True), "url": full_url, "category": source["category"]})
            if len(out) >= 20:
                break
        return out

    return []


def summarize_article(client: Anthropic, article: dict, system_prompt: str, model: str) -> str | None:
    """Downloads the article full text and asks Claude to summarize. Returns markdown bullets or None if SKIP."""
    try:
        html = requests.get(article["url"], timeout=TIMEOUT).text
    except requests.RequestException as e:
        print(f"   ⚠️  fetch failed for {article['url']}: {e}", file=sys.stderr)
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
                "content": f"Title: {article['title']}\n\nContent:\n{text}",
            }
        ],
    )
    body = msg.content[0].text.strip()
    if body.upper().startswith("SKIP"):
        return None
    return body


def compose_newsletter(today: str, summaries: list[dict]) -> str:
    """Composes the final newsletter markdown."""
    nice_date = datetime.now().strftime("%A %B %d, %Y")
    if not summaries:
        return (
            f"# 🧠 Your AI Brief — {nice_date}\n\n"
            f"No relevant updates today.\n"
        )

    parts = [f"# 🧠 Your AI Brief — {nice_date}\n", f"## {len(summaries)} updates today\n"]
    for s in summaries:
        emoji = EMOJI_BY_CATEGORY.get(s["category"], "🆕")
        parts.append(f"### {emoji} {s['title']}\n{s['summary']}\n- 🔗 {s['url']}\n")
    return "\n".join(parts)


def main() -> int:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or "XXXX" in api_key:
        print("❌ ANTHROPIC_API_KEY not configured in .env", file=sys.stderr)
        return 1

    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-7")
    client = Anthropic(api_key=api_key)

    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))["sources"]
    state = json.loads((ROOT / "state.json").read_text(encoding="utf-8"))
    system_prompt = (ROOT / "prompt.txt").read_text(encoding="utf-8")
    seen = set(state.get("seen_articles", []))

    NEWSLETTER_DIR.mkdir(exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    start = time.time()
    print(f"🚀 Starting newsletter for {today}")

    summaries: list[dict] = []
    processed: list[str] = []
    skipped = 0

    for source in sources:
        print(f"📖 {source['name']}...")
        articles = extract_articles(source)
        new = [a for a in articles if a["url"] not in seen]
        for art in new[:5]:  # cap at 5 articles/source to keep tokens reasonable
            processed.append(art["url"])
            summary = summarize_article(client, art, system_prompt, model)
            if summary:
                summaries.append({**art, "summary": summary})
            else:
                skipped += 1

    output = compose_newsletter(today, summaries)
    out_path = NEWSLETTER_DIR / f"{today}.md"
    out_path.write_text(output, encoding="utf-8")

    state["seen_articles"] = list(seen | set(processed))
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    (ROOT / "state.json").write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    duration = time.time() - start
    print(f"\n✅ Newsletter generated: {out_path}")
    print(f"   - {len(sources)} sources consulted")
    print(f"   - {len(processed)} articles read")
    print(f"   - {len(summaries)} articles included")
    print(f"   - {skipped} articles skipped")
    print(f"   - {duration:.1f} seconds total")

    return 0


if __name__ == "__main__":
    sys.exit(main())
