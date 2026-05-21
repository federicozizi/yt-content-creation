# Automatic setup — Claude Code, read this

> ⚠️ Italian twin: `CONTENUTI/newsletter-personale-ai-con-claude-code/materiali-variante-2/INIZIO_QUI.md` — keep both in sync.

You've been launched inside the materials folder of the **Personal AI Newsletter — Variant 2 (Anthropic API + HTML/RSS parsing)**. You only do: prerequisites + venv + dependencies + API key + first run. ~5 minutes.

## What to do

### 1. Check prerequisites

```bash
python --version    # must be ≥ 3.10
```

If missing: direct to https://www.python.org/downloads/

### 2. Show what the system will do

In 3 sentences:
- The script downloads HTML/RSS of the 3 sources in `sources.json`
- For each new article (not in `state.json`), it passes the clean text to Claude API for summarization
- Saves a markdown file in `newsletter/YYYY-MM-DD.md`

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

Ask the user for the Anthropic API key (`sk-ant-...`). If they don't have one: https://console.anthropic.com → Settings → API Keys.

### 5. (Optional) Customize sources and prompt

- "Do you want to change the sources?" → open `sources.json`. Explain the difference between `type: html` (needs CSS selector) and `type: rss` (more stable, no selector).
- "Do you want to change the tone?" → open `prompt.txt`. It's pure text, you edit it without constraints.

### 6. First test run

```bash
python newsletter.py
```

Wait ~1-2 minutes. Show at the end:
- The file generated in `newsletter/YYYY-MM-DD.md`
- The change to `state.json`

### 7. (Optional) Scheduling

Open `scheduling/crontab-example.txt`, show the user the line suitable for their OS.

## Notes for you (Claude Code)

- **Don't create separate project folders**.
- **Verify dependency installation**: `pip install` can fail on Windows for BeautifulSoup/lxml. If it happens, suggest `pip install --upgrade pip` first.
- Direct tone.
- If a command fails, show the error and suggest the fix.
