<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/docs/connettori-pacchetto-vs-custom.md -->

# Pre-built package vs custom sub-agents — when to use which

The recurring question, once you've set up the 3 components, is: "do I do this thing with the Anthropic package or with a custom sub-agent?"

This guide gives you the operational criteria.

## The rule in one sentence

> **If the thing you need to do is something other small businesses** in your industry or across industries also do (payroll, invoices, briefings, monthly close, marketing) → **package**.
>
> **If the thing is specific to your business model**, your niche, a local rule, or your custom Supabase data → **custom sub-agent**.

## The 5 criteria to decide

### 1. Does the thing already exist as a package workflow?

Open the list of 15 workflows (`docs/claude-for-small-business-howto.md`). If you find something similar: start there. You avoid reinventing the wheel, and Anthropic will keep it updated.

### 2. Does the thing use data that lives only in Supabase?

Example: your clients' tax regimes, the firm's internal notes, the custom deadlines you've tracked yourself.

→ **Custom sub-agent**. The package sees QuickBooks, HubSpot, Gmail — not Supabase, unless you've connected it as a custom MCP (see `claude-for-small-business-howto.md` section "How to connect Supabase via MCP to the package"). Even after connecting, the package does NOT have business logic custom to your industry — it only uses it as a lookup table.

### 3. Does the thing have local-specific rules?

Example: country-specific contract clauses, country-specific tax regime thresholds, reduced VAT rates for specific industries, municipality-level tourist taxes.

→ **Custom sub-agent**. The package is generic and US-first. Local-specific rules you have to write yourself.

### 4. Does the thing involve an external action?

Example: send emails, make payments, publish a post, sign contracts.

→ **Package**, always. The package has clean OAuth integration with the tools that perform the action (Gmail, PayPal, etc.) and crucially has built-in human approval. Writing a custom sub-agent that sends emails is masochism: you'd have to handle SMTP, deliverability, OAuth, etc.

If you need custom logic BEFORE the send (e.g. "read Supabase notes to modulate the tone"): combine the two. Custom sub-agent prepares the data in Supabase, the package reads from Supabase via MCP and does the send.

### 5. Does the thing change often?

Example: rules for a promotion that changes every 3 months, the structure of a report you're asked to revise every quarter.

→ **Custom sub-agent**, because you edit it in markdown in 30 seconds. The package is less flexible on micro-adjustments.

## Decision table (summary)

| What you need to do | Package | Custom | Both |
|---|---|---|---|
| Standard monthly accounting close | ✅ /close-month | | |
| Standard invoice reminders | ✅ /invoice-chaser | | |
| Invoice reminders with tone varying by Supabase notes | | | ✅ Custom fills Supabase, package reads and sends |
| Monday briefing | ✅ /monday-brief | | |
| Classify a particular ambiguous receipt type | | ✅ document-classifier | |
| Check tax regime threshold | | ✅ regime-checker | |
| Firm's custom deadlines (board renewal, etc.) | | ✅ deadline-alerter | |
| Marketing campaign with visuals | ✅ /run-campaign | | |
| Marketing campaign with your branding rules | | | ✅ Custom checks guidelines, package executes |
| Generic contract review | ✅ /contract-review | | |
| Contract review with country-specific clauses | | | ✅ Package does formal review, custom checks specific clauses |
| Cash flow forecast | ✅ /cash-flow | | |
| Tourist tax calculation per municipality | | ✅ Custom | |

## Common combination patterns

### Pattern 1: "Custom enriches, package executes"

- Custom sub-agent reads uploaded documents and enriches Supabase with classifications/notes.
- Package (e.g. `/close-month`) reads Supabase + standard tools and produces the final output.

Example: document-classifier classifies ambiguous receipts → /close-month counts them correctly in the deductible total.

### Pattern 2: "Custom checks, package blocked"

- Custom sub-agent verifies a condition is true before a package workflow runs.
- If the condition is false, blocks or modifies the package's behavior.

Example: regime-checker writes `invoice_chaser_flag = 'do_not_chase'` in internal_notes if a client just exceeded the limit → when you run /invoice-chaser, the package reads the flag and skips that client.

### Pattern 3: "Package scheduled, custom on-demand"

- Package workflows run at fixed frequency (Monday morning, end of month).
- Custom sub-agents run when you need them, from Agent View, with a click.

Example: /monday-brief automatic every Monday at 8, deadline-alerter on-demand before a firm meeting.

## What NOT to combine

- **Don't duplicate logic**: if /close-month already knows how to close the month, don't write `close-month-custom.md`. Instead modify the prompt you give to /close-month with additional instructions.
- **Don't bypass human approval**: if you have a custom sub-agent that sends emails without going through the package, you're hurting yourself. Always go through the package's tools for external actions.
- **Don't put business logic in both places**: if the rule "client Bianchi shouldn't be chased" is both in the package as a prompt-rule and in the sub-agent as a Supabase flag, sooner or later they'll diverge. Decide ONE place, put it there, the other reads it.
