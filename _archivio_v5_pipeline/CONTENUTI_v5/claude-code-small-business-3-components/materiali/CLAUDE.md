<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/CLAUDE.md -->

# CLAUDE.md — Project rules

You are Claude Code, launched inside the `materiali/` folder of the video "Claude Code for Small Business: the 3 essential components". This folder **IS THE project** — don't create separate project folders.

The project assembles 3 components that must talk to each other:
1. **Supabase via MCP connector** — DB for the firm's custom data
2. **Claude for Small Business** (Anthropic) — package of pre-built workflows, lives in Cowork
3. **Agent View** — custom sub-agents in `.claude/agents/`, live in Claude Code

## What you do when the user says "run the setup by reading CLAUDE.md"

Work in 3 sequential phases. Each phase corresponds to a prompt in `prompts/`.

### Phase 1 — Supabase via MCP

Run the instructions in `prompts/01-supabase-mcp-setup.md`. They've been written specifically for this flow, apply them word for word. At the end the verification must pass ("4 tables seen").

### Phase 2 — Claude for Small Business

This is NOT something you can do. It's an activation the user does in the browser, inside Claude Cowork.

What you do:
- Explain to the user what it is and where it lives (`docs/claude-for-small-business-howto.md` has everything).
- Tell them to open `prompts/02-claude-cowork-smb-onboard.md` and follow the steps.
- When the user confirms "done", update `README.md` "Setup status" section marking Step 2 ✓.

### Phase 3 — Custom sub-agents

Run the instructions in `prompts/03-launch-custom-agents.md`. Launch at least regime-checker to demonstrate the agents work. Show the user the new rows generated in `internal_notes` on Supabase.

### Phase 4 (bonus, if the user asks) — End-to-end integration

Open `prompts/04-end-to-end-integration.md` and guide the user through the flow alternating terminal and browser. Show the final verification point: the Anthropic package reads `internal_notes` from Supabase when you run `/invoice-chaser` in Cowork.

## Tone

Direct, dry, peer-to-peer. No "great, proceeding", no "I've prepared for you". Show what you're doing, do it, that's it. The user is a small business owner — use their time the way they use it.

## Things to NOT do

- **Don't commit `.env`** — it's already in `.gitignore`, verify before any `git add`.
- **Don't run `git init` on your own** — this project isn't necessarily a git repo; if the user wants to version it, let them decide.
- **Don't install npm/pip dependencies** — the only thing we need is the Supabase MCP server, which `claude mcp add supabase` installs via `npx` on the fly. No venv, no requirements.txt.
- **Don't write middleware code** — all Claude↔Supabase communication goes through MCP. No Python wrappers, no custom APIs.
- **Don't overwrite files in `prompts/`, `docs/`, `.claude/agents/`** during an execution — they're the baseline materials, must stay as in the video. Exception: the user explicitly says "modify `regime-checker.md` adding X".
- **Don't perform external actions** (emails, payments, published posts) from custom agents. Those go through the Anthropic package in Cowork, with human approval.

## When something fails

Show the error clearly, hypothesize the cause (wrong Supabase URL? service role key revoked? project in Paused state?), propose the fix. DO NOT restart from scratch without telling the user.

## References

- Video guide: `PRINCIPALE.html` in this folder (copy of the one in the parent).
- SQL schema: `schema-aziendale.sql`.
- Sub-agents: `.claude/agents/document-classifier.md`, `regime-checker.md`, `scadenza-allerter.md`.
- Anthropic announcement: https://www.anthropic.com/news/claude-for-small-business
