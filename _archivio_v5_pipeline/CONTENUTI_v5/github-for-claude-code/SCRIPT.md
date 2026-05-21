# SCRIPT — GitHub for Claude Code (EN)

> ⚠️ **Gemello italiano**: `CONTENUTI/github-per-claude-code/SCRIPT.md`. Solo le righe `🎙️ DIRE (verbatim)` cambiano lingua; il resto resta in italiano (note di regia per te).

Script per registrazione del video **"GitHub for Claude Code (even if you're not a developer)"** in lingua inglese.

Regole di sistema:
- **1 clip = 1 schermata sola.**
- **PRINCIPALE.html è la slide primaria.** Lo uso a schermo nelle clip dove devo spiegare un concetto, parlando sopra. CAMERA solo per hook, riepilogo, CTA.
- Schermate ammesse: `CAMERA` · `PRINCIPALE.html` (versione EN) · `TERMINALE` · `BROWSER GitHub` · `EDITOR/FILE`.
- Setup e installazioni → **citate al volo**, mai dimostrate. Rimando sempre ai materiali gratuiti sulla **Skool community**.

---

## 0. SETUP UNA TANTUM

- [ ] **Account GitHub throwaway** creato (es. `claude-yt-demo`).
- [ ] **Profilo browser dedicato** "YT-DEMO".
- [ ] **OBS Studio** con 3 scene: `CAM`, `SCREEN`, `SCREEN+CAM` (riserva).
- [ ] **Hotkey OBS** memorizzati.
- [ ] **Microfono** posizionato, livello picco -6dB.
- [ ] **Skool community URL** (versione EN o landing per audience anglofona).
- [ ] **Sistema billing Anthropic** funzionante.
- [ ] **OS in inglese** o UI di GitHub/Claude in inglese per coerenza.

---

## 1. PRE-REC GIORNATA (30-45 min)

### A. Credenziali del giorno

- [ ] `console.anthropic.com` → Settings → API Keys → **Create Key**. Nome: `YT-DEMO-EN-2026-05-16-REVOCARE`. Copia in un file scratch in VS Code.
- [ ] Login GitHub col throwaway account nel profilo "YT-DEMO".

### B. Repo demo pulito

```powershell
Remove-Item -Recurse -Force C:\demo-competitor-brief -ErrorAction SilentlyContinue
gh repo delete claude-yt-demo/demo-competitor-brief --yes 2>$null

Copy-Item -Recurse "C:\Users\zizif\Desktop\YT content creation\CONTENUTI\github-for-claude-code\materiali" "C:\demo-competitor-brief"
cd C:\demo-competitor-brief

gh repo create claude-yt-demo/demo-competitor-brief --private --source . --push
gh secret set ANTHROPIC_API_KEY
```

- [ ] Modifica `competitors.json` con 3 nomi verosimili internazionali
- [ ] `git add competitors.json; git commit -m "config: real competitors"; git push`

### C. Artefatti pre-cotti

```powershell
gh workflow run daily-brief.yml
gh run watch
gh pr list  # verifica PR daily-brief
```

- [ ] PR del daily-brief → **Tab 5**

```powershell
gh label create claude-task --color "8B5CF6" --description "Task to delegate to Claude"
gh issue create --title "Add Adyen to the competitors" --body "Add Adyen as 4th competitor.`nWebsite: adyen.com`nPricing: adyen.com/pricing`nLinkedIn: linkedin.com/company/adyen"
gh issue list
gh issue edit 1 --add-label claude-task
# aspetta 1-2 min
gh pr list
```

- [ ] Seconda PR → **Tab 6**

### D. File esca per Trucco 5

```powershell
cd C:\demo-competitor-brief
Copy-Item .github\hooks\pre-commit-claude-review.sh .git\hooks\pre-commit
```

- [ ] **NON creare ancora `config-leak.txt`** — file scratch in VS Code pronto con:
  ```
  # test config
  ANTHROPIC_API_KEY=sk-ant-FAKE-DEMO-NOT-REAL-abc123xyz789
  ```

### E. Worktree

- [ ] Verifica che `C:\demo-competitor-brief\.worktrees\` NON esista

### F. Tab del browser (ordine fisso)

| Tab | URL | Uso |
|---|---|---|
| T1 | `file:///.../CONTENUTI/github-for-claude-code/PRINCIPALE.html` | Slide principale (EN) |
| T2 | `github.com/claude-yt-demo/demo-competitor-brief` | Home repo |
| T3 | `github.com/claude-yt-demo/demo-competitor-brief/issues/new` | Nuova issue Trucco 4 |
| T4 | `github.com/claude-yt-demo/demo-competitor-brief/pulls` | Lista PR |
| T5 | PR del daily-brief | Risultato Trucco 3 |
| T6 | PR della issue Adyen | Risultato Trucco 4 |

- [ ] Zoom 110%, bookmark bar nascosta
- [ ] PRINCIPALE.html EN in cima. Ancore: `#what-is`, `#what-build`, `#how-works`, `#trick-1`, `#trick-2`, `#trick-3`, `#trick-4`, `#trick-5`, `#beyond`, `#recap`

### G. Terminale

- [ ] PowerShell in `C:\demo-competitor-brief`, font **Cascadia Code 18pt**, prompt corto, history pulita

### H. Lavagnetta digitale (opzionale — 2 pagine per il hook)

Testi in inglese:

1. **GITHUB = OFFICE FOR CLAUDE**
2. **5 TRICKS → 1 SYSTEM**

Per il resto del video la lavagnetta NON serve.

### I. Verifiche finali

- [ ] Focus Assist attivo, notifiche/Slack chiusi
- [ ] OBS test 30s → controllo audio → cancella

**Da qui in poi: REC ON → fai → REC OFF.**

---

## 2. CLIP — ELENCO COMPLETO

Totale: **23 clip** (3 CAMERA, 9 PRINCIPALE.html, 11 demo). Tempo target video finale: 16-20 minuti.

| # | Schermata | Tipo | Argomento |
|---|---|---|---|
| 01 | CAMERA | LIVE | Hook |
| 02 | PRINCIPALE.html | LIVE | What is GitHub |
| 03 | PRINCIPALE.html | LIVE | What we'll build |
| 04 | PRINCIPALE.html | LIVE | How it works |
| 05 | CAMERA | LIVE | Quick setup + Skool reference |
| 06 | PRINCIPALE.html | LIVE | Trick 1 — Persistent memory |
| 07 | EDITOR | LIVE | Trick 1 demo: CLAUDE.md |
| 08 | PRINCIPALE.html | LIVE | Trick 2 — Worktree |
| 09 | TERMINALE | LIVE | Trick 2 demo: `git worktree add` |
| 10 | TERMINALE | PRE-COTTO | Trick 2 demo: 3 Claude Code |
| 11 | TERMINALE | LIVE | Trick 2 demo: `gh pr create` |
| 12 | PRINCIPALE.html | LIVE | Trick 3 — GitHub Actions |
| 13 | EDITOR | LIVE | Trick 3 demo: `daily-brief.yml` |
| 14 | TERMINALE | LIVE | Trick 3 demo: `gh workflow run` |
| 15 | BROWSER GitHub | PRE-COTTO | Trick 3 demo: resulting PR |
| 16 | PRINCIPALE.html | LIVE | Trick 4 — Issues from phone |
| 17 | BROWSER GitHub | LIVE | Trick 4 demo: create issue |
| 18 | BROWSER GitHub | PRE-COTTO | Trick 4 demo: resulting PR |
| 19 | PRINCIPALE.html | LIVE | Trick 5 — Pre-commit hook |
| 20 | TERMINALE | MISTO | Trick 5 demo: blocked commit |
| 21 | PRINCIPALE.html | LIVE | Other uses of the pattern |
| 22 | CAMERA | LIVE | Recap |
| 23 | CAMERA | LIVE | CTA Skool + consulting |

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`
- Lavagnetta pagine 1 e 2 a portata

**🎙️ DIRE (verbatim):**
> If you use Claude Code, you probably open it, give it a task, it works, you close it. And it forgets everything.
> In this video I'll show you 5 tricks to turn Claude into an assistant that works 24 hours a day, even with your PC off, that receives tasks from your phone, and that delivers results ready for you to approve.
> The tool that makes this possible is called GitHub. *(turn the whiteboard pg. 1)* Yes, GitHub. No, you don't have to write code.

**🖥️ MOSTRARE:** te in camera, lavagnetta sull'ultima frase.

**🎬 LIVE**

---

## CLIP 02 — What is GitHub

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html EN), scrolla a `#what-is`

**🎙️ DIRE (parla sopra la slide):**
- GitHub is an online platform where you keep project folders (repos)
- Free up to 2000 minutes/month of automations
- 4 things we need: **Repo**, **Issue**, **Pull request**, **Actions** — scorrile col cursore mentre le citi
- Leggi a voce il box giallo

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "What is GitHub". Fermati sul box giallo 3 secondi.

**🎬 LIVE**

---

## CLIP 03 — What we'll build

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#what-build`

**🎙️ DIRE (parla sopra):**
- We'll use the same example as the previous video: a brief on the 3 competitors that arrives ready every morning at 7
- Difference from before: this time it runs by itself in the cloud, you launch nothing
- Mostra il diagramma, leggi i passaggi a voce
- Key sentence: "it costs a few cents per day and the example is the brief, but at the end of the video we'll see that the same 5 tricks work for any recurring flow"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "What we'll build today". Diagramma scuro 8-10 secondi.

**🎬 LIVE**

---

## CLIP 04 — How it works

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#how-works`

**🎙️ DIRE (parla sopra):**
- 5 tricks, from the simplest to the most powerful
- Puntali a schermo sul diagramma di architettura
- Anticipa: 3 tricks active in the repo (CLAUDE.md, Pull Request, Actions), 2 local on the PC (Worktree, Pre-commit)

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "How the system works". Diagramma scuro al centro.

**🎬 LIVE**

---

## CLIP 05 — Quick setup (Skool reference)

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> To follow this video you need 4 things: a free GitHub account, Claude Code installed, an Anthropic API key, and the materials I'm using today.
> It costs about $20/month for the Claude subscription, or under $2/month of API if you prefer pay-per-use. GitHub is free.
> The whole setup — account, key, first test — is already documented in the materials. You find the complete folder for free in my Skool community, link below. You download it, open Claude Code inside, tell it "run the setup", and in 5 minutes the system runs.
> I won't waste time showing how to install things. Let's go straight to the 5 tricks.

**🖥️ MOSTRARE:** te in camera, parli diretto.

**🎬 LIVE**

---

## CLIP 06 — Trick 1 (Persistent memory)

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html EN), scrolla a `#trick-1`

**🎙️ DIRE (verbatim per il concetto):**
> Trick number 1: persistent memory.
> Problem: every time you open Claude Code, it starts from zero. It doesn't know you want output in English, it doesn't know your tone of voice, it doesn't know which files it shouldn't touch.
> Solution: a file called CLAUDE.md at the root of the repo. Claude reads it automatically at the start of every session. Write the rules once, they're valid forever.

Poi a voce libera:
- Leggi il box giallo puntandolo
- Cita i 3 punti di "What it solves"
- Anticipa la demo: "now I'll show you a real CLAUDE.md, already written"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trick 1. Soffermati sul box giallo.

**🎬 LIVE**

---

## CLIP 07 — Trick 1 demo: CLAUDE.md

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-competitor-brief\CLAUDE.md` aperto, font 16pt

**🎙️ DIRE (punti):**
- "This is the real CLAUDE.md of our demo repo"
- Leggi `## Conventions`: output language English, brief max 400 words, no committed secrets
- Mostra `## Key files`: here I tell Claude which files it can touch and when
- Key point: "if tomorrow a colleague enters or launches a session in the cloud, they start already aligned to these rules. Zero re-explaining."

**🖥️ MOSTRARE:** EDITOR con CLAUDE.md aperto. Scrolla dall'alto al basso.

**🎬 LIVE**

---

## CLIP 08 — Trick 2 (Worktree)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#trick-2`

**🎙️ DIRE (verbatim per il concetto):**
> Trick number 2: three Claudes in parallel, without stepping on each other's toes.
> You have three independent tasks today. If you launch them one after the other in the same folder, you waste time. If you launch them all together in the same folder, they step on each other: they modify the same files, they overwrite.
> Solution: a thing from git called "worktree". It's like having 3 separate rooms for 3 different Claudes. Each works in its own, the original stays untouched.

Poi a voce libera:
- Leggi il box giallo
- Cita i 3 punti di "What it solves"
- Anticipa demo: "now we actually create 3 worktrees"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trick 2.

**🎬 LIVE**

---

## CLIP 09 — Trick 2 demo: create worktree

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`
- `git status` → "nothing to commit"

**🎙️ DIRE (punti):**
- "Now I create 3 worktrees, one for each task"
- Digita commentando

**🖥️ MOSTRARE:** TERMINALE:

```powershell
git worktree add .worktrees\add-delta -b feat/delta
git worktree add .worktrees\change-model -b feat/model
git worktree add .worktrees\fix-linkedin -b fix/linkedin
git worktree list
```

**🎬 LIVE**

---

## CLIP 10 — Trick 2 demo: 3 Claude Code in action

**🧰 Cosa preparare prima della camera:**
- 3 finestre Claude Code Desktop già aperte, ognuna nel rispettivo worktree

**🎙️ DIRE (punti):**
- "Three windows, three worktrees, three tasks"
- Mostra che in ognuna scrivi un prompt diverso
- Key point: "they work in parallel, each one only sees its own file system, zero conflicts"

**🖥️ MOSTRARE:** TERMINALE — desktop con 3 finestre affiancate.

**🎬 PRE-COTTO**

---

## CLIP 11 — Trick 2 demo: pull request

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief\.worktrees\add-delta`
- Almeno 1 modifica da committare

**🎙️ DIRE (punti):**
- "When a worktree produces a result I like, I turn it into a pull request"

**🖥️ MOSTRARE:** TERMINALE:

```powershell
git add .
git commit -m "feat: add delta corp"
git push -u origin feat/delta
gh pr create --fill
```

**🎬 LIVE**

---

## CLIP 12 — Trick 3 (GitHub Actions)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#trick-3`

**🎙️ DIRE (verbatim per il concetto):**
> Trick number 3: Claude works even with your PC off.
> You want a report every morning at 7. You can't keep the PC on all night. Local cron isn't enough because if you close the laptop, everything stops.
> Solution: GitHub Actions. It's an automation system that runs on GitHub's servers, not on your PC. You write a small recipe — "at 7 every day, start Claude and have it do X" — and GitHub runs it forever, free up to 2000 minutes per month.

Poi a voce libera:
- Leggi il box giallo
- Costi: ~30 minutes/month of Actions + ~$0.30-1.50/month of API
- Anticipa demo

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trick 3.

**🎬 LIVE**

---

## CLIP 13 — Trick 3 demo: the workflow file

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-competitor-brief\.github\workflows\daily-brief.yml` aperto

**🎙️ DIRE (punti):**
- "This is the file that tells GitHub what to do and when"
- Indica `cron: "5 7 * * *"` → "every day at 7:05"
- Indica gli `steps:` → "take the repo, install Claude, execute the prompt, open a PR"
- Key point: "this file is already in the materials, you don't have to write it from scratch"

**🖥️ MOSTRARE:** EDITOR con `daily-brief.yml`. Soffermati su cron e steps.

**🎬 LIVE**

---

## CLIP 14 — Trick 3 demo: manual launch

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`

**🎙️ DIRE (punti):**
- "I launch the workflow manually, without waiting for 7 tomorrow morning"

**🖥️ MOSTRARE:** TERMINALE:

```powershell
gh workflow run daily-brief.yml
```

→ "✓ Created workflow_dispatch event"

**🎬 LIVE** — stacca qui.

---

## CLIP 15 — Trick 3 demo: resulting PR

**🧰 Cosa preparare prima della camera:**
- Tab 5 attiva (PR pre-cotta del daily-brief)
- Vista "Files changed"

**🎙️ DIRE (punti):**
- "This is the PR that arrived one minute after the last run"
- Mostra il file `briefs/YYYY-MM-DD.md`: new file, ~30 lines
- Leggi a voce i primi 3 "TOP INSIGHT"
- Key point: "if I like it I click Merge, it enters main, and tomorrow another one arrives. That's it."

**🖥️ MOSTRARE:** BROWSER GitHub. Tab 5, vista Files changed.

**🎬 PRE-COTTO**

---

## CLIP 16 — Trick 4 (Issues from phone)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#trick-4`

**🎙️ DIRE (verbatim per il concetto):**
> Trick number 4: delegate tasks from your phone in 30 seconds.
> An idea hits you while you're out: "it would be nice to add a new competitor". Normally: you go home, open the PC, launch Claude, explain, check, save. Five, ten minutes.
> Solution: open the GitHub app on your phone. You write an "issue" — it's a digital sticky note with the task. You add a label. A GitHub Action listens for the event, runs Claude in the cloud, it implements the change and opens a pull request. When you get home you have the proposal ready for approval.

Poi a voce libera:
- Leggi il box giallo
- Formula: **issue = command, label = submit, pull request = response**
- Anticipa demo

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trick 4.

**🎬 LIVE**

---

## CLIP 17 — Trick 4 demo: create issue

**🧰 Cosa preparare prima della camera:**
- Tab 3 attiva (`github.com/.../issues/new`)
- Browser vista mobile

**🎙️ DIRE (punti):**
- "Let's pretend I'm out, I open GitHub on my phone"
- Scrivi titolo + descrizione, aggiungi label, submit

**🖥️ MOSTRARE:** BROWSER GitHub vista mobile.

**Dati**:
- Title: `Add Klarna as 5th competitor`
- Body: `Add Klarna as a new competitor. Website: klarna.com. Pricing: klarna.com/business/pricing. LinkedIn: linkedin.com/company/klarna.`
- Labels: `claude-task`

**🎬 LIVE** — stacca dopo submit.

---

## CLIP 18 — Trick 4 demo: resulting PR

**🧰 Cosa preparare prima della camera:**
- Tab 6 attiva (PR pre-cotta della issue Adyen)
- Vista "Files changed"

**🎙️ DIRE (punti):**
- "This is the PR that arrived 60 seconds after adding the label to a similar issue"
- Mostra il diff su `competitors.json`: 4 lines added
- Key point: "if I like it I merge, if not I close. Zero risk."

**🖥️ MOSTRARE:** BROWSER GitHub. Tab 6, vista Files changed.

**🎬 PRE-COTTO**

---

## CLIP 19 — Trick 5 (Pre-commit hook)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#trick-5`

**🎙️ DIRE (verbatim per il concetto):**
> Trick number 5, the last one: automatic quality check before saving.
> Typical scenario: you're about to save some changes. Maybe there's a password you copied by mistake inside, a private note, a forgotten TODO.
> Solution: a small script that git runs automatically before every save. The script sends the changes to Claude, Claude reads them in 2 seconds, and gives you an OK or a BLOCK. If BLOCK, the save doesn't go through and tells you what to fix.

Poi a voce libera:
- Leggi il box giallo
- "What it solves": no committed passwords, no TODOs, no notes
- Anticipa demo

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trick 5.

**🎬 LIVE**

---

## CLIP 20 — Trick 5 demo: blocked commit

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`
- Hook pre-commit attivo
- VS Code con uno scratch file pronto col contenuto del file esca

**🎙️ DIRE (punti):**
- "I create a file with the innocent name 'config' and put an API key inside by mistake"
- Provo a salvarlo, mostro il blocco

**🖥️ MOSTRARE:** TERMINALE:

```powershell
code config-leak.txt
# (incolla, salva, chiudi VS Code)

git add config-leak.txt
git commit -m "test config"
```

→ Output atteso:
```
🔍 Claude review in progress...
❌ BLOCK: possible API key detected in config-leak.txt
   Looks like an Anthropic key (sk-ant-...).
To bypass (at your risk): git commit --no-verify
```

Poi:
```powershell
git restore --staged config-leak.txt
Remove-Item config-leak.txt
```

**🎬 MISTO** — `git add`/`commit` LIVE; screenshot backup in `C:\demo-recovery\hook-output.png`.

---

## CLIP 21 — Other uses of the pattern

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html EN), scrolla a `#beyond`

**🎙️ DIRE (punti):**
- "The brief example is one of a thousand ways these 5 tricks combine"
- Scorri i 5 use case a video, commentali:
  - Daily lead qualification
  - Weekly reputation audit
  - Internal knowledge base
  - Social content generation
  - Onboarding new collaborators
- Key sentence: "the pattern is always the same. Only what Claude does changes"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Other practical uses". Fermati su ogni use case 3-4 secondi.

**🎬 LIVE**

---

## CLIP 22 — Recap

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Recap of the 5 tricks:
> One: CLAUDE.md in the repo, persistent memory, rules once and they last forever.
> Two: git worktree, three Claudes in parallel without stepping on each other.
> Three: GitHub Actions, Claude in the cloud on schedules you decide, even with your PC off.
> Four: issue with label, you delegate tasks from your phone in 30 seconds.
> Five: pre-commit hook, automatic quality check before every save.
> Everything is already configured. You download, launch Claude Code inside the folder, and in 5 minutes the system runs.

**🖥️ MOSTRARE:** te in camera.

**🎬 LIVE**

---

## CLIP 23 — CTA Skool + consulting

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> The complete material — workflows, hooks, prompts, example CLAUDE.md files — is free in my Skool community. Link in the description below. Free membership, you download everything, and if you have questions ask them there.
> If you want to adapt this pattern to your industry — lead qualification, audit, knowledge base, content — and don't feel like doing it alone, reach out: contacts are always in the description.
> If you found this video useful, leave a like and subscribe. See you in the next one.

**🖥️ MOSTRARE:** te in camera, sguardo dritto sull'ultima frase.

**🎬 LIVE**

---

## 3. POST-REC (5 minuti)

- [ ] `console.anthropic.com` → Settings → API Keys → trova `YT-DEMO-EN-...` → **Revoke**
- [ ] Cancella la chiave dal file scratch in VS Code
- [ ] `gh secret list` sul repo demo: verifica
- [ ] Chiudi tab del browser YT-DEMO + logout
- [ ] Backup grezzo delle clip su disco esterno
- [ ] (Opzionale) `gh repo delete claude-yt-demo/demo-competitor-brief --yes`
- [ ] (Opzionale) `Remove-Item -Recurse -Force C:\demo-competitor-brief`

---

## 4. CHECKLIST DI MONTAGGIO

- [ ] Ordine clip 01 → 23 rispettato
- [ ] Tagli secchi tra schermate diverse
- [ ] Clip PRE-COTTO ben raccordate alla LIVE precedente (audio continuo)
- [ ] Su CLIP 15 e CLIP 18 (PR pre-cotte): blurra eventuali dati personali
- [ ] CTA finale (CLIP 23) ha link in descrizione del video pronto
- [ ] Audio normalizzato a -14 LUFS
- [ ] Sottotitoli: genera in automatico in inglese, rivedi nomi tecnici
- [ ] Coerenza linguistica: PRINCIPALE.html mostrato a video è la versione EN
