# Schedule the newsletter with Claude Routines

Claude Routines is the scheduling system built into Claude Code. It runs prompts at recurring times without your PC needing anything special open — it just needs to be on and Claude Code installed.

## Quick start

```bash
# From the materials folder
cd /path/to/materiali

# Create the "daily-newsletter" routine: every day at 8:00
claude routines add daily-newsletter \
  --schedule "0 8 * * *" \
  --cwd "$(pwd)" \
  --prompt "run prompts/newsletter-daily.md"
```

Parameter explanation:
- `daily-newsletter` → routine name (must be unique)
- `--schedule "0 8 * * *"` → cron syntax: minute, hour, day-of-month, month, day-of-week. `"0 8 * * *"` = every day at 8:00
- `--cwd "$(pwd)"` → working directory (must be the materials folder, where `sources.json` and the other files live)
- `--prompt "..."` → the prompt to execute

## Checks

```bash
# List active routines
claude routines list
```

Expected output:
```
📋 Active routines:
   • daily-newsletter — every day at 08:00 — next: tomorrow 08:00
```

```bash
# Manual run (to test without waiting for the scheduled time)
claude routines run daily-newsletter
```

## Change time

```bash
# Example: move to 18:00
claude routines edit daily-newsletter --schedule "0 18 * * *"
```

## Temporarily disable

```bash
claude routines pause daily-newsletter
# resume:
claude routines resume daily-newsletter
```

## Delete permanently

```bash
claude routines remove daily-newsletter
```

## Common schedule examples

| When | Cron expression |
|---|---|
| Every day at 8:00 | `"0 8 * * *"` |
| Weekdays only (Mon-Fri) at 8 | `"0 8 * * 1-5"` |
| Every Monday at 9 | `"0 9 * * 1"` |
| Twice a day (8 and 18) | `"0 8,18 * * *"` |
| Every 3 hours | `"0 */3 * * *"` |

If you're unsure, use https://crontab.guru/ to verify the expression.

## When NOT to use Claude Routines

- **If your PC is off**: Routines only runs if Claude Code is active on your machine. If you want a system that runs even with the PC off, you need cloud scheduling (e.g. GitHub Actions — see dedicated video).
- **If you're on a server without Claude Code installed**: use Linux cron directly. See `crontab-example.txt`.
