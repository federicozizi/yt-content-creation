# Revisione: La tua newsletter AI personale con Claude Code

**Data:** 2026-05-16
**File rivisti:** PRINCIPALE.html + SCRIPT.md + materiali/ (cartelle IT + EN)
**Verdetto:** PRONTO CON RAFFORZAMENTI ⚠️

> Questo è un file di revisione PRIVATA. Non va consegnato al pubblico. Serve a te per applicare modifiche al pacchetto prima di registrare.

---

## Tipo di contenuto identificato

**Build di mini-tool concreto** — il pubblico costruisce un sistema funzionante (newsletter automatizzata) seguendo 4 step. Dopo il video, ha qualcosa di replicabile sulla propria macchina in 3 minuti.

Standard del canale completamente applicabile. Format coerente col video precedente (GitHub per Claude Code) ma con un caso study molto più snello e replicabile.

---

## Blocchi standard applicabili

| Blocco | Necessario? | Motivazione |
|---|---|---|
| Introduzione pratica e rapida | sì | Format build → sempre |
| Descrizione del sistema | sì | C'è un'architettura concreta (4 file + Claude Code + Routines) |
| Analisi pratica | sì | Setup + prerequisiti vanno citati anche se rinviati a Skool |
| Dimostrazione live | sì | C'è una demo reale del primo run (CLIP 14-15) |

---

## Verifica blocchi presenti

### Introduzione — ✅
CLIP 01 (hook) + CLIP 02-04 (cos'è/cosa costruiremo/come funziona) coprono benissimo l'apertura. Il hook è efficace: parte dal pain reale ("quante volte al giorno apri Twitter senza trovare nulla"). Tempo stimato: ~3 minuti, in linea col target del canale.

### Descrizione del sistema — ✅
CLIP 04 (PRINCIPALE.html → #come-funziona) ha un diagramma di architettura chiaro e ben fatto. I 3 pezzi (file, Claude Code, Routines) sono visualizzati nel diagramma scuro. Lo spettatore capisce in 30 secondi com'è strutturato.

### Analisi pratica — ⚠️
Prerequisiti minimali (giusto: solo Claude Code). Setup interamente rinviato a Skool (CLIP 05) — coerente con la regola "setup non si dimostra mai a video". **Manca però la trasparenza sui costi**: il sistema usa l'abbonamento Claude (Pro/Max), non viene mai detto esplicitamente che servono ~$20/mese di subscription. Per chi usa l'API key, non viene quantificato il costo per run (~$0.01-0.05). Sezione "Cos'è" e "Setup iniziale" del PRINCIPALE.html sono vaghe sul "se hai già un abbonamento Claude ti basta loggarti" senza dire cosa fare chi non ce l'ha.

### Dimostrazione — ✅
CLIP 14-15 (lancio claude + file generato) sono il momento "wow" del video. Visivamente forte: terminale che gira, file che appare, lettura del markdown. Sotto i 90 secondi totali. CLIP 18 (claude routines add) chiude bene mostrando lo scheduling reale.

---

## Verifiche trasversali

- **Audience non tecnica**: ⚠️
  Il prompt orchestratore (`prompts/newsletter-daily.md`) è molto tecnico. Cita `WebFetch` come tool, parla di "ISO 8601 timestamp", "filter", "deep-dive". Il pubblico non-tech che apre questo file dopo aver scaricato i materiali rischia di spaventarsi. **Aggiungerei un paragrafo di intro al prompt in italiano semplice tipo: "questo è il foglio di istruzioni che Claude segue ogni mattina. Non devi capirlo né modificarlo — è già pronto."**

- **Stile user-oriented**: ✅
  Niente "Da spiegare:" o "Menzione X". Tutto è prosa diretta. Il SCRIPT.md ha gli unici brief regia, ma è privato.

- **Materiali funzionanti**: ⚠️
  Non testati end-to-end. Punti di rischio reali:
  1. La pagina `https://www.anthropic.com/news` potrebbe essere caricata dinamicamente con JavaScript — WebFetch di Claude Code potrebbe vedere solo HTML statico con poco contenuto. **Da testare PRIMA della registrazione**: lanciare manualmente il prompt e verificare che Claude estragga davvero la lista articoli.
  2. Il sintassi `claude routines add` è inventata (Claude Routines esiste come concetto nel canale ma non ho verificato la sintassi esatta CLI). **Verifica con `claude routines --help`** che i flag `--schedule`, `--cwd`, `--prompt` esistano davvero. Se la sintassi reale è diversa, aggiorna sia il prompt che lo SCRIPT che gli HTML.

- **Riproducibilità**: ✅
  Cartella `materiali/` è davvero ready-to-test (1 comando, cd + claude --print). Pattern flat rispettato.

- **Apertura concreta**: ✅
  Cosa fa il sistema → esempio concreto del file output (diagram in #cosa-costruiremo) → perché → setup. Ordine corretto.

- **Community-box finale**: ✅
  Presente, con doppia CTA (Skool + consulenza). Versione SCRIPT.md (CLIP 21) è verbatim e ben calibrata.

- **Effetto wow**: ⚠️
  La newsletter generata fa "wow", ma il wow potrebbe essere più forte se nel diagramma di esempio (sezione #cosa-costruiremo) si vedesse un format più visivamente accattivante. Attualmente è puro markdown bullet — funzionale ma asciutto. **Considerare di mostrare un'opzione "newsletter HTML" o "newsletter con tabellina pulita"** come variante, magari in una clip B-roll.

- **Sincronia bilingue**: ✅
  PRINCIPALE.html IT e EN sono mirror fedeli. SCRIPT.md ha solo DIRE tradotti. Materiali rinominati correttamente (`INIZIO_QUI.md` → `START_HERE.md`, `esempio-output.md` → `example-output.md`, `fonti.json` → `sources.json`, `docs/email-opzionale.md` → `docs/email-optional.md`).

- **Coerenza linguistica EN**: ✅
  Nessun residuo italiano nei file EN. Verificato: CLAUDE.md, README.md, START_HERE.md, sources.json (chiavi `name`/`url`/`category`/`description` in EN), prompts/newsletter-daily.md, scheduling/claude-routines.md, docs/email-optional.md, example-output.md tutti coerentemente in inglese.

---

## Modifiche concrete da applicare al pacchetto

### 1. PRINCIPALE.html IT — sezione #setup
**Problema**: trasparenza sui costi. Lo spettatore non sa quanto costa l'abbonamento Claude o l'API.
**Suggerimento**: aggiungi una riga dentro il `<li>` di Claude Code installato, tipo:
> *Funziona su Mac, Windows, Linux. Serve un abbonamento Claude (Pro a 20$/mese, Max a 100$/mese) oppure una API key con consumo a uso (~$0.01-0.05 a run di newsletter, quindi indicativamente $0.30-1.50/mese).*

Replica identico in PRINCIPALE.html EN (sezione `#setup`, stesso `<li>`).

### 2. SCRIPT.md IT — CLIP 05
**Problema**: lo stesso, manca la cifra a voce.
**Suggerimento**: nel verbatim del DIRE, aggiungi tra "Claude Code installato" e "i materiali":
> *Costa circa 20 dollari al mese di abbonamento Claude, oppure se preferisci pagare a consumo ti costerà sotto i 2 dollari al mese di API.*

Replica in SCRIPT.md EN CLIP 05.

### 3. `materiali/prompts/newsletter-daily.md` (IT + EN)
**Problema**: prompt molto tecnico, può intimidire il pubblico non-tech che lo apre.
**Suggerimento**: aggiungi in testa al file, prima del titolo `# Prompt orchestratore`, un blocco:
```markdown
> **A chi sta leggendo per curiosità**: questo è il foglio di istruzioni che Claude segue ogni mattina per generare la tua newsletter. Non devi capirlo né modificarlo — è già pronto. Tu modifichi solo `fonti.json` (cosa leggere) e `CLAUDE.md` (come scrivere). Per il resto, Claude legge questo file e fa il lavoro.
```

In EN:
```markdown
> **For those reading out of curiosity**: this is the instruction sheet Claude follows every morning to generate your newsletter. You don't need to understand it or change it — it's already set up. You only edit `sources.json` (what to read) and `CLAUDE.md` (how to write). For everything else, Claude reads this file and does the work.
```

### 4. PRE-REC SCRIPT.md (IT + EN) — sezione B
**Problema**: il pre-warming dice "verifica 1 ora prima che anthropic.com/news carichi normalmente e abbia articoli recenti". Manca il fallback se la pagina è JS-only.
**Suggerimento**: aggiungi sotto la nota esistente:
> Se WebFetch di Claude Code non riesce a estrarre articoli dalla pagina news (perché caricata via JavaScript), aggiungi temporaneamente in `fonti.json` un URL alternativo testato che ritorna HTML statico (es. la versione RSS se esiste: `https://www.anthropic.com/news/rss` da verificare). In ultima istanza, falsifica il primo run usando un blog con HTML statico (es. `https://simonwillison.net/`) per garantire output.

### 5. PRINCIPALE.html IT + EN — diagramma in #cosa-costruiremo
**Problema**: esempio markdown un po' asciutto.
**Suggerimento opzionale**: prima del diagram, aggiungi una frase tipo:
> Il formato di default è markdown (leggibile ovunque). Se preferisci HTML ben formattato o un layout email-style, modifichi il prompt orchestratore in 2 righe.

Replica identico in EN sotto la sezione `#what-build`.

### 6. SCRIPT.md IT + EN — CLIP 14 plan B
**Problema**: se Claude non riesce a estrarre nulla durante il LIVE, ti trovi col terminale fermo e niente da mostrare.
**Suggerimento**: aggiungi sotto il `🎬 LIVE` di CLIP 14:
> ⚠️ Se la run fallisce o produce un risultato troppo scarno: stacca la rec, controlla l'output Claude per capire dove ha avuto difficoltà, modifica temporaneamente `fonti.json` con una fonte più affidabile (es. blog statico), rilancia. Niente di tutto questo va a video — tu mostri solo il run che funziona.

---

## Punti deboli che impatterebbero engagement

1. **Hook potrebbe essere più "tagliente"**: l'apertura è buona ma il pain "non trovi mai niente di utile" potrebbe diventare più viscerale ("conosci quella sensazione di aver perso 2 ore su LinkedIn senza imparare niente?"). Modifica opzionale al verbatim di CLIP 01.

2. **Manca un confronto "prima/dopo" visivo**: nelle clip 14-15 mostri il sistema che funziona ma non c'è un momento "guarda quanto tempo risparmi". Considera una clip extra (opzionale, da inserire dopo CLIP 15) in CAMERA dove dici una cifra tipo "in 90 secondi sai quello che ti farebbe leggere 50 articoli in 2 ore di scroll".

3. **CLIP 19 (altri usi) è solo letta a video**: potrebbe perdere tensione. Considera di animare il momento mettendo un'enfasi su 1-2 use case che ti senti più adatti al tuo pubblico (es. brand monitoring per agenzie), invece di 5 case che tutti suonano uguali.

---

## Verdetto

**PRONTO CON RAFFORZAMENTI**. Il pacchetto è solido, lo script è eseguibile, i materiali sono coerenti tra IT ed EN. I rafforzamenti consigliati sono modifiche di 30 minuti totali e migliorano significativamente:
1. La trasparenza sui costi (oggi assente, sarà la prima domanda nei commenti)
2. La robustezza tecnica del LIVE (il rischio "WebFetch non vede articoli dinamici" va anticipato)
3. L'engagement nelle sezioni più "tecniche" (prompt orchestratore intimidatorio, CLIP 19 piatta)

**Bloccante reale prima di registrare**: testare end-to-end il prompt orchestratore una volta sul tuo PC reale, per verificare che WebFetch funzioni sulle pagine Anthropic. Se non funziona, sistema le fonti in `fonti.json` con alternative testate PRIMA di accendere la camera.
