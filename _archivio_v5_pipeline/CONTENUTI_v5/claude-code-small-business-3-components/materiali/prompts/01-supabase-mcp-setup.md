<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/prompts/01-supabase-mcp-setup.md -->

# Prompt 01 — Supabase via MCP connector setup

Use this prompt **inside the `materiali/` folder**, by launching `claude` and pasting it right after. Claude Code runs the whole procedure, guiding you where human input is needed (creating the Supabase project, copying the keys).

## When to use it

Right away, before everything else. Without Supabase + MCP no custom sub-agent can run.

## Setup

```
cd materiali
claude
```

Then paste the prompt below.

---

## PROMPT

```
Full setup of the first component: Supabase via MCP connector.

CONTEXT:
We're building the "Claude Code for Small Business — 3 components" infrastructure.
Component 1 = Supabase database via MCP connector, where the firm's CUSTOM data
will live (clients, tax_regimes, custom_deadlines, internal_notes).

STEPS:

1. Verify the schema is present
   - Confirm that ./schema-aziendale.sql exists in this materials folder.
   - Open it briefly and show the user the 4 tables defined (clients,
     tax_regimes, custom_deadlines, internal_notes) + the 2 helpful views.

2. Guide the user to create the Supabase project
   - Explain: "go to supabase.com, create an account if you don't have one
     (free), click 'New project', pick a name (e.g. 'firm-demo' or your firm's
     name), region close to you, DB password saved in a password manager (not
     in the clear)".
   - Wait for confirmation that the project is created.

3. Load the schema
   - Explain: "Supabase panel → SQL Editor → New query → paste ALL the
     contents of schema-aziendale.sql → click Run".
   - Wait for confirmation that they see the 4 tables in Table Editor.

4. Configure credentials in .env
   - Verify .env exists (if not, copy from .env.example).
   - Ask the user:
     a) "Go to Settings → API of your Supabase project, copy the Project URL,
        paste it here (I'll put it in .env, not in the clear on screen)"
     b) "Same page, copy the service_role key. ⚠️ This key grants full
        access to the DB, never share it and never commit it."
   - Save the two values in .env to SUPABASE_URL and
     SUPABASE_SERVICE_ROLE_KEY. Confirm the save without re-printing the
     values to the screen.

5. Install the Supabase MCP connector
   - Verify that ./.claude/mcp.json exists (it's already in the materials).
   - Run in shell:
     claude mcp add supabase
   - If the command asks for URL and key interactively, take the values from
     .env.
   - If the setup was already done in the past (the entries are already in
     Claude Code's MCP registry), confirm with the user and proceed to test.

6. Test the connector
   - Run mentally (as if you were a new Claude session):
     "show me the tables in the Supabase DB and how many rows they have"
   - Show the result. Expected: 4 tables, of which tax_regimes with 5 rows
     (from the seed), the other 3 with 0 rows.
   - If you see the 4 tables: ✅ Step 1 done. Report this to the user.
   - If you see errors: diagnose (wrong key? wrong URL? project still
     initializing?) and propose the fix.

7. Next step
   - Tell the user: "Step 1 done. Step 2 is activating Claude for Small
     Business inside Claude Cowork — not something I do, you do it in the
     browser. Open prompts/02-claude-cowork-smb-onboard.md for instructions
     when you're ready."

RULES:

- Never print the service_role key to the screen after saving it.
- Don't create separate project folders: this materials folder IS the project,
  we work inside it.
- If something fails, show the error and propose the fix. Don't restart
  from scratch without telling the user.

Go.
```
