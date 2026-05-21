# Automatic setup — Claude Code, read this

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/INIZIO_QUI.md` — keep both in sync.

You've been launched inside the materials folder of the **GitHub for Claude Code** template. Everything is already here: Actions workflows, pre-commit hook, orchestrator prompt, repo context `CLAUDE.md`. You only do: prerequisites + create GitHub repo + secret + first test. ~5 minutes.

## What to do

### 1. Check prerequisites

```bash
gh --version            # GitHub CLI: https://cli.github.com
gh auth status          # must say "Logged in"
claude --version        # if missing: npm install -g @anthropic-ai/claude-code
```

If something's missing, flag it to the user with the right links.

### 2. Ask for the new repo name

Ask the user:
- Repo name (e.g. `competitor-intel`)
- Private or public? (default: private)

### 3. Create the GitHub repo from the current folder

```bash
gh repo create <name> --private --source . --push
```

This: initializes git locally, makes the first commit, creates the repo on GitHub, pushes. All in one command.

### 4. Add the ANTHROPIC_API_KEY secret

Ask the user for their Anthropic API key (`sk-ant-...`). If they don't have one, send them to https://console.anthropic.com → Settings → API Keys.

```bash
gh secret set ANTHROPIC_API_KEY
# (paste the key when prompted)
```

### 5. Configure the competitors

Open `competitors.json`, show it to the user, and help them replace the 3 placeholders with their real competitors.

Commit and push:

```bash
git add competitors.json
git commit -m "config: real competitors"
git push
```

### 6. Manual workflow test

```bash
gh workflow run daily-brief.yml
gh run watch
```

Wait 1-2 minutes. When done:

```bash
gh pr list
```

You should see the brief's PR. Show it to the user:

```bash
gh pr view --web
```

### 7. (Optional) Activate the pre-commit hook locally

If the user wants TRICK #5 (pre-commit review) also locally:

```bash
cp .github/hooks/pre-commit-claude-review.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 8. All set

From tomorrow at 7:05 UTC a PR will arrive every morning with the brief.

To disable: Actions tab on GitHub → workflow → Disable.
To change time: edit `cron:` in `.github/workflows/daily-brief.yml`.

## Notes for you (Claude Code)

- **Don't create separate project folders**: this folder IS the project repo.
- **Don't remove `CLAUDE.md`**: it's the file that gives you persistent context in the repo. If you delete it, future sessions start blind.
- Direct, concise tone. No academic paragraphs.
- If a command fails, show the error and suggest the fix instead of starting over.
