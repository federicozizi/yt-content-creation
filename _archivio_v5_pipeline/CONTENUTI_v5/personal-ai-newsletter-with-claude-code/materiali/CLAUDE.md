# Persistent instructions for Claude Code

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali/CLAUDE.md` — keep both in sync.

This file is **automatically** read by every Claude Code session that starts inside this folder. It defines: what the system does, what tone to write in, what to skip, how to manage state.

## What this system does

Personal daily newsletter: every morning at 8, Claude visits the sources listed in `sources.json`, identifies new articles (comparing with `state.json`), summarizes them in `newsletter/YYYY-MM-DD.md`, updates the state.

## Newsletter tone

- English, direct, colloquial (the way a founder would talk to a peer)
- Max 3-5 bullets per article
- Max 1 line per bullet
- No generic intros/outros ("here are today's news…", "happy reading!")
- No marketing adjectives ("revolutionary", "incredible", "game-changer")
- Always the original link at the end of each article

## What to emphasize

- Concrete numbers (versions, percentages, prices, dates)
- What changes for those who use the product/service
- Availability or release dates
- Any breaking changes or deprecations

## What to skip

- Partnership announcements without concrete details
- Open positions, sponsored events, generic conference recaps
- "Filler" articles that repeat things already said
- Stuff already covered in previous runs (check `state.json` first)

## State management (`state.json`)

`state.json` is long-term memory. Structure:

```json
{
  "seen_articles": [
    "https://www.anthropic.com/news/claude-sonnet-4-7",
    "https://www.anthropic.com/research/constitutional-ai-v2"
  ],
  "last_run": "2026-05-16T08:00:00Z"
}
```

Rules:
- Before processing an article, check if the URL is in `seen_articles`
- If yes → skip (even if it seems relevant)
- If no → process and add the URL to `seen_articles` AFTER writing the newsletter
- Update `last_run` on every execution

## Output

- File: `newsletter/YYYY-MM-DD.md` (date of the run, YYYY-MM-DD)
- If the date already exists (e.g. manual test repeated on the same day), **overwrite** — the most recent run wins
- Format: see `example-output.md`

## Style

- No acronyms or technical terms without a 3-word explanation
- Emojis 🚀 📄 🔧 🆕 ⚠️ to separate sections — no more than 1-2 emojis per article
- Never first person ("Anthropic launched…", not "we launched…")
