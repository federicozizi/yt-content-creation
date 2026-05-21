# Execution example — what you see when the system runs

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/esempio-output.md` — keep both in sync.

## 1. The GitHub Action starts by itself at 7:05

Go to the repo's **Actions** tab. You see the `Daily Competitor Brief` run with status 🟢:

```
✓ Checkout repo
✓ Setup Node
✓ Install Claude Code CLI
✓ Run Claude Code with daily-brief prompt
✓ Open PR with the brief
```

## 2. You find a PR opened automatically

Repo's **Pull requests** tab:

```
📊 Daily Competitor Brief — auto                    #42
   auto/daily-brief-7821 → main
   bot: github-actions
```

## 3. Open the PR and read the brief

The diff shows a new file: `briefs/2026-05-08.md`:

```markdown
# Daily Competitor Brief — Thursday May 8, 2026

## TOP INSIGHT
1. Acme raised Pro €49 → €56 (+15%)
2. Beta Inc launched the Notion integration yesterday
3. Gamma Co published a case study with 310 reactions

## Per competitor

### Acme
- 🔴 **Pricing**: Pro €49 → €56 (+15%)
- 🟡 **Features**: no announcements last 7 days
- 🔵 **Social**: 2 weekly posts, medium engagement

### Beta Inc
- ⚪ **Pricing**: unchanged
- 🟢 **Features**: Notion integration live since May 7
- 🔵 **Social**: top post Notion (180 reactions)

### Gamma Co
- ⚪ **Pricing**: unchanged
- 🟡 **Features**: no announcements
- 🟢 **Social**: "ABC Corp" case study (310 reactions)

## Action suggestion
Publish a pricing comparison vs Acme today: their +15% is an opening.
```

## 4. You merge it (if OK)

Click `Merge pull request`. The brief enters `main`. The next day, at 7:05, a new one arrives.

---

## Example of the "issue → automatic task" flow

1. You open an issue: *"Add Delta Corp as 4th competitor too"*
2. You add label `claude-task`
3. 30-60 seconds later, the GitHub Action has opened a PR that modifies `competitors.json` adding Delta Corp
4. You review the PR and merge it
