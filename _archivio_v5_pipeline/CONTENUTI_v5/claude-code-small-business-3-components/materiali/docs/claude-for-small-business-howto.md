<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/docs/claude-for-small-business-howto.md -->

# Claude for Small Business — detailed how-to

Everything you need to make the most of the Anthropic package for small businesses.

## Release status

- **Launch date**: May 13, 2026.
- **Official announcement**: https://www.anthropic.com/news/claude-for-small-business
- **Plugin page**: https://claude.com/plugins/small-business
- **Geographic availability**: US-first for now, but the Google Workspace, Microsoft 365, HubSpot, DocuSign, Canva connectors work immediately from the EU too. QuickBooks and PayPal require US accounts for some advanced features; in the EU they work in basic mode.

## Prerequisites

- **Claude Cowork Team plan** (doesn't work on single Pro).
- **At least one connected tool**. Even just Google Workspace is enough to get started — many workflows read Drive and Gmail.

## Activation

In a Cowork chat:

```
/smb-onboard
```

The guided procedure starts. Typical questions:

1. **Business industry** (accounting, law firm, e-commerce, agency, trades, etc.).
2. **Tools you already pay for**: check only the ones you actually use. NOT everything.
3. **Permissions for each tool**: for each checked tool, an OAuth runs in the browser. You authorize with your account.

At the end you see a new "Small Business" section in the sidebar.

## The 15 workflows (slash commands)

At the time of release (May 2026), the 15 documented commands are:

| Command | What it does | Tools it uses |
|---|---|---|
| `/monday-brief` | Monday summary: cash, invoices, leads, next action | QuickBooks, HubSpot, Supabase MCP (if config) |
| `/close-month` | Monthly close: reconciliation + P&L narrative | QuickBooks, Excel/Google Sheets |
| `/invoice-chaser` | Automatic overdue invoice reminders | QuickBooks, Gmail/Outlook |
| `/plan-payroll` | Payroll planning + paystubs | Payroll system, QuickBooks |
| `/run-campaign` | Marketing campaign: copy + visuals + list | HubSpot, Canva, Gmail |
| `/contract-review` | Contract review, highlights risky clauses | DocuSign |
| `/business-pulse` | Live dashboard of key KPIs | all connectors |
| `/lead-triage` | Sorts incoming leads by priority | HubSpot |
| `/tax-prep` | Tax return prep, groups documents | QuickBooks, Google Drive |
| `/hiring-packet` | Onboarding packet for a new hire | DocuSign, Google Workspace |
| `/customer-sentiment` | Sentiment summary from emails/messages | Gmail, Slack |
| `/cash-flow` | 30/60/90 day cash flow forecast | QuickBooks |
| `/margin-analyzer` | Margin analysis by product/service | QuickBooks, Excel |
| `/expense-categorizer` | Automatic expense categorization | QuickBooks, Drive |
| `/vendor-payments` | Schedule supplier payments | QuickBooks, PayPal |

Each command runs in a Cowork chat. The first time you run it, a mini-wizard starts ("which period? which account? approve before sending?"). Following times it remembers your choices.

## The 15 skills

"Skills" are smaller building blocks that activate AUTOMATICALLY inside the workflows. You don't call them with a slash command, but you see them cited in workflow output:

- cash-flow forecasting
- margin analysis
- lead triage
- invoice chasing
- contract review
- customer sentiment
- tax prep
- hiring packet builder
- expense categorization
- vendor payment scheduling
- (and 5 others not fully documented in the announcement)

## Available connectors

### Included in the base package

- **Intuit QuickBooks** — accounting
- **PayPal** — payments
- **HubSpot** — CRM
- **Canva** — graphic design
- **DocuSign** — contracts and e-signature
- **Google Workspace** — Gmail, Drive, Calendar, Sheets, Docs
- **Microsoft 365** — Outlook, OneDrive, Teams, Excel, Word

### Optional (added manually)

- Slack
- Stripe
- Square
- **Custom MCP** — any MCP server you expose (e.g. our Supabase!). This is how the package sees your custom data.

## How to connect Supabase via MCP to the package

This is the important part for integration with custom sub-agents in Claude Code.

1. In Cowork: Settings → Connectors → "Add custom MCP".
2. Enter:
   - **URL**: same `SUPABASE_URL` as `.env`.
   - **Auth**: same `SUPABASE_SERVICE_ROLE_KEY` as `.env`.
3. Give the connector a name (e.g. "Firm DB").
4. Save.

From this moment, package workflows that read "your DB" (e.g. `/monday-brief` when it cites "alerts from internal_notes") see Supabase via MCP, exactly like Claude Code does.

## Security guarantees (again)

- **Permission inheritance**: the package NEVER sees more than what your connected account sees. If a teammate doesn't have access to a Drive folder with their account, they don't see it through Claude either.
- **Mandatory human approval** for any external action (email send, payment, post). Nothing is automatic.
- **Anthropic doesn't train on your business data** on Team/Enterprise plans. Contractual guarantee.

## What to do when a workflow doesn't do what you want

Three options in order of preference:

1. **Change the prompt inside the workflow**: each command accepts natural-language arguments. E.g.: `/monday-brief focusing only on retail industry clients`. The workflow obeys.
2. **Use a skill alone**: instead of launching the big workflow, you call the single skill. E.g.: `/cash-flow for the next 60 days`.
3. **Write a custom sub-agent in Claude Code**: if what you need is structurally different from what the package does (e.g. parse a specific country-particular document type), switch to Agent View. That's the "when A, when B" rule of the video.

## What NOT to do

- Don't connect ALL connectors at first onboard. Security+clarity suffer. Add them as you go.
- Don't test workflows that send emails/payments in production the first time. Sandbox first.
- Don't expect the package to know country-specific tax law peculiarities at 100%. Those remain the responsibility of your custom sub-agents.
