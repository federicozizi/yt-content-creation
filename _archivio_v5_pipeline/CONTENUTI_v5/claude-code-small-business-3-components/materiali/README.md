<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/README.md -->

# Claude Code for Small Business — video materials

The 3 essential components: Supabase via MCP, Claude for Small Business (Anthropic package), Agent View with custom sub-agents.

**Nothing exotic to install beyond Claude Code, a free Supabase account, and a Claude Cowork Team plan.**

## What's in this folder

```
.
├── README.md                                  ← you're reading this
├── CLAUDE.md                                  ← Claude Code reads it on its own: project rules
├── .gitignore                                 ← protects .env and other sensitive files
├── .env.example                               ← Supabase credentials template
├── PRINCIPALE.html                            ← copy of the video guide, offline
├── schema-aziendale.sql                       ← 4 ready Supabase tables
├── example-output.md                          ← what the final result looks like
├── .claude/
│   ├── mcp.json                               ← Supabase MCP connector config
│   └── agents/
│       ├── document-classifier.md             ← sub-agent: classifies ambiguous documents
│       ├── regime-checker.md                  ← sub-agent: tax regime threshold alerts
│       └── scadenza-allerter.md               ← sub-agent: morning custom deadlines
├── prompts/
│   ├── 01-supabase-mcp-setup.md               ← Step 1 setup
│   ├── 02-claude-cowork-smb-onboard.md        ← Step 2 setup (in browser)
│   ├── 03-launch-custom-agents.md             ← Step 3 setup
│   └── 04-end-to-end-integration.md           ← full 3-component flow
└── docs/
    ├── supabase-mcp-howto.md                  ← MCP in detail, troubleshooting, security
    ├── claude-for-small-business-howto.md     ← the Anthropic package A-Z
    └── package-vs-custom.md                   ← when to use one vs the other
```

## Quick start (3 steps in ~30 minutes)

```
# 1. Step 1 — Supabase via MCP
cp .env.example .env             # then fill in SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY
claude
# Paste the prompt from prompts/01-supabase-mcp-setup.md.

# 2. Step 2 — Claude for Small Business
# All in the browser, NOT in terminal. Open claude.com/cowork (requires Team plan),
# type /smb-onboard in the chat, follow instructions in prompt 02.

# 3. Step 3 — Agent View with custom sub-agents
claude
# Paste the prompt from prompts/03-launch-custom-agents.md.

# 4. (Bonus) See all 3 working together
# Follow prompts/04-end-to-end-integration.md (alternates terminal and browser).
```

## Automatic setup (alternative)

Run `claude` inside this folder and type:

> "Run the setup by reading CLAUDE.md."

Claude Code starts from Step 1, guides you step by step, asks for human input when needed (Supabase project creation, package activation in Cowork) and proceeds on its own where it can.

## Setup status

Update these entries as you complete each step (Claude Code can do this for you at the end of each):

- [ ] Step 1 — Supabase via MCP active
- [ ] Step 2 — Claude for Small Business package active in Cowork
- [ ] Step 3 — Custom sub-agents working in Agent View
- [ ] Integration — Supabase visible from both Code and Cowork (see prompts/04)

## For the video audience

In the video I used the accounting firm as the case study. The schema is industry-agnostic — see the "Beyond the accounting firm" section of PRINCIPALE.html for how to apply it to a law firm, e-commerce, agency, B&B, trades.

## Credential security

- `.env` with the Supabase service_role key is already protected by `.gitignore`. Don't remove it.
- The Anthropic package manages its own OAuths inside Cowork — they're never saved in this folder.
- If you've exposed the service_role key by mistake (public commit, screenshot, etc.), go IMMEDIATELY to Supabase Settings → API → "Reset service_role secret" and update `.env`. Details in `docs/supabase-mcp-howto.md` security section.
