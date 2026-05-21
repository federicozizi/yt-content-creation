# AUTOMAZIONE 2 — MATERIALE PRATICO + PRINCIPALE.html + SCRIPT.md (bilingue)

Stadio 3 della pipeline. Trasforma il knowledge dello stadio 2 in **tre cose, tutte in 2 lingue (IT + EN gemelli)**:
1. La cartella `materiali/` **flat e ready-to-test** — l'utente la scarica, modifica `.env` e `<config>.json`, lancia. Niente sottocartelle numerate, niente file da spostare.
2. **`PRINCIPALE.html`**: file HTML autonomo che è insieme **scaletta video per il regista** E **guida consegnabile al pubblico** alla fine del video.
3. **`SCRIPT.md`**: copione clip-per-clip del video, struttura definita nel root CLAUDE.md. Una clip = una schermata.

**Output bilingue**: ogni file di sopra esiste in 2 cartelle gemelle (`CONTENUTI/<slug-it>/` + `CONTENUTI/<slug-en>/`). Vedi root CLAUDE.md sezione "Regola bilingue" per dettagli su cosa tradurre e cosa lasciare in italiano.

## Doppio scopo dell'HTML

Lo stesso file vale per:
- **Regista durante registrazione**: lo apre a fianco al terminale e segue le sezioni come traccia.
- **Spettatore alla fine del video**: lo riceve come materiale scaricabile per replicare il sistema.

NON servono due versioni. Uno solo, scritto in prosa user-oriented, funziona per entrambi.

## Input

- `_guida_draft.md` (knowledge dallo stadio 2) nella cartella `CONTENUTI/<slug-idea>/`
- Titolo + descrizione originali da `ideas.md`

## Output (struttura FLAT obbligatoria, in 2 cartelle gemelle)

```
CONTENUTI/<slug-it>/             ← versione italiana (lingua "madre")
├── PRINCIPALE.html              ← file HTML self-contained
├── SCRIPT.md                    ← copione clip-per-clip (vedi root CLAUDE.md)
└── materiali/                   ← cartella PRONTA AL LANCIO — l'utente non sposta file
    ├── README.md                ← OBBLIGATORIO: quick start manuale (3-5 comandi)
    ├── INIZIO_QUI.md            ← OBBLIGATORIO: prompt per Claude Code (setup automatico)
    ├── .gitignore               ← OBBLIGATORIO: protegge .env e altri file sensibili
    ├── .env.example             ← OBBLIGATORIO se ci sono credenziali: template da cui l'utente fa cp .env.example .env
    ├── requirements.txt         ← se Python (al root, non in sottocartella)
    ├── <script principale>      ← es. team_agenti.py, al root
    ├── <config principale>      ← es. competitors.json, al root
    ├── <eventuali sottocartelle di file omogenei>  ← es. prompts/, .claude/agents/, scheduling/
    ├── esempio-output.md        ← come si presenta il risultato atteso
    └── docs/                    ← OPZIONALE: guide aggiuntive su scheduling, troubleshooting, ecc.
```

### Principio "ready-to-test"

L'utente scarica la cartella materiali. **Senza spostare nessun file**, fa solo:

```bash
cd materiali
cp .env.example .env       # poi compila .env coi suoi valori
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
python <script>.py         # o `claude` se è il Metodo A
```

**Vietato**:
- Sottocartelle numerate `01-`, `02-`, `03-` come struttura primaria — sono organizzazione didattica fittizia che costringe l'utente a copiare file in giro
- Documentazione `README.md` nelle sottocartelle invece che al root
- File "isolati" in sottocartelle che lo script si aspetta al root (es. `competitors.json` in `02-config/competitors.json` quando lo script lo legge da `./competitors.json`)
- `.env` o `.env.example` nascosti in sottocartelle — devono stare accanto allo script che li carica con `load_dotenv()`

### Sottocartelle ammesse (solo per gruppi OMOGENEI)

Quando hai un gruppo di file dello stesso tipo, una sottocartella va bene:
- `prompts/` per i system prompt dei ruoli (file .txt)
- `.claude/agents/` per i sub-agent Claude Code (file .md con frontmatter)
- `scheduling/` per file di schedulazione (crontab-example.txt, .github/workflows/*.yml)
- `docs/` per guide di approfondimento

**Mai** una sottocartella per un singolo file. **Mai** una sottocartella per separare "step" — la separazione step la fai nei numeri delle sezioni HTML, non nel filesystem.

## OBBLIGATORIO: i 4 file alla radice

Ogni cartella `materiali/` (e ogni `materiali-variante-N/`) DEVE avere alla radice questi 4 file:

### 1. `README.md` — quick start manuale

Per l'utente sviluppatore-esperto che vuole sapere subito cosa fare. Template:

```markdown
# Team di agenti AI — [Nome del metodo]

**Tutto pronto per l'uso.** Configura `.env` + `<config>.json` e lancia.

## Prerequisiti
- [elenco minimale: Python ≥ X, Node ≥ Y, API key da dove, ecc.]

## Quick start (N comandi)

\```bash
# 1. [Comando 1]
# 2. [Comando 2]
# ...
\```

## Cosa c'è in questa cartella

\```
.
├── README.md         ← stai leggendo questo
├── INIZIO_QUI.md     ← alternativa: setup automatico via Claude Code
├── .env.example      ← template credenziali (copia in .env)
...
\```

## Setup automatico (alternativa)
Lancia `claude` dentro questa cartella e scrivi "esegui il setup leggendo INIZIO_QUI.md".

## Sicurezza credenziali
Il `.gitignore` esclude già `.env` dai commit. Non rimuoverlo.
```

### 2. `INIZIO_QUI.md` — prompt per Claude Code

Per l'utente non tecnico che lascia fare a Claude Code. Template:

```markdown
# Setup automatico — Claude Code, leggi qui

Sei stato lanciato dentro la cartella materiali del **[Nome metodo]**. Tutto è già qui dentro al root: lo script, i config, il template `.env.example`, il `.gitignore`. Tu fai solo: prerequisiti + venv + credenziali. ~3 minuti.

## Cosa fare

### 1. Verifica prerequisiti
[lista check minimale]

### 2. Setup ambiente
Lavoriamo **direttamente in questa cartella** (no progetto separato — tutto è già pronto qui).
[comandi venv + pip install]

### 3. Configura le credenziali
\```bash
cp .env.example .env
\```
Chiedi all'utente i valori uno alla volta:
- [valore 1] — se non ce l'ha: [link e istruzioni]
- [valore 2] — ...

Scrivi i valori in `.env`. **Verifica che `.gitignore` esista già** (c'è di default) e contenga `.env` — è il caso.

### 4. Configura il config principale
Apri `<config>.json` e aiuta l'utente a sostituire i placeholder coi suoi valori reali.

### 5. Test
[comando per il primo run + cosa aspettarsi]

### 6. Schedulazione (opzionale)
Suggerisci di andare in `scheduling/` per attivare l'automazione.

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: la cartella materiali stessa È il progetto.
- **Non rimuovere `.gitignore`**.
- Tono diretto, conciso. Niente paragrafi accademici.
- Se qualcosa fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
```

### 3. `.gitignore` — protezione credenziali OBBLIGATORIA

Anche se il progetto non sarà committato in git, il file deve esistere. Quando l'utente farà `git init` (per scheduling via GitHub Actions o per backup), proteggerà già da solo. Template minimo:

```gitignore
# === Credenziali (CRITICO) ===
.env
.env.*
!.env.example
*.pem
*.key

# === Output ===
briefs/
logs/
*.log

# === Linguaggio specifico (es. Python) ===
.venv/
venv/
__pycache__/
*.pyc

# === Sistema operativo ===
.DS_Store
Thumbs.db

# === IDE ===
.vscode/
.idea/
```

### 4. `.env.example` — template credenziali (se applicabile)

Solo se il sistema usa credenziali. Tutti i valori sono **placeholder fittizi**, mai veri. L'utente fa `cp .env.example .env` e compila `.env` coi suoi valori. Esempio:

```
# Copia questo file in `.env` e compila i valori reali.
# NON committare `.env` (è già in .gitignore).

ANTHROPIC_API_KEY=sk-ant-...
GMAIL_USER=tuoindirizzo@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
BRIEF_RECIPIENT=tuoindirizzo@gmail.com
```

## Sicurezza credenziali — regole assolute

1. **Mai committare credenziali vere** in nessun file dei materiali. Usa solo placeholder fittizi.
2. **Mai mostrare credenziali a video**: nella sezione HTML che spiega l'esecuzione, dire esplicitamente *"compila .env coi tuoi valori — io non lo faccio a schermo per ovvi motivi di sicurezza"*.
3. **Lo script deve cercare `.env` accanto a sé** (cwd o `Path(__file__).parent`), non in sottocartelle. Coerente con la posizione di `.env.example`.
4. **Il `.gitignore` deve essere creato PRIMA di `git init`**: nel template di INIZIO_QUI.md, se prevedi `git init`, l'ordine deve essere `.gitignore` esistente → `git init` → primo commit.
5. **Avvertimento esplicito nel HTML pubblico**: se l'utente committa `.env` per sbaglio, le credenziali sono compromesse anche dopo averle rimosse dalla storia git (i bot scansionano GitHub continuamente). Vanno **revocate e ricreate**, non solo rimosse.

## Anatomia obbligatoria — scaletta narrativa video

L'HTML è una **scaletta video mostrata a schermo durante la registrazione**. La struttura segue l'ordine in cui il regista parla nel video, dall'apertura concettuale alla chiusura.

**Principio cardine**: il topic dell'idea (es. "creare un team di agenti AI") è il PROTAGONISTA. Un eventuale case study (es. "monitoraggio competitor") è solo l'esempio applicato che dimostra il pattern. Lo spettatore deve uscire con un pattern riutilizzabile, non con una soluzione single-purpose.

```html
<!DOCTYPE html>
<html lang="it">
<head>...</head>
<body>

<header>
  <h1><Titolo del topic generale, NON del case study></h1>
  <p class="subtitle"><1 frase che inquadra il pattern></p>
</header>

<section class="metodo-switch">...</section>
<nav class="toc">...</nav>

<!-- 1. APERTURA CONCETTUALE -->
<section id="cosa-e">
  <h2>Cos'è [il topic generale]</h2>
  <p>[Definizione in 1-2 frasi.]</p>
  <p>[Cosa lo distingue da approcci alternativi.]</p>
  <p>[Quando ha senso usarlo.]</p>
</section>

<!-- 2. CASE STUDY APPLICATO -->
<section id="cosa-costruiremo">
  <h2>Cosa costruiremo oggi</h2>
  <p>[Frase di inquadramento: "Per dimostrare il pattern useremo un esempio concreto..."]</p>
  <p>[Descrizione del case study + mockup del risultato in <div class="diagram">]</p>
  <p>[Frase di generalizzazione: "questo è UN esempio. Vedremo a fine video come il pattern si applica a..."]</p>
</section>

<!-- 3. ARCHITETTURA -->
<section id="come-funziona">
  <h2>Come funziona il sistema</h2>
  <p>[I "mattoni" tecnici del pattern — concetti, non solo nomi tool.]</p>
  <div class="diagram">[Schema architettura]</div>
</section>

<!-- 4. SETUP -->
<section id="setup">
  <h2>Setup iniziale</h2>
  [Prerequisiti + script di init in step numerati]
</section>

<!-- 5. STEP DI COSTRUZIONE -->
<section class="block" id="step-1">
  <h3>Step 1 — [Nome del passaggio]</h3>
  
  <p>[CONCETTO GENERALE del passaggio in 1-2 frasi. Punto puntabile a schermo.]</p>
  
  <h4>Nel nostro caso</h4>
  <p>[Come si applica al case study specifico in 2-3 frasi.]</p>
  
  <h4>Cosa fare</h4>
  <ol class="steps">[step numerati con .action / .note / .output]</ol>
  
  <p class="materiali-link">[link materiali]</p>
</section>

<!-- ripetere per Step 2, 3, ... N -->

<!-- 6. GENERALIZZAZIONE — IMPORTANTE -->
<section id="oltre-il-case">
  <h2>Oltre [il case study]: come applicare il pattern</h2>
  <p>[Frase di apertura: "lo stesso pattern vale per..."]</p>
  <ul>
    [3-5 use case diversi dove lo stesso pattern si applica, ognuno descritto in 2-3 righe]
  </ul>
</section>

<!-- 7. RIEPILOGO -->
<section id="riepilogo">
  <h2>Riepilogo</h2>
  <p>[Cosa lo spettatore ha imparato sul PATTERN, non sul case study.]</p>
  <ul class="checks">[deliverables]</ul>
</section>

<!-- 8. MATERIALI -->
<section id="materiali-overview">
  <h2>Materiali allegati</h2>
  <table class="compare">...</table>
</section>

<!-- 9. CTA COMMUNITY -->
<section class="community-box">...</section>

<footer>...</footer>
</body>
</html>
```

## Componenti slide-friendly aggiuntivi

Oltre alle classi CSS già definite, **introdurre questi componenti per favorire la lettura a schermo durante la registrazione**:

- `.concetto-chiave` — box visivo distintivo per la frase principale di una sezione (1-2 righe). Bordo colorato, testo più grande del normale. Va usato per i punti che il regista vuole "puntare e leggere a voce".
- `.applicazione` — header `<h4>` standardizzato "Nel nostro caso" che separa visivamente concetto generale da applicazione al case study.
- `.cosa-fare` — header `<h4>` standardizzato "Cosa fare" che introduce gli step pratici.

## Regole di scrittura per la scaletta narrativa

- **Apertura concettuale obbligatoria**: la prima sezione DOPO header/metodo-switch/TOC deve essere "Cos'è [il topic]", non "Cosa fa il sistema". Inquadra il pattern, non l'esempio.
- **Esempio chiaramente etichettato come esempio**: nel "Cosa costruiremo oggi" usa frasi tipo "per dimostrare il pattern useremo X come esempio concreto" — non far credere che il video sia su X.
- **Sezione finale di generalizzazione**: SEMPRE presente. Lista 3-5 altri use case dove lo stesso pattern si applica.
- **Focus su DIFFERENZE e PERCHÉ**, non su step di setup. Gli step di setup li fa Claude Code via INIZIO_QUI.md. Il documento spiega: cos'è, come funziona ad alto livello, quando ha senso usarlo, perché questo metodo invece di un altro.
- **Setup minimale nel HTML**: 1 frase tipo "Lancia Claude Code dentro la cartella materiali e digli 'esegui il setup'. Fa tutto da solo." Niente `pip install`, niente `mkdir`, niente `cp .env.example .env`.
- **Comandi terminale solo per i momenti wow**: il lancio del sistema, i log dei watcher in parallelo, il commit/email finale. Quelli sono gli highlight visivi che il pubblico vuole vedere.
- **Paragrafi corti** (3-5 righe max). Più whitespace.
- **Niente "Da spiegare:", "Cosa annunciare:", "Menzione X"** — sono brief regia, vietati nell'HTML pubblico.

## Tono: pratico, conversazionale, asciutto

Il linguaggio deve avvicinarsi al modo in cui l'utente parla nei video. Pratico, diretto, senza fronzoli accademici.

Esempi del tono giusto:
- ❌ "Si potrebbe ipotizzare di utilizzare un singolo agente generico, ma il context window risulterebbe sovraccarico."
- ✅ "Un agente solo che fa tutto si confonde. Quattro agenti specializzati no."
- ❌ "Per la massima portabilità, lo script Python è privo di dipendenze esterne pesanti."
- ✅ "Lo script Python gira ovunque. Niente Docker, niente server, basta Python."

Niente "Spettabile", niente "In tale ottica", niente "Si rende necessario". Solo cose dette come le diresti a un cliente o a un amico imprenditore.

## Cosa NON usare nell'HTML

- ❌ `.review-note` (suggerimenti di revisione) — vanno in un file separato `_revisione.md`, NON nell'HTML che riceve il pubblico.
- ❌ `.verdict-summary` — materiale interno, non per il pubblico.
- ❌ Frasi tipo "**Da spiegare:**", "**Cosa annunciare:**", "**Menzione X (indiretta):**", "**Cosa fai qui:**", "**Cosa mostrare a schermo:**". Sono brief regia, vanno trasformati in prosa diretta user-oriented.
- ❌ Hero-stats con costo/tempo nel header.
- ❌ `.wow-stat` con numeri giganti dentro le sezioni.
- ❌ Badge per ogni blocco (⏱️ tempo, 🟢 difficoltà, 🤯 wow).
- ❌ "Block-promise" tipo "Il momento in cui agganci lo spettatore".
- ❌ Aperture marketing tipo "Il tipo di sistema che fino al 2024 costava 5.000€ a un'agenzia".
- ❌ Boilerplate motivazionale ("Sei pronto?? 🚀").

## CSS minimo (palette canale)

```css
:root {
  --primary: #2563eb;
  --primary-dark: #1d4ed8;
  --text: #111827;
  --muted: #6b7280;
  --bg: #ffffff;
  --bg-soft: #fafbfc;
  --border: #e5e7eb;
  --code-bg: #f3f4f6;
  --output-bg: #ecfdf5;
  --output-border: #10b981;
  --switch-bg: #eff6ff;
  --switch-border: #93c5fd;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { font-family: system-ui, -apple-system, "Inter", "Segoe UI", sans-serif; color: var(--text); background: var(--bg); line-height: 1.7; max-width: 880px; margin: 0 auto; padding: 32px 24px 64px; font-size: 16px; }
h1 { font-size: 1.95rem; margin: 0 0 6px; line-height: 1.2; letter-spacing: -0.01em; }
h2 { font-size: 1.45rem; margin-top: 48px; padding-bottom: 6px; border-bottom: 2px solid var(--primary); }
h3 { font-size: 1.2rem; margin-top: 30px; color: var(--primary); }
h4 { font-size: 1.05rem; margin-top: 20px; }
p { margin: 12px 0; }
.subtitle { color: var(--muted); margin-top: 0; font-size: 1rem; }
nav.toc { display: flex; gap: 16px; flex-wrap: wrap; padding: 12px 0; margin: 18px 0 24px; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); font-size: 0.9rem; }
nav.toc a { color: var(--primary); text-decoration: none; font-weight: 500; }
.metodo-switch { background: var(--switch-bg); border: 1px solid var(--switch-border); border-radius: 8px; padding: 16px 20px; margin: 20px 0; }
.metodo-switch h2 { margin: 0 0 8px; border: none; padding: 0; font-size: 1.05rem; color: var(--primary-dark); }
.metodo-switch ul { list-style: none; padding-left: 0; margin: 8px 0 0; }
.block { background: var(--bg-soft); border: 1px solid var(--border); border-radius: 8px; padding: 20px 24px; margin: 24px 0; }
.block h3 { margin-top: 0; }
ol.steps { padding-left: 0; counter-reset: step; list-style: none; margin-top: 16px; }
ol.steps > li { margin-bottom: 22px; padding-left: 38px; position: relative; }
ol.steps > li::before { counter-increment: step; content: counter(step); position: absolute; left: 0; top: 2px; width: 26px; height: 26px; border-radius: 50%; background: var(--primary); color: white; font-weight: 700; font-size: 0.85rem; display: flex; align-items: center; justify-content: center; }
ol.steps li > strong:first-child { display: block; margin-bottom: 6px; font-size: 1.02rem; }
.action { background: #1e293b; color: #e2e8f0; padding: 10px 14px; border-radius: 6px; font-family: "SF Mono", Menlo, monospace; font-size: 0.88rem; margin: 8px 0; overflow-x: auto; white-space: pre-wrap; }
.action::before { content: "▶  "; color: #38bdf8; }
.action.no-prompt::before { content: "📁  "; }
.note { background: #fff; padding: 10px 14px; border-radius: 4px; margin: 8px 0; font-size: 0.95rem; border-left: 3px solid var(--primary); }
.output { background: var(--output-bg); padding: 8px 14px; border-radius: 4px; font-size: 0.9rem; margin: 8px 0; border-left: 3px solid var(--output-border); font-family: "SF Mono", Menlo, monospace; }
.output::before { content: "✅  "; font-family: system-ui, sans-serif; font-weight: 700; }
code { background: var(--code-bg); padding: 2px 6px; border-radius: 3px; font-family: "SF Mono", Menlo, monospace; font-size: 0.92em; }
.materiali-link { margin-top: 18px; padding-top: 12px; border-top: 1px dashed var(--border); font-size: 0.94rem; }
.materiali-link::before { content: "📎  "; }
.diagram { font-family: "SF Mono", Menlo, monospace; background: #0f172a; color: #e2e8f0; padding: 14px; border-radius: 6px; font-size: 0.8rem; white-space: pre; overflow-x: auto; margin: 16px 0; line-height: 1.4; }
ul.checks { list-style: none; padding-left: 0; }
ul.checks li { padding: 5px 0; padding-left: 24px; position: relative; }
ul.checks li::before { content: "✓"; color: var(--output-border); font-weight: 700; position: absolute; left: 0; top: 5px; }
table.compare { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.92rem; }
table.compare th, table.compare td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); vertical-align: top; }
table.compare th { background: var(--bg-soft); font-weight: 600; color: var(--primary-dark); }
.community-box { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 18px 22px; margin: 24px 0; }
.community-box h3 { margin-top: 0; color: #166534; }
footer { margin-top: 48px; padding-top: 18px; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.85rem; text-align: center; }
@media print { body { max-width: none; padding: 0 16px; font-size: 11pt; } nav.toc, footer { display: none; } .block, .metodo-switch, .community-box { break-inside: avoid; } h2, h3 { break-after: avoid; } .action { background: #f3f4f6; color: #1e293b; border: 1px solid var(--border); } .diagram { background: #f3f4f6; color: #1e293b; } }
```

## Procedura step-by-step (cosa fa Claude)

### 1. Leggi il knowledge dallo stadio 2
Apri `_guida_draft.md`. Estrai panoramica, prerequisiti, step procedurali, errori comuni, alternative tecniche.

### 2. Mappa il knowledge a file flat al root della cartella materiali

Identifica:
- **1 script/punto-di-ingresso principale** (es. `team_agenti.py`, `daily-brief.md`, `workflow.json`) → al root
- **1 config principale modificabile dall'utente** (es. `competitors.json`) → al root
- **Eventuali gruppi OMOGENEI** (es. 4 prompt → `prompts/`, 4 sub-agent → `.claude/agents/`, file di scheduling → `scheduling/`)
- **Esempio output** (`esempio-output.md`) → al root
- **Eventuali docs di approfondimento** (troubleshooting, scheduling avanzato) → in `docs/`

NON mappare a sottocartelle numerate `01-setup/`, `02-config/`, `03-script/` ecc. — è anti-pattern.

### 3. Genera i file pratici
- Crea i file effettivi (script, file di config, esercizi) **al root della cartella materiali** o nelle sottocartelle omogenee.
- I contenuti devono essere **funzionanti**, non placeholder.
- Scrivi UN solo `README.md` al root della cartella materiali (quick start manuale + mappa di tutti i file).
- Crea `INIZIO_QUI.md`, `.gitignore`, `.env.example` (se servono credenziali) seguendo i template della sezione "OBBLIGATORIO: i 4 file alla radice".
- **Verifica i path nello script**: tutti i file di config devono essere letti relativamente al root della cartella materiali (es. `Path(__file__).parent / "competitors.json"`), non con percorsi tipo `config/competitors.json` che presupporrebbero sottocartelle.
- **Settings Claude Code**: se servono settings (Agent Teams, permessi, ecc.), metterli in `.claude/settings.json` (path che Claude Code legge davvero). MAI creare file tipo `claude-settings.json` al root — Claude Code li ignora.
- **Mai creare script che ricreano la struttura** (tipo `init-progetto.sh` che fa `mkdir -p` + `git init`): la cartella materiali È GIÀ il progetto. Uno script che crea sottocartelle o cartelle separate contraddice la struttura flat e confonde sia l'utente che Claude Code.
- **INIZIO_QUI.md non deve fare `git init`** a meno che git non sia strettamente necessario per il funzionamento del sistema. Se serve git, deve essere esplicitamente motivato nel file.

### 4. Costruisci PRINCIPALE.html
Riempi il template (vedi anatomia sopra). Verifica che la **Panoramica** abbia le 3 sotto-sezioni obbligatorie:
1. **Cosa fa il sistema, in concreto** — descrizione passo-passo dell'esecuzione reale.
2. **Esempio dell'output finale** — risultato concreto in `<div class="diagram">`.
3. **Perché lo facciamo così** — motivazioni delle scelte.

Per ogni Step:
- Apertura: 1-2 paragrafi user-oriented che spiegano cos'è e perché serve.
- Sotto-sezione "Cosa fare" con `<ol class="steps">`.
- Ogni step: `<strong>` + `<div class="action">` + `<p>` con spiegazione + opzionale `<div class="output">`.
- Link finale ai materiali.

**Slide-friendly** (regola della v5): ogni sezione deve essere autosufficiente come slide a schermo durante la registrazione. Titolo H2/H3 grosso, frase-killer nel box `.concetto-chiave`, 3-5 bullet leggibili a distanza, eventuale `.diagram`. Niente paragrafi-fiume che a schermo sono noiosi. Vedi root CLAUDE.md sezione "Regola PRINCIPALE.html è la slide primaria" per dettagli.

### 4b. Genera la COPIA dentro materiali/

Dopo aver salvato PRINCIPALE.html al livello `<slug-it>/`, crea una **copia identica** in `<slug-it>/materiali/PRINCIPALE.html` con i link interni aggiustati:

| Link originale | Diventa nella copia |
|---|---|
| `href="materiali/X"` | `href="X"` |
| `href="PRINCIPALE.html"` | `href="../PRINCIPALE.html"` |
| `href="VARIANTE-1.html"` | `href="../VARIANTE-1.html"` |
| `href="VARIANTE-2.html"` | `href="../VARIANTE-2.html"` |

Aggiungi/aggiorna il commento HTML in testa: `<!-- ⚠️ COPIA dentro materiali/ — l'originale è ../PRINCIPALE.html. Gemello inglese: ... -->`

Comando bash di esempio (sed):
```bash
sed -E \
  -e 's|href="materiali/|href="|g' \
  -e 's|href="PRINCIPALE\.html"|href="../PRINCIPALE.html"|g' \
  -e 's|href="VARIANTE-1\.html"|href="../VARIANTE-1.html"|g' \
  -e 's|href="VARIANTE-2\.html"|href="../VARIANTE-2.html"|g' \
  <slug-it>/PRINCIPALE.html > <slug-it>/materiali/PRINCIPALE.html
```

Lo stesso per la versione EN (`<slug-en>/PRINCIPALE.html` → `<slug-en>/materiali/PRINCIPALE.html`).

**Sync**: ogni modifica futura al PRINCIPALE.html "padre" DEVE essere replicata nella copia. È la stessa logica del mirror IT↔EN, ma applicata a parent↔materiali/.

### 5. Genera SCRIPT.md (copione di registrazione)

Vedi root CLAUDE.md sezione "SCRIPT.md — file di registrazione clip-per-clip" per la struttura obbligatoria completa, **incluse le 2 regole "1 clip = 1 schermata" e "PRINCIPALE.html è la slide primaria — usalo molto"**.

Riassunto:
- **Sezione 0 SETUP UNA TANTUM**: account throwaway, profilo browser, OBS, mic
- **Sezione 1 PRE-REC GIORNATA**: checklist 20-45 min con credenziali del giorno, repo demo pulito, artefatti pre-cotti, tab del browser in ordine fisso, terminale configurato, lavagnetta (OPZIONALE — solo se aggiunge davvero qualcosa rispetto alla slide HTML)
- **Sezione 2 CLIP — elenco completo**: tabella con tutte le clip e tipo schermata
- **Sezione 3 CLIP 01...N**: una clip per ogni schermata distinta del video, struttura minimale a 4 voci (Cosa preparare prima · DIRE · MOSTRARE · LIVE/PRE-COTTO/MISTO). MAI mischiare 2 schermate in una clip.
- **Sezione 4 POST-REC**: revoca chiavi API, cancella `.env`, logout, backup grezzi
- **Sezione 5 CHECKLIST MONTAGGIO**: ordine clip, audio, censure, sottotitoli

Mappatura **slide-first** sezioni HTML → clip:

- Header/hook → 1 clip CAMERA (uno dei pochi momenti CAMERA giustificati)
- "Cos'è [il topic]" → 1 clip `PRINCIPALE.html` (parli sopra la slide)
- "Cosa costruiremo" → 1 clip `PRINCIPALE.html`
- "Come funziona" → 1 clip `PRINCIPALE.html`
- "Setup iniziale" → 1 clip `PRINCIPALE.html` o CAMERA breve con rimando esplicito alla community Skool
- Per ogni Step pratico (Trucco/Passaggio N):
  - **1 clip `PRINCIPALE.html`** su `#step-N` → parli SOPRA la slide, leggi/punti il box giallo `.concetto-chiave`, commenti i bullet. **Questa clip sostituisce l'eventuale "intro CAMERA con lavagnetta"** (non più un default).
  - 1-3 clip demo (TERMINALE / BROWSER GitHub / EDITOR / ecc.)
- "Oltre [case study]" → 1 clip `PRINCIPALE.html`
- "Riepilogo" → 1 clip CAMERA (sguardo dritto)
- CTA Skool + consulenza → 1 clip CAMERA (verbatim obbligatorio)

**Bilancio target**: per un video di 12-20 min, max 3-5 clip CAMERA su un totale di 15-25 clip. Il resto è PRINCIPALE.html (slide) + demo concrete.

Per ogni demo, decidi esplicitamente:
- 🎬 **LIVE**: comando rapido e affidabile
- 📼 **PRE-COTTO**: artefatto creato in PRE-REC
- 🔀 **MISTO**: comando LIVE + risultato PRE-COTTO mostrato dopo

### 6. Mirror EN (cartella gemella)

Subito dopo aver generato `<slug-it>/`, replica tutto in `<slug-en>/`:

- `PRINCIPALE.html`: traduzione completa, audience anglofona. Stesse classi CSS, stessa anatomia.
- `SCRIPT.md`: traduci SOLO le righe `🎙️ DIRE (verbatim)`. Lascia in **italiano** le sezioni `🧰 Cosa preparare prima della camera`, `🖥️ MOSTRARE`, `🎬 LIVE/PRE-COTTO/MISTO`, PRE-REC, POST-REC, CHECKLIST MONTAGGIO (sono note per il regista, non per la voce). Aggiungi in testa: `> ⚠️ Gemello italiano: CONTENUTI/<slug-it>/SCRIPT.md`.
- `materiali/`: stessa struttura flat, contenuti tradotti:
  - `CLAUDE.md` (regole repo) → in inglese
  - `README.md` (quick start) → in inglese
  - `INIZIO_QUI.md` → diventa `START_HERE.md` in inglese
  - `prompts/*.md` → tradotti, output del prompt anche in inglese
  - `esempio-output.md` → diventa `example-output.md`, contenuti tradotti
  - `docs/*.md` → tradotti
  - `competitors.json` (o config) → schema invariato, esempi con nomi internazionali se possibile
  - `.env.example` → commenti in inglese
  - `.github/workflows/*.yml` → commenti tradotti se ce ne sono
  - `.gitignore` → identico (file path puri)

Aggiungi in testa a ogni file gemello (in commento appropriato per il formato) un riferimento al fratello italiano per non perdere la corrispondenza.

### 7. Verifica di qualità

**Struttura materiali (flat, ready-to-test)**:
- [ ] Niente sottocartelle `01-`, `02-`, `03-` come struttura primaria.
- [ ] Al root della cartella materiali ci sono: `README.md`, `INIZIO_QUI.md`, `.gitignore`, e (se servono credenziali) `.env.example`.
- [ ] Sottocartelle solo per gruppi omogenei (`prompts/`, `.claude/agents/`, `scheduling/`, `docs/`).
- [ ] Lo script principale è al root, non in `03-script/`.
- [ ] Il config principale (es. `competitors.json`) è al root, non in `02-config/`.
- [ ] Lo script legge i config da path relativi al root (es. `Path(__file__).parent / "config.json"`), non da sottocartelle.
- [ ] Il flusso utente è: `cp .env.example .env` → compila → lancia. Niente copia di file in giro.

**Coerenza path (CRITICO — errore frequente)**:
- [ ] **Tutti i path nei prompt/agent .md matchano la struttura reale**: se il file è `competitors.json` al root, i prompt dicono `competitors.json`, MAI `config/competitors.json`.
- [ ] **Grep di verifica**: dopo aver generato i file, esegui `grep -r "config/" materiali/` e verifica che nessun file referenzi path inesistenti.
- [ ] **Settings Claude Code nel path giusto**: se esiste, è in `.claude/settings.json` — MAI `claude-settings.json` al root.
- [ ] **Niente script `init-progetto.sh`** o simili che ricreano la struttura da zero.
- [ ] **docs/ aggiornati**: se ci sono file in `docs/`, i path che referenziano (es. "apri `daily-brief.md`") devono puntare alla posizione reale (root), non a vecchie sottocartelle.
- [ ] **README.md aggiornato**: la mappa dei file nel README deve riflettere esattamente i file presenti nella cartella, senza file inesistenti o mancanti.
- [ ] **Ordine operazioni negli agent**: se un agent deve rinominare un file prima di scriverne uno nuovo (es. `pricing.md` → `pricing-previous.md`), l'istruzione di rename deve venire PRIMA dell'istruzione di scrittura, non dopo.

**Sicurezza credenziali**:
- [ ] `.env.example` ha solo placeholder fittizi (mai chiavi reali).
- [ ] `.gitignore` esclude `.env` (con eccezione `!.env.example`).
- [ ] Il HTML pubblico avverte di non committare `.env` e cosa fare se succede (revoca + ricreazione).

**HTML pubblico**:
- [ ] Niente frasi tipo "Da spiegare:", "Cosa annunciare:", "Menzione X", "Cosa fai qui:".
- [ ] Niente `.review-note` o `.verdict-summary` dentro PRINCIPALE.html.
- [ ] HTML self-contained (CSS inline, no CDN).
- [ ] Apertura chiara: "Cosa fa il sistema, in concreto" + esempio reale.
- [ ] Sezione "Setup iniziale" con prerequisiti comuni (Claude Code, API key, eventuali credenziali, account opzionali) PRIMA delle sezioni dei singoli metodi/step.
- [ ] Sezione setup di ogni metodo: il metodo PRIMARIO è "apri Claude Code nella cartella materiali → scrivi 'esegui il setup leggendo INIZIO_QUI.md'". I comandi terminale manuali vanno in un `<details>` "Approfondimento tecnico" a fine sezione.
- [ ] Claude Desktop (app) presentato come interfaccia consigliata, CLI come alternativa nell'approfondimento tecnico.
- [ ] Community-box finale con CTA dirette al pubblico.

**File funzionanti**:
- [ ] Tutti i file in `materiali/` sono funzionanti (no TODO).
- [ ] Lo script gira così com'è dopo `cp .env.example .env` + compilazione.

## Comandi utente che attivano questa automazione

- "crea i materiali per [titolo idea]"
- "stadio 3 sull'idea [titolo]"
- "produci PRINCIPALE.html per [titolo idea]"
- "produci SCRIPT.md per [titolo idea]"
- "rifai lo script per [idea]"

## Cosa NON fa questa automazione

- NON fa scraping online (presuppone che `_guida_draft.md` esista)
- NON inietta i suggerimenti di revisione (lo fa lo stadio 5, in un file separato)
- NON crea le 2 varianti tecniche (lo fa lo stadio 6)
- NON pubblica nulla — solo file locali in `CONTENUTI/<slug-it>/` e `CONTENUTI/<slug-en>/`
