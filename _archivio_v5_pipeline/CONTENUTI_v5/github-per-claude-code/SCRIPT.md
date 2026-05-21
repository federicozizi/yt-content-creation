# SCRIPT — GitHub per Claude Code (IT)

> ⚠️ **Gemello inglese**: `CONTENUTI/github-for-claude-code/SCRIPT.md`. Solo le righe `🎙️ DIRE (verbatim)` cambiano lingua; il resto resta in italiano (note di regia per te).

Script per registrazione del video **"GitHub per Claude Code (anche se non sei un tecnico)"**.

Regole di sistema:
- **1 clip = 1 schermata sola.** Mai mischiare CAMERA + SCHERMO nella stessa clip.
- **PRINCIPALE.html è la slide primaria.** Lo uso a schermo nelle clip dove devo spiegare un concetto, parlando sopra. CAMERA solo per hook, riepilogo, CTA.
- Schermate ammesse: `CAMERA` · `PRINCIPALE.html` · `TERMINALE` · `BROWSER GitHub` · `EDITOR/FILE`.
- Setup e installazioni → **citate al volo**, mai dimostrate. Rimando sempre ai materiali gratuiti sulla **Skool community**.

---

## 0. SETUP UNA TANTUM (cose della vita, non si rifanno mai più)

- [ ] **Account GitHub throwaway** creato (es. `claude-yt-demo`). Mai usare l'account personale.
- [ ] **Profilo browser dedicato** "YT-DEMO" (Firefox o Chrome). Nessun bookmark personale.
- [ ] **OBS Studio** con 3 scene: `CAM`, `SCREEN`, `SCREEN+CAM` (riserva).
- [ ] **Hotkey OBS** memorizzati (es. F8 = CAM, F9 = SCREEN).
- [ ] **Microfono** posizionato, livello picco -6dB.
- [ ] **Skool community URL** memorizzato (lo dici a memoria nella CTA finale).
- [ ] **Sistema billing Anthropic** funzionante.

---

## 1. PRE-REC GIORNATA (30-45 min)

### A. Credenziali del giorno

- [ ] `console.anthropic.com` → Settings → API Keys → **Create Key**. Nome: `YT-DEMO-2026-05-16-REVOCARE`. Copia in un file scratch in VS Code.
- [ ] Login GitHub col throwaway account nel profilo "YT-DEMO".

### B. Repo demo pulito

```powershell
Remove-Item -Recurse -Force C:\demo-competitor-brief -ErrorAction SilentlyContinue
gh repo delete claude-yt-demo/demo-competitor-brief --yes 2>$null

Copy-Item -Recurse "C:\Users\zizif\Desktop\YT content creation\CONTENUTI\github-per-claude-code\materiali" "C:\demo-competitor-brief"
cd C:\demo-competitor-brief

gh repo create claude-yt-demo/demo-competitor-brief --private --source . --push
gh secret set ANTHROPIC_API_KEY  # incolla la chiave
```

- [ ] Modifica `competitors.json` con 3 nomi verosimili (es. Stripe, Square, Adyen)
- [ ] `git add competitors.json; git commit -m "config: competitor reali"; git push`

### C. Artefatti pre-cotti (PR per Trucchi 3 e 4)

```powershell
# Pre-cotto Trucco 3
gh workflow run daily-brief.yml
gh run watch
gh pr list  # verifica PR daily-brief
```

- [ ] PR del daily-brief tenuta aperta su **Tab 5** del browser

```powershell
# Pre-cotto Trucco 4
gh label create claude-task --color "8B5CF6" --description "Task da delegare a Claude"
gh issue create --title "Aggiungi Adyen ai competitor" --body "Aggiungi Adyen come 4° competitor.`nSito: adyen.com`nPricing: adyen.com/pricing`nLinkedIn: linkedin.com/company/adyen"
gh issue list  # nota il numero
gh issue edit 1 --add-label claude-task
# aspetta 1-2 min
gh pr list  # verifica nuova PR per chiudere #1
```

- [ ] Seconda PR tenuta aperta su **Tab 6**

### D. File esca per Trucco 5

```powershell
cd C:\demo-competitor-brief
Copy-Item .github\hooks\pre-commit-claude-review.sh .git\hooks\pre-commit
```

- [ ] **NON creare ancora `config-leak.txt`** — lo crei live nel Trucco 5. Contenuto pronto in un file scratch in VS Code:
  ```
  # config di test
  ANTHROPIC_API_KEY=sk-ant-FAKE-DEMO-NOT-REAL-abc123xyz789
  ```

### E. Worktree

- [ ] Verifica che `C:\demo-competitor-brief\.worktrees\` NON esista (se sì, `git worktree remove --force .worktrees\*`)

### F. Tab del browser (ordine fisso)

| Tab | URL | Uso |
|---|---|---|
| T1 | `file:///.../CONTENUTI/github-per-claude-code/PRINCIPALE.html` | Slide principale |
| T2 | `github.com/claude-yt-demo/demo-competitor-brief` | Home repo |
| T3 | `github.com/claude-yt-demo/demo-competitor-brief/issues/new` | Nuova issue Trucco 4 |
| T4 | `github.com/claude-yt-demo/demo-competitor-brief/pulls` | Lista PR |
| T5 | PR del daily-brief (da step C) | Risultato Trucco 3 |
| T6 | PR della issue Adyen (da step C) | Risultato Trucco 4 |

- [ ] Zoom browser a **110%**, bookmark bar nascosta
- [ ] PRINCIPALE.html in cima. Test ancore: `#cosa-e`, `#cosa-costruiremo`, `#come-funziona`, `#trucco-1`, `#trucco-2`, `#trucco-3`, `#trucco-4`, `#trucco-5`, `#oltre`, `#riepilogo`

### G. Terminale

- [ ] PowerShell in `C:\demo-competitor-brief`, font **Cascadia Code 18pt**, prompt corto, history pulita

### H. Lavagnetta digitale (opzionale — 2 pagine per il hook)

Solo 2 pagine, per CLIP 01:

1. **GITHUB = UFFICIO PER CLAUDE** (testo grande)
2. **5 TRUCCHI → 1 SISTEMA** (testo grande)

Per il resto del video la lavagnetta NON serve: le slide HTML fanno il lavoro.

### I. Verifiche finali

- [ ] Focus Assist attivo, notifiche/Slack chiusi, telefono silenzioso
- [ ] OBS test 30s → controllo audio → cancella

**Da qui in poi: REC ON → fai → REC OFF.**

---

## 2. CLIP — ELENCO COMPLETO

Totale: **23 clip** (3 CAMERA, 9 PRINCIPALE.html, 11 demo). Tempo target video finale: 16-20 minuti.

| # | Schermata | Tipo | Argomento |
|---|---|---|---|
| 01 | CAMERA | LIVE | Hook |
| 02 | PRINCIPALE.html | LIVE | Cos'è GitHub |
| 03 | PRINCIPALE.html | LIVE | Cosa costruiremo |
| 04 | PRINCIPALE.html | LIVE | Come funziona il sistema |
| 05 | CAMERA | LIVE | Setup veloce + rimando Skool |
| 06 | PRINCIPALE.html | LIVE | Trucco 1 — Memoria persistente |
| 07 | EDITOR | LIVE | Trucco 1 demo: CLAUDE.md |
| 08 | PRINCIPALE.html | LIVE | Trucco 2 — Worktree |
| 09 | TERMINALE | LIVE | Trucco 2 demo: `git worktree add` |
| 10 | TERMINALE | PRE-COTTO | Trucco 2 demo: 3 Claude Code |
| 11 | TERMINALE | LIVE | Trucco 2 demo: `gh pr create` |
| 12 | PRINCIPALE.html | LIVE | Trucco 3 — GitHub Actions |
| 13 | EDITOR | LIVE | Trucco 3 demo: `daily-brief.yml` |
| 14 | TERMINALE | LIVE | Trucco 3 demo: `gh workflow run` |
| 15 | BROWSER GitHub | PRE-COTTO | Trucco 3 demo: PR risultante |
| 16 | PRINCIPALE.html | LIVE | Trucco 4 — Issue dal telefono |
| 17 | BROWSER GitHub | LIVE | Trucco 4 demo: crea issue |
| 18 | BROWSER GitHub | PRE-COTTO | Trucco 4 demo: PR risultante |
| 19 | PRINCIPALE.html | LIVE | Trucco 5 — Pre-commit hook |
| 20 | TERMINALE | MISTO | Trucco 5 demo: commit bloccato |
| 21 | PRINCIPALE.html | LIVE | Altri usi del pattern |
| 22 | CAMERA | LIVE | Riepilogo |
| 23 | CAMERA | LIVE | CTA Skool + consulenza |

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`
- Lavagnetta pagine 1 e 2 a portata

**🎙️ DIRE (verbatim):**
> Se usi Claude Code, probabilmente lo apri, gli dai un task, lui lavora, tu chiudi. E lui dimentica tutto.
> In questo video ti mostro 5 trucchi per trasformare Claude in un assistente che lavora 24 ore su 24, anche col PC spento, che riceve task dal tuo telefono, e che ti consegna risultati pronti da approvare.
> Lo strumento che lo permette si chiama GitHub. *(giri la lavagnetta pag. 1)* Sì, GitHub. No, non devi scrivere codice.

**🖥️ MOSTRARE:** te in camera, lavagnetta sull'ultima frase.

**🎬 LIVE**

---

## CLIP 02 — Cos'è GitHub

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html), scrolla a `#cosa-e`

**🎙️ DIRE (parla sopra la slide):**
- GitHub è una piattaforma online dove tieni cartelle di progetto (repo)
- Gratis fino a 2000 minuti/mese di automazioni
- 4 cose che ci servono: **Repo**, **Issue**, **Pull request**, **Actions** — scorrile col cursore mentre le citi
- Leggi a voce il box giallo `.concetto-chiave`

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Cos'è GitHub". Fermati sul box giallo 3 secondi.

**🎬 LIVE**

---

## CLIP 03 — Cosa costruiremo

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#cosa-costruiremo`

**🎙️ DIRE (parla sopra):**
- Useremo come esempio lo stesso sistema del video precedente: un brief sui 3 competitor che ogni mattina alle 7 ti arriva pronto
- Differenza con prima: stavolta gira da solo in cloud, tu non lanci niente
- Mostra il diagramma a schermo, leggi i passaggi a voce
- Frase chiave: "costa pochi centesimi al giorno e l'esempio è il brief, ma a fine video vedremo che gli stessi 5 trucchi funzionano per qualunque flusso ricorrente"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Cosa costruiremo oggi". Diagramma scuro 8-10 secondi.

**🎬 LIVE**

---

## CLIP 04 — Come funziona

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#come-funziona`

**🎙️ DIRE (parla sopra):**
- 5 trucchi, dal più semplice al più potente
- Puntali a schermo sul diagramma di architettura
- Anticipa: 3 trucchi attivi nel repo (CLAUDE.md, Pull Request, Actions), 2 in locale sul PC (Worktree, Pre-commit)

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Come funziona il sistema". Diagramma scuro al centro.

**🎬 LIVE**

---

## CLIP 05 — Setup veloce (rimando Skool)

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Per seguire questo video ti servono 4 cose: un account GitHub gratis, Claude Code installato, una chiave API Anthropic, e i materiali che uso oggi.
> Costa circa 20 dollari al mese di abbonamento Claude, oppure sotto i 2 dollari/mese di API se preferisci pagare a consumo. GitHub è gratis.
> Tutto il setup — account, chiave, primo test — è già documentato nei materiali. Trovi la cartella completa gratis nella mia community Skool, link sotto. La scarichi, apri Claude Code dentro, gli dici "fai il setup", e in 5 minuti il sistema gira.
> Io qui non perdo tempo a far vedere come si installano le cose. Andiamo dritti ai 5 trucchi.

**🖥️ MOSTRARE:** te in camera, parli diretto.

**🎬 LIVE**

---

## CLIP 06 — Trucco 1 (Memoria persistente)

**🧰 Cosa preparare prima della camera:**
- OBS scena `SCREEN`
- Tab 1 (PRINCIPALE.html), scrolla a `#trucco-1`

**🎙️ DIRE (verbatim per il concetto, libero sul resto):**
> Trucco numero 1: memoria persistente.
> Problema: ogni volta che apri Claude Code, lui parte da zero. Non sa che vuoi output in italiano, non sa il tuo tone of voice, non sa quali file non deve toccare.
> Soluzione: un file chiamato CLAUDE.md al root del repo. Claude lo legge automaticamente all'avvio di ogni sessione. Scrivi le regole una volta, valgono per sempre.

Poi a voce libera:
- Leggi il box giallo puntandolo
- Cita i 3 punti di "Cosa risolve"
- Anticipa la demo: "ora ti faccio vedere un CLAUDE.md vero, già scritto"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trucco 1. Soffermati sul box giallo.

**🎬 LIVE**

---

## CLIP 07 — Trucco 1 demo: CLAUDE.md

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-competitor-brief\CLAUDE.md` aperto, font 16pt

**🎙️ DIRE (punti):**
- "Questo è il CLAUDE.md vero del nostro repo demo"
- Leggi `## Convenzioni`: lingua italiano, max 400 parole, niente segreti committati
- Mostra `## File chiave`: qui dico a Claude quali file può toccare e quando
- Key point: "se domani entra un collega o lancia una sessione in cloud, parte già allineato a queste regole. Zero rispiegazione."

**🖥️ MOSTRARE:** EDITOR con CLAUDE.md aperto. Scrolla dall'alto al basso.

**🎬 LIVE**

---

## CLIP 08 — Trucco 2 (Worktree)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#trucco-2`

**🎙️ DIRE (verbatim per il concetto):**
> Trucco numero 2: tre Claude in parallelo, senza pestarsi i piedi.
> Hai tre task indipendenti oggi. Se li lanci uno dopo l'altro nella stessa cartella, perdi tempo. Se li lanci tutti insieme nella stessa cartella, si pestano i piedi: modificano gli stessi file, si sovrascrivono.
> Soluzione: una cosa di git che si chiama "worktree". È come avere 3 stanze separate per 3 Claude diversi. Ognuno lavora nella sua, l'originale resta intoccato.

Poi a voce libera:
- Leggi il box giallo
- Cita i 3 punti di "Cosa risolve"
- Anticipa demo: "ora creiamo davvero 3 worktree"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trucco 2.

**🎬 LIVE**

---

## CLIP 09 — Trucco 2 demo: crea worktree

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`
- `git status` → "nothing to commit"
- `.worktrees\` non esiste

**🎙️ DIRE (punti):**
- "Ora creo 3 worktree, uno per ogni task"
- Digita commentando

**🖥️ MOSTRARE:** TERMINALE. Comandi:

```powershell
git worktree add .worktrees\aggiungi-delta -b feat/delta
git worktree add .worktrees\cambia-modello -b feat/modello
git worktree add .worktrees\fix-linkedin -b fix/linkedin
git worktree list
```

**🎬 LIVE**

---

## CLIP 10 — Trucco 2 demo: 3 Claude Code in azione

**🧰 Cosa preparare prima della camera:**
- 3 finestre Claude Code Desktop già aperte e disposte
- Ogni finestra `cd` nel rispettivo worktree, `claude` lanciato, pronta al prompt

**🎙️ DIRE (punti):**
- "Tre finestre, tre worktree, tre task"
- Mostra che in ognuna scrivi un prompt diverso
- Key point: "lavorano in parallelo, ognuno vede solo il suo file system, zero conflitti"

**🖥️ MOSTRARE:** TERMINALE — desktop con 3 finestre affiancate.

**🎬 PRE-COTTO**

---

## CLIP 11 — Trucco 2 demo: pull request

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief\.worktrees\aggiungi-delta`
- Almeno 1 modifica da committare

**🎙️ DIRE (punti):**
- "Quando un worktree produce un risultato che mi convince, lo trasformo in pull request"

**🖥️ MOSTRARE:** TERMINALE:

```powershell
git add .
git commit -m "feat: aggiungi delta corp"
git push -u origin feat/delta
gh pr create --fill
```

**🎬 LIVE**

---

## CLIP 12 — Trucco 3 (GitHub Actions)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#trucco-3`

**🎙️ DIRE (verbatim per il concetto):**
> Trucco numero 3: Claude lavora anche col PC spento.
> Vuoi un report ogni mattina alle 7. Non puoi tenere il PC acceso tutta la notte. Cron locale non basta perché se chiudi il portatile, salta tutto.
> Soluzione: GitHub Actions. È un sistema di automazioni che gira sui server di GitHub, non sul tuo PC. Tu scrivi una piccola ricetta — "alle 7 di ogni giorno fai partire Claude e fagli X" — e GitHub la esegue per sempre, gratis fino a 2000 minuti al mese.

Poi a voce libera:
- Leggi il box giallo
- Costi: ~30 minuti/mese di Actions + ~$0.30-1.50/mese di API
- Anticipa demo: "ora ti mostro il file YAML del workflow, poi lo lancio, e ti faccio vedere il risultato"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trucco 3.

**🎬 LIVE**

---

## CLIP 13 — Trucco 3 demo: il file workflow

**🧰 Cosa preparare prima della camera:**
- VS Code con `C:\demo-competitor-brief\.github\workflows\daily-brief.yml` aperto

**🎙️ DIRE (punti):**
- "Questo è il file che dice a GitHub cosa fare e quando"
- Indica `cron: "5 7 * * *"` → "ogni giorno alle 7:05"
- Indica gli `steps:` → "prendi il repo, installa Claude, fai eseguire il prompt, apri PR"
- Key point: "questo file è già nei materiali, non devi scriverlo da zero"

**🖥️ MOSTRARE:** EDITOR con `daily-brief.yml`. Soffermati su cron e steps.

**🎬 LIVE**

---

## CLIP 14 — Trucco 3 demo: lancio manuale

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`

**🎙️ DIRE (punti):**
- "Lancio il workflow a mano, senza aspettare le 7 di domani"

**🖥️ MOSTRARE:** TERMINALE:

```powershell
gh workflow run daily-brief.yml
```

→ Output: "✓ Created workflow_dispatch event"

**🎬 LIVE** — stacca qui, non aspettare la run live.

---

## CLIP 15 — Trucco 3 demo: PR risultante

**🧰 Cosa preparare prima della camera:**
- Tab 5 attiva (PR pre-cotta del daily-brief)
- Vista "Files changed"

**🎙️ DIRE (punti):**
- "Questa è la PR che è arrivata dopo un minuto dall'ultima run"
- Mostra il file `briefs/YYYY-MM-DD.md`: nuovo file, ~30 righe
- Leggi a voce i primi 3 "TOP INSIGHT"
- Key point: "se mi convince clicco Merge, entra in main, e domani ne arriva un'altra. Tutto qui."

**🖥️ MOSTRARE:** BROWSER GitHub. Tab 5, vista Files changed.

**🎬 PRE-COTTO**

---

## CLIP 16 — Trucco 4 (Issue dal telefono)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#trucco-4`

**🎙️ DIRE (verbatim per il concetto):**
> Trucco numero 4: delegare task dal telefono in 30 secondi.
> Idea che ti viene fuori dall'ufficio: "sarebbe bello aggiungere un competitor nuovo". Normalmente: torni a casa, apri il PC, lanci Claude, gli spieghi, controlli, salvi. Cinque, dieci minuti.
> Soluzione: apri l'app GitHub sul telefono. Scrivi una "issue" — è un post-it digitale col task. Le metti un'etichetta. Una GitHub Action ascolta l'evento, gira Claude in cloud, lui implementa la modifica e apre una pull request. Quando torni a casa hai la proposta pronta da approvare.

Poi a voce libera:
- Leggi il box giallo
- Formula: **issue = comando, etichetta = submit, pull request = risposta**
- Anticipa demo: "ora apro una issue dal browser come se fossi dal telefono"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trucco 4.

**🎬 LIVE**

---

## CLIP 17 — Trucco 4 demo: crea issue

**🧰 Cosa preparare prima della camera:**
- Tab 3 attiva (`github.com/.../issues/new`)
- Browser in vista mobile (Ctrl+Shift+I → device toolbar)

**🎙️ DIRE (punti):**
- "Faccio finta di essere fuori, apro GitHub sul telefono"
- Scrivi titolo e descrizione, aggiungi label, submit

**🖥️ MOSTRARE:** BROWSER GitHub vista mobile.

**Dati**:
- Titolo: `Aggiungi Klarna come 5° competitor`
- Body: `Aggiungi Klarna come nuovo competitor. Sito: klarna.com. Pricing: klarna.com/business/pricing. LinkedIn: linkedin.com/company/klarna.`
- Labels: `claude-task`

**🎬 LIVE** — stacca dopo submit.

---

## CLIP 18 — Trucco 4 demo: PR risultante

**🧰 Cosa preparare prima della camera:**
- Tab 6 attiva (PR pre-cotta della issue Adyen)
- Vista "Files changed"

**🎙️ DIRE (punti):**
- "Questa è la PR arrivata 60 secondi dopo aver aggiunto l'etichetta a una issue analoga"
- Mostra il diff su `competitors.json`: 4 righe aggiunte
- Key point: "se mi piace mergio, se non mi piace chiudo. Zero rischi."

**🖥️ MOSTRARE:** BROWSER GitHub. Tab 6, vista Files changed.

**🎬 PRE-COTTO**

---

## CLIP 19 — Trucco 5 (Pre-commit hook)

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#trucco-5`

**🎙️ DIRE (verbatim per il concetto):**
> Trucco numero 5, l'ultimo: controllo qualità automatico prima di salvare.
> Scenario tipico: stai per salvare delle modifiche. Magari c'è dentro una password che hai copiato per sbaglio, un appunto privato, un TODO dimenticato.
> Soluzione: un piccolo script che git esegue automaticamente prima di ogni salvataggio. Lo script manda le modifiche a Claude, Claude le legge in 2 secondi, e ti dà un OK o un BLOCCO. Se BLOCCO, il salvataggio non parte e ti dice cosa correggere.

Poi a voce libera:
- Leggi il box giallo
- "Cosa risolve": niente password committate, niente TODO, niente appunti
- Anticipa demo: "ora provo davvero a committare un file con dentro una chiave finta"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione Trucco 5.

**🎬 LIVE**

---

## CLIP 20 — Trucco 5 demo: commit bloccato

**🧰 Cosa preparare prima della camera:**
- Terminale in `C:\demo-competitor-brief`
- Hook pre-commit attivo (fatto in step D)
- VS Code con uno scratch file pronto col contenuto del file esca

**🎙️ DIRE (punti):**
- "Creo un file col nome innocuo 'config' e dentro ci metto per sbaglio una chiave API"
- Provo a salvarlo, mostro il blocco di Claude

**🖥️ MOSTRARE:** TERMINALE:

```powershell
code config-leak.txt
# incolla, salva, chiudi

git add config-leak.txt
git commit -m "config di test"
```

→ Output atteso:
```
🔍 Claude review in corso...
❌ BLOCCO: rilevata possibile chiave API in config-leak.txt
   Sembra una chiave Anthropic (sk-ant-...).
Per bypassare (a tuo rischio): git commit --no-verify
```

Poi:
```powershell
git restore --staged config-leak.txt
Remove-Item config-leak.txt
```

**🎬 MISTO** — `git add`/`commit` LIVE; se l'hook fallisce per ambiente Windows, hai screenshot di backup in `C:\demo-recovery\hook-output.png`.

---

## CLIP 21 — Altri usi del pattern

**🧰 Cosa preparare prima della camera:**
- Tab 1 (PRINCIPALE.html), scrolla a `#oltre`

**🎙️ DIRE (punti):**
- "L'esempio del brief competitor è uno dei mille modi in cui questi 5 trucchi si combinano"
- Scorri i 5 use case a video, commentali brevemente:
  - Lead qualification quotidiana
  - Audit reputazione settimanale
  - Knowledge base interna
  - Generazione contenuti social
  - Onboarding nuovi collaboratori
- Frase chiave: "il pattern è sempre lo stesso. Cambia solo cosa fa Claude"

**🖥️ MOSTRARE:** PRINCIPALE.html sezione "Altri usi pratici". Fermati su ogni use case 3-4 secondi.

**🎬 LIVE**

---

## CLIP 22 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Riepilogo dei 5 trucchi:
> Uno: CLAUDE.md nel repo, memoria persistente, regole una volta e valgono sempre.
> Due: git worktree, tre Claude in parallelo senza pestarsi i piedi.
> Tre: GitHub Actions, Claude in cloud secondo orari che decidi, anche col PC spento.
> Quattro: issue con etichetta, deleghi task dal telefono in 30 secondi.
> Cinque: pre-commit hook, controllo qualità automatico prima di ogni salvataggio.
> Tutto è già configurato. Tu scarichi, lanci Claude Code dentro la cartella, e in 5 minuti il sistema gira.

**🖥️ MOSTRARE:** te in camera.

**🎬 LIVE**

---

## CLIP 23 — CTA Skool + consulenza

**🧰 Cosa preparare prima della camera:**
- OBS scena `CAM`

**🎙️ DIRE (verbatim):**
> Il materiale completo — workflow, hook, prompt, file CLAUDE.md di esempio — è gratis nella mia community Skool. Link nella descrizione qui sotto. Membership gratuita, scarichi tutto, e se hai domande chiedi lì dentro.
> Se vuoi adattare questo pattern al tuo settore — lead qualification, audit, knowledge base, contenuti — e non te la senti di farlo da solo, scrivimi: i contatti li trovi sempre in descrizione.
> Se questo video ti è stato utile, lascia un like e iscriviti. Ci vediamo nel prossimo.

**🖥️ MOSTRARE:** te in camera, sguardo dritto sull'ultima frase.

**🎬 LIVE**

---

## 3. POST-REC (sicurezza, 5 minuti)

- [ ] `console.anthropic.com` → Settings → API Keys → trova `YT-DEMO-...` → **Revoke**
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
- [ ] Sottotitoli: rivedi i 5 nomi di trucco e le frasi tecniche
