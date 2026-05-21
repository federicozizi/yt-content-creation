# SCRIPT — La tua newsletter AI personale con Claude Code (IT)

> ⚠️ **Gemello inglese**: `CONTENUTI/personal-ai-newsletter-with-claude-code/SCRIPT.md`. Ogni modifica qui DEVE essere replicata nel gemello (solo `🎙️ DIRE` cambia lingua; il resto resta in italiano).

Script per registrazione del video **"La tua newsletter AI personale con Claude Code"**.

Regole di sistema:
- **1 clip = 1 schermata sola.** Mai mischiare CAMERA + SCHERMO nella stessa clip.
- **PRINCIPALE.html è la slide primaria.** Lo uso a schermo nelle clip dove devo spiegare un concetto, parlando sopra. CAMERA solo per hook, riepilogo, CTA.
- Schermate ammesse: `CAMERA` · `PRINCIPALE.html` · `TERMINALE` · `EDITOR/FILE` · `FILE BROWSER/EXPLORER`.
- Setup e installazioni → **citate al volo**, mai dimostrate. Rimando sempre ai materiali gratuiti sulla **Skool community**.

---

## 0. SETUP UNA TANTUM

- [ ] **Profilo browser dedicato** "YT-DEMO" (Firefox o Chrome). Nessun bookmark personale.
- [ ] **OBS Studio** con 3 scene: `CAM`, `SCREEN`, `SCREEN+CAM` (riserva).
- [ ] **Hotkey OBS** per switchare scena (es. F8 = CAM, F9 = SCREEN).
- [ ] **Microfono** posizionato, livello picco testato a -6dB.
- [ ] **Claude Code** loggato col tuo abbonamento (Pro o Max) sul PC di registrazione.
- [ ] **Skool community URL** memorizzato (lo dici a memoria nella CTA finale).

---

## 1. PRE-REC GIORNATA (20-30 min)

### A. Cartella demo pulita

```powershell
Remove-Item -Recurse -Force C:\demo-newsletter -ErrorAction SilentlyContinue
Copy-Item -Recurse "C:\Users\zizif\Desktop\YT content creation\CONTENUTI\newsletter-personale-ai-con-claude-code\materiali" "C:\demo-newsletter"
cd C:\demo-newsletter

Get-Content state.json
# Deve mostrare: { "articoli_visti": [], "ultimo_run": null }

Test-Path newsletter
# Deve dire: False
```

- [ ] `state.json` vuoto, cartella `newsletter/` non esistente

### B. Pre-warming Anthropic news

Verifica 1 ora prima della registrazione che `https://www.anthropic.com/news` carichi normalmente e abbia articoli recenti. Se necessario, aggiungi temporaneamente in `fonti.json` una fonte molto attiva con HTML statico (es. `https://simonwillison.net/`) per garantire output non vuoto durante il LIVE.

### C. Tab del browser (ordine fisso)

| Tab | URL | Uso |
|---|---|---|
| T1 | `file:///.../CONTENUTI/newsletter-personale-ai-con-claude-code/PRINCIPALE.html` | Slide principale |
| T2 | `https://www.anthropic.com/news` | Per mostrare visivamente la fonte se serve |

- [ ] Zoom browser a **110%**, bookmark bar nascosta
- [ ] PRINCIPALE.html in cima. Test scroll a ogni ancora: `#cosa-e`, `#cosa-costruiremo`, `#come-funziona`, `#setup`, `#step-1`, `#step-2`, `#step-3`, `#step-4`, `#oltre`, `#riepilogo`

### D. Terminale

- [ ] PowerShell aperta in `C:\demo-newsletter`, font **Cascadia Code 18pt**, prompt corto: `function prompt { "PS> " }`, `Clear-History; cls`

### E. Editor

- [ ] VS Code, font 16pt, tema chiaro per leggibilità
- [ ] 2 file pronti da aprire al momento giusto (NON aperti adesso): `C:\demo-newsletter\fonti.json`, `C:\demo-newsletter\CLAUDE.md`

### F. Esplora risorse

- [ ] Una finestra di Esplora risorse aperta a `C:\demo-newsletter\`, vista "Dettagli"

### G. Lavagnetta digitale (opzionale — 1 pagina)

Solo 1 pagina, da mostrare nella CLIP 01 (hook) come supporto visivo:

1. **NEWSLETTER PERSONALE AI** (testo grande)

Per il resto del video la lavagnetta NON serve: la slide HTML fa il lavoro.

### H. Verifiche finali

- [ ] Focus Assist Windows attivo, Slack/Discord/Outlook chiusi, telefono silenzioso
- [ ] OBS test 30s → controllo audio → cancella

**Da qui in poi: REC ON → fai → REC OFF.**

---

## 2. CLIP — ELENCO COMPLETO

Totale: **19 clip** (3 CAMERA, 8 PRINCIPALE.html, 8 demo). Tempo target video finale: 14-17 minuti.

| # | Schermata | Tipo | Argomento |
|---|---|---|---|
| 01 | CAMERA | LIVE | Hook |
| 02 | PRINCIPALE.html | LIVE | Cos'è una newsletter AI personale |
| 03 | PRINCIPALE.html | LIVE | Cosa costruiremo (mostra esempio output) |
| 04 | PRINCIPALE.html | LIVE | Come funziona |
| 05 | CAMERA | LIVE | Setup veloce + rimando Skool |
| 06 | PRINCIPALE.html | LIVE | Step 1 — Le fonti |
| 07 | EDITOR | LIVE | Step 1 demo: fonti.json |
| 08 | PRINCIPALE.html | LIVE | Step 2 — Il tono |
| 09 | EDITOR | LIVE | Step 2 demo: CLAUDE.md |
| 10 | PRINCIPALE.html | LIVE | Step 3 — Il primo run |
| 11 | TERMINALE | LIVE | Step 3 demo: lancio claude |
| 12 | EDITOR/FILE EXPLORER | LIVE | Step 3 demo: file generato |
| 13 | PRINCIPALE.html | LIVE | Step 4 — Schedulazione |
| 14 | TERMINALE | LIVE | Step 4 demo: claude routines add |
| 15 | PRINCIPALE.html | LIVE | Step 5 — Team di agenti |
| 16 | EDITOR | LIVE | Step 5 demo: i 2 file sub-agent |
| 17 | PRINCIPALE.html | LIVE | Altri usi del pattern |
| 18 | CAMERA | LIVE | Riepilogo |
| 19 | CAMERA | LIVE | CTA Skool + consulenza |

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`
- Lavagnetta pagina 1 (`NEWSLETTER PERSONALE AI`) rivolta verso di te (la giri sul punto chiave)

**🎙️ DIRE (verbatim):**
> Quante volte al giorno apri Twitter, LinkedIn, Hacker News, blog di settore, per non perderti le novità? E quante volte trovi davvero qualcosa di utile?
> In questo video costruiamo un sistema che fa esattamente questa cosa al posto tuo. Ogni mattina, mentre fai colazione, trovi sulla scrivania un file con le 3-5 cose che contano davvero per te, riassunte in 30 righe. *(giri la lavagnetta)* La tua newsletter AI personale, fatta da Claude, solo per te.

**🖥️ MOSTRARE:** te in camera, lavagnetta che giri sull'ultima frase.

**🎬 LIVE**

---

## CLIP 02 — Cos'è una newsletter AI personale

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html), scrolla a `#cosa-e`

**🎙️ DIRE (parla SOPRA la slide):**
- Newsletter normale: scritta da una persona, mandata a migliaia, argomenti che spesso non ti interessano, pubblicità in mezzo
- Newsletter AI personale: scritta da Claude per *te solo*, fonti tue, frequenza tua, tono tuo
- Leggi a voce il box giallo `.concetto-chiave` puntandolo col cursore
- Scendi sui 5 bullet (locale, privato, modificabile in 30 sec, schedulabile, senza duplicati) commentandoli brevemente

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Cos'è una newsletter AI personale". Scrolla lentamente, fermati sul box giallo per 3 secondi.

**🎬 LIVE**

---

## CLIP 03 — Cosa costruiremo

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#cosa-costruiremo`

**🎙️ DIRE (parla sopra):**
- "Per dimostrare il pattern useremo un caso semplice e verificabile: una newsletter sulle novità di Anthropic"
- Mostra il blocco diagram con l'esempio di output, leggi a voce il titolo "La tua AI Brief — venerdì 16 maggio 2026" e i 3 titoli articolo
- Key point: "tu apri il file, leggi in 90 secondi, ne sai quanto chi passa 2 ore al giorno a seguire l'ecosistema"
- Anticipa: "l'esempio è Anthropic ma a fine video vedremo che lo stesso pattern funziona per qualunque sito"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Cosa costruiremo oggi". Il diagramma scuro è il protagonista — fermati lì 8-10 secondi.

**🎬 LIVE**

---

## CLIP 04 — Come funziona

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#come-funziona`

**🎙️ DIRE (parla sopra):**
- "Solo 3 pezzi, tutti file di testo che modifichi con VS Code"
- Mostra il diagramma di architettura: cartella newsletter + Claude Code + Routines
- Spiega i 4 file: `fonti.json` (cosa leggere), `CLAUDE.md` (come scrivere), `prompts/` (cosa fare), `state.json` (memoria)
- Key point: "niente Python, niente API esterne, niente database. Solo Claude e file"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Come funziona il sistema". Diagramma scuro al centro.

**🎬 LIVE**

---

## CLIP 05 — Setup veloce (rimando Skool)

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Per seguire questo video ti servono 2 cose: Claude Code installato — funziona su Mac, Windows e Linux — e i materiali che uso oggi.
> Costa circa 20 dollari al mese di abbonamento Claude, oppure se preferisci pagare a consumo ti costerà sotto i 2 dollari al mese di API.
> I materiali sono gratis nella mia community Skool, link sotto. Scarichi la cartella, apri Claude Code dentro, gli dici "fai il setup", e in 3 minuti hai la tua prima newsletter.
> Non perdo tempo a far vedere come si installa Claude. Andiamo dritti ai 4 step.

**🖥️ MOSTRARE:** te in camera, parli diretto.

**🎬 LIVE**

---

## CLIP 06 — Step 1 (Le fonti)

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html), scrolla a `#step-1`

**🎙️ DIRE (verbatim per il concetto, libero sul resto):**
> Step numero 1: le fonti.
> Le fonti sono i siti che Claude visita ogni mattina. Per dirgli "leggi questi" c'è un file: `fonti.json`. Lo modifichi con VS Code. Aggiungi una fonte, ne togli una, in 10 secondi.

Poi a voce libera:
- Leggi il box giallo `.concetto-chiave` puntandolo
- Mostra il blocco JSON di esempio, spiega che le 3 fonti sono: pagina news Anthropic, pagina research, changelog Claude Code
- Anticipa: "ora ti faccio vedere il file reale"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 1. Soffermati sul box giallo e sul blocco JSON di esempio.

**🎬 LIVE**

---

## CLIP 07 — Step 1 demo: fonti.json

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-newsletter\fonti.json` aperto, font 16pt

**🎙️ DIRE (punti):**
- "Questo è il file reale del nostro sistema"
- Indica i 3 blocchi: nome, URL, categoria
- "Se domani voglio aggiungere il blog di OpenAI, copio uno di questi blocchi, cambio l'URL, salvo. Fine."
- Mostra modificandolo: aggiungi velocemente una 4ª fonte fake per dimostrare quanto è semplice

**🖥️ MOSTRARE:** EDITOR con `fonti.json` aperto. Modifica live, ma piccola (aggiungi 1 voce).

**🎬 LIVE**

---

## CLIP 08 — Step 2 (Il tono)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#step-2`

**🎙️ DIRE (verbatim per il concetto):**
> Step numero 2: il tono.
> Una newsletter scritta male è peggio di nessuna newsletter. Se Claude scrive paragrafi di 10 righe e usa parole tipo "rivoluzionario" e "incredibile", non leggerai mai il file. Per dirgli come scrivere c'è il file `CLAUDE.md`. Lo modifichi una volta, vale per sempre.

Poi a voce libera:
- Leggi a voce il box giallo
- Indica le 3 sezioni dell'esempio nel blocco mostrato: Tono, Cosa enfatizzare, Cosa scartare
- "20 righe di regole che valgono per tutti i run futuri"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 2.

**🎬 LIVE**

---

## CLIP 09 — Step 2 demo: CLAUDE.md

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-newsletter\CLAUDE.md` aperto

**🎙️ DIRE (punti):**
- "Questo è il file reale"
- Scrolla alle 3 sezioni: Tono, Cosa enfatizzare, Cosa scartare
- Mostra le regole "max 3-5 bullet per articolo", "niente intro generiche", "niente aggettivi marketing"
- Key point: "Claude lo legge automaticamente all'avvio. Non devo mai ripetergli queste regole."

**🖥️ MOSTRARE:** EDITOR con `CLAUDE.md` aperto. Scrolla lentamente dall'alto al basso.

**🎬 LIVE**

---

## CLIP 10 — Step 3 (Il primo run)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#step-3`

**🎙️ DIRE (verbatim per il concetto):**
> Step numero 3: il primo run. Adesso fai partire Claude la prima volta e vedi se quello che ci aspettiamo arriva davvero. Un solo comando.

Poi a voce libera:
- Leggi a voce il box giallo
- Cita i 4 passaggi visibili nello step
- Anticipa: "ora lo facciamo davvero, in diretta"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 3.

**🎬 LIVE**

---

## CLIP 11 — Step 3 demo: lancio claude

**🧰 Cosa preparare prima della camera:**
- Terminale PowerShell in `C:\demo-newsletter`
- Verifica che `state.json` sia ancora vuoto e che `newsletter/` non esista

**🎙️ DIRE (punti):**
- "Sono nella cartella. Lancio il prompt orchestratore."
- Digita il comando, leggi a voce mentre lo digiti

**🖥️ MOSTRARE:** TERMINALE. Comando:

```powershell
claude --print "$(Get-Content prompts\newsletter-daily.md -Raw)"
```

→ Claude stampa i suoi step in tempo reale. Lascia che vada per ~60-90 secondi commentando: "sta visitando la pagina news Anthropic… ora research… ora il changelog…"

→ Al termine vedi il riepilogo:
```
✅ Newsletter generata: newsletter/2026-05-16.md
   - 3 fonti consultate
   - 5 articoli nuovi trovati
   - 3 articoli inclusi
   - 2 articoli scartati (filler)
   - Tempo totale: 67 secondi
```

**🎬 LIVE**

⚠️ Se la run è lenta o produce risultato scarno: in post-produzione accelera la parte di output del terminale (8x), così la clip resta sotto 60 secondi. Se fallisce: stacca, modifica temporaneamente `fonti.json` con fonte più affidabile, rilancia. Niente di questo va a video.

---

## CLIP 12 — Step 3 demo: il file newsletter

**🧰 Cosa preparare prima della camera:**
- File Explorer aperto su `C:\demo-newsletter\`, VS Code pronto

**🎙️ DIRE (punti):**
- "Apro la cartella, vedo che è apparsa una cartella nuova: `newsletter/`"
- Doppio-click su `newsletter/` → vedi il file `YYYY-MM-DD.md`
- Doppio-click sul file → si apre in VS Code
- Leggi a voce i primi 2-3 titoli articolo
- Key point: "questo è ciò che ti arriva ogni mattina. 30 righe, 90 secondi di lettura."

**🖥️ MOSTRARE:** FILE EXPLORER + EDITOR (flusso continuo, una sola schermata).

**🎬 LIVE**

---

## CLIP 13 — Step 4 (Schedulazione)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#step-4`

**🎙️ DIRE (verbatim per il concetto):**
> Step numero 4: lo scheduling.
> Funziona, abbiamo visto. Ma se devo lanciarlo a mano ogni mattina, è una rottura. Vogliamo che parta da solo. Per questo c'è Claude Routines: un sistema integrato in Claude Code che fa partire i prompt a orari decisi da te. Una riga di config.

Poi a voce libera:
- Leggi a voce il box giallo
- Indica i 3 passi visibili: create routine, verify, manual test
- "Da domani mattina alle 8 ti trovi sempre un nuovo file"
- Cita brevemente la nota su Task Scheduler/cron come fallback

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 4.

**🎬 LIVE**

---

## CLIP 14 — Step 4 demo: claude routines add

**🧰 Cosa preparare prima della camera:**
- Terminale PowerShell in `C:\demo-newsletter`

**🎙️ DIRE (punti):**
- "Creo la routine: una sola riga di comando"
- Digita commentando ogni pezzo
- Mostra la verifica con `claude routines list`

**🖥️ MOSTRARE:** TERMINALE. Comandi:

```powershell
claude routines add daily-newsletter `
  --schedule "0 8 * * *" `
  --cwd $PWD `
  --prompt "esegui prompts/newsletter-daily.md"

claude routines list
```

→ Output atteso:
```
📋 Active routines:
   • daily-newsletter — every day at 08:00 — next: tomorrow 08:00
```

**🎬 LIVE**

---

## CLIP 15 — Step 5 (Team di agenti)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#step-5`

**🎙️ DIRE (verbatim per il concetto):**
> Step numero 5: rendiamo il sistema intelligente.
> Adesso aggiungiamo 2 piccoli agenti specializzati che si attivano in automatico quando serve. Uno fa il "rescue" se la giornata è vuota e va a pescare contenuti da fonti secondarie. L'altro è uno "spotter" che evidenzia i major update — un nuovo modello, un nuovo tool — in cima al file, così non te li perdi mai. L'orchestratore principale li chiama in automatico. Tu non fai niente.

Poi a voce libera:
- Leggi il box giallo `.concetto-chiave` puntandolo
- Indica i 2 box `.use-case` (empty-day-rescue 🚑 e major-update-spotter 🚨), commentali brevemente
- Mostra il diagramma scuro coi flow (orchestrator → branch su 0 risultati → spotter sempre)
- Anticipa la demo: "ora ti mostro i 2 file degli agenti, sono solo testo"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Step 5. Soffermati sul box giallo e sul diagramma scuro.

**🎬 LIVE**

---

## CLIP 16 — Step 5 demo: i 2 file sub-agent

**🧰 Cosa preparare prima della camera:**
- VS Code con 2 tab aperte: `C:\demo-newsletter\.claude\agents\empty-day-rescue.md` e `.claude\agents\major-update-spotter.md`
- Font 16pt

**🎙️ DIRE (punti):**
- "Questi sono i 2 file degli agenti. Solo testo. Apriamo il primo."
- Su `empty-day-rescue.md`: indica il frontmatter YAML in cima (`name`, `description`, `tools`) → "questo dice a Claude Code: c'è un sub-agent, si chiama X, fa Y, può usare questi tool"
- Scrolla sulle istruzioni in italiano del corpo del file → "il resto sono istruzioni in italiano semplice: quando ti chiamano, vai sulle fonti di fallback, pesca 1-2 contenuti, aggiungili al file"
- Switcha tab a `major-update-spotter.md`: stesso pattern, frontmatter + istruzioni
- Key point: "non c'è codice. Sono file di testo. Domani vuoi aggiungere un 3° agente — un fact-checker, un traduttore — crei un nuovo file qui dentro, dici all'orchestratore quando chiamarlo, fine."

**🖥️ MOSTRARE:** EDITOR con i 2 file sub-agent. Switcha tra le 2 tab durante la spiegazione.

**🎬 LIVE**

---

## CLIP 17 — Altri usi del pattern

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#oltre`

**🎙️ DIRE (punti):**
- "Abbiamo costruito una newsletter sulle novità Anthropic, ma il sistema funziona per qualunque caso"
- Scorri i 5 use case a video, commentali brevemente:
  - Newsletter competitor
  - Newsletter di settore B2B
  - Newsletter di paper accademici
  - Newsletter di trend social
  - Newsletter "clipping" per brand monitoring
- Frase chiave: "cambi 2 file — `fonti.json` e `CLAUDE.md` — e Claude lavora per un altro caso. Il resto è identico."

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Altri usi". Scrolla lento, fermati su ogni use case 3-4 secondi.

**🎬 LIVE**

---

## CLIP 18 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Riepilogo dei 5 step:
> Uno: definisci le fonti in `fonti.json` — i siti che vuoi monitorare.
> Due: definisci il tono in `CLAUDE.md` — come Claude deve scrivere.
> Tre: lancia il primo run — un solo comando, e hai la tua prima newsletter.
> Quattro: schedula con Claude Routines — una riga, e parte da sola ogni mattina.
> Cinque: aggiungi il team di sub-agent — due piccoli file in `.claude/agents/` che gestiscono i giorni vuoti e ti evidenziano i major update in cima al file. Zero pensieri.
> Tutto è già configurato nei materiali. Scarichi, lanci Claude Code dentro, in 3 minuti il sistema gira.

**🖥️ MOSTRARE:** te in camera.

**🎬 LIVE**

---

## CLIP 19 — CTA Skool + consulenza

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Il materiale completo — `fonti.json` di esempio, `CLAUDE.md` pronto, prompt orchestratore, guida scheduling, opzione email — è gratis nella mia community Skool. Link nella descrizione. Membership gratuita, scarichi tutto, e se hai domande chiedi lì dentro.
> Se vuoi adattare il sistema al tuo settore — competitor monitoring, brand monitoring, newsletter di settore custom — e non te la senti di farlo da solo, scrivimi: i contatti li trovi in descrizione.
> Se questo video ti è stato utile, lascia un like e iscriviti. Ci vediamo nel prossimo.

**🖥️ MOSTRARE:** te in camera, sguardo dritto in macchina sull'ultima frase.

**🎬 LIVE**

---

## 3. POST-REC (5 minuti)

- [ ] Backup grezzo delle clip su disco esterno prima del montaggio
- [ ] (Opzionale) Cancella la cartella demo: `Remove-Item -Recurse -Force C:\demo-newsletter`
- [ ] Niente chiavi API da revocare (questo sistema non ne usa)

---

## 4. CHECKLIST DI MONTAGGIO

- [ ] Ordine clip 01 → 19 rispettato
- [ ] Tagli secchi tra schermate diverse
- [ ] Su CLIP 11 (lancio claude live): considera accelerazione 4-8x della parte centrale di output
- [ ] Su CLIP 12: verifica che il file newsletter mostrato a video non contenga dati personali
- [ ] Su CLIP 16 (2 file sub-agent): font editor a 16pt minimo per leggibilità del frontmatter YAML a video
- [ ] CTA finale (CLIP 19) ha link in descrizione del video pronto
- [ ] Audio normalizzato a -14 LUFS
- [ ] Sottotitoli: genera in automatico, rivedi i nomi file (`fonti.json`, `CLAUDE.md`, `Claude Routines`)
