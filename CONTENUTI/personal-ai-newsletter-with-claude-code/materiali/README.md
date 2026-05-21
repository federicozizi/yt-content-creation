# Personal AI Newsletter — template

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali/README.md` — keep both in sync.

**Ready to use.** Minimal system that every morning visits the sources you decide, summarizes the news in the tone you prefer, saves a markdown file to your desk. No Python, no external APIs, just Claude Code.

## Prerequisites

- [Claude Code installed](https://claude.com/code) and logged in (Pro/Max or API key)

Nothing else.

## Quick start (3 commands)

```bash
# 1. Enter the folder
cd materiali

# 2. Launch Claude with the orchestrator prompt
claude --print "$(cat prompts/newsletter-daily.md)"

# 3. Open the generated file
# (it will appear in newsletter/YYYY-MM-DD.md)
```

Done. The first newsletter is in `newsletter/`.

## Automatic setup (recommended for non-technical users)

Launch Claude Code inside this folder:

```bash
claude
> run the setup by reading START_HERE.md
```

Claude Code does it all by itself: checks prerequisites, asks for 1-2 confirmations, launches the first run, shows you the result.

## What's in this folder

```
.
├── README.md                          ← you're reading this
├── START_HERE.md                      ← guided setup for Claude Code
├── CLAUDE.md                          ← STEP 2: tone and rules for the newsletter
├── .gitignore                         ← protects state.json and output
├── sources.json                       ← STEP 1: list of primary sources to monitor
├── sources-fallback.json              ← STEP 5: secondary sources for empty days
├── state.json                         ← memory of seen URLs (Claude updates it)
├── example-output.md                  ← how a generated newsletter looks
├── prompts/
│   └── newsletter-daily.md            ← STEP 3: orchestrator prompt
├── .claude/
│   └── agents/
│       ├── empty-day-rescue.md        ← STEP 5: sub-agent for empty days
│       └── major-update-spotter.md    ← STEP 5: sub-agent for major updates
├── scheduling/
│   ├── claude-routines.md             ← STEP 4: scheduling with Routines
│   └── crontab-example.txt            ← STEP 4: local cron fallback
└── docs/
    └── email-optional.md              ← optional — receive via email
```

## The 5 steps in summary

| # | Step | File | What you do |
|---|---|---|---|
| 1 | Define the sources | `sources.json` | Add/remove URLs of sites to monitor |
| 2 | Define the tone | `CLAUDE.md` | Edit the writing rules |
| 3 | First run | `prompts/newsletter-daily.md` | Launch Claude with the prompt |
| 4 | Schedule | `scheduling/claude-routines.md` | One line: starts by itself every morning |
| 5 | Agent team | `.claude/agents/*.md` + `sources-fallback.json` | 2 sub-agents: empty-day handling + major-update spotlight |

## What to change to adapt it to your case

- **Change topic** (e.g. from Anthropic to competitors): edit `sources.json` with new URLs
- **Change tone** (e.g. more technical, more colloquial, different language): edit `CLAUDE.md`
- **Change time** (e.g. from 8 to 18): edit the routine with `claude routines edit`
- **Change output format** (e.g. from markdown to email-ready HTML): edit `prompts/newsletter-daily.md`

## What should NOT be committed to git

- `state.json` → contains URLs you've consulted, it's "private"
- `newsletter/*.md` → personal output, you don't want it on public GitHub

The `.gitignore` already excludes them by default. Don't remove it if you plan to version the folder.
