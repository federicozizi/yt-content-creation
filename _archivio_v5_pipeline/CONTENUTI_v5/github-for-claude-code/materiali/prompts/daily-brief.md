# Orchestrator prompt — Daily Competitor Brief

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/prompts/daily-brief.md` — keep both in sync.

You are running today's **Daily Competitor Brief**.

## What to do

1. Read `competitors.json` (3 competitors with `pricing_url`, `blog_url`, `linkedin_url`).
2. For each competitor, in parallel:
   - **Pricing**: open `pricing_url`, extract current plans with prices
   - **Features**: open `blog_url`, extract blog posts from the last 7 days
   - **Social**: open `linkedin_url`, extract top posts (>50 reactions, ≤7 days)
3. Synthesize into `briefs/<today YYYY-MM-DD>.md` following the structure below.
4. Commit: branch `auto/<date>-brief`, message `daily brief YYYY-MM-DD`. Open PR against `main`.

## Output structure (`briefs/YYYY-MM-DD.md`)

```markdown
# Daily Competitor Brief — <readable date>

## TOP INSIGHT
1. ...
2. ...
3. ...

## Per competitor

### <Name>
- 🟢/🔴/⚪ **Pricing**: <line>
- 🟢/🟡 **Features**: <line>
- 🔵/🟢 **Social**: <line>

## Action suggestion (optional)
<1 sentence, only if a concrete action emerges>
```

## Rules

- Language: English
- Max length: 400 words
- No invented prices/posts: if a page is inaccessible, write `N/A` and move on
- No long narration: bullets of facts
