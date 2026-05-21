# AUTOMAZIONE 1 — GUIDA

Stadio 2 della pipeline. Fa il **research tecnico** sull'idea — sintetizza online le migliori pratiche su "come fare quella cosa specifica" — e ne ricava la sostanza che alimenterà la sezione **Panoramica** + le **istruzioni dei singoli step** dell'HTML PRINCIPALE.

## Obiettivo

Per una specifica idea (es. "Come creare un team di agenti AI con Claude Code"), produrre il **knowledge base tecnico** che servirà a costruire l'HTML PRINCIPALE: una procedura unica step-by-step, dall'installazione/setup ai test finali, sintetizzata da più fonti online in **una procedura potenziata** che funziona al 100%.

NB: questa automazione **NON produce più un file `GUIDA.md` separato** (vecchia v2). Il suo output è il knowledge tecnico che lo stadio 3 (MATERIALE_PRATICO) userà per:
- la sezione **"Panoramica"** dell'HTML
- la sezione **"Prerequisiti"** dell'HTML
- gli **esercizi guidati passo passo** del corpo dell'HTML

In pratica: fai il research, accumula il sapere tecnico, passalo allo stadio 3 (in conversazione o in un file scratch `GUIDA_DRAFT.md` temporaneo che poi viene cancellato dopo che PRINCIPALE.html è completo).

## Input

- Una sezione di `CONTENT_IDEA_DATABASE/ideas.md`:
  - **Titolo** (es. "Come creare un team di agenti AI con Claude Code")
  - **Descrizione** in linguaggio naturale

## Procedura step-by-step (cosa fa Claude)

### 1. Identifica l'idea
- Leggi `CONTENT_IDEA_DATABASE/ideas.md`
- Match con il titolo richiesto dall'utente (anche match parziale)
- Estrai titolo + descrizione

### 2. Pianifica la ricerca
Decomponi il "come fare X" in domande atomiche da rispondere:
- Quali sono i prerequisiti? (versione tool, account, conoscenze)
- Qual è l'installazione/setup base?
- Quali sono i passaggi principali?
- Quali sono i test finali?
- Quali sono gli errori comuni?
- Esistono **più approcci tecnici** validi? (importante per lo stadio 6 che produrrà varianti)

### 3. Scraping / WebSearch
Cerca online (WebSearch + WebFetch) coprendo questi tipi di fonti:
- **Documentazione ufficiale** dei tool coinvolti (priorità massima)
- **Guide tecniche su blog** specializzati
- **Tutorial YouTube** (cercare via WebSearch)
- **Repository GitHub** con esempi funzionanti (WebFetch dei README)
- **Discussioni Reddit / forum / Hacker News** per casi reali e gotcha
- **Articoli ufficiali Anthropic, OpenAI, ecc.**

Per ogni fonte raccolta, salva: cosa dice, quanto è autorevole, quanto è recente.

### 4. Sintesi unificata
Se esistono N approcci diversi:
- Identifica i punti di convergenza
- Identifica i punti di divergenza
- **Scegli l'approccio MIGLIORE** combinando i pezzi più solidi
- Produci **UNA procedura unica**, NON un confronto, per il flusso PRINCIPALE
- Annota mentalmente (o in scratch) **gli altri 2 approcci** più solidi: serviranno come base per le 2 varianti dello stadio 6

### 5. Organizza il sapere per lo stadio 3
Struttura il materiale tecnico in modo che lo stadio 3 (MATERIALE_PRATICO) possa direttamente trasformarlo nelle sezioni dell'HTML:

- **Per la sezione "Panoramica"** dell'HTML:
  - Cosa lo spettatore costruirà
  - Cosa imparerà (5-10 deliverable concreti)
  - Quanto tempo richiede

- **Per la sezione "Prerequisiti"** dell'HTML:
  - Versioni minime di tool/SDK
  - Account/abbonamenti necessari
  - Conoscenze richieste (mantenere bassa la barriera)

- **Per gli "Esercizi guidati"** del corpo HTML:
  - Una sequenza di step atomici, ognuno con: cosa fare, comando esatto, output atteso
  - Errori comuni e fix per ogni step
  - Il "perché" dietro ogni passaggio (per la sezione di descrizione del sistema)

- **Per le "Varianti tecniche alternative"** (a uso dello stadio 6):
  - I 2-3 approcci alternativi più solidi che hai trovato online
  - Con quale tool/stack si farebbero
  - Pro/contro vs il principale

### 6. Output
Scrivi un file scratch `CONTENUTI/<slug-it>/_guida_draft.md` con tutto il sapere strutturato, organizzato per le sezioni HTML che servono. Questo file è **temporaneo**: lo stadio 3 lo legge e lo trasforma in PRINCIPALE.html, poi può essere cancellato (oppure lasciato come backup di research).

**Lingua e mirror**: `_guida_draft.md` esiste **SOLO nella cartella italiana** `<slug-it>/`. È knowledge interno usato da Claude per generare gli artefatti in ENTRAMBE le lingue allo stadio 3 — non serve un gemello EN perché nessun file dello stadio 3 legge `_guida_draft.md` direttamente in EN. Lo stadio 3 traduce on-the-fly mentre genera i materiali EN.

Struttura raccomandata di `_guida_draft.md`:

```markdown
# Knowledge base: <titolo idea>

> Research del 2026-MM-GG da N fonti.

## Panoramica
[per sezione HTML "Panoramica"]

## Prerequisiti
[per sezione HTML "Prerequisiti"]

## Architettura del sistema
[per sezione HTML "Descrizione del sistema"]

## Procedura step-by-step (per gli esercizi guidati)
### Step 1 — ...
- comando: ...
- output atteso: ...
- errori comuni: ...
[ripetere per ogni step]

## Errori comuni globali (tabella)

## Approfondimenti opzionali

## Approcci tecnici ALTERNATIVI (per le varianti)
### Alternativa A (es. n8n + Claude API)
- pro: ...
- contro: ...
- stack tecnico: ...
### Alternativa B (es. Python + cron + API)
- pro: ...
- contro: ...

## Fonti consultate
- [link 1] — descrizione
- [link 2] — ...
```

## Regole

- **Niente confronti irrisolti**: nel knowledge per il flusso PRINCIPALE, c'è UNA procedura, non "puoi farlo così oppure così".
- **Ma cattura SEMPRE 2-3 alternative** per gli stadi successivi (lo stadio 6 ne avrà bisogno).
- **Comandi e codice ESATTI**: niente "esegui un comando per installare X", scrivi `npm install -g claude-code`.
- **Verificabilità**: ogni step ha un modo per controllare che sia andato a buon fine.
- **Aggiornata**: priorità a fonti recenti (ultimi 6 mesi).
- **Lingua**: italiano. I comandi e nomi tecnici restano in inglese.

## Comandi utente che attivano questa automazione

- "fai la guida per [titolo idea]"
- "stadio 2 sull'idea [titolo]"
- "ricerca su [titolo idea]"

## Cosa NON fa questa automazione

- NON produce direttamente PRINCIPALE.html (lo fa lo stadio 3)
- NON crea i materiali pratici (script, esercizi, file)
- NON valuta la qualità rispetto allo standard del canale
