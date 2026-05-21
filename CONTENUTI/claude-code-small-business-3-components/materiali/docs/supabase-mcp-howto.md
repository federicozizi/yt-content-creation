<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/docs/supabase-mcp-howto.md -->

# Supabase via MCP — detailed how-to

How the Supabase MCP connector works, what to do when it breaks, and the security best practices.

## What MCP is

**MCP** = Model Context Protocol. Open protocol published by Anthropic in November 2024 that lets AI models talk to external services in a structured way.

It works like this:
- A service (Supabase, GitHub, Slack, etc.) exposes an "MCP server" — a small process that declares: "here are the functions I can do, here are the parameters, here are the output types".
- Claude (Code or Cowork) connects to the server and uses those functions as additional tools, exactly like it uses Read/Write/Bash.

For small business owners: this means Claude can run SQL queries on your DB without you writing any middleware code.

## Supabase connector setup

### 1. Install the Supabase MCP server

Anthropic and Supabase distribute the official server as an npm package:

```bash
claude mcp add supabase
```

The command adds an entry to Claude Code's MCP registry (`~/.claude/mcp.json` usually, or in the project if you have a `.claude/mcp.json` like this materials folder).

### 2. Configure credentials

The server needs:
- `SUPABASE_URL`: your project's Project URL (e.g. `https://abcdefghij.supabase.co`)
- `SUPABASE_SERVICE_ROLE_KEY`: the service role key (secret!)

In this folder, we put them in `.env` and the `.claude/mcp.json` file pulls them via `${SUPABASE_URL}` and `${SUPABASE_SERVICE_ROLE_KEY}`. See `.env.example` for the template.

### 3. Verify

```bash
claude
> "List tables in the Supabase DB"
```

Expected output: list of tables + row count.

If you see an error like "MCP server not found" or "connection refused", probably:
- `SUPABASE_URL` is wrong (e.g. you put the dashboard URL `https://supabase.com/dashboard/project/xxxxx` instead of the API URL `https://xxxxx.supabase.co`).
- The service role key has been rotated or revoked.
- The Supabase project is "Paused" (happens if inactive for >7 days on the free plan). Reactivate it from the dashboard.

## What the Supabase MCP server can do

Functions exposed (at the time of this video):

- **list_tables**: DB table list
- **execute_sql**: runs an SQL query (both SELECT and INSERT/UPDATE/DELETE)
- **list_migrations**: applied migrations history
- **apply_migration**: applies a (versioned) migration
- **list_extensions**: active Postgres extensions
- **generate_typescript_types**: generates TS types from schema (handy if you have a frontend)
- **list_branches**, **create_branch**, **merge_branch**: Supabase branch management (beta feature)
- **get_advisors**: Supabase's automatic security/performance suggestions
- **get_logs**: project logs

In Claude Code, these functions appear as tools of the form `mcp__supabase__<name>`. Custom agents that declare `tools: mcp__supabase` inherit access.

## Security best practices

### Service Role Key vs Anon Key

The **service role key** bypasses Row Level Security (RLS) and has full DB access. Use it ONLY for backend agents (like our local Claude Code), NEVER for applications exposed to the public.

The **anon key** respects RLS and grants access only to what policies allow. Use it if you want Claude to see only a subset of data (e.g. only public tables, only the logged-in client).

**For this video's setup**: service role key is fine because we're in a local firm environment. But if you put Claude on a shared server or screen-share with third parties, consider switching to anon key + appropriate RLS.

### Never commit .env

`.gitignore` in this folder already excludes `.env` (with exception for `.env.example`). Verify with:

```bash
git check-ignore .env
```

Expected output: `.env` (means it's ignored). If not, check `.gitignore`.

### What to do if you've exposed the service role key by mistake

(E.g.: you put it in a public commit, in a social screenshot, you pasted it in the wrong Slack channel.)

1. **Immediately**: Supabase Dashboard → Settings → API → "Reset service_role secret". The old key stops working immediately.
2. **Update `.env`** with the new value.
3. **Check Supabase logs** (Dashboard → Database → Logs) for suspicious queries in recent days — if you find traffic you don't recognize, consider exporting the schema, removing the project, and recreating it.

## Frequent queries for the "accounting firm" case

Examples you can give directly to `claude` once MCP is working:

```
"Show me all forfettario regime clients who've billed over 80% of the limit"

"Insert a new client with company_name 'Rossi Firm LLC', VAT '12345678901', tax_regime_code 'ordinario'"

"For the client with ID X, add an internal note of type 'comment' with text 'revisit tax position for 2027' and author 'mario'"

"How many custom deadlines do we have coming up in the next 7 days?"
```

All these run via MCP — no SQL written by hand, Claude generates it.
