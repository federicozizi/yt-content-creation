<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/prompts/04-integrazione-end-to-end.md -->

# Prompt 04 — End-to-end orchestration of the 3 components

This prompt shows the "typical Monday morning" of the accounting firm — when all 3 components work together.

## Prerequisites

- Steps 1, 2, 3 completed and working separately.
- At least a few clients in `clients` on Supabase with `tax_regime_code` and `current_year_revenue` populated (so regime-checker can find data and produce real alerts).
- Claude for Small Business package active in Cowork, with at least QuickBooks (sandbox) and Google Workspace connected.

## Flow

The flow alternates **Cowork (browser)** and **Claude Code (terminal)**, because the package lives in Cowork and the custom agents live in Code. The bridge is Supabase via MCP, readable by both.

### Step A — In Cowork (browser)

Open Cowork, new chat, type:

```
/monday-brief
```

Expected output: Monday operational summary that includes:
- Current cash (read from QuickBooks)
- Invoices due this week (QuickBooks)
- New CRM leads (HubSpot if connected, otherwise the line is omitted)
- **+ Alerts from internal_notes on Supabase**, because the package also reads your custom DB via MCP

Verify in the output there are lines like:
> ⚠️ 2 clients near forfettario limit (alerts from regime-checker last week)

If you don't see Supabase lines, the package may not yet have the Supabase MCP connector configured at the Cowork workspace level. If that's your case: in Cowork → Settings → Connectors → Add custom MCP → URL and key of Supabase (same as .env). Anthropic supports custom MCP in Team workspaces since May 2026.

### Step B — In Claude Code (terminal)

Open the terminal, inside `materiali/`:

```bash
claude
```

And paste:

```
Launch regime-checker and deadline-alerter in sequence, as you would on a
Monday morning before the firm's meeting.

After:
1. Show the deadline-alerter report (file logs/deadlines-YYYY-MM-DD.md).
2. Show how many new internal_notes rows regime-checker generated in total.

Go.
```

Wait for it to finish. Go check in Supabase Table Editor that `internal_notes` has the new rows generated.

### Step C — Back in Cowork

Return to Cowork, type:

```
/invoice-chaser
```

The package:
1. Reads from QuickBooks the invoices unpaid over 30 days.
2. **For each client with unpaid invoice, before writing the email it checks internal_notes on Supabase** looking for rows with non-null `invoice_chaser_flag` for that client.
3. If it finds `invoice_chaser_flag = 'do_not_chase'` → skips that client.
4. If it finds `invoice_chaser_flag = 'soft_chase'` → adapts the tone.
5. Proposes the resulting emails.

**DO NOT click "Approve" if you're in production** — stop to read what it would propose, decide if it's good, and only then send. For testing, leave the proposed emails without sending them.

### Step D — Integration verification

The point of this step is to demonstrate that **the Anthropic package read Supabase**. To verify:

1. Take a client from the `/invoice-chaser` report.
2. Go to Supabase Table Editor → `internal_notes` → filter by that `client_id` with non-null `invoice_chaser_flag`.
3. Confirm the tone of the email proposed by the package is consistent with the flag (if "do_not_chase", the client should NOT have been in the list; if "soft_chase", the text should be less aggressive than the default).

If consistency is there: **the 3 components talk**. You have an infrastructure, not 3 disjoint tools.

## What signals the flow is working

- `/monday-brief` cites both rows from QuickBooks (cash) and from Supabase (alerts).
- regime-checker writes to `internal_notes` without duplicates.
- `/invoice-chaser` reads `invoice_chaser_flag` from Supabase and modulates the texts.
- All final outputs (emails, reports) go through human approval — nothing automatic.

## What to do if something doesn't connect

- **Package can't see Supabase**: add a custom MCP in Cowork (Settings → Connectors).
- **Custom agents don't write to internal_notes**: verify `.env` is present and `claude mcp add supabase` ran successfully. Direct test: `claude` + "do a test INSERT into internal_notes".
- **Package and agents write inconsistently** (e.g. duplicate alerts): usually a deduplication issue in the custom sub-agent. See deduplication instructions in `.claude/agents/regime-checker.md`.
