<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/esempio-output.md -->

# Example: what a typical day looks like once the system is running

Monday morning, accounting firm "Demo Firm & Partners". The 3 components have been active for a week. Here's what the user sees on 3 screens.

## Screen 1 — Claude Cowork: `/monday-brief`

```
> /monday-brief

📊 Monday Brief — Monday May 18, 2026

💰 Current cash: $12,450 (source: QuickBooks)
📑 Invoices due this week: 4 (total $3,200)
🆕 New CRM leads: 7 (source: HubSpot)

⚠️ Alerts from firm DB (Supabase MCP):
  • Client "Bianchi LLC" reached 83% of forfettario limit
    (alert from regime-checker, 2 days ago, not yet read)
  • Client "Verdi Construction" reached 91% of forfettario limit
    (alert from regime-checker, 5 days ago)
  • 3 firm custom deadlines in the next 7 days
    (alert from deadline-alerter this morning)

📌 Suggested next action:
  Call "Mario Bianchi" first (hot CRM lead 3 days old)
  and plan a meeting with "Verdi Construction" to discuss
  tax regime switch for 2027.

OK to send the summary email to the firm's partners?
[ Approve ] [ Edit ] [ Cancel ]
```

The user clicks **Approve**. An internal email goes to the firm's 3 partners with the brief.

## Screen 2 — Claude Code (Agent View): regime-checker

```
$ claude agents

  ┌─────────────────────────────────────────────────────────────────┐
  │  AGENT VIEW — claude-code-small-business                         │
  ├─────────────────────────────────────────────────────────────────┤
  │                                                                  │
  │  ▼ document-classifier      [ready]                              │
  │     Classifies ambiguous documents                              │
  │                                                                  │
  │  ▼ regime-checker           [running] — started 09:15            │
  │     Checks tax regime thresholds                                 │
  │                                                                  │
  │  ▼ deadline-alerter         [completed] — ended 09:08            │
  │     Report in logs/deadlines-2026-05-18.md                       │
  │                                                                  │
  └─────────────────────────────────────────────────────────────────┘
```

Open the `regime-checker` stream:

```
[09:15:03] Starting regime-checker run
[09:15:04] Query v_clients_near_limit via Supabase MCP…
[09:15:05]   → 2 clients returned
[09:15:05] Client "Bianchi LLC": 83% of forfettario limit
[09:15:06]   Duplicate check last 7d → no recent alerts
[09:15:06]   INSERT internal_notes (type=threshold_alert, author=agent:regime-checker)
[09:15:07] Client "Verdi Construction": 91% of forfettario limit
[09:15:08]   Duplicate check last 7d → existing alert from 5d ago
[09:15:08]   SKIP — duplicate, not regenerating
[09:15:09] End regime-checker run
[09:15:09] Summary: 2 clients checked, 1 new alert, 1 skipped
[09:15:09] Log saved to logs/regime-checker-2026-05-18.log
```

## Screen 3 — Supabase: the row just inserted

Open Table Editor → `internal_notes` → sort by `created_at` DESC. First row:

| field | value |
|---|---|
| `id` | `f8a3b2c1-...` |
| `client_id` | `<id of Bianchi LLC>` |
| `type` | `threshold_alert` |
| `text` | `Client Bianchi LLC reached 83% of forfettario regime limit. Consider preparing for an early switch.` |
| `author` | `agent:regime-checker` |
| `invoice_chaser_flag` | `null` |
| `read` | `false` |
| `created_at` | `2026-05-18 09:15:06+00` |

Later, when you run `/invoice-chaser` in Cowork, the Anthropic package will query this same table (via the custom MCP connector configured in Cowork Settings) and will see these rows to modulate the reminders.

## What you DON'T see (and that's good)

- **No automatically sent email**. `/monday-brief` proposed an internal summary; you approved it. Later `/invoice-chaser` will propose 3 reminder emails; you'll decide whether to send them.
- **No change to clients' tax regime**. regime-checker only generated an alert. Regime switching is a decision of the lead accountant.
- **No writes to QuickBooks or HubSpot from custom agents**. The package's tools can do those (with human approval). Custom agents only touch Supabase.

## From the external client's point of view (e.g. "Bianchi LLC")

The client:
1. Receives an email from the accountant asking to schedule a meeting to discuss the regime switch.
2. Does NOT receive an automatic email. The accountant decided to write it after reading the alert.
3. Sees an organized, on-the-ball, proactive firm.

The infrastructure is invisible. What the client feels is just "the firm remembered me before I asked them to".
