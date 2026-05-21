# GitHub for Claude Code — repo template

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/README.md` — keep both in sync.

**Ready to use as a GitHub template.** Inside you'll find 5 practical tricks already configured: persistent context, cloud scheduling, issue → automatic PR, pre-commit code review, worktree pattern for parallel tasks.

## Prerequisites

- GitHub account
- [GitHub CLI `gh`](https://cli.github.com/) installed and authenticated (`gh auth login`)
- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- Anthropic API key (https://console.anthropic.com)

## Quick start

```bash
# 1. Create a new GitHub repo from this folder
gh repo create my-claude-repo --private --source . --push

# 2. Add the ANTHROPIC_API_KEY secret to the repo
gh secret set ANTHROPIC_API_KEY

# 3. Edit competitors.json with your 3 real competitors

# 4. Manual trigger of the first brief (to test)
gh workflow run daily-brief.yml

# 5. Wait 1-2 minutes, then:
gh run watch
gh pr list  # you should see the brief's PR
```

From tomorrow at 7:05 UTC the brief arrives by itself as a PR every morning.

## Automatic setup (recommended for non-technical users)

Launch Claude Code inside this folder:

```bash
claude
> run the setup by reading START_HERE.md
```

Claude Code does it all by itself: creates the GitHub repo, sets the secret, runs the first test, explains what happened.

## What's in this folder

```
.
├── README.md                                  ← you're reading this
├── START_HERE.md                              ← guided setup for Claude Code
├── CLAUDE.md                                  ← TRICK #1: persistent context in the repo
├── .gitignore                                 ← protects .env and sensitive files
├── .env.example                               ← credentials template (for local testing)
├── competitors.json                           ← competitor list (editable)
├── example-output.md                          ← how the expected result looks
├── prompts/
│   └── daily-brief.md                         ← brief orchestrator prompt
├── .github/
│   ├── workflows/
│   │   ├── daily-brief.yml                    ← TRICK #3: Claude scheduled in cloud
│   │   └── issue-task.yml                     ← TRICK #4: issue → automatic PR
│   └── hooks/
│       └── pre-commit-claude-review.sh        ← TRICK #5: pre-commit review
└── docs/
    ├── worktree-pattern.md                    ← TRICK #2: 3 Claudes in parallel
    └── github-actions-setup.md                ← secrets and permissions guide
```

## The 5 tricks in summary

| # | Trick | File | What it solves |
|---|---|---|---|
| 1 | `CLAUDE.md` in the repo | `CLAUDE.md` | Persistent context for every session |
| 2 | Parallel worktrees | `docs/worktree-pattern.md` | 3 Claudes in parallel without conflicts |
| 3 | Scheduled GitHub Actions | `.github/workflows/daily-brief.yml` | Claude runs even with PC off |
| 4 | Issue → automatic PR | `.github/workflows/issue-task.yml` | Task backlog managed by labels |
| 5 | Pre-commit review | `.github/hooks/pre-commit-claude-review.sh` | Auto-review before commit |

## Credentials security

- **Never commit `.env`**: the `.gitignore` excludes it. In production, credentials live in the repo's **GitHub Secrets**, not in local files.
- **Never print secrets in Action logs**: GitHub masks them automatically, but still avoid `echo $ANTHROPIC_API_KEY`.
- If you accidentally commit `.env`: revoke the key immediately at https://console.anthropic.com and create a new one. Removing it from git history **isn't enough** — bots scan GitHub constantly.
