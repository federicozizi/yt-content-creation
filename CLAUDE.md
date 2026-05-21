# YouTube Content Creation System (v5 — bilingue IT+EN, con SCRIPT registrazione, senza stadio editing animazioni)

Sistema per la produzione di contenuti YouTube sul canale **AI applicata al business**, da idee scritte manualmente fino a un pacchetto completo: **3 file HTML** (1 principale + 2 metodi tecnici alternativi) consegnabili al pubblico alla fine del video, materiali pratici, **SCRIPT.md di registrazione**, file di revisione interno per il regista. Ogni contenuto ha **2 cartelle gemelle** (italiano + inglese).

## Pipeline (5 stadi, mirror bilingue ad ogni stadio)

Il **mirror bilingue NON è uno stadio finale separato**: ogni stadio della pipeline produce i suoi artefatti DIRETTAMENTE in entrambe le cartelle gemelle (`<slug-it>/` e `<slug-en>/`). Il sistema considera un'idea "lavorata" solo quando ENTRAMBE le cartelle hanno tutti gli output dello stadio appena concluso.

```
[1] CONTENT_IDEA_DATABASE/ideas.md           ← l'utente scrive titoli + descrizioni (solo IT)
                ↓
[2] AUTOMAZIONE_GUIDA                        ← _guida_draft.md (knowledge interno, SOLO IT, usato da Claude)
                ↓
[3] AUTOMAZIONE_MATERIALE_PRATICO            ← PRINCIPALE.html + SCRIPT.md + materiali/  (IT + EN)
                ↓
[4] AUTOMAZIONE_CONTROLLO (Influencer Sim.)  ← _revisione.md  (SOLO IT — il regista è italiano, indipendentemente da quale versione registra; revisiona ENTRAMBE le cartelle)
                ↓
[5] AUTOMAZIONE_VARIANTI                     ← VARIANTE-1.html + VARIANTE-2.html (+ rispettivi materiali)  (IT + EN)
```

**Stadio editing animazioni rimosso** (v5): le slide animate non vengono più generate. L'HTML PRINCIPALE.html è già la "slide" mostrata a schermo durante il video; non serve un livello aggiuntivo di animazioni Sora/Veo/Runway. Cartella `AUTOMAZIONE_EDITING/` rimossa.

**Riassunto cosa vive dove**:

| File | IT | EN | Note |
|---|---|---|---|
| `ideas.md` | ✅ | ❌ | input umano, solo italiano |
| `_guida_draft.md` | ✅ | ❌ | knowledge interno, Claude lo usa per generare entrambe le cartelle |
| `PRINCIPALE.html` | ✅ | ✅ | gemelli |
| `SCRIPT.md` | ✅ | ✅ | gemelli; nella versione EN solo `🎙️ DIRE` è in inglese, il resto in italiano |
| `materiali/` (incluso CLAUDE.md, README, prompts, ecc.) | ✅ | ✅ | gemelli con file tradotti |
| `_revisione.md` | ✅ | ❌ | un solo file IT che copre entrambe le cartelle |
| `VARIANTE-*.html` + materiali rispettivi | ✅ | ✅ | gemelli |

## Output finale per ogni idea (bilingue)

Ogni idea produce **2 cartelle gemelle**:

```
CONTENUTI/
├── <slug-it>/                          ← versione italiana (la lingua "madre")
│   ├── PRINCIPALE.html                 ← guida consegnabile (metodo principale)
│   ├── VARIANTE-1.html                 ← guida consegnabile (metodo alt. 1)
│   ├── VARIANTE-2.html                 ← guida consegnabile (metodo alt. 2)
│   ├── SCRIPT.md                       ← script di registrazione (clip-per-clip)
│   ├── _revisione.md                   ← file PRIVATO con suggerimenti revisione
│   ├── materiali/                      ← cartella FLAT ready-to-test
│   │   ├── PRINCIPALE.html             ← COPIA del fratello con link aggiustati
│   │   ├── CLAUDE.md, README.md, …
│   │   └── …
│   ├── materiali-variante-1/           ← cartella della variante 1
│   │   ├── VARIANTE-1.html             ← COPIA del fratello con link aggiustati
│   │   └── …
│   └── materiali-variante-2/           ← cartella della variante 2
│       ├── VARIANTE-2.html             ← COPIA del fratello con link aggiustati
│       └── …
└── <slug-en>/                          ← gemella inglese, stessa anatomia
```

I file con prefisso `_` sono privati: il regista li usa per migliorare la registrazione, non vengono consegnati al pubblico.

### Regola "HTML anche dentro materiali" (REGOLA GLOBALE)

Ogni cartella `materiali/`, `materiali-variante-1/`, `materiali-variante-2/` DEVE contenere una **copia del rispettivo HTML padre** (PRINCIPALE.html dentro materiali/, VARIANTE-N.html dentro materiali-variante-N/). Stessa lingua della cartella madre.

**Perché**: chi scarica solo la cartella `materiali/` deve avere subito sotto mano la guida HTML (per ripasso post-video, reference offline, consultazione mentre lavora). Non deve dover navigare al livello superiore.

**Link da aggiustare nella copia**:
- `href="materiali/X"` → `href="X"` (siamo già dentro)
- `href="PRINCIPALE.html"` → `href="../PRINCIPALE.html"`
- `href="VARIANTE-1.html"` → `href="../VARIANTE-1.html"`
- `href="VARIANTE-2.html"` → `href="../VARIANTE-2.html"`

In testa alla copia, commento HTML che la identifichi come COPIA e linki l'originale:
```html
<!-- ⚠️ COPIA dentro materiali/ — l'originale è ../PRINCIPALE.html. Gemello inglese: ... -->
```

**Sync**: ogni modifica al PRINCIPALE.html "padre" DEVE essere replicata nella copia dentro materiali/ con i link aggiustati. Idem per le VARIANTI.

## Regola bilingue (REGOLA GLOBALE)

**Ogni idea genera 2 cartelle gemelle** in `CONTENUTI/`. Per ogni file in una cartella DEVE esistere il gemello nell'altra.

**Convenzioni slug**:
- Italiano: lo slug naturale dell'idea (es. `github-per-claude-code`)
- Inglese: traduzione naturale dello slug (es. `github-for-claude-code`)
- Termini propri restano invariati (es. `claude-agents-view` resta `claude-agents-view`)

**Cosa si traduce**:
- HTML pubblici (PRINCIPALE, VARIANTI): traduzione completa, audience anglofona
- `SCRIPT.md`: la sezione `🎙️ DIRE (verbatim)` va in inglese; le sezioni `🧰 Cosa preparare`, `🖥️ MOSTRARE`, `🎬 LIVE/PRE-COTTO/MISTO`, PRE-REC, POST-REC restano **in italiano** (sono note per te, non per la voce)
- `materiali/` (CLAUDE.md, README, INIZIO_QUI, prompts/, esempio-output): tradotti — l'audience EN scarica materiali in EN
- Le COPIE di PRINCIPALE.html / VARIANTE-N.html dentro le cartelle materiali: stessa lingua della cartella che le contiene (mai mescolare IT in cartella EN)

**Cosa NON si traduce**:
- `_revisione.md`: solo IT (il regista è italiano, copre entrambe le cartelle)
- `_guida_draft.md`: solo IT (knowledge interno, usato da Claude per generare entrambe le lingue allo stadio 3)

**Sync obbligatorio**: ogni modifica a un file in una cartella DEVE essere replicata nel gemello prima di considerare il task concluso. Non lasciare mai le due versioni divergenti. Ogni file gemello porta in testa un commento/header che linka al fratello.

**Comando trigger**: l'utente può dire "sync IT→EN per [idea]" o "sync EN→IT per [idea]" per forzare l'allineamento.

## SCRIPT.md — file di registrazione clip-per-clip (REGOLA GLOBALE)

Ogni cartella `<slug>/` ha un `SCRIPT.md` che è il copione del video.

Struttura obbligatoria:

```
0. SETUP UNA TANTUM       ← cose della vita (account throwaway, profilo browser, OBS)
1. PRE-REC GIORNATA       ← checklist 30-45 min, da fare TUTTO prima di accendere la camera
   - credenziali del giorno
   - repo/progetto demo pulito
   - artefatti pre-cotti (PR già esistenti, screenshot di backup, ecc.)
   - tab del browser in ordine fisso
   - terminale configurato (font, prompt, history)
   - lavagnetta — N pagine già scritte/disegnate
2. CLIP — elenco completo (tabella riepilogativa)
3. CLIP 01...N (uno per blocco, struttura minimale a 4 voci)
4. POST-REC               ← sicurezza (revoca chiavi, cancella .env, logout)
5. CHECKLIST MONTAGGIO    ← ordine clip, audio, censure, sottotitoli
```

### Regola "1 clip = 1 schermata"

Ogni clip mostra **una sola schermata**, mai mischiata con altre. Schermate ammesse:
- `CAMERA` (te in inquadratura, può includere la lavagnetta digitale)
- `PRINCIPALE.html` (browser con la guida)
- `TERMINALE`
- `BROWSER GitHub` (o altro browser non-PRINCIPALE.html)
- `EDITOR/FILE` (VS Code, Notepad++ con un file aperto)

Mai due nella stessa clip. Le combinazioni si fanno in montaggio, non in registrazione.

### Regola "PRINCIPALE.html è la slide primaria — usalo molto"

`PRINCIPALE.html` (e `VARIANTE-N.html`) sono **slide replacement** ufficiali del video. Devono essere usati come schermata in TUTTE le clip dove il pubblico deve capire un concetto, non solo nelle "introduzioni". Questo significa:

- **Default per i concetti**: se devi spiegare a parole un punto (cosa è X, perché serve, come funziona, riepilogo intermedio di uno step), usa `PRINCIPALE.html` a schermo scrollato alla sezione giusta. La tua voce-over commenta. NIENTE CAMERA con lavagnetta come default — solo se aggiunge davvero qualcosa.
- **CAMERA solo quando serve davvero**: hook iniziale, CTA finale, momenti di "ti guardo dritto negli occhi" (max 2-4 clip CAMERA su tutto il video, non una per ogni step).
- **Lavagnetta è opzionale**: usabile per CAMERA dell'hook/CTA o come variazione di ritmo, mai come sostituzione di una slide HTML che dice la stessa cosa.
- **Struttura del PRINCIPALE.html deve essere funzionale a entrambi gli usi**: titoli grossi, frasi-chiave evidenziate (`.concetto-chiave` box giallo), bullet leggibili a schermo da distanza, diagrammi puntabili. Scriverlo pensando "questo è ANCHE una slide" — non solo "questo è una guida da leggere".

Mappatura tipo per ogni Step pratico (es. Step N del PRINCIPALE.html):
- 1 clip `PRINCIPALE.html` su `#step-N` → tu parli sopra la slide, spieghi il concetto leggendo/puntando il box giallo e i bullet
- 1-3 clip demo (`TERMINALE`/`EDITOR`/`BROWSER`) → mostri il fare reale

Niente clip CAMERA "intro step" come default. Lo step parte già dalla sua slide HTML.

### Struttura minimale di ogni blocco CLIP

Solo queste 4 voci, in quest'ordine:

```markdown
## CLIP NN — Titolo breve

**🧰 Cosa preparare prima della camera:**
- (micro-checklist 10-30 secondi: switcha tab, posiziona terminale, prendi pagina N della lavagnetta)

**🎙️ DIRE (verbatim per hook/concetti/CTA; punti per demo):**
> (verbatim)

**🖥️ MOSTRARE:** (quale schermata + cosa specifico — es. "PRINCIPALE.html scrollato a #trucco-1, soffermati sul box giallo")

**🎬 LIVE | PRE-COTTO | MISTO**
> (eventuale nota su come gestire la live vs il pre-cotto)
```

NON aggiungere altre voci (no tempo stimato, no dove guardare, no plan B — il PRE-REC dovrebbe averli prevenuti). Tutto quello che richiede preparazione vera (account, secret, artefatti, lavagnetta) va in PRE-REC, non dentro il blocco clip.

### Tre livelli di preparazione

1. **SETUP** (una sola volta nella vita): account, profilo browser, OBS, microfono
2. **PRE-REC** (30-45 min prima di registrare la giornata): tutto il resto
3. **Cosa preparare PRIMA della camera** (10-30 sec dentro ogni clip): solo verifica/switch di cose già pronte dal PRE-REC

### Editor di riferimento: VS Code

**VS Code è l'editor canonico** usato dall'utente per gestire i file durante la registrazione e nella vita quotidiana. Quando un contenuto deve menzionare "con cosa modifichi un file" (PRINCIPALE.html, SCRIPT.md, materiali, prompt agli utenti su come modificare i propri file), va citato **sempre e solo VS Code**.

- ❌ "Lo modifichi col Blocco Note" / "edit it with Notepad"
- ❌ "Lo modifichi con Notepad++"
- ❌ "Lo modifichi con un editor di testo a scelta"
- ✅ "Lo modifichi con VS Code" / "edit it with VS Code"

Lo stesso vale per i comandi terminale dimostrati a video: per aprire file usa `code <path>` (CLI di VS Code), non `notepad <path>`. Per appunti veloci durante il PRE-REC (es. parcheggio temporaneo di una chiave API), usa "un file scratch in VS Code", non "un Blocco Note temporaneo".

Eccezione: gli step di setup automatico (`INIZIO_QUI.md`) possono restare neutri ("un editor a scelta") solo se il setup è destinato a un utente finale che potrebbe non avere VS Code. Per tutto ciò che il regista mostra a video, VS Code è il default obbligatorio.

### SCRIPT.md della versione EN

- La struttura è identica.
- Le sezioni PRE-REC, POST-REC, MONTAGGIO, `🧰 Cosa preparare`, `🖥️ MOSTRARE`, `🎬 LIVE/PRE-COTTO/MISTO` restano **in italiano** (sono note per te).
- Solo `🎙️ DIRE` va tradotto in inglese (è quello che pronunci davanti alla camera per l'audience EN).

## Struttura "ready-to-test" delle cartelle materiali (REGOLA GLOBALE)

Ogni cartella `materiali/`, `materiali-variante-1/`, `materiali-variante-2/` deve essere **pronta al lancio senza spostare file**. L'utente fa solo: `cp .env.example .env` → compila → lancia. Niente sottocartelle numerate `01-`, `02-` come struttura primaria.

Layout obbligatorio al ROOT di ogni cartella materiali:

```
materiali/  (o materiali-variante-N/)
├── README.md           ← OBBLIGATORIO: quick start manuale (3-5 comandi)
├── INIZIO_QUI.md       ← OBBLIGATORIO: prompt per Claude Code (setup automatico)
├── .gitignore          ← OBBLIGATORIO: protegge .env e file sensibili
├── .env.example        ← OBBLIGATORIO se ci sono credenziali
├── requirements.txt    ← se Python (al root, mai in sottocartella)
├── <script>.py         ← punto di ingresso, al root
├── <config>.json       ← config principale, al root
├── esempio-output.md   ← come si presenta il risultato atteso
├── prompts/            ← OK: gruppo omogeneo (tutti i system prompt)
├── .claude/agents/     ← OK: gruppo omogeneo (tutti i sub-agent)
├── scheduling/         ← OK: gruppo omogeneo (cron + GitHub Actions)
└── docs/               ← OPZIONALE: guide aggiuntive (troubleshooting, scheduling avanzato)
```

**Vietato**: sottocartelle numerate `01-setup/`, `02-config/`, `03-script/` come struttura primaria. Sottocartelle solo per gruppi OMOGENEI di file (più prompt, più sub-agent, più file di scheduling).

Dettagli nei CLAUDE.md degli stadi 3 (`AUTOMAZIONE_MATERIALE_PRATICO/`) e 6 (`AUTOMAZIONE_VARIANTI/`).

## Sicurezza credenziali (REGOLA GLOBALE)

1. **Mai credenziali vere** in nessun file dei materiali. Solo placeholder fittizi in `.env.example`.
2. **Mai mostrare `.env` a video**: il pubblico vede solo `.env.example`. A voce: *"compila .env coi tuoi valori — io non lo faccio a schermo per ovvi motivi di sicurezza"*.
3. **`.gitignore` deve esistere PRIMA di `git init`** in ogni progetto.
4. **HTML deve avvertire**: se l'utente committa `.env` per sbaglio, le credenziali vanno **revocate e ricreate** (rimuoverle dalla storia git da sole non basta — i bot scansionano GitHub).

## Doppio scopo dei file HTML

I 3 HTML (PRINCIPALE + 2 VARIANTI) hanno **doppio scopo**:

1. **Per il regista durante la registrazione**: scaletta strutturata che traccia l'arco del video.
2. **Per lo spettatore alla fine del video**: guida completa scaricabile per replicare il sistema.

Lo stesso file vale per entrambi: si scrive una volta, in prosa user-oriented.

## Struttura del progetto

```
YT content creation/
├── CLAUDE.md                          ← questo file
├── credentials.json + token.json      ← OAuth Google (legacy, opzionale)
├── CONTENT_IDEA_DATABASE/             ← input umano
│   ├── CLAUDE.md
│   └── ideas.md
├── CONTENUTI/                         ← output finale: 2 cartelle per idea (IT + EN)
│   ├── <slug-it>/
│   └── <slug-en>/
├── AUTOMAZIONE_GUIDA/                 ← stadio 2
├── AUTOMAZIONE_MATERIALE_PRATICO/     ← stadio 3 (produce PRINCIPALE.html + SCRIPT.md + materiali/)
├── AUTOMAZIONE_CONTROLLO/             ← stadio 4 (produce _revisione.md)
└── AUTOMAZIONE_VARIANTI/              ← stadio 5 (produce VARIANTE-*.html + materiali-variante-N/)
```

## Identità del canale

- **Tema**: AI applicata al business, casi d'uso pratici
- **Audience**: utenti **non tecnici** (imprenditori, manager, marketer, freelance, curiosi). NON developer.
- **Stile**: pratico, divulgativo, accessibile
- **Durata video target**: 10–25 minuti
- **Format prevalente**: build di mini-tool/sistema concreto, dimostrato live, replicabile dallo spettatore

## Scaletta narrativa degli HTML (slide replacement)

I 3 file HTML sono **slide replacement**: il regista li mostra a schermo durante la registrazione, sostituendo PowerPoint o slide tradizionali. La struttura segue il flusso narrativo del video, con **focus sul topic generale dell'idea** (es. "creare un team di agenti AI") e un eventuale case study chiaramente etichettato come esempio applicato.

Sezioni obbligatorie nell'ordine narrativo:

1. **Header** (titolo del topic generale + sottotitolo)
2. **`metodo-switch`** (navigazione tra le 3 versioni)
3. **TOC**
4. **Cos'è [il topic]** — apertura concettuale (definizione + cosa lo distingue + quando ha senso)
5. **Cosa costruiremo oggi** — case study come esempio applicato + mockup output + frase di generalizzazione
6. **Come funziona il sistema** — i "mattoni" tecnici + diagramma architettura
7. **Setup iniziale** — prerequisiti + script di init
8. **Step 1, 2, ... N** — passaggi pratici, ognuno con: concetto generale → applicazione al case study → cosa fare
9. **Oltre [il case study]: come applicare il pattern** — generalizzazione con 3-5 use case alternativi
10. **Riepilogo** — cosa lo spettatore ha imparato sul pattern (non solo sul case)
11. **Materiali allegati** — tabella delle cartelle
12. **`community-box`** finale — CTA dirette al pubblico (Skool community + consulenza)

Le **menzioni community + consulenza** vivono SOLO nella `community-box` finale, mai sparpagliate nel documento.

## Standard del canale (struttura tipica del video)

I video del canale tipicamente seguono questi 4 blocchi narrativi:

1. **Introduzione pratica e rapida**: hook + elenco di cosa si farà + menzioni indirette
2. **Descrizione del sistema + perché si fa così**
3. **Analisi pratica**: setup, prerequisiti
4. **Dimostrazione**: esecuzione live con risultati visibili

Questi 4 blocchi mappano sulla scaletta narrativa HTML (le sezioni 4-5 = Introduzione; sezione 6 = Descrizione; sezione 7 = Analisi pratica; sezioni 8 = Dimostrazione).

## Comandi utente tipici

I comandi "lavora", "rifai", ecc. **producono SEMPRE i file in entrambe le cartelle gemelle** (IT + EN) per gli stadi che hanno doppia lingua. Non serve specificare "anche in EN" — è il comportamento di default.

- "aggiorna le idee" → apri `CONTENT_IDEA_DATABASE/ideas.md`
- "lavora sull'idea [titolo]" → esegui **tutta la pipeline 2→3→4→5** sull'idea selezionata; al termine entrambe le cartelle `<slug-it>/` e `<slug-en>/` esistono e contengono TUTTI gli artefatti finali
- "rifai il PRINCIPALE per [idea]" → rigenera PRINCIPALE.html (IT + EN gemelli)
- "rifai le varianti per [idea]" → rigenera VARIANTE-1.html + VARIANTE-2.html (IT + EN)
- "rifai lo script per [idea]" → rigenera SCRIPT.md (IT + EN)
- "rifai i materiali per [idea]" → rigenera materiali/ (IT + EN)
- "controlla [idea]" → rifai stadio 4 (rigenera `_revisione.md`, solo IT, copre entrambe le cartelle)
- "sync IT→EN per [idea]" → forza riallineamento: propaga tutte le modifiche italiane sulla cartella EN
- "sync EN→IT per [idea]" → forza riallineamento: propaga tutte le modifiche inglesi sulla cartella IT
- "solo IT per [idea]" → eccezione esplicita: produci/aggiorna SOLO la cartella italiana (uso raro, da non usare di default)
- "solo EN per [idea]" → eccezione esplicita: produci/aggiorna SOLO la cartella inglese

## Regole d'oro per gli HTML (non negoziabili)

1. **Doppio scopo**: lo stesso file serve sia al regista come scaletta sia al pubblico come guida.
2. **Prosa user-oriented**: niente "Da spiegare:", "Cosa annunciare:", "Menzione X (indiretta)", "Cosa fai qui:". Trasforma in prosa diretta che spiega al lettore.
3. **Niente brief regia dentro l'HTML pubblico**: i suggerimenti di revisione (`_revisione.md`) sono privati.
4. **Apertura concreta**: la Panoramica DEVE avere "Cosa fa il sistema, in concreto" + "Esempio dell'output finale" + "Perché lo facciamo così" PRIMA di entrare nei dettagli architetturali.
5. **HTML self-contained**: CSS inline, nessuna dipendenza esterna (no CDN, no Google Fonts).
6. **Tono pratico e immediato**, no decorazione promozionale.

## Tre regole d'oro globali

1. **Audience non tecnica**: linguaggio da divulgatore, NON da tutorial dev.
2. **Pratico e applicato**: ogni contenuto produce qualcosa di concreto e replicabile.
3. **Stile didattico in seconda persona**, MAI prima persona simulata.

## Memoria persistente

I feedback dell'utente accumulati nelle conversazioni passate sono in `~/.claude/projects/C--Users-zizif-Desktop-YT-content-creation/memory/`. Leggerli sempre come contesto aggiuntivo.
