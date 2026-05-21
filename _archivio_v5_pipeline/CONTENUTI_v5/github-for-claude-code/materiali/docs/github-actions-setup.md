# GitHub Actions setup with Claude Code

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/docs/github-actions-setup.md` — keep both in sync.

How to run Claude Code in the cloud (even with your PC off), scheduled or triggered by GitHub events.

## 1. Add the secrets to the repo

Go to **Settings → Secrets and variables → Actions → New repository secret** and create:

| Name | Value | How to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | https://console.anthropic.com → Settings → API Keys |
| `GMAIL_APP_PASSWORD` (opt.) | `xxxx xxxx xxxx xxxx` | https://myaccount.google.com/apppasswords (requires 2FA) |

> **Important**: GitHub secrets are **write-only** once created. You can no longer read them. Save them in a password manager before pasting.

## 2. The 2 included workflows

### `daily-brief.yml` — Scheduled brief

Trigger: every day at 7:05 UTC (`cron: "5 7 * * *"`) + manual.

What it does:
1. Checkout the repo
2. Install Node + Claude Code CLI
3. Run Claude Code with the prompt in `prompts/daily-brief.md`
4. Open a PR with the generated brief (`peter-evans/create-pull-request`)

You merge it when you have 30 seconds.

### `issue-task.yml` — Issue → automatic PR

Trigger: every time a `claude-task` label is added to an issue.

What it does:
1. Reads the issue body
2. Passes it to Claude Code as a prompt
3. Claude implements the change + opens a PR that closes the issue

Typical workflow:
- Open issue: *"Add Delta Corp to the competitors too"*
- Add label `claude-task`
- 1 minute later you find a PR ready to review

## 3. `GITHUB_TOKEN` permissions

In the workflow you see:

```yaml
permissions:
  contents: write
  pull-requests: write
```

They're needed because Claude must be able to commit and open PRs. **No `admin`** — Claude shouldn't delete repos or manage users.

## 4. Costs

GitHub Actions on public repos is **free and unlimited**. On private repos you get 2,000 minutes/month free on the Free plan, 3,000 on Pro.

A `daily-brief.yml` run consumes ~30-60 seconds → **~3 minutes/month** if it runs every day. Negligible.

The real costs are on the Anthropic API side: ~$0.01-0.05 per run depending on prompt complexity and chosen model.

## 5. Debugging when a run fails

**Actions** tab → click on the red run → click on the failed step → read the log.

Common errors:
| Error | Cause | Fix |
|---|---|---|
| `ANTHROPIC_API_KEY: not found` | Secret not created | Settings → Secrets → create `ANTHROPIC_API_KEY` |
| `claude: command not found` | Install step skipped | Verify the `Install Claude Code CLI` step is present |
| `Permission denied for github-actions` | Missing `permissions:` | Add `contents: write, pull-requests: write` |
| Claude doesn't open the PR | Branch already exists | The `peter-evans/create-pull-request` step has `delete-branch: true` — verify |

## 6. Limiting when it runs (to not waste API credit)

If you want it to run only on weekdays:

```yaml
on:
  schedule:
    - cron: "5 7 * * 1-5"   # Mon-Fri
```

If you want to temporarily disable it without deleting it:
- **Actions** tab → click on the workflow → **Disable workflow**
