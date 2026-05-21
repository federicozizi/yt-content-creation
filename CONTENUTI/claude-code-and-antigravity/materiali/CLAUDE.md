<!-- ⚠️ Italian twin: CONTENUTI/claude-code-e-antigravity/materiali/CLAUDE.md -->

# CLAUDE.md — Project rules

You are Claude Code, launched inside the `materiali/` folder of the video "Claude Code + Antigravity: how to use them together". This folder **is not the user's real project** — it's the video materials folder, containing prompts and a guide.

The **real project** is the user's site (e.g. `~/path/to/your-site/`). You'll work there when the user tells you to.

## What you do when the user says "run the setup by reading CLAUDE.md"

### 1. Verify prerequisites

Ask the user:
- "Do you already have a site (even a single `index.html`) where you want to apply this workflow?"
- If yes: ask for the absolute path of the folder.
- If no: offer to create a minimal demo one here under `sito-demo/` (header + hero + 3 sections + footer), so they can test without preparing a real site.

Check that they have access to Antigravity (`antigravity.google.com`). If they don't know what it is, send them to `../PRINCIPALE.html` section "What this integration is".

### 2. Prepare them to receive the Antigravity artifact

In their **real project**, create (if not already there):
- A subfolder `_from_antigravity/` where the HTML they download from the cloud will land.
- A `.gitignore` (if missing) with `_from_antigravity/_archive/` inside, so discarded variants aren't committed.

Explain that the flow is:
1. They go into Antigravity, do the work described in `prompts/antigravity-parallel-draft.md`.
2. They download the winning artifact and place it as `_from_antigravity/landing-winner.html`.
3. They come back here, run `claude` again inside their **site** folder, and give you the prompt from `prompts/claude-code-handoff.md`.

### 3. (When they come back with the artifact) Run the integration

When the user passes you the handoff prompt and asks you to integrate `landing-winner.html` into the existing `index.html`:

- **Read both files**: old and new.
- **Identify what to preserve from the old**:
  - Internal links (`href="/about"`, `href="/contact"`, etc.) — must remain the real site's, not the artifact's invented ones.
  - Meta tags (`<meta name="description">`, OpenGraph, etc.) — preserve.
  - Asset paths (`img src="..."`, `<link rel="stylesheet">`) — if the artifact uses new ones, choose: either keep them (but the matching files need to exist) or swap them with the old ones.
  - Analytics scripts, tracking pixels, tag manager — preserve.
- **Take from the new**:
  - Structure, copy, visual style (inline CSS or classes).
- **Show the full diff before touching the file**. Use `git diff` if the project is a repo, otherwise list changes in a clear markdown block.
- **Wait for the user's explicit OK** before overwriting `index.html`. Never apply the change silently.
- **After OK, overwrite and commit** with a message like `feat: refresh home (variant <style> from Antigravity)`. If the project isn't a git repo, skip the commit and just notify.
- **Archive discarded artifacts**: if `_from_antigravity/` has other 2 HTMLs that weren't chosen, move them to `_from_antigravity/_archive/` renaming them by style (`landing-corporate.html`, `landing-aggressive.html`).

## Tone

Direct, dry, peer-to-peer. No "great, proceeding", no "I've prepared for you". Show what you're doing, do it, that's it.

## Don't

- Never run `git push` on your own, not even after the commit. That's the user's call.
- Don't modify `index.html` without showing the diff first and getting explicit OK.
- Don't install dependencies (npm, pip): not needed here.
- Don't create "project" folders separate from this one: the video materials are only prompts and guides. The "project" is the user's site, which lives elsewhere.
- Don't overwrite files in `prompts/` — they're prompts the user must be able to copy at any time.

## References

- Full video guide: `../PRINCIPALE.html` (or `PRINCIPALE.html` in this folder, it's a copy).
- Sample final result: `example-output.md`.
