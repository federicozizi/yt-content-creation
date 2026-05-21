<!-- ⚠️ Italian twin: CONTENUTI/claude-code-piccoli-business-3-componenti/materiali/prompts/02-claude-cowork-smb-onboard.md -->

# Prompt 02 — Activating the Claude for Small Business package

This step happens **in the browser, inside Claude Cowork**. It's not something Claude Code can do for you: the Small Business package is a Cowork plugin, not a Code plugin.

But Claude Code can **prepare the way** for you and then **read/write the same Supabase** the package will use — see `prompts/04-end-to-end-integration.md` for how the two talk to each other.

## What to do in the browser (no Claude Code)

### 1. Verify your plan

- Log into `claude.com/cowork`.
- If you don't see "Cowork" in the side navigation, you have the single Pro plan. You need to upgrade to **Team** (~$25/user/month). Go to Settings → Plan → Upgrade.
- If you see Cowork: good, proceed.

### 2. Launch the package onboarding

Open a new Cowork chat and type:

```
/smb-onboard
```

The guided procedure starts (Anthropic calls it "Small Business setup"). Answer these questions:

- **Business industry**: pick the closest match (accounting / law firm / e-commerce / agency / trades / other).
- **Tools you already use**: it offers a list. Check only the ones you actually use (e.g. QuickBooks for accounting, Google Workspace for email and Drive). Don't check everything.
- **Permissions**: for each checked tool, a standard OAuth flow runs in the browser. Give consent. Anthropic has pre-registered the app, so you DON'T need Google Cloud console, you DON'T need manual credentials.json.

### 3. Verify the workflows are available

At the end of onboarding you'll see a new "Small Business" section in the sidebar with the 15 activated workflows. Try:

```
/monday-brief
```

Expected output: a summary that cites current cash (from QuickBooks if connected) and new leads (from HubSpot if connected). If it says "data not available" for some source, that tool isn't connected — go back to add it only if you need it.

## What to do next (back in Claude Code)

When you've completed onboarding in the browser:

```bash
cd materiali
claude
```

And paste:

```
The Claude for Small Business package has been activated in Cowork.
Update ./README.md to mark this status (add a "Setup status" section with
three entries: Supabase MCP ✓ | Claude for Small Business ✓ | Agent View ⏳).
Then proceed to prompt 03 for the custom sub-agents.
```

## Things to NOT do

- Don't connect ALL the tools on the list. Start with 2-3 you actually use. Add others only when you need them.
- Don't test workflows that perform external actions (e.g. `/invoice-chaser` or `/run-campaign`) in production the first time. Use a sandbox QuickBooks / HubSpot if possible for the first runs, or stop before the final approval so nothing actually sends.
- Don't screen-share Cowork logged in publicly: the sidebar shows real business data once the tools are connected.

## References

- Official announcement: https://www.anthropic.com/news/claude-for-small-business
- Plugin page: https://claude.com/plugins/small-business
- Detailed how-to: `docs/claude-for-small-business-howto.md` in this folder
