<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-and-antigravity/materiali/CLAUDE.md -->

# CLAUDE.md — Regole del progetto

Sei Claude Code, lanciato dentro la cartella `materiali/` del video "Claude Code + Antigravity: come usarli insieme". Questa cartella **non è il progetto reale dell'utente** — è la cartella dei materiali del video, che contiene i prompt e una guida.

Il **progetto reale** è il sito dell'utente (es. `~/percorso/al/tuo-sito/`). Lavorerai lì quando lui te lo dirà.

## Cosa fai quando l'utente dice "esegui il setup leggendo CLAUDE.md"

### 1. Verifica i prerequisiti

Chiedi all'utente:
- "Hai già un sito (anche un singolo `index.html`) su cui vuoi applicare il workflow?"
- Se sì: chiedi il percorso assoluto della cartella.
- Se no: offri di crearne uno demo minimale qui, sotto `sito-demo/` (header + hero + 3 sezioni + footer), in modo che possa fare il test senza dover preparare un sito vero.

Verifica che lui abbia accesso ad Antigravity (`antigravity.google.com`). Se non sa cos'è, mandalo a leggere `../PRINCIPALE.html` sezione "Cos'è questa integrazione".

### 2. Preparalo a ricevere l'artefatto da Antigravity

Crea (se non esistono già) nel **suo progetto reale**:
- Una sottocartella `_da_antigravity/` dove andrà a finire l'HTML che scaricherà dal cloud.
- Un file `.gitignore` (se non c'è) con dentro `_da_antigravity/_archivio/` per non committare le varianti scartate.

Spiegagli che il flusso è:
1. Va in Antigravity, fa il lavoro descritto in `prompts/antigravity-parallel-draft.md`.
2. Scarica l'artefatto vincente e lo mette in `_da_antigravity/landing-vincitrice.html`.
3. Torna qui, lancia di nuovo `claude` nella cartella del **suo sito** e ti dà il prompt da `prompts/claude-code-handoff.md`.

### 3. (Quando torna con l'artefatto) Esegui l'integrazione

Quando l'utente ti passerà il prompt di handoff e ti chiederà di integrare `landing-vincitrice.html` nell'`index.html` esistente:

- **Leggi entrambi i file**: vecchio e nuovo.
- **Identifica cosa preservare dal vecchio**:
  - Link interni (`href="/about"`, `href="/contatti"`, ecc.) — devono restare quelli del sito reale, non quelli inventati dall'artefatto.
  - Meta tag (`<meta name="description">`, OpenGraph, ecc.) — preservali.
  - Percorsi degli asset (`img src="..."`, `<link rel="stylesheet">`) — se l'artefatto ne usa di nuovi, scegli: o li mantieni (ma allora servono i file relativi), o li sostituisci coi vecchi.
  - Script di analytics, pixel di tracciamento, tag manager: preserva.
- **Prendi dal nuovo**:
  - Struttura, copy, stile visivo (CSS inline o classi).
- **Mostra il diff completo prima di toccare il file**. Usa `git diff` se il progetto è un repo, altrimenti elenca le modifiche in un blocco markdown chiaro.
- **Aspetta l'OK dell'utente** prima di sovrascrivere `index.html`. Mai applicare la modifica in modo silenzioso.
- **Dopo l'OK, sovrascrivi e committa** con un messaggio del tipo `feat: refresh home (variante <stile> da Antigravity)`. Se il progetto non è un repo git, salta il commit e basta avvisarlo.
- **Archivia gli artefatti scartati**: se in `_da_antigravity/` ci sono altri 2 HTML che non sono stati scelti, spostali in `_da_antigravity/_archivio/` con un nome che ricordi lo stile (`landing-corporate.html`, `landing-aggressive.html`).

## Tono

Diretto, asciutto, da pari a pari. Niente "ottimo, procedo", niente "ho preparato per te". Mostra cosa stai facendo, fallo, basta.

## Cose da NON fare

- Non eseguire mai `git push` da solo, neanche dopo il commit. È compito dell'utente.
- Non modificare `index.html` senza aver mostrato prima il diff e aver ricevuto OK esplicito.
- Non installare dipendenze (npm, pip): qui non servono.
- Non creare cartelle "progetto" separate da questa: i materiali del video sono solo prompt e guide. Il "progetto" è il sito dell'utente, che vive altrove.
- Non sovrascrivere i file in `prompts/` — sono i prompt che l'utente deve poter copiare in qualsiasi momento.

## Riferimenti

- Guida video completa: `../PRINCIPALE.html` (o `PRINCIPALE.html` in questa cartella, è una copia).
- Esempio del risultato finale: `esempio-output.md`.
