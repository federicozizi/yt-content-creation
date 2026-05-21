# YouTube Content Creation — v6 (struttura snella + ricerca automatica)

Sistema per produrre contenuti YouTube sul canale **AI applicata al business**. Struttura radicalmente semplificata rispetto alle versioni precedenti: ogni contenuto e' **3 cose**, niente di piu'.

## Cos'e' cambiato rispetto a v5

- **Niente piu' pipeline a 5 stadi**, niente piu' cartelle gemelle IT+EN, niente piu' SCRIPT.md, niente piu' _revisione.md, niente piu' 2 varianti tecniche per contenuto.
- **Una sola lingua di produzione** (italiano), con traduzione inglese del solo file PRINCIPALE per valutare se rifare il video in inglese.
- **Ricerca automatica delle idee**: due volte al giorno (mattina + sera) viene eseguita una ricerca remota (`/schedule`) che propone nuovi contenuti virali rivisitati sul mio settore.

## Le 3 cose che compongono ogni contenuto

Per ogni idea selezionata si produce **una sola cartella** in `CONTENUTI/<slug>/` che contiene **esattamente** queste 3 cose:

### 1. `materiali/` — cartella zippabile per il pubblico

Cosa lo spettatore scarica alla fine del video.

Contenuto MINIMO obbligatorio:
- `README.md` → guida **step-by-step a prova di idiota** per replicare quello che faccio nel video (installare plugin, usare strumenti, capire i concetti). C'e' SEMPRE, anche se non ci sono file pratici.
- `DISCLAIMER.md` → **solo se il contenuto usa `.env` o credenziali**. Ricorda all'utente di togliere le proprie credenziali prima di condividere o committare i materiali.

Contenuto opzionale (solo se il video lo richiede):
- File concreti che servono al video (script, prompt, config, esempi). Tutti al root della cartella, niente sottocartelle numerate.

### 2. `PRINCIPALE.html` — guida regista per registrare

Guida **per me** durante la registrazione. **Non** e' per il pubblico, **non** e' una slide pubblica, **non** e' un documento pubblicabile. E' solo la scaletta che leggo/guardo mentre registro.

Struttura obbligatoria:

1. **Intro persuasiva (max 1 minuto)** — stile Liam Ottley / Nate Herk:
   - Hook secco
   - Cosa faremo nel video, elencato (quasi sempre)
   - Promessa concreta che invoglia a guardare fino alla fine
   - Tono: corto, denso, efficace. MAI sopra il minuto.

2. **Step 1, 2, ..., N** — ogni step contiene **esattamente 2 cose**:
   - **Cosa mostrare a schermo**: cosa disegnare sulla lavagna (se e' uno step concettuale) o cosa far vedere a schermo (se e' uno step pratico).
   - **Cosa dire**: testo verbatim di quello che pronuncio. **Niente riferimenti temporali** (no "per 30 secondi", no "ora prendi 2 minuti", no marker di durata). Solo testo da leggere.

3. **CTA finale** — chiusura del video.

Niente altro nel PRINCIPALE.html: no preparazione PRE-REC, no checklist montaggio, no varianti tecniche, no metadati extra. Tutto quello che serve PRIMA della registrazione (account, credenziali, artefatti) lo gestisco fuori dal file.

### 3. `PRINCIPALE_ENG.html` — traduzione inglese del PRINCIPALE

Stessa struttura, **tutto tradotto in inglese** (intro + step + CTA), per valutare se rifare il video anche in lingua inglese.

Vive nella stessa cartella del PRINCIPALE.html italiano. Non e' bilingue per audience — e' un'opzione per me.

## Struttura della cartella progetto

```
yt-content-creation/
|-- CLAUDE.md                          <- questo file (regole globali)
|-- IDEE/                              <- input: idee da cui partire
|   |-- CLAUDE.md
|   |-- manuali.md                     <- idee scritte da me a mano
|   |-- topics.md                      <- appunti su macro-temi
|   `-- ricerche-auto/                 <- idee generate dallo /schedule (2x al giorno)
|       |-- YYYY-MM-DD-mattina.md
|       `-- YYYY-MM-DD-sera.md
|-- RICERCA_AUTOMATICA/                <- config dello scheduling
|   |-- CLAUDE.md
|   `-- prompt-ricerca.md              <- prompt usato dallo /schedule
|-- CONTENUTI/                         <- output: contenuti prodotti
|   |-- CLAUDE.md
|   `-- <slug>/                        <- una cartella per contenuto
|       |-- PRINCIPALE.html
|       |-- PRINCIPALE_ENG.html
|       `-- materiali/
|           |-- README.md              <- guida step-by-step pubblico
|           |-- DISCLAIMER.md          <- solo se .env/credenziali
|           `-- ... (eventuali file)
|-- _TEMPLATE_CONTENUTO/               <- template di partenza
`-- _archivio_v5_pipeline/             <- roba della vecchia pipeline (riferimento)
```

## Flusso operativo

### Generazione automatica idee (2x al giorno via /schedule)

Lo schedule remoto esegue il prompt definito in `RICERCA_AUTOMATICA/prompt-ricerca.md`. L'output:
- Cerca su web/YouTube/Twitter/Reddit cosa sta diventando virale su: **AI automazioni, software, Claude Code, intelligenza artificiale per il business**
- Calcola la **media dei contenuti virali** sull'argomento
- Propone **5-8 idee nuove** che NON sono copie banali — sono varianti, combinazioni, angoli inediti
- Scrive il file in `IDEE/ricerche-auto/YYYY-MM-DD-{mattina|sera}.md`

Ogni esecuzione produce un file nuovo (non sovrascrive). Lo storico resta consultabile.

### Selezione idea da produrre

L'utente sceglie un'idea da una delle fonti (`IDEE/manuali.md` o un file in `IDEE/ricerche-auto/`) e dice:

> "lavora sull'idea [titolo o keyword]"

Claude trova l'idea, genera la cartella `CONTENUTI/<slug>/` con le 3 cose (materiali/, PRINCIPALE.html, PRINCIPALE_ENG.html).

### Comandi tipici

- `aggiorna le idee manuali` -> apre `IDEE/manuali.md`
- `che idee abbiamo` -> elenca titoli da `IDEE/manuali.md` + ultimo file di `IDEE/ricerche-auto/`
- `lavora sull'idea X` -> produce `CONTENUTI/<slug>/` completa (materiali + PRINCIPALE + PRINCIPALE_ENG)
- `rifai il PRINCIPALE per X` -> rigenera solo i due HTML
- `rifai i materiali per X` -> rigenera solo `materiali/`
- `traduci il PRINCIPALE di X` -> rigenera solo PRINCIPALE_ENG.html

## Identita' del canale (REGOLE GLOBALI)

- **Tema**: AI applicata al business, casi d'uso pratici
- **Audience**: utenti **non tecnici** (imprenditori, manager, marketer, freelance, curiosi). NON developer.
- **Stile**: pratico, divulgativo, accessibile. Mai gergo tecnico senza spiegarlo.
- **Durata video target**: 8-18 minuti
- **Format prevalente**: build di mini-tool/sistema concreto, dimostrato live, replicabile dallo spettatore
- **Persona narrativa**: seconda persona ("tu fai X"), MAI prima persona finta ("ho creato X").

## Editor di riferimento

**VS Code** e' l'editor canonico. Quando il README delle materiali dice "modifica il file X", deve dire "apri X con VS Code", mai Blocco Note / Notepad / "editor di testo a scelta". Per i comandi: `code <path>`, non `notepad <path>`.

## Sicurezza credenziali (REGOLA GLOBALE)

1. **Mai credenziali vere nei materiali.** Solo placeholder fittizi (`.env.example`).
2. **Mai `.env` a video.** A voce dico "compila .env coi tuoi valori, non lo faccio a schermo per ovvi motivi di sicurezza".
3. **`.gitignore` esiste prima di `git init`** in ogni progetto pratico.
4. **Quando ci sono credenziali -> `DISCLAIMER.md` obbligatorio** dentro `materiali/`, che ricorda:
   - di non committare il `.env`
   - di **revocare e rigenerare** le credenziali se per sbaglio sono finite su GitHub (cancellarle dalla storia git da sole non basta — i bot scansionano).

## Stile del PRINCIPALE.html (regole non negoziabili)

1. **Solo per me come regista** — non pubblicabile, non self-contained per pubblico esterno.
2. **Niente riferimenti temporali** (no minuti, no "per X secondi", no timer).
3. **Ogni step = 2 sezioni soltanto**: cosa mostrare + cosa dire. Punto.
4. **Intro sotto 1 minuto** (parametro qualitativo: si legge in ~50-70 secondi a voce normale).
5. **HTML self-contained** (CSS inline, nessuna dipendenza esterna).
6. **Tono leggibile a colpo d'occhio** mentre registro — font grandi, sezioni evidenti.

## Stile del README.md dentro materiali/ (regole non negoziabili)

1. **A prova di idiota** — assume zero conoscenze tecniche pregresse.
2. **Step numerati** — un click/comando per step, non agglomerare.
3. **Spiega anche i concetti** — non solo "fai X", anche "X serve perche' Y".
4. **Quick start in cima**: 3-5 comandi/click per partire (se il contenuto e' eseguibile) o riassunto in 5 punti (se e' concettuale).
5. **Linguaggio divulgativo** — stessa audience del video, niente gergo dev.

## Memoria persistente

I feedback dell'utente accumulati nelle conversazioni passate sono in `~/.claude/projects/C--Users-zizif-Desktop-Lavoro-Progetti-lavorativi-GitHub-yt-content-creation/memory/`. Leggerli sempre come contesto aggiuntivo.
