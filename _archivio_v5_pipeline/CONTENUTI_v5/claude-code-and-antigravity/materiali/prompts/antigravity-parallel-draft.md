<!-- ⚠️ Italian twin: CONTENUTI/claude-code-e-antigravity/materiali/prompts/antigravity-parallel-draft.md -->

# Prompt for Antigravity — parallel drafting of variants

This is the prompt you paste **into each of the 3 agent sessions** you spawn in Antigravity. The only thing that changes between the 3 sessions is the word `<<STYLE>>`.

---

## Setup in the Antigravity workspace

1. Create a new workspace (e.g. `homepage-refresh-<project-name>`).
2. Upload the starting `index.html` (the current home you want to refresh).
3. Spawn 3 agent sessions, all on the same starting file.
4. In each one paste the prompt below, replacing `<<STYLE>>` with one of these three values:
   - `corporate` (formal, monochrome, trust-focused)
   - `friendly` (warm colors, people imagery, conversational tone)
   - `aggressive` (big claims, urgency, dominant CTA)
5. Hit enter in all three. They run in parallel.

---

## PROMPT to paste in each session

```
You are a senior designer/copywriter. You have the index.html uploaded to the workspace, which is the home page of an existing site.

Your task: produce a NEW version of index.html in <<STYLE>> style.

CONSTRAINTS:
- Preserve the MEANING of the page: who the brand is, what it offers, why to contact it. Change the tone and visual, not the substance.
- Preserve the semantic STRUCTURE: header, hero, main sections, footer. Don't add new sections unless the <<STYLE>> style explicitly demands them.
- Preserve the LABELS of the links in the menu (if the original had "About", "Services", "Contact", they must stay — the href can be "#" for now, but the labels are fixed).
- NO external scripts, NO CDN calls, NO Google Fonts. Inline CSS or inside <style> only.
- Single self-contained HTML file. Same name: index.html.

STYLE INTERPRETATION FOR <<STYLE>>:
- "corporate": monochrome palette (greys + 1 navy/blue accent), sober sans-serif typography, authoritative copy, short sentences, claims about reliability and experience, secondary CTA.
- "friendly": warm palette (red/orange/yellow desaturated on cream background), rounded or friendly serif typography, second-person copy, micro-stories, claims about relationship and support, "let's start together" CTA.
- "aggressive": high-contrast palette (black + 1 neon accent), bold large typography, claims in caps, numbers and percentages emphasized, sense of urgency, dominant and repeated CTA.

DELIVERABLES:
1. The rewritten index.html (single file, ready for rendering).
2. A rendered preview (Antigravity does this by default — make sure it's visible in the workspace).
3. At the end of the file, in an HTML comment, write 2 lines: the applied style and a sentence explaining the main tone choice ("I went with X because Y").

Work autonomously. When done, DON'T publish anything — leave the artifact ready for download in the workspace.
```

---

## What to expect

- Average time per agent: 2-4 minutes.
- The 3 agents run in parallel: total wait time is the slowest one, not the sum.
- Each produces 1 HTML file + 1 rendered preview + 1 screenshot.
- You don't interrupt — Antigravity notifies you when each is done.

## What to do next

1. Open the 3 previews in the workspace, place the windows side by side.
2. Pick the one that convinces you most (with your eyes, not by reading the code).
3. Right-click the winning artifact → "Download artifact" → save it as `landing-winner.html` in your site's folder (subfolder `_from_antigravity/`).
4. (Optional) Download the other 2 as `landing-<style>.html` if you want to archive them.
5. Back on your PC, open Claude Code inside the site folder, and use the prompt in `claude-code-handoff.md` for the final integration.
