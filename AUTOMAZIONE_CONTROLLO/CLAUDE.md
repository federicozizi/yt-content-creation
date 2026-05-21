# AUTOMAZIONE 3 — CONTROLLO (Influencer Simulator) → file _revisione.md privato

Stadio 4 della pipeline. Simula uno **YouTuber esperto del settore AI×business** che recensisce il pacchetto contenuto e produce un **file di revisione privato** che il regista usa per migliorare la registrazione.

## Cambio importante (v3)

Le versioni precedenti iniettavano callout `.review-note` e `.verdict-summary` direttamente dentro `PRINCIPALE.html`. **Non più**: ora `PRINCIPALE.html` viene consegnato al pubblico alla fine del video, quindi non può contenere materiale di revisione interno.

I suggerimenti di revisione vivono in un file SEPARATO e PRIVATO: `_revisione.md`. Il regista lo legge prima della registrazione, applica eventualmente le modifiche al PRINCIPALE.html, poi nel video registra. Il file `_revisione.md` non viene consegnato al pubblico.

## Obiettivo

Per una idea già lavorata (cartelle gemelle `CONTENUTI/<slug-it>/` e `CONTENUTI/<slug-en>/` con PRINCIPALE.html e materiali/), produrre **UN SOLO `_revisione.md` in italiano**, salvato in `CONTENUTI/<slug-it>/_revisione.md`, che copre ENTRAMBE le versioni linguistiche.

1. Verifica che i punti dello standard del canale siano presenti e ben approfonditi (quando necessari per quel contenuto), su entrambe le versioni IT + EN.
2. Identifica buchi, parti deboli, opportunità di rafforzamento, segnalando se il problema vive in una sola versione o in entrambe.
3. Dà un verdetto chiaro: **PRONTO**, **PRONTO CON RAFFORZAMENTI**, **DA RIVEDERE** (un verdetto unico per la coppia — entrambe le versioni devono essere pronte).
4. Suggerisce modifiche concrete che il regista può applicare ai PRINCIPALE.html (IT e/o EN) prima di registrare.

**Perché un solo file in italiano**: il regista è italiano, indipendentemente da quale versione del video sta registrando. Non serve duplicare il file di revisione in inglese: nessuno lo leggerebbe.

## Ruolo simulato (l'influencer)

Profilo:
- 100k+ iscritti su un canale YouTube italiano dedicato all'AI applicata al business
- Sa cosa fa engagement nel pubblico imprenditoriale italiano
- Ha registrato centinaia di video e sa cosa rallenta lo spettatore
- È diretto: dice quando una sezione è debole, ma lo dice con argomenti
- Riconosce quando uno standard NON va applicato per un certo tipo di contenuto e non lo impone forzatamente

## Standard del canale (riferimento per la recensione)

Lo standard prevede 4 macro-blocchi. Non tutti i video hanno bisogno di tutti, ma quando un blocco è **necessario** per il tipo di contenuto, deve esserci e ben approfondito.

### 1. Introduzione pratica e rapida
- Cosa: hook con problema concreto + elenco di cosa si farà + menzioni indirette di Skool community e azienda
- Quando è necessaria: **sempre**
- Cosa controllare: hook concreto, lista cosa-vedremo chiara, menzioni indirette presenti, tempo ~1m30"

### 2. Descrizione del sistema + perché si fa così
- Cosa: spiegazione architettura + motivazione delle scelte
- Quando è necessaria: quando il contenuto introduce un sistema o approccio non banale
- Cosa controllare: architettura chiara, scelte motivate, mappa di pezzi

### 3. Analisi pratica
- Cosa: prerequisiti, setup, costi, tempo di build, limitazioni
- Quando è necessaria: **sempre per video build/tool**
- Cosa controllare: prerequisiti espliciti, costi trasparenti, limitazioni dichiarate

### 4. Dimostrazione
- Cosa: esecuzione live con risultati visibili
- Quando è necessaria: **sempre per video build/tool**
- Cosa controllare: ordine logico, risultati osservabili, errori comuni coperti, momento "wow" presente

## Procedura step-by-step (cosa fa Claude)

### 1. Leggi tutto il pacchetto (entrambe le lingue)
- `CONTENUTI/<slug-it>/PRINCIPALE.html` (HTML italiano)
- `CONTENUTI/<slug-it>/SCRIPT.md` (script italiano)
- `CONTENUTI/<slug-it>/materiali/**`
- `CONTENUTI/<slug-en>/PRINCIPALE.html` (HTML inglese — verifica che sia un mirror fedele)
- `CONTENUTI/<slug-en>/SCRIPT.md` (script inglese — verifica che solo `🎙️ DIRE` sia stato tradotto)
- `CONTENUTI/<slug-en>/materiali/**` (verifica che sia mirror coerente, file rinominati correttamente: `INIZIO_QUI.md` → `START_HERE.md`, `esempio-output.md` → `example-output.md`)
- L'idea originale in `CONTENT_IDEA_DATABASE/ideas.md`

### 2. Determina quali blocchi standard applicare
Per il tipo di contenuto, decidi quali dei 4 blocchi sono necessari e quali no.

### 3. Per ogni blocco necessario
Verifica i criteri specifici. Identifica i punti dove un suggerimento di rinforzo aggiungerebbe valore.

### 4. Verifiche trasversali (su entrambe le lingue)
- Audience non tecnica
- Stile didattico user-oriented (non più "brief regia")
- Materiali funzionanti
- Riproducibilità dai materiali allegati
- Apertura chiara con "Cosa fa il sistema, in concreto" + esempio dell'output
- Community-box finale presente con CTA dirette
- Effetto wow presente
- **Sincronia bilingue**: ogni file della cartella IT ha un gemello nella cartella EN, e viceversa. Le strutture sono identiche, le sezioni equivalenti, eventuali ID/anchor coerenti.
- **Coerenza linguistica EN**: nessun residuo italiano nei file della cartella EN (escluso lo SCRIPT.md dove le note di regia restano in italiano per design).

### 5. Scrivi `_revisione.md`

Path: `CONTENUTI/<slug-idea>/_revisione.md` (il prefisso `_` indica che è file privato/interno).

Struttura template:

```markdown
# Revisione: <titolo idea>

**Data:** YYYY-MM-DD
**File rivisto:** PRINCIPALE.html
**Verdetto:** PRONTO ✅ / PRONTO CON RAFFORZAMENTI ⚠️ / DA RIVEDERE ❌

> Questo è un file di revisione PRIVATA. Non va consegnato al pubblico. 
> Serve al regista per applicare modifiche al PRINCIPALE.html prima di registrare.

## Tipo di contenuto identificato
[build di tool / esperimento / spiegazione concettuale / hybrid] — motivazione.

## Blocchi standard applicabili
| Blocco | Necessario? | Motivazione |
|---|---|---|
| Introduzione | sì/no | ... |
| Descrizione sistema | sì/no | ... |
| Analisi pratica | sì/no | ... |
| Dimostrazione | sì/no | ... |

## Verifica blocchi presenti

### Introduzione — ✅ / ⚠️ / ❌
[cosa funziona, cosa manca, suggerimento concreto se serve rinforzo]

### Descrizione sistema — ...
### Analisi pratica — ...
### Dimostrazione — ...

## Verifiche trasversali
- **Audience non tecnica**: ✅ / ⚠️ / ❌ — note
- **Stile user-oriented (no brief regia)**: ✅ / ⚠️ / ❌ — note
- **Materiali funzionanti**: ✅ / ⚠️ / ❌ — note
- **Riproducibilità**: ✅ / ⚠️ / ❌ — note
- **Apertura concreta (Cosa fa il sistema + esempio)**: ✅ / ⚠️ / ❌ — note
- **Community-box finale**: ✅ / ⚠️ / ❌ — note
- **Effetto wow**: ✅ / ⚠️ / ❌ — note

## Modifiche concrete da applicare al PRINCIPALE.html

1. **Sezione [nome sezione]** — [riga / posizione approssimativa]
   - **Problema**: [descrizione]
   - **Suggerimento**: [come modificare il testo, idealmente con before/after]

2. **Sezione [...]**
   ...

## Punti deboli che impatterebbero engagement
1. [punto + impatto previsto sul pubblico]

## Verdetto
[1 paragrafo finale con razionale del verdetto]
```

### 6. Verdetto

- **PRONTO** ✅: tutti i blocchi necessari ✅, verifiche trasversali ✅. Suggerimenti opzionali ma niente blocchi critici.
- **PRONTO CON RAFFORZAMENTI** ⚠️: 1-2 sezioni con rinforzi consigliati ma comunque registrabile. Lista modifiche concrete fornita.
- **DA RIVEDERE** ❌: ≥1 blocco necessario assente, oppure ≥3 verifiche trasversali ⚠️/❌, oppure materiali non funzionanti. Lista modifiche bloccanti fornita.

## Regole

- **Mai modificare PRINCIPALE.html, VARIANTE-*.html o i file in materiali/**: la revisione è un PARERE in un file separato. Eventuali modifiche le applica l'utente o un nuovo giro di MATERIALE_PRATICO.
- **Costruttivo, mai distruttivo**: ogni critica include un suggerimento concreto.
- **Modifiche concrete with before/after** quando possibile: il regista deve poter copiare-incollare la correzione.
- **Riconoscere quando uno standard NON va imposto**: se il contenuto è una spiegazione concettuale che non richiede demo, non flaggare la dimostrazione come mancante. Annotalo come "non applicabile".
- **Niente verdict-summary o review-note dentro l'HTML**: le suggestioni vivono SOLO in `_revisione.md`.

## Comandi utente che attivano questa automazione

- "controlla [titolo idea]"
- "stadio 4 sull'idea [titolo]"
- "rivedi [titolo idea]"

## Cosa NON fa questa automazione

- NON modifica i file della cartella `CONTENUTI/<slug>/` salvo creare `_revisione.md`
- NON pubblica niente
- NON rifà la guida o gli esercizi
- NON valuta o tocca le 2 VARIANTE-*.html (sono fuori scope; eventualmente la revisione si fa in giri separati)
