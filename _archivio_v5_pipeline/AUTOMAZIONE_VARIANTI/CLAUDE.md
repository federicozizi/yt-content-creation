# AUTOMAZIONE 4 — VARIANTI (2 metodi tecnici alternativi, bilingue IT+EN)

Stadio 5 e finale della pipeline. Produce **2 file HTML alternativi** (in entrambe le lingue) che rappresentano lo stesso topic realizzato con **metodi tecnici diversi**, ma che portano allo stesso risultato finale.

## Obiettivo

L'utente vuole poter scegliere **quale metodo registrare** in base a:
- pubblico target (es. chi usa già Claude Code vs chi usa n8n vs chi vuole controllo Python)
- complessità desiderata
- eventuale serie già in corso

Output (in ENTRAMBE le cartelle gemelle):
- `CONTENUTI/<slug-it>/VARIANTE-1.html` + `CONTENUTI/<slug-en>/VARIANTE-1.html`: stesso topic, metodo tecnico A
- `CONTENUTI/<slug-it>/VARIANTE-2.html` + `CONTENUTI/<slug-en>/VARIANTE-2.html`: stesso topic, metodo tecnico B
- Le rispettive `materiali-variante-N/` esistono in entrambe le cartelle (file tradotti come per `materiali/` del PRINCIPALE — vedi `AUTOMAZIONE_MATERIALE_PRATICO/CLAUDE.md` per la mappatura traduzioni).

Il `PRINCIPALE.html` resta come "metodo principale" (il più allineato col canale o quello più solido tecnicamente). Le 2 varianti sono alternative legittime, non versioni inferiori.

**Mirror bilingue**: ogni file di variante e ogni file dentro `materiali-variante-N/` esiste in entrambe le cartelle gemelle. Stesse regole di traduzione del PRINCIPALE: HTML completamente tradotto, materiali tradotti con file rinominati (`INIZIO_QUI.md` → `START_HERE.md`, `esempio-output.md` → `example-output.md`, ecc.), `.gitignore`/`.env.example`/workflow YAML con commenti tradotti.

## Doppio scopo (uguale al PRINCIPALE)

Anche le VARIANTE-*.html sono **slide replacement durante la registrazione** E **guida consegnabile al pubblico**. Stessa scaletta narrativa, stessi componenti CSS, stesse regole di tono del PRINCIPALE.html.

## Cosa NON cambia tra principale e varianti

- Il **topic generale** (es. "creare un team di agenti AI")
- L'**obiettivo finale** del video
- Il **risultato concreto** per lo spettatore
- Il **case study applicato** (es. "competitor brief giornaliero") — è lo stesso esempio che mostriamo in tutte e 3 le versioni
- Lo **standard del canale** applicabile
- Lo **stile user-oriented** (no brief regia, no decorazioni promozionali)
- La **scaletta narrativa** (apertura concettuale → case study → architettura → setup → step → generalizzazione → riepilogo)

## Cosa cambia tra principale e varianti

- **Stack tecnologico**: tool, librerie, servizi usati per implementare il pattern
- **Filosofia**: es. "all-in-Anthropic" vs "no-code" vs "DIY-script"
- **Audience leggermente diversa**: ognuna parla a un sottoinsieme un po' diverso del pubblico
- **Architettura tecnica**: i "mattoni" del sistema cambiano (es. Agent Teams + Routines vs Cron + HTTP nodes vs asyncio.gather)
- **Materiali pratici**: ognuno ha i suoi script/file specifici per quel metodo

## Esempio concreto (idea "team di agenti AI")

Caso reale del video "team di agenti AI con Claude Code" — formato 3-metodi-in-uno (PRINCIPALE = video unione che mostra A + B + C, VARIANTE-1 = no-code visuale alternativo).

| | Metodo A (in PRINCIPALE) | Metodo B (in PRINCIPALE) | Metodo C (in PRINCIPALE) | VARIANTE-1 |
|---|---|---|---|---|
| Stack | Claude Code + Agent Teams + Routines | Anthropic SDK raw + asyncio + cron | Claude Agent SDK (Python) + cron/GH Actions | n8n + Claude API + scheduler n8n |
| Filosofia | Zero codice, tutto Claude Code | DIY a basso livello | "Claude Code come libreria" | No-code visuale |
| Audience | Chi usa già Claude Code | Chi vuole controllo totale | Chi vuole programmaticità senza riscrivere il loop | Chi usa n8n/Make |

**Regola di coerenza ecosistema**: in un video Claude, i metodi del PRINCIPALE devono stare tutti nell'ecosistema Anthropic (Claude Code, Anthropic SDK raw, Claude Agent SDK, Managed Agents). Strumenti che usano Claude solo "come API esterna" (Apps Script, Make, Zapier, n8n) vanno bene come VARIANTE separata, **mai** come metodo principale del confronto. Vedi `~/.claude/projects/.../memory/feedback_coerenza_ecosistema.md`.

## Procedura step-by-step (cosa fa Claude)

### 1. Raccogli il contesto
- Leggi `PRINCIPALE.html` per capire il topic generale, il case study scelto, e la scaletta narrativa.
- Leggi `_guida_draft.md` (sezione "Approcci tecnici ALTERNATIVI" se presente).
- Leggi `materiali/**` per capire la profondità dei materiali principali.

### 2. Identifica i 2 metodi tecnici alternativi
Se lo stadio 2 ha pre-identificato le alternative, usale. Altrimenti fai una breve ricerca.

Criteri di scelta:
- **Devono essere REALI e funzionanti**, non teoriche.
- **Coprire approcci genuinamente DIVERSI** (no "stesso approccio con un library leggermente diverso").
- **Avere ognuna un'audience identificabile**.

### 3. Per OGNI variante (1 e 2), produci un HTML completo

**Identica scaletta narrativa del PRINCIPALE.html**. Vedi `AUTOMAZIONE_MATERIALE_PRATICO/CLAUDE.md` per il template completo. Riassunto delle sezioni obbligatorie:

1. **Header** con titolo + sottotitolo (titolo del topic generale, NON del case study)
2. **`metodo-switch`** con `📍 Stai qui` sull'opzione corrente
3. **TOC**
4. **Cos'è [il topic generale]** — apertura concettuale (definizione + cosa lo distingue + quando ha senso)
5. **Cosa costruiremo oggi (il case study)** — esempio applicato, mockup output, frase chiave "questo è UN esempio del pattern"
6. **Come funziona il sistema** — i "mattoni" tecnici DEL METODO SPECIFICO della variante (non quelli del principale!) + diagramma adattato
7. **Setup** — prerequisiti e setup specifici della variante
8. **Step 1, 2, ... N** — i passi pratici specifici, ognuno con `.concetto-chiave` + `<h4>Nel nostro caso</h4>` + `<h4>Cosa fare</h4>`
9. **Oltre [il case study]: come applicare il pattern** — generalizzazione con 3-5 use case dove lo stesso pattern + stack della variante si applica
10. **Riepilogo** — cosa lo spettatore ha imparato (sul pattern + sullo stack della variante)
11. **Materiali allegati** — tabella delle cartelle specifiche della variante
12. **Community-box** — CTA dirette al pubblico

### 4. Genera materiali separati per ogni variante (struttura FLAT obbligatoria)

Se i materiali pratici sono **significativamente diversi** dal principale (è la norma per le varianti):
- Crea cartelle separate `materiali-variante-1/` e `materiali-variante-2/` con i file specifici.
- **Stessa struttura flat ready-to-test del PRINCIPALE**: vedi `AUTOMAZIONE_MATERIALE_PRATICO/CLAUDE.md` — al root ci sono `README.md`, `INIZIO_QUI.md`, `.gitignore`, `.env.example` (se servono credenziali), script principale, config principale. Niente sottocartelle numerate.
- I link `<a href="materiali-variante-1/...">` puntano a queste cartelle.
- **Copia obbligatoria del file HTML padre dentro la cartella materiali della variante** (regola "HTML anche dentro materiali"): `materiali-variante-1/VARIANTE-1.html` è copia di `<slug>/VARIANTE-1.html` con link aggiustati. Stesso comando sed di AUTOMAZIONE_MATERIALE_PRATICO, ma sostituisci `href="materiali-variante-1/X"` → `href="X"`. Idem per la variante 2.

Se la variante condivide alcuni materiali col principale (es. gli stessi 4 file `.claude/agents/*.md` perché due metodi diversi caricano gli stessi sub-agent), **riusali** copiandoli identici nella cartella della variante: ogni cartella materiali deve essere autosufficiente, l'utente non deve mai navigare tra cartelle diverse per assemblare il sistema.

### 4b. Riusabilità tra metodi — esempio "stessi sub-agent"

Se la variante usa gli stessi artefatti del principale (es. il Metodo C "Claude Agent SDK" carica gli stessi `.claude/agents/*.md` del Metodo A "Claude Code CLI"):
- **Copia** i file in entrambe le cartelle materiali (la duplicazione è voluta — autosufficienza > DRY)
- **Spiega esplicitamente** nel README/HTML della variante che sono identici al PRINCIPALE: *"i 4 sub-agent in `.claude/agents/` sono gli stessi del Metodo A — riusi il prototipo CLI come backend del tuo script Python, zero riscrittura"*

### 5. Aggiorna il blocco metodo-switch in tutti e 3 gli HTML

In ognuno dei 3 file (PRINCIPALE, VARIANTE-1, VARIANTE-2), il blocco `metodo-switch` deve avere `📍 Stai qui` sull'opzione corrente e link funzionanti alle altre 2.

### 6. Verifica di qualità

Per ogni variante:

**Coerenza con PRINCIPALE**:
- [ ] La sezione "Cos'è [il topic generale]" è IDENTICA o quasi al PRINCIPALE.
- [ ] La sezione "Cosa costruiremo oggi" è IDENTICA o quasi al PRINCIPALE.
- [ ] La sezione "Come funziona il sistema" è SPECIFICA per il metodo della variante.
- [ ] Gli Step pratici sono SPECIFICI per il metodo della variante.
- [ ] La sezione "Oltre [il case study]" mantiene gli stessi 5 use case del PRINCIPALE adattandoli allo stack della variante.
- [ ] CSS identico al PRINCIPALE (palette, classi, layout).
- [ ] Community-box finale presente.
- [ ] Il blocco metodo-switch è in cima e linka correttamente alle altre versioni.

**Materiali della variante (struttura flat ready-to-test)**:
- [ ] La cartella `materiali-variante-N/` segue le stesse regole di `materiali/` del PRINCIPALE.
- [ ] Al root ci sono `README.md`, `INIZIO_QUI.md`, `.gitignore`, e (se applicabile) `.env.example`.
- [ ] Niente sottocartelle numerate `01-`, `02-` ecc.
- [ ] Lo script principale è al root e legge i config da path relativi al root.
- [ ] L'utente fa solo `cp .env.example .env` → compila → lancia.
- [ ] Se la variante riusa artefatti del PRINCIPALE (es. file `.md`), sono COPIATI nella cartella della variante (autosufficienza > DRY).

**Coerenza path (CRITICO — errore frequente)**:
- [ ] **Tutti i path nei prompt/agent .md matchano la struttura reale del filesystem**: se il config è `competitors.json` al root, i prompt dicono `competitors.json`, MAI `config/competitors.json`.
- [ ] **Se copi agent .md dal PRINCIPALE**, verifica che i path nei file copiati siano ancora corretti per la struttura della variante. Non copiare e basta — leggi e adatta.
- [ ] **Settings Claude Code**: se servono, metterli in `.claude/settings.json`, MAI `claude-settings.json` al root.
- [ ] **Niente script che ricreano la struttura** (init-progetto.sh o simili): la cartella materiali-variante-N/ È il progetto.
- [ ] **docs/ aggiornati**: tutti i path nei file docs/ devono puntare alla posizione reale (root della variante), non a vecchie sottocartelle.
- [ ] **README.md aggiornato**: la mappa dei file deve riflettere esattamente i file presenti nella cartella.
- [ ] **Ordine operazioni negli agent**: se un agent rinomina un file prima di scriverne uno nuovo, l'istruzione di rename deve venire PRIMA della scrittura.

**Sicurezza**:
- [ ] `.env.example` ha solo placeholder fittizi.
- [ ] `.gitignore` esclude `.env` e altri file sensibili.
- [ ] Il HTML pubblico avverte sui rischi del commit accidentale di credenziali.

**Pulizia**:
- [ ] Niente "Da spiegare:", "Cosa fai qui:", "Menzione X (indiretta)" o brief regia.
- [ ] Niente review-note o verdict-summary nell'HTML pubblico.

## Regole

- **Le 2 varianti devono essere DAVVERO diverse**: stack diverso, filosofia diversa. Non variazioni minori dello stesso approccio.
- **Topic e case study identici al PRINCIPALE**: cambia solo COME costruiamo il sistema, non COSA costruiamo o PERCHÉ.
- **Onestà sui pro/contro**: nella sezione "Cos'è" o "Cosa costruiremo", dichiara esplicitamente quando questa via è preferibile e quando no rispetto al principale.
- **HTML self-contained** (CSS inline, nessuna dipendenza esterna).
- **Stile e tipografia coerenti** con `PRINCIPALE.html`.
- **Niente brief regia** dentro l'HTML pubblico.

## Comandi utente che attivano questa automazione

- "fai le varianti per [titolo idea]"
- "stadio 5 sull'idea [titolo]"
- "2 varianti tecniche di [titolo idea]"

## Cosa NON fa questa automazione

- NON modifica `PRINCIPALE.html`, salvo aggiornare il blocco `metodo-switch` in cima per linkare alle 2 varianti.
- NON crea più di 2 varianti (sempre esattamente 2 — il principale + 2 alternative = 3 totali).
- NON pubblica niente — file locali in `CONTENUTI/<slug-it>/` e `CONTENUTI/<slug-en>/`.
