"""
Personal AI Newsletter — Variant 1 (Claude Agent SDK)

Visits the sources in sources.json, identifies new articles (compared to state.json),
summarizes them in newsletter/YYYY-MM-DD.md following the rules in CLAUDE.md,
updates state.json.

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

from dotenv import load_dotenv

try:
    from claude_agent_sdk import Agent
except ImportError:
    print("❌ Missing claude-agent-sdk. Install with: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).parent
NEWSLETTER_DIR = ROOT / "newsletter"


def main() -> int:
    load_dotenv(ROOT / ".env")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or "XXXX" in api_key:
        print("❌ ANTHROPIC_API_KEY not configured in .env", file=sys.stderr)
        return 1

    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-7")

    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    state = json.loads((ROOT / "state.json").read_text(encoding="utf-8"))
    tone = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")

    NEWSLETTER_DIR.mkdir(exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = NEWSLETTER_DIR / f"{today}.md"

    system = (
        "You are an assistant that generates daily personal newsletters on a topic of interest.\n"
        "You have access to the web_fetch tool to read web pages.\n"
        "ALWAYS follow the tone and format rules below.\n\n"
        f"{tone}"
    )

    prompt = f"""Generate today's newsletter ({today}).

SOURCES TO VISIT (in parallel):
{json.dumps(sources, ensure_ascii=False, indent=2)}

ALREADY-SEEN ARTICLES (don't re-propose):
{json.dumps(state.get("seen_articles", []), ensure_ascii=False, indent=2)}

INSTRUCTIONS:
1. For each source, read the page with web_fetch and extract articles published in the last 48 hours.
2. Filter: keep only articles NOT already seen.
3. For each new article, read the full content (web_fetch of the full URL) and summarize following CLAUDE.md.
4. Compose the newsletter file following the structure in CLAUDE.md (header, section per article with emoji, final link).
5. Save the result exactly at: {output_path.as_posix()}
6. Respond with a structured summary (JSON) of what you did:
   {{
     "processed_articles": ["url1", "url2"],
     "included_articles": N,
     "skipped_articles": M,
     "seconds": T
   }}
"""

    print(f"🚀 Starting newsletter for {today} (model: {model})")
    start = time.time()

    agent = Agent(
        model=model,
        system=system,
        tools=["web_fetch", "file_write"],
        api_key=api_key,
    )

    result = agent.run(prompt)
    duration = time.time() - start

    # Update state with processed URLs
    try:
        summary = json.loads(result.text) if hasattr(result, "text") else {}
    except json.JSONDecodeError:
        summary = {}

    new_urls = summary.get("processed_articles", [])
    state["seen_articles"] = list({*state.get("seen_articles", []), *new_urls})
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    (ROOT / "state.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✅ Newsletter generated: {output_path}")
    print(f"   - {summary.get('included_articles', '?')} articles included")
    print(f"   - {summary.get('skipped_articles', '?')} articles skipped")
    print(f"   - {duration:.1f} seconds total")

    return 0


if __name__ == "__main__":
    sys.exit(main())
