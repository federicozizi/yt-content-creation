# Automatic setup — Claude Code, read this

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali-variante-1/INIZIO_QUI.md` — keep both in sync.

You've been launched inside the materials folder of the **Personal AI Newsletter — Variant 1 (Claude Agent SDK)**. You only do: check prerequisites + venv + dependencies + API key + first run. ~5 minutes.

## What to do

### 1. Check prerequisites

```bash
python --version    # must be ≥ 3.10
```

If missing: direct user to https://www.python.org/downloads/

### 2. Show the user what the system will do

In 3 sentences:
- Every morning (when scheduled), the Python script visits the 3 Anthropic sources in `sources.json`
- Uses Claude Agent SDK to generate a markdown summary of updates in `newsletter/`
- Updates `state.json` to avoid re-proposing seen articles

### 3. Python environment setup

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
# or: .venv\Scripts\activate    on Windows
pip install -r requirements.txt
```

### 4. Configure the API key

```bash
cp .env.example .env
```

Ask the user for their Anthropic API key (`sk-ant-...` format). If they don't have one: https://console.anthropic.com → Settings → API Keys → Create Key.

Open `.env`, replace the placeholder with the real key. **Verify that `.gitignore` exists** and contains `.env`.

### 5. (Optional) Customize sources and tone

Ask:
- "Do you want to change the sources?" → open `sources.json` and help editing
- "Do you want to change the tone?" → open `CLAUDE.md`, `## Newsletter tone` section

If the user says "leave everything and do the first run", skip to step 6.

### 6. First test run

```bash
python newsletter.py
```

Wait ~1-2 minutes. The script prints progress in console while the Agent works. When done, show:
- The file generated in `newsletter/YYYY-MM-DD.md`
- The change to `state.json`

### 7. (Optional) cron scheduling

Ask: "Do you want it to start by itself every morning?"

If yes:
- Open `scheduling/crontab-example.txt` and show the line suitable for their OS
- On Mac/Linux: help with `crontab -e`, paste the line replacing the placeholder paths
- On Windows: explain activation via Task Scheduler

## Notes for you (Claude Code)

- **Don't create separate project folders**: this folder IS the project.
- **Don't commit `.env`**: it's in `.gitignore`, but if the user runs `git add -A` flag the risk.
- **Verify `claude-agent-sdk` installs without errors** — it's the critical package. If it fails, suggest `pip install --upgrade pip` and retry.
- Direct, concise tone.
- If a command fails, show the error and suggest the fix instead of starting over.
