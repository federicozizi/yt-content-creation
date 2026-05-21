# Automatic setup — Claude Code, read this

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali/INIZIO_QUI.md` — keep both in sync.

You've been launched inside the materials folder of the **Personal AI Newsletter**. Everything is already here: `sources.json` with 3 example sources (Anthropic news/research/changelog), `CLAUDE.md` with the tone, `prompts/newsletter-daily.md` with the orchestrator, empty `state.json` ready to populate. You only do: check prerequisites + first test run. ~3 minutes.

## What to do

### 1. Check prerequisites

```bash
claude --version
```

If missing: `npm install -g @anthropic-ai/claude-code` (or the preferred install method on https://claude.com/code).

The user must already be logged into Claude Code with a plan (Pro/Max) or with an API key configured. Verify with:

```bash
claude /status
```

If not logged in, stop the setup and ask them to log in first.

### 2. Show the user what the system will do

In 3 sentences:
- It will visit the 3 Anthropic sources in `sources.json`
- It will summarize never-before-seen articles in a markdown file inside `newsletter/`
- It will update `state.json` to avoid re-proposing the same articles in future runs

### 3. (Optional) Customize sources or tone

Ask the user:
- "Do you want to change the sources?" If yes, open `sources.json` and help them edit/add/remove entries.
- "Do you want to change the writing tone?" If yes, open `CLAUDE.md` and show them the `## Newsletter tone` section.

If the user says "leave everything as it is and do the first run", skip directly to step 4.

### 4. First test run

Launch the orchestrator prompt:

```bash
claude --print "$(cat prompts/newsletter-daily.md)"
```

Wait for it to finish (~1-2 minutes). Show the user:
- The file created in `newsletter/YYYY-MM-DD.md`
- The change to `state.json` (URLs added to seen articles)

### 5. (Optional) Scheduling

Ask: "Do you want it to start by itself every morning?"

If yes:
- Show the guide in `scheduling/claude-routines.md`
- Help the user create the routine with `claude routines add daily-newsletter --schedule "0 8 * * *" --cwd "$(pwd)" --prompt "run prompts/newsletter-daily.md"`
- Verify with `claude routines list`

If no: explain they can always manually relaunch the command from step 4.

### 6. (Optional) Email

If they ask "can I receive it via email instead of reading it in the file?":
- Open `docs/email-optional.md`
- Email configuration requires a Gmail App Password — guide them step by step

## Notes for you (Claude Code)

- **Don't create separate project folders**: this folder IS the project.
- **Don't remove `CLAUDE.md`**: it's your persistent context (tone, rules, state management).
- **Don't manually edit `state.json`** during setup: it gets populated on the first run.
- Direct, concise tone. No academic paragraphs.
- If a command fails, show the error and suggest the fix instead of starting over.
