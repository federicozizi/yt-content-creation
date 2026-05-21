<!-- ⚠️ Italian twin: CONTENUTI/claude-code-e-antigravity/materiali/README.md -->

# Claude Code + Antigravity — video materials

Combined workflow: Antigravity explores in parallel (cloud), you pick, Claude Code integrates locally.

**Nothing to install beyond Claude Code and a Google account.** The files in here are prompts and rules — copy and paste.

## What's in this folder

```
.
├── README.md                                  ← you're reading this
├── CLAUDE.md                                  ← Claude Code reads it on its own: project memory
├── .gitignore                                 ← protects private artifacts
├── PRINCIPALE.html                            ← a copy of the video guide, handy offline
├── prompts/
│   ├── antigravity-parallel-draft.md          ← prompt to paste in Antigravity
│   └── claude-code-handoff.md                 ← prompt to give Claude Code locally
└── example-output.md                          ← what the result looks like after the workflow
```

## Quick start (3 moves)

```
# 1. Open Antigravity in the browser (antigravity.google.com),
#    upload your index.html into the workspace, spawn 3 sessions.
#    In each one, paste the prompt from prompts/antigravity-parallel-draft.md
#    changing only the word STYLE.

# 2. When the 3 agents finish, pick the best preview,
#    download the artifact as "landing-winner.html"
#    and place it in this folder.

# 3. Run Claude Code inside your real site folder:
cd ~/path/to/your-site
claude
#    and paste the prompt from prompts/claude-code-handoff.md
```

That's it. No venv, no API key, no pip install: it's two tools you already use, in order.

## Automatic setup (alternative)

Run `claude` inside this folder and type:

> "Run the setup by reading CLAUDE.md."

Claude Code reads the project rules and walks you through (a) verifying you have a site to work on, (b) preparing the structure to receive the artifact from Antigravity, (c) loading the handoff prompt when you come back from the cloud.

## Security

- Antigravity works in an isolated sandbox, so it doesn't see your local files. Upload only files you're comfortable exposing to the cloud (a public landing's `index.html` is usually fine).
- The artifact you download from Antigravity is static HTML. Open it in VS Code before passing it to Claude Code, to glance-check there are no suspicious external scripts.
- The `.gitignore` in this folder excludes the `_archive/` subfolder where discarded artifacts end up: nothing sensitive, but nothing to commit either.

## For the video audience

In the video I showed the "refresh a home page" case. The pattern works for anything made of files: emails in N tones, client proposals from N angles, documentation in N voices. The Antigravity part only changes its prompt, the Claude Code part only changes "which file to integrate the artifact into".
