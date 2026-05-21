# Personal AI Newsletter — Variant 2 (Anthropic API + HTML/RSS parsing)

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali-variante-2/README.md` — keep both in sync.

**Same pattern as the other 2 methods, stripped to the bone.** ~80 lines of Python that download HTML/RSS of the sources, extract articles with BeautifulSoup/feedparser, send Claude API only the clean text, save the markdown.

## Prerequisites

- Python ≥ 3.10
- An Anthropic API key (https://console.anthropic.com)

## Quick start (4 commands)

```bash
cd materiali-variante-2
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # then fill in ANTHROPIC_API_KEY
python newsletter.py
```

The file appears in `newsletter/YYYY-MM-DD.md`.

## Automatic setup (recommended)

```bash
claude
> run the setup by reading START_HERE.md
```

## What's in this folder

```
.
├── README.md              ← you're reading this
├── START_HERE.md          ← guided setup for Claude Code
├── .gitignore             ← protects .env, state.json, output
├── .env.example           ← template ANTHROPIC_API_KEY
├── requirements.txt       ← anthropic, requests, beautifulsoup4, feedparser, python-dotenv
├── newsletter.py          ← THE SCRIPT (~80 lines)
├── sources.json           ← sources HTML + RSS
├── prompt.txt             ← summary prompt for Claude
├── state.json             ← memory of seen URLs
├── example-output.md      ← generated newsletter example
└── scheduling/
    └── crontab-example.txt ← cron examples Mac/Linux/Windows
```

## Key differences from previous methods

| Aspect | Main | Variant 1 | Variant 2 (this) |
|---|---|---|---|
| Stack | Claude Code CLI | Claude Agent SDK | Anthropic API + Python stdlib + requests |
| CLAUDE.md loader | automatic | manual (open in Python) | the "tone" lives in pure `prompt.txt` |
| Agent loop | yes (CLI does everything) | yes (Agent SDK) | NO (procedural code) |
| Tool use | yes (WebFetch) | yes (web_fetch) | NO (requires explicit `requests`) |
| Claude tokens per run | high | medium | low (you send only clean text) |
| Cost/run | $0 (subscription) or ~$0.05 (API) | ~$0.05 | ~$0.005-0.01 |
| Headless server | no | yes | yes (even Raspberry Pi) |
| Magic | a lot | medium | zero |

## Costs

Anthropic API: ~$0.002-0.01 per run (you send only the clean texts, not the raw HTMLs).
For one run/day → ~$0.10-0.30/month.

## Credentials security

- `.env` is in `.gitignore`. Don't remove it.
- If you commit `.env` by mistake, **revoke the key** on console.anthropic.com.
