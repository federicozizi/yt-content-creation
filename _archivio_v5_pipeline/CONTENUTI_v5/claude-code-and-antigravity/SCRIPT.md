# SCRIPT.md — Claude Code + Antigravity: how to use them together

> ⚠️ Gemello italiano: `CONTENUTI/claude-code-e-antigravity/SCRIPT.md`.
> Solo le righe `🎙️ DIRE` qui sono in inglese — il resto (PRE-REC, MOSTRARE, LIVE/PRE-COTTO/MISTO, POST-REC, montaggio) resta **in italiano** perché sono note per il regista.

Durata target: **7 minuti**.
Stile: pratico, conversazionale. Un workflow chiaro, un caso d'esempio, un pattern che generalizza.

---

## 0. SETUP UNA TANTUM

Cose della vita, da fare una sola volta e basta:

- Account Google con accesso ad Antigravity attivo (verifica login a `antigravity.google.com`).
- Profilo Chrome dedicato "youtube-demo" — niente cronologia personale, niente estensioni inutili.
- Claude Code installato globalmente (`claude --version` deve funzionare).
- OBS configurato con due scene: `BROWSER` (1920x1080, finestra Chrome) e `TERMINALE` (1920x1080, terminale a tutto schermo, font 18pt, prompt minimale).
- Microfono testato, livello -12dB di picco.
- Webcam con sfondo neutro per le clip CAMERA.

---

## 1. PRE-REC GIORNATA (30-40 min prima di registrare)

Tutto quello che NON deve essere fatto live, da preparare prima di accendere la camera:

### Account e ambiente
- [ ] Login a `antigravity.google.com` con il profilo Chrome "youtube-demo". Verifica che il workspace creato per la demo (`homepage-refresh-demo`) sia vuoto e pronto.
- [ ] Terminale aperto nella cartella `~/demo/mio-sito-fake/` (sito demo già preparato — vedi sotto).

### Repo demo
- [ ] Cartella `~/demo/mio-sito-fake/` esiste e contiene un `index.html` brutto-ma-funzionante (header, hero, 3 sezioni, footer). Stile generico, copy bidimensionale: deve essere chiaramente "una home che ha bisogno di un refresh".
- [ ] Dentro c'è anche una sottocartella `materiali/` con i 2 prompt pronti da copiare.
- [ ] `git status` deve essere pulito.

### Artefatti pre-cotti (BACKUP)
- [ ] Tre file HTML pre-generati in `~/demo/backup/`: `landing-corporate.html`, `landing-friendly.html`, `landing-aggressive.html`. Servono solo se Antigravity è lento o down.
- [ ] Screenshot delle 3 preview salvati in `~/demo/backup/screenshots/`.

### Tab del browser in ordine fisso
1. Antigravity workspace (dashboard pronta, vuota)
2. PRINCIPALE.html locale (per le clip slide — versione EN)
3. Il sito demo "vecchio" aperto in localhost

### Terminale
- [ ] Cwd in `~/demo/mio-sito-fake/`
- [ ] Prompt impostato per essere leggibile (es. `PS1='\W $ '`)
- [ ] History pulita

### Materiali clip
- [ ] PRINCIPALE.html (EN) aperto in VS Code in parallelo per consultazione
- [ ] Copione clip-per-clip stampato o su secondo monitor

---

## 2. CLIP — elenco completo

| # | Schermata | Durata | Modalità |
|---|---|---|---|
| 01 | CAMERA | ~25s | LIVE |
| 02 | PRINCIPALE.html `#cosa-e` | ~50s | LIVE |
| 03 | PRINCIPALE.html `#cosa-costruiremo` | ~40s | LIVE |
| 04 | PRINCIPALE.html `#come-funziona` | ~30s | LIVE |
| 05 | PRINCIPALE.html `#setup` | ~25s | LIVE |
| 06 | PRINCIPALE.html `#step-1` | ~25s | LIVE |
| 07 | BROWSER Antigravity | ~70s | MISTO (live spawn, preview accelerata in editing) |
| 08 | PRINCIPALE.html `#step-2` | ~20s | LIVE |
| 09 | BROWSER Antigravity | ~40s | LIVE (scelta + download) |
| 10 | PRINCIPALE.html `#step-3` | ~25s | LIVE |
| 11 | TERMINALE (Claude Code) | ~60s | LIVE |
| 12 | PRINCIPALE.html `#oltre` | ~35s | LIVE |
| 13 | CAMERA | ~20s | LIVE |
| 14 | CAMERA | ~25s | LIVE (CTA verbatim) |

**Totale stimato**: ~7 min.

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`.
- Postura aperta, sguardo dritto in camera.

**🎙️ DIRE (verbatim):**
> "You're using Claude Code and that's fine. Now there's also Antigravity, Google's new agent IDE, and you've asked yourself: should I use them together? In 7 minutes I'll show you how. No forcing it — each one does the piece it's best at, and you put them in order."

**🖥️ MOSTRARE:** Solo CAMERA. Niente lavagnetta — il tempo è poco, la prima slide HTML arriva subito dopo.

**🎬 LIVE**

---

## CLIP 02 — Cos'è questa integrazione

**🧰 Cosa preparare prima della camera:**
- Switcha a tab PRINCIPALE.html, scorri fino alla sezione `#cosa-e`. Verifica che i due box `.concetto-chiave` siano entrambi visibili senza scrollare.

**🎙️ DIRE (verbatim per il concetto, libero per i punti):**
> "Claude Code and Antigravity are both AI agents working for you, but they live in opposite places and do opposite things. Antigravity lives in the cloud: open the browser, give it an instruction, it spawns agents in parallel — each one works on its own and returns files you can preview and approve. Claude Code lives on your PC: sees your real files, edits your repo, makes the commits. Putting them together isn't about making them fight. It's about giving each one the piece of work they're best at."

**🖥️ MOSTRARE:** PRINCIPALE.html scrollato a `#cosa-e`. Punta col cursore i 2 box gialli `.concetto-chiave` mentre li commenti.

**🎬 LIVE**

---

## CLIP 03 — Cosa faremo oggi (case study)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#cosa-costruiremo`. Verifica che il diagramma `.diagram` sia ben visibile.

**🎙️ DIRE (verbatim):**
> "Concrete case to demonstrate the pattern: refresh the home page of a site you already have. You've got an index.html that looks tired. You want to see 3 different visual versions before deciding. And you want the winner stitched into your repo, not floating around in the cloud. Three moves: Antigravity churns out 3 variants in parallel, you pick with your eyes, Claude Code does the final mile at home."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-costruiremo`. Soffermati sul diagramma ASCII per ~10s.

**🎬 LIVE**

---

## CLIP 04 — Come funziona

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#come-funziona`. La lista numerata dei 3 pezzi deve essere visibile.

**🎙️ DIRE:**
> "Three pieces in sequence. Antigravity Manager: the browser interface where you give one prompt and it dispatches it to N agents. Artifacts: the files and previews each agent produces — you don't read code, you look at the render. Claude Code: the final mile, on your PC, takes the chosen version and integrates it into your real project. Division rule, read the yellow box: explore in the cloud, cut and stitch locally."

**🖥️ MOSTRARE:** PRINCIPALE.html `#come-funziona`. Punta il box `.concetto-chiave` finale.

**🎬 LIVE**

---

## CLIP 05 — Setup

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#setup`. Lista checks visibile.

**🎙️ DIRE:**
> "Minimum setup: Google account with Antigravity access, Claude Code you already use, a project folder with your index.html. If you don't have a site, the materials include a demo one ready to go. For the operational setup: inside the materials folder run claude and tell it 'run the setup by reading CLAUDE.md'. One minute."

**🖥️ MOSTRARE:** PRINCIPALE.html `#setup`. Punta la lista `ul.checks`.

**🎬 LIVE**

---

## CLIP 06 — Step 1 (concetto)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#step-1`. Concetto-chiave visibile sopra il fold.

**🎙️ DIRE:**
> "First step, the piece you couldn't do quickly on your own: generate 3 alternatives at the same time, in 3 separate environments. Claude Code is sequential — one instance, one machine, one thing at a time. Antigravity spawns 3 agents in the cloud with a click. Three heads in parallel, you wait only once. In our case: corporate style, friendly, aggressive. Three almost identical prompts, only the word STYLE changes."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-1`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 07 — Demo Antigravity (spawn + lavoro parallelo)

**🧰 Cosa preparare prima della camera:**
- Switcha a tab Antigravity (workspace `homepage-refresh-demo`, vuoto).
- Apri in un secondo monitor il file `materiali/prompts/antigravity-parallel-draft.md` da cui copierai il prompt.
- Tieni a portata il vecchio `index.html`.

**🎙️ DIRE (libero, da commento mentre fai):**
> "I upload the starting file, spawn 3 sessions, paste the prompt in each one changing only the style. Hit enter on all three. Now they work together, not in line. While they work, the dashboard tells me where each one is."

**🖥️ MOSTRARE:** BROWSER su Antigravity. Mostra: workspace → upload `index.html` → spawn 3 sessioni → paste prompt × 3 → run. Le 3 barre di progresso nella dashboard.

**🎬 MISTO**
> Spawn delle 3 sessioni LIVE (3-4 min accelerati a ~30s in editing). Rendering dei progressi in time-lapse 4-8x.

---

## CLIP 08 — Step 2 (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-2`. Concetto-chiave visibile.

**🎙️ DIRE:**
> "When the 3 agents finish, Antigravity doesn't dump a blob of code on you to read. It shows you the render. Three previews side by side. You judge with your eyes in 30 seconds per version: this one's too cold, this one's shouting, this one's got the right tone."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 09 — Demo Antigravity (scelta + download artefatto)

**🧰 Cosa preparare prima della camera:**
- Le 3 sessioni in Antigravity hanno terminato (se non è arrivato in tempo, usa i 3 file pre-cotti in `~/demo/backup/`).
- Apri le 3 preview affiancate (split view, o 3 tab adiacenti).

**🎙️ DIRE (libero, da commento):**
> "Three homes, side by side. The corporate is cold. The aggressive is shouting. The friendly's claim is weak but the tone is right. I take the friendly. Right click, download artifact, save it as landing-winner.html in the materials folder of my site."

**🖥️ MOSTRARE:** BROWSER Antigravity con le 3 preview, poi il flusso di download.

**🎬 LIVE**

---

## CLIP 10 — Step 3 (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-3`. Concetto-chiave visibile.

**🎙️ DIRE:**
> "The HTML I downloaded is nice but disconnected from my project. It uses made-up links, doesn't have my meta tags, may have renamed files that already exist. Antigravity was working in a sandbox — it knew nothing about my repo. Claude Code does. It reads everything, understands what to preserve, and makes a clean commit. It's the final mile at home."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 11 — Demo Claude Code (integrazione locale)

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `TERMINALE`. Cwd in `~/demo/mio-sito-fake/`.
- Il file `landing-winner.html` è già salvato in `./materiali/` o pre-cotto.
- Apri in secondo monitor `materiali/prompts/claude-code-handoff.md`.

**🎙️ DIRE (libero, da commento):**
> "I open Claude Code in the site folder. Paste the handoff prompt: read landing-winner.html, fuse it with index.html keeping links, meta and assets, and show me the diff before touching the file. It reads both files, proposes the merge. Diff on screen: I drop the weak claim, accept the new sections, keep my internal links that it recognized. I approve. Commit with a sensible message. Done."

**🖥️ MOSTRARE:** TERMINALE: `cd ~/demo/mio-sito-fake && claude` → paste prompt → diff → accept → commit.

**🎬 LIVE** (se la generazione del diff è lenta, accelera 2x in editing; il commit finale realtime).

---

## CLIP 12 — Oltre il caso

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#oltre`. I 5 box `.use-case` visibili scrollando lentamente.

**🎙️ DIRE:**
> "The schema works every time you have multiple plausible paths and a human eye needs to choose. Sales emails in three tones. Client proposal from three angles. Competitor audit in parallel, one per competitor. Product documentation in three voices. Idea testing with three mini-landings. Antigravity explores, you pick, Claude Code closes."

**🖥️ MOSTRARE:** PRINCIPALE.html `#oltre`. Scrolla lentamente attraverso i 5 box.

**🎬 LIVE**

---

## CLIP 13 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`.

**🎙️ DIRE (verbatim):**
> "Quick recap. Antigravity when you need to explore in parallel: three versions instead of one, without overheating your PC. Claude Code when you need to close the loop inside the real project: real files, your structure, your commits. The bridge is the artifact: download from Antigravity, hand it to Claude Code. No magic API, no hard integration. Just a workflow with you in the middle being the judge."

**🖥️ MOSTRARE:** CAMERA. Sguardo dritto.

**🎬 LIVE**

---

## CLIP 14 — CTA Skool + consulenza

**🧰 Cosa preparare prima della camera:**
- Resta su CAMERA.
- Tieni gli URL community/consulenza pronti per il lower-third in editing.

**🎙️ DIRE (verbatim — non improvvisare):**
> "If you're into other AI-to-AI integration patterns — Claude Code with n8n, with GitHub Actions, with Antigravity in more complex workflows — they're in the Skool community, link in the description. It's where I share the workflows I actually use, with prompts and configurations. If you have a specific case at your company and you want to know whether the parallel-plus-local pattern solves a real problem, there's also direct consulting: we start from your actual flow and I tell you which piece belongs in the cloud and which one belongs locally. Link in the description for that too. See you in the next video."

**🖥️ MOSTRARE:** CAMERA. Sorriso a fine frase, poi taglio.

**🎬 LIVE**

---

## 3. POST-REC (sicurezza)

Subito dopo aver fermato la registrazione:

- [ ] Logout dal workspace Antigravity demo.
- [ ] Cancella la cartella `~/demo/mio-sito-fake/.git` se hai pushato durante le prove.
- [ ] Verifica che `landing-winner.html` non contenga dati personali o chiavi.
- [ ] Chiudi Claude Code (`exit`).
- [ ] Salva i raw OBS in `~/registrazioni/<data>-claude-antigravity-en/`.

---

## 4. CHECKLIST MONTAGGIO

- [ ] Ordine clip: 01 → 14.
- [ ] Time-lapse della CLIP 07 a ~30 secondi.
- [ ] Lower-third sui link Skool/consulenza nella CLIP 14.
- [ ] Audio: noise gate, EQ, compressione leggera. Livello di uscita -14 LUFS.
- [ ] Sottotitoli EN autogenerati + correzione manuale dei nomi propri.
- [ ] Censure: nessuna.
- [ ] Thumbnail (versione EN): split del frame con preview Antigravity a sinistra e terminale Claude Code a destra. Testo: "1 + 1 = 5 in 7 minutes".
- [ ] Descrizione video (in inglese): link al repo template, link Skool, link consulenza.
- [ ] End screen: card al video precedente sul workflow parallelo + iscriviti.
