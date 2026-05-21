# Persistent instructions for Claude Code

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/CLAUDE.md` — keep both in sync.

This file is **automatically** read by every Claude Code session that starts inside this repo. It's the "external brain" that gives the agent persistent context: project rules, conventions, do/don't.

> When you work in this repo, follow the rules below. If the user asks you something that contradicts them, ask for confirmation.

## What this repo does

Mini **competitor intelligence** system: every morning at 7 a GitHub Action launches you (Claude Code) to produce a brief on the 3 competitors listed in `competitors.json`. The brief lands in `briefs/<date>.md` and gets committed in the repo.

## Conventions

- **Output language**: English
- **Brief format**: markdown, max 400 words, structure defined in `prompts/daily-brief.md`
- **No committed secrets**: API keys, passwords, tokens only live in GitHub Secrets (`ANTHROPIC_API_KEY`, `GMAIL_APP_PASSWORD`, etc.)
- **Branch policy**: work on feature branch `auto/<date>-<slug>`, never directly on `main`
- **Commit message**: `daily brief YYYY-MM-DD` for generated briefs. `fix:`, `feat:`, `docs:` for system changes.

## Key files

| File | What it is | When to touch it |
|---|---|---|
| `competitors.json` | List of 3 competitors to monitor | When the user wants to change competitors |
| `prompts/daily-brief.md` | Orchestrator prompt | Only if the user asks to change brief structure |
| `.github/workflows/daily-brief.yml` | Scheduled Action 7:05 every day | Only if the user asks to change cron or trigger |
| `.github/workflows/issue-task.yml` | Action that processes issues with `claude-task` label | Only if the user asks to change the flow |
| `briefs/` | Output of daily briefs | Read-only, never edit past brief files by hand |

## Style

- Direct, dry, colloquial English tone
- No academic paragraphs
- When you produce a brief, follow EXACTLY the structure in `prompts/daily-brief.md`
