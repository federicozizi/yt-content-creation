# Personal AI Newsletter — Variant 1 (Claude Agent SDK Python)

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali-variante-1/README.md` — keep both in sync.

**Same pattern as the main method, but as a Python script.** Uses the official `claude-agent-sdk` library to orchestrate a Claude Agent with web-fetching tools, generate the newsletter, save it.

## Prerequisites

- Python ≥ 3.10
- An Anthropic API key (https://console.anthropic.com)

## Quick start (4 commands)

```bash
cd materiali-variante-1
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # then fill in ANTHROPIC_API_KEY
python newsletter.py
```

The first newsletter file appears in `newsletter/YYYY-MM-DD.md`.

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
├── CLAUDE.md              ← tone and newsletter rules (identical to MAIN)
├── .gitignore             ← protects .env, state.json, output
├── .env.example           ← template ANTHROPIC_API_KEY
├── requirements.txt       ← claude-agent-sdk, python-dotenv
├── newsletter.py          ← THE MAIN SCRIPT
├── sources.json           ← list of sources to monitor
├── state.json             ← memory of seen URLs (the script updates it)
├── example-output.md      ← example of generated newsletter
└── scheduling/
    └── crontab-example.txt ← cron examples Mac/Linux/Windows
```

## Key differences from the main method

| Aspect | Main method | Variant 1 (this) |
|---|---|---|
| Language | none (just MD prompt) | Python ~50 lines |
| CLAUDE.md loader | automatic (CLI) | manual in the script |
| Execution | `claude` CLI | `python newsletter.py` |
| API key | not needed if you have a subscription | always needed |
| Scheduling | Claude Routines | cron / Task Scheduler |
| Custom logic | hard | easy (you edit Python) |
| Headless server | no | yes |

## Costs

Anthropic API: ~$0.01-0.05 per run depending on prompt size. For one run/day → ~$0.30-1.50/month.

## Credentials security

- `.env` is in `.gitignore`. Don't remove it.
- If you commit `.env` by mistake, **revoke the key** on console.anthropic.com and create a new one: removing it from git history isn't enough (bots scan GitHub).
