# SCRIPT — Your personal AI newsletter with Claude Code (EN)

> ⚠️ **Gemello italiano**: `CONTENUTI/newsletter-personale-ai-con-claude-code/SCRIPT.md`. Solo le righe `🎙️ DIRE (verbatim)` cambiano lingua; il resto resta in italiano (note di regia per te).

Script per registrazione del video **"Your personal AI newsletter with Claude Code"** in lingua inglese.

Regole di sistema:
- **1 clip = 1 schermata sola.**
- **PRINCIPALE.html è la slide primaria.** Lo uso a schermo nelle clip dove devo spiegare un concetto, parlando sopra. CAMERA solo per hook, riepilogo, CTA.
- Schermate ammesse: `CAMERA` · `PRINCIPALE.html` (versione EN) · `TERMINALE` · `EDITOR/FILE` · `FILE BROWSER/EXPLORER`.
- Setup e installazioni → **citate al volo**, mai dimostrate. Rimando sempre ai materiali gratuiti sulla **Skool community**.

---

## 0. SETUP UNA TANTUM

- [ ] **Profilo browser dedicato** "YT-DEMO".
- [ ] **OBS Studio** con 3 scene: `CAM`, `SCREEN`, `SCREEN+CAM` (riserva).
- [ ] **Hotkey OBS** memorizzati.
- [ ] **Microfono** posizionato, livello picco -6dB.
- [ ] **Claude Code** loggato sul PC di registrazione.
- [ ] **Skool community URL** (versione EN o landing per audience anglofona).
- [ ] **OS in inglese** o quanto meno UI di Claude Code in inglese, per coerenza.

---

## 1. PRE-REC GIORNATA (20-30 min)

### A. Cartella demo pulita

```powershell
Remove-Item -Recurse -Force C:\demo-newsletter -ErrorAction SilentlyContinue
Copy-Item -Recurse "C:\Users\zizif\Desktop\YT content creation\CONTENUTI\personal-ai-newsletter-with-claude-code\materiali" "C:\demo-newsletter"
cd C:\demo-newsletter

Get-Content state.json
# Deve mostrare: { "seen_articles": [], "last_run": null }

Test-Path newsletter
# Deve dire: False
```

- [ ] `state.json` vuoto, cartella `newsletter/` non esistente

### B. Pre-warming Anthropic news

Verifica 1 ora prima della registrazione che `https://www.anthropic.com/news` abbia articoli recenti. Se necessario, aggiungi temporaneamente in `sources.json` una fonte molto attiva con HTML statico per garantire output non vuoto durante il LIVE.

### C. Tab del browser (ordine fisso)

| Tab | URL | Uso |
|---|---|---|
| T1 | `file:///.../CONTENUTI/personal-ai-newsletter-with-claude-code/PRINCIPALE.html` | Slide principale (EN) |
| T2 | `https://www.anthropic.com/news` | Per mostrare la fonte se serve |

- [ ] Zoom browser a **110%**, bookmark bar nascosta
- [ ] PRINCIPALE.html in cima. Ancore: `#what-is`, `#what-build`, `#how-works`, `#setup`, `#step-1`, `#step-2`, `#step-3`, `#step-4`, `#beyond`, `#recap`

### D. Terminale

- [ ] PowerShell in `C:\demo-newsletter`, font **Cascadia Code 18pt**, prompt corto, history pulita.

### E. Editor

- [ ] VS Code, font 16pt
- [ ] File pronti da aprire al momento giusto: `C:\demo-newsletter\sources.json`, `C:\demo-newsletter\CLAUDE.md`

### F. Esplora risorse

- [ ] Finestra aperta a `C:\demo-newsletter\`, vista "Dettagli"

### G. Lavagnetta digitale (opzionale — 1 pagina)

Solo 1 pagina, per CLIP 01 (hook). Testo in inglese:

1. **PERSONAL AI NEWSLETTER** (testo grande)

Per il resto del video la lavagnetta NON serve: la slide HTML fa il lavoro.

### H. Verifiche finali

- [ ] Focus Assist Windows attivo, notifiche chiuse, telefono silenzioso
- [ ] OBS test 30s → controllo audio → cancella

**Da qui in poi: REC ON → fai → REC OFF.**

---

## 2. CLIP — ELENCO COMPLETO

Totale: **19 clip** (3 CAMERA, 8 PRINCIPALE.html, 8 demo). Tempo target video finale: 14-17 minuti.

| # | Schermata | Tipo | Argomento |
|---|---|---|---|
| 01 | CAMERA | LIVE | Hook |
| 02 | PRINCIPALE.html | LIVE | What is a personal AI newsletter |
| 03 | PRINCIPALE.html | LIVE | What we'll build (shows output example) |
| 04 | PRINCIPALE.html | LIVE | How it works |
| 05 | CAMERA | LIVE | Quick setup + Skool reference |
| 06 | PRINCIPALE.html | LIVE | Step 1 — The sources |
| 07 | EDITOR | LIVE | Step 1 demo: sources.json |
| 08 | PRINCIPALE.html | LIVE | Step 2 — The tone |
| 09 | EDITOR | LIVE | Step 2 demo: CLAUDE.md |
| 10 | PRINCIPALE.html | LIVE | Step 3 — The first run |
| 11 | TERMINALE | LIVE | Step 3 demo: launch claude |
| 12 | EDITOR/FILE EXPLORER | LIVE | Step 3 demo: generated file |
| 13 | PRINCIPALE.html | LIVE | Step 4 — Scheduling |
| 14 | TERMINALE | LIVE | Step 4 demo: claude routines add |
| 15 | PRINCIPALE.html | LIVE | Step 5 — Agent team |
| 16 | EDITOR | LIVE | Step 5 demo: the 2 sub-agent files |
| 17 | PRINCIPALE.html | LIVE | Other uses of the pattern |
| 18 | CAMERA | LIVE | Recap |
| 19 | CAMERA | LIVE | CTA Skool + consulting |

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`
- Lavagnetta pagina 1 (`PERSONAL AI NEWSLETTER`) rivolta verso di te

**🎙️ DIRE (verbatim):**
> How many times a day do you open Twitter, LinkedIn, Hacker News, industry blogs, just to not miss what's new? And how many times do you actually find something useful?
> In this video we're building a system that does exactly this for you. Every morning, while you have breakfast, you find on your desk a file with the 3-5 things that truly matter to you, summarized in 30 lines. *(turn the whiteboard)* Your personal AI newsletter, written by Claude, just for you.

**🖥️ MOSTRARE:** te in camera, lavagnetta che giri sull'ultima frase.

**🎬 LIVE**

---

## CLIP 02 — What is a personal AI newsletter

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html EN), scrolla a `#what-is`

**🎙️ DIRE (parla sopra la slide):**
- Normal newsletter: written by one person, sent to thousands, topics you often don't care about, ads in the middle
- Personal AI newsletter: written by Claude for *you only*, your sources, your frequency, your tone
- Leggi il box giallo `.concetto-chiave` puntandolo col cursore
- Scendi sui 5 bullet (local, private, editable in 30s, schedulable, no duplicates) commentandoli

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "What is a personal AI newsletter". Fermati sul box giallo 3 secondi.

**🎬 LIVE**

---

## CLIP 03 — What we'll build

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#what-build`

**🎙️ DIRE (parla sopra):**
- "To demonstrate the pattern we'll use a simple, verifiable case: a newsletter on Anthropic's new releases"
- Mostra il blocco diagram con l'esempio output, leggi a voce "Your AI Brief — Friday May 16, 2026" e i 3 titoli
- Key point: "you open the file, read in 90 seconds, you know as much as someone who spends 2 hours a day following the ecosystem"
- Anticipa: "the example is Anthropic, but at the end of the video we'll see that the same pattern works for any site"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "What we'll build today". Diagramma scuro al centro 8-10 secondi.

**🎬 LIVE**

---

## CLIP 04 — How it works

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#how-works`

**🎙️ DIRE (parla sopra):**
- "Only 3 pieces, all text files you edit with VS Code"
- Mostra il diagramma di architettura
- Spiega i 4 file: `sources.json`, `CLAUDE.md`, `prompts/`, `state.json`
- Key point: "no Python, no external APIs, no databases. Just Claude and files"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "How the system works".

**🎬 LIVE**

---

## CLIP 05 — Quick setup (Skool reference)

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> To follow this video you need 2 things: Claude Code installed — works on Mac, Windows and Linux — and the materials I'm using today.
> It costs about $20/month for the Claude subscription, or if you prefer pay-per-use it'll cost you under $2/month of API.
> The materials are free in my Skool community, link below. Download the folder, open Claude Code inside, tell it "run the setup", and in 3 minutes you have your first newsletter.
> I won't waste time showing how to install Claude. Let's go straight to the 4 steps.

**🖥️ MOSTRARE:** te in camera, parli diretto.

**🎬 LIVE**

---

## CLIP 06 — Step 1 (The sources)

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html EN), scrolla a `#step-1`

**🎙️ DIRE (verbatim per il concetto, libero sul resto):**
> Step number 1: the sources.
> The sources are the sites Claude visits every morning. To tell it "read these" there's a file: `sources.json`. You edit it with VS Code. Add a source, remove one, in 10 seconds.

Poi a voce libera:
- Leggi il box giallo puntandolo
- Mostra il blocco JSON di esempio, le 3 fonti
- Anticipa: "now I'll show you the real file"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 1.

**🎬 LIVE**

---

## CLIP 07 — Step 1 demo: sources.json

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-newsletter\sources.json` aperto

**🎙️ DIRE (punti):**
- "This is the real file"
- Indica i 3 blocchi: name, URL, category
- "If tomorrow I want to add OpenAI's blog, I copy one of these blocks, change the URL, save. Done."
- Modifica live, aggiungi 1 voce per mostrare quanto è semplice

**🖥️ MOSTRARE:** EDITOR con `sources.json` aperto.

**🎬 LIVE**

---

## CLIP 08 — Step 2 (The tone)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#step-2`

**🎙️ DIRE (verbatim per il concetto):**
> Step number 2: the tone.
> A poorly written newsletter is worse than no newsletter. If Claude writes paragraphs of 10 lines and uses words like "revolutionary" and "incredible", you'll never read the file. To tell it how to write, there's the file `CLAUDE.md`. You edit it once, it lasts forever.

Poi a voce libera:
- Leggi il box giallo
- Indica le 3 sezioni dell'esempio: Tone, What to emphasize, What to skip
- "20 lines of rules that apply to all future runs"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 2.

**🎬 LIVE**

---

## CLIP 09 — Step 2 demo: CLAUDE.md

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-newsletter\CLAUDE.md` aperto

**🎙️ DIRE (punti):**
- "This is the real file"
- Scrolla alle 3 sezioni
- Mostra le regole "max 3-5 bullets per article", "no generic intros", "no marketing adjectives"
- Key point: "Claude reads it automatically at startup. I never have to repeat these rules."

**🖥️ MOSTRARE:** EDITOR con `CLAUDE.md` aperto.

**🎬 LIVE**

---

## CLIP 10 — Step 3 (The first run)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#step-3`

**🎙️ DIRE (verbatim per il concetto):**
> Step number 3: the first run. Now we start Claude for the first time and see if what we expect actually arrives. One single command.

Poi a voce libera:
- Leggi il box giallo
- Cita i 4 passaggi visibili
- Anticipa: "now we do it for real, live"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 3.

**🎬 LIVE**

---

## CLIP 11 — Step 3 demo: launch claude

**🧰 Cosa preparare prima della camera:**
- Terminale PowerShell in `C:\demo-newsletter`
- `state.json` vuoto, `newsletter/` non esistente

**🎙️ DIRE (punti):**
- "I'm in the folder. I launch the orchestrator prompt."
- Digita commentando

**🖥️ MOSTRARE:** TERMINALE. Comando:

```powershell
claude --print "$(Get-Content prompts\newsletter-daily.md -Raw)"
```

→ Claude stampa i suoi step. Lascia ~60-90 secondi commentando: "it's visiting the Anthropic news page… now research… now the changelog…"

→ Output finale:
```
✅ Newsletter generated: newsletter/2026-05-16.md
   - 3 sources consulted
   - 5 new articles found
   - 3 articles included
   - 2 articles skipped (filler)
   - Total time: 67 seconds
```

**🎬 LIVE**

⚠️ Se la run è lenta/scarna: in post-produzione accelera 4-8x la parte di output. Se fallisce: stacca, modifica `sources.json`, rilancia.

---

## CLIP 12 — Step 3 demo: the newsletter file

**🧰 Cosa preparare prima della camera:**
- File Explorer aperto su `C:\demo-newsletter\`, VS Code pronto

**🎙️ DIRE (punti):**
- "I open the folder, I see that a new folder appeared: `newsletter/`"
- Doppio-click → vedi `YYYY-MM-DD.md` → doppio-click → si apre in VS Code
- Leggi a voce i primi 2-3 titoli
- Key point: "this is what arrives every morning. 30 lines, 90 seconds of reading."

**🖥️ MOSTRARE:** FILE EXPLORER + EDITOR (flusso continuo).

**🎬 LIVE**

---

## CLIP 13 — Step 4 (Scheduling)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#step-4`

**🎙️ DIRE (verbatim per il concetto):**
> Step number 4: the scheduling.
> It works, we've seen it. But if I have to launch it by hand every morning, it's a hassle. We want it to start by itself. For this there's Claude Routines: a system built into Claude Code that starts prompts at times you decide. One line of config.

Poi a voce libera:
- Leggi il box giallo
- Indica i 3 passi
- "From tomorrow morning at 8 you'll always find a new file"
- Cita nota su Task Scheduler/cron come fallback

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 4.

**🎬 LIVE**

---

## CLIP 14 — Step 4 demo: claude routines add

**🧰 Cosa preparare prima della camera:**
- Terminale PowerShell in `C:\demo-newsletter`

**🎙️ DIRE (punti):**
- "I create the routine: just one command line"
- Digita commentando ogni pezzo
- Verifica con `claude routines list`

**🖥️ MOSTRARE:** TERMINALE. Comandi:

```powershell
claude routines add daily-newsletter `
  --schedule "0 8 * * *" `
  --cwd $PWD `
  --prompt "run prompts/newsletter-daily.md"

claude routines list
```

→ Output:
```
📋 Active routines:
   • daily-newsletter — every day at 08:00 — next: tomorrow 08:00
```

**🎬 LIVE**

---

## CLIP 15 — Step 5 (Agent team)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#step-5`

**🎙️ DIRE (verbatim per il concetto):**
> Step number 5: let's make the system smart.
> Now we add 2 small specialized agents that activate automatically when needed. One does the "rescue" if the day is empty, fishing out content from secondary sources. The other is a "spotter" that highlights major updates — a new model, a new tool — at the top of the file, so you never miss them. The main orchestrator calls them automatically. You do nothing.

Poi a voce libera:
- Leggi il box giallo `.concetto-chiave` puntandolo
- Indica i 2 box `.use-case` (empty-day-rescue 🚑 e major-update-spotter 🚨), commentali brevemente
- Mostra il diagramma scuro coi flow
- Anticipa la demo: "now I'll show you the 2 agent files, they're just text"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 5. Soffermati sul box giallo e sul diagramma scuro.

**🎬 LIVE**

---

## CLIP 16 — Step 5 demo: the 2 sub-agent files

**🧰 Cosa preparare prima della camera:**
- VS Code con 2 tab aperte: `C:\demo-newsletter\.claude\agents\empty-day-rescue.md` e `.claude\agents\major-update-spotter.md`
- Font 16pt

**🎙️ DIRE (punti):**
- "These are the 2 agent files. Just text. Let's open the first."
- Su `empty-day-rescue.md`: indica il frontmatter YAML in cima (`name`, `description`, `tools`) → "this tells Claude Code: there's a sub-agent, called X, does Y, can use these tools"
- Scrolla sulle istruzioni in inglese del corpo del file → "the rest is plain English instructions: when they call you, go to the fallback sources, fish out 1-2 contents, add them to the file"
- Switcha tab a `major-update-spotter.md`: stesso pattern, frontmatter + istruzioni
- Key point: "no code. They're text files. Tomorrow you want to add a 3rd agent — a fact-checker, a translator — you create a new file in here, tell the orchestrator when to call it, done."

**🖥️ MOSTRARE:** EDITOR con i 2 file sub-agent. Switcha tra le 2 tab durante la spiegazione.

**🎬 LIVE**

---

## CLIP 17 — Other uses of the pattern

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#beyond`

**🎙️ DIRE (punti):**
- "We built a newsletter on Anthropic news, but the system works for any case"
- Scorri i 5 use case, commentali brevemente:
  - Competitor newsletter
  - B2B industry newsletter
  - Academic paper newsletter
  - Social trend newsletter
  - "Clipping" newsletter for brand monitoring
- Key sentence: "you change 2 files — `sources.json` and `CLAUDE.md` — and Claude works for another case. The rest is identical."

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Beyond Anthropic". Fermati su ogni use case 3-4 secondi.

**🎬 LIVE**

---

## CLIP 18 — Recap

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Recap of the 5 steps:
> One: define the sources in `sources.json` — the sites you want to monitor.
> Two: define the tone in `CLAUDE.md` — how Claude should write.
> Three: launch the first run — one single command, and you have your first newsletter.
> Four: schedule with Claude Routines — one line, and it starts by itself every morning.
> Five: add the sub-agent team — two small files in `.claude/agents/` that handle empty days and highlight major updates at the top of the file. Zero worries.
> Everything is already configured in the materials. You download, launch Claude Code inside, in 3 minutes the system runs.

**🖥️ MOSTRARE:** te in camera.

**🎬 LIVE**

---

## CLIP 19 — CTA Skool + consulting

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> The complete material — example `sources.json`, ready `CLAUDE.md`, orchestrator prompt, scheduling guide, email option — is free in my Skool community. Link in the description. Free membership, you download everything, and if you have questions ask them there.
> If you want to adapt the system to your industry — competitor monitoring, brand monitoring, custom industry newsletter — and don't feel like doing it alone, reach out: contacts are always in the description.
> If you found this video useful, leave a like and subscribe. See you in the next one.

**🖥️ MOSTRARE:** te in camera, sguardo dritto.

**🎬 LIVE**

---

## 3. POST-REC (5 minuti)

- [ ] Backup grezzo delle clip su disco esterno
- [ ] (Opzionale) Cancella la cartella demo: `Remove-Item -Recurse -Force C:\demo-newsletter`
- [ ] Niente chiavi API da revocare

---

## 4. CHECKLIST DI MONTAGGIO

- [ ] Ordine clip 01 → 19 rispettato
- [ ] Tagli secchi tra schermate diverse
- [ ] Su CLIP 11: accelerazione 4-8x della parte centrale di output
- [ ] Su CLIP 12: file newsletter senza dati personali
- [ ] Su CLIP 16 (2 file sub-agent): font editor a 16pt minimo per leggibilità del frontmatter YAML
- [ ] CTA finale (CLIP 19) ha link in descrizione del video pronto
- [ ] Audio normalizzato a -14 LUFS
- [ ] Sottotitoli: genera in automatico in inglese, rivedi nomi file (`sources.json`, `CLAUDE.md`, `Claude Routines`)
- [ ] Coerenza linguistica: PRINCIPALE.html mostrato a video è la versione EN
