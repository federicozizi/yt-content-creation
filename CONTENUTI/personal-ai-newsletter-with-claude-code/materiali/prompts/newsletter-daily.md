# Orchestrator prompt — Personal AI Newsletter

You are generating today's personal newsletter. Follow the steps below in order. Remember: `CLAUDE.md` defines tone, format and things to skip — read it if you don't already have it in context.

## What to do

### 1. Load current state

Read `state.json`. Memorize:
- `seen_articles`: the list of URLs already processed in previous runs
- `last_run`: timestamp of the last successful run

### 2. Load the sources

Read `sources.json`. Memorize the list of sources with `name`, `url`, `category`.

### 3. Visit each source (in parallel)

For each source in `sources.json`:
- Open the URL (`WebFetch`)
- Extract the list of published articles with: title, URL, date
- Filter: keep only articles published in the last 48 hours AND NOT present in `seen_articles`

### 4. Deep-dive each new article

For each article that passed the filter:
- Open its full URL (`WebFetch`)
- Extract the relevant content (skipping navigation, footer, related links)
- Summarize in 3-5 bullets following the rules in `CLAUDE.md` (section "Newsletter tone")
- Apply the "What to emphasize" and "What to skip" criteria from `CLAUDE.md`

If an article, after reading, falls into the skip criteria (filler, partnership without details, etc.): skip. Don't include it, but still add it to `seen_articles` to avoid reprocessing it tomorrow.

### 5. Compose the newsletter file

Create `newsletter/YYYY-MM-DD.md` (date of the run, ISO format).

Structure:

```markdown
# 🧠 Your AI Brief — <day> <readable date in English>

## <N> updates today

### <category emoji> <Article 1 title>
- <bullet 1>
- <bullet 2>
- <bullet 3>
- 🔗 <original URL>

### <category emoji> <Article 2 title>
...

---
Generated in <X> seconds · <N> articles read · <M> articles skipped (already seen or filtered)
```

Emojis per category:
- 🚀 product (launches, features, model releases)
- 📄 research (papers, white papers)
- 🔧 changelog (release notes)
- 🆕 other categories added by the user in `sources.json`

If there's nothing to report today:

```markdown
# 🧠 Your AI Brief — <date>

No relevant updates today. All <N> sources consulted haven't published anything new in the last 48 hours.

---
Generated in <X> seconds · <N> sources consulted
```

Don't invent news to "fill" — if it's a dead day, it's a dead day.

### 6. Update state

Edit `state.json`:
- Add to `seen_articles` ALL URLs processed today (both those included in the newsletter and those skipped post-reading — the important thing is not to re-propose them)
- Update `last_run` to the current ISO 8601 timestamp (e.g. `"2026-05-16T08:00:00Z"`)

### 7. Call the team's sub-agents

At this point, the file `newsletter/YYYY-MM-DD.md` exists. Now you hand off to the team of specialized sub-agents living in `.claude/agents/`:

**If K (articles included) == 0** → call the `empty-day-rescue` sub-agent:
> "Launch empty-day-rescue. Today's newsletter file is empty. Fish out 1-2 deep-dives from the secondary sources in sources-fallback.json and add them to the file."

Wait for it to finish. It will read its instructions file in `.claude/agents/empty-day-rescue.md`, do the work, modify the newsletter file by adding a "📚 Today's deep-dives" section, update `state.json`.

**Always, even if K > 0** → call the `major-update-spotter` sub-agent:
> "Launch major-update-spotter on the file newsletter/YYYY-MM-DD.md. Check if there's at least one major update (new model, new tool/service, breaking change) and, if so, highlight it at the top of the file."

Wait for it to finish. It will read its instructions file in `.claude/agents/major-update-spotter.md`, classify contents, and if it finds major updates will add a `🚨 MAJOR UPDATE` box at the top of the file.

### 8. Print final summary

After both sub-agents have finished, in console print:

```
✅ Newsletter generated: newsletter/YYYY-MM-DD.md
   - N primary sources consulted
   - M new articles found
   - K articles included
   - L articles skipped (filler/already seen)
   - <empty-day-rescue: invoked/skipped — any added contents>
   - <major-update-spotter: N major updates highlighted / no major updates>
   - Total time: <X> seconds
```

## Absolute rules

- **Output language**: English (unless `CLAUDE.md` says otherwise)
- **Never invent content**: if you can't read an article, flag it in the final summary but don't write its summary
- **Never duplicate**: before processing, check `seen_articles`
- **Never manually edit `sources.json`**: the user edits it, you just read it
- **Sub-agents are mandatory**: step 7 is NOT optional. The sub-agent team is integral to the flow. If Claude Code doesn't recognize sub-agents (e.g. missing `.claude/agents/` folder), flag it in the final summary but don't block the rest of the execution.
