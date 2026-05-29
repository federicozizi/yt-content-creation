# Claude 4.8 + Dynamic Workflows: 10 agenti per il tuo calendario editoriale

> Materiali del video YouTube **"Claude 4.8: faccio lavorare 10 agenti in parallelo sul mio business (la nuova feature 'Dynamic Workflows')"**.
> Dentro questa cartella trovi tutto quello che ho mostrato dal vivo: 10 piccoli script che bussano a 10 piattaforme diverse, un orchestratore che li lancia tutti insieme, e una dashboard che si apre da sola nel browser con i trend del momento.

---

## In 30 secondi - cosa fa

Lanci un comando. In meno di 10 secondi un sistema apre 10 piattaforme contemporaneamente (Hacker News, Reddit, YouTube, Google News, GitHub, Product Hunt, Medium, Dev.to, Lobsters, Hugging Face), tira giu' i 100 trend del momento, te li mette in una dashboard pulita nel browser. Se in piu' ci colleghi Claude 4.8 con il prompt che trovi qui dentro, ti trasforma quei 100 titoli in **30 idee video gia' pronte** divise per format.

E' il prototipo di "quello che faccio la domenica sera" — fatto pero' in tre minuti, e in modo che si possa rifare tutti i giorni.

---

## Quick start (per chi ha gia' Python installato)

```bash
# 1. Entra nella cartella materiali
cd materiali

# 2. Installa le 2 librerie necessarie
pip install -r requirements.txt

# 3. Lancia tutto
python orchestrator.py
```

La dashboard si apre da sola nel browser. Fine. Se non hai Python o vuoi capirci di piu', vai alla **Guida completa** qui sotto.

---

## Cosa ti serve prima di iniziare

- [ ] **Python 3.10 o superiore** - [https://www.python.org/downloads/](https://www.python.org/downloads/) - il linguaggio in cui sono scritti i 10 scraper. Se non lo hai, durante l'installazione spunta la casella **"Add Python to PATH"** in fondo alla prima schermata, altrimenti il terminale non lo trova.
- [ ] **VS Code** - [https://code.visualstudio.com](https://code.visualstudio.com) - l'editor di testo che useremo per leggere i file. Gratis.
- [ ] **(Opzionale, solo per la "strada 2" del video)** **Claude Code** + un account con accesso a Opus 4.8 - [https://claude.com/code](https://claude.com/code). Se non lo hai, la strada 1 (orchestratore Python) funziona lo stesso ed e' gia' tantissimo.
- [ ] **Una connessione internet decente**: lo script fa 10 richieste in parallelo verso 10 siti diversi.

Tempo totale per il primo setup: **circa 10 minuti**. Dopo, il sistema gira con un comando.

---

## Le 10 piattaforme monitorate (e perche' queste)

| Piattaforma | Cosa ti porta | File scraper |
|---|---|---|
| **Hacker News** | Le notizie tech che bucano oggi (community molto esigente) | `scrapers/hackernews.py` |
| **Reddit r/artificial** | Discussioni reali di chi usa l'AI tutti i giorni | `scrapers/reddit.py` |
| **Dev.to** | Tutorial pratici e build dimostrative | `scrapers/devto.py` |
| **Product Hunt** | Lanci di prodotti AI di oggi | `scrapers/producthunt.py` |
| **Medium** | Approfondimenti lunghi, opinioni di settore | `scrapers/medium.py` |
| **GitHub Trending** | I progetti open-source che stanno esplodendo oggi | `scrapers/github_trending.py` |
| **Lobste.rs** | Community tecnica selezionata, segnali di qualita' | `scrapers/lobsters.py` |
| **YouTube** | Ultimi video del canale Matt Wolfe (uno dei piu' grossi su AI) | `scrapers/youtube_ai.py` |
| **Google News IT** | La stampa italiana mainstream sull'AI | `scrapers/google_news.py` |
| **Hugging Face Papers** | I paper di ricerca che faranno notizia fra 3 mesi | `scrapers/huggingface_papers.py` |

**Importante**: tutte queste piattaforme sono interrogate tramite endpoint **pubblici** che **non richiedono API key**. Quindi non devi registrarti da nessuna parte, non devi mettere credenziali da nessuna parte, non c'e' nessun `.env` da compilare. Apri e usi.

---

## Guida completa passo-passo

### Step 1 - Installa Python

**Cosa stiamo facendo**: i 10 scraper sono scritti in Python. Senza Python sul tuo PC il sistema non parte.

1. Vai su [python.org/downloads](https://www.python.org/downloads/) e clicca il pulsante grosso "Download Python 3.X.Y".
2. Apri il file scaricato.
3. **IMPORTANTE**: nella prima schermata, in basso, spunta la casella **"Add Python to PATH"**. Senza questa spunta, il terminale non vedra' Python e ti dara' errore "comando non trovato".
4. Premi "Install Now" e aspetta. Quando finisce, premi "Close".
5. Per verificare che sia andato a buon fine: apri il terminale (su Windows tasto Win + R, scrivi `cmd`, premi invio) e digita `python --version`. Dovresti vedere qualcosa tipo `Python 3.12.3`. Se invece esce un errore, riparti dal punto 3.

**Errore comune**: hai installato Python ma il terminale dice "python non riconosciuto come comando". Soluzione: probabilmente hai dimenticato la spunta "Add Python to PATH". Reinstalla Python avendo cura di metterla.

---

### Step 2 - Apri la cartella in VS Code

**Cosa stiamo facendo**: VS Code ci serve per vedere i file, modificarli (se vuoi cambiare le piattaforme) e per usare il suo terminale integrato senza uscire dalla finestra.

1. Apri VS Code.
2. Menu in alto: **File -> Apri cartella...** (o `Ctrl+K Ctrl+O`).
3. Naviga fino alla cartella `materiali/` di questo progetto e selezionala.
4. A sinistra vedrai l'elenco dei file. A questo punto, apri il terminale integrato: menu **Terminale -> Nuovo terminale** (o `Ctrl+ò`).

Da adesso ogni comando del tutorial lo scrivi in quel terminale.

---

### Step 3 - Installa le 2 librerie

**Cosa stiamo facendo**: gli scraper usano due librerie esterne per fare le richieste web (`requests`) e leggere l'HTML di GitHub (`beautifulsoup4`). Le installiamo con un comando.

Nel terminale di VS Code, scrivi:

```bash
pip install -r requirements.txt
```

Premi invio. Vedrai scorrere qualche riga di "Installing collected packages..." e in pochi secondi avrai finito.

**Errore comune**: `pip` non riconosciuto. Significa che Python non e' nel PATH (vedi Step 1). Soluzione veloce: prova `python -m pip install -r requirements.txt`.

---

### Step 4 - Lancia l'orchestratore (la strada 1)

**Cosa stiamo facendo**: l'orchestratore lancia i 10 scraper tutti insieme, raccoglie i risultati, costruisce la dashboard HTML e te la apre nel browser. Senza che tu debba fare altro.

Nel terminale, scrivi:

```bash
python orchestrator.py
```

Premi invio. Cosa vedi:

1. Il log scorre con 10 righe `OK <nome piattaforma> -> 10 trend`. Se vedi `X` invece di `OK`, quel singolo scraper non ha funzionato (la piattaforma e' giu' o ha bloccato la richiesta). Gli altri 9 vanno avanti comunque.
2. Riga finale: `Dashboard scritta: .../dashboard.html`.
3. Il browser si apre automaticamente sulla dashboard.

Adesso hai sotto gli occhi 10 card, una per piattaforma, ognuna con i 10 trend del momento, cliccabili. Questa e' la **strada 1**, quella che funziona da sola senza Claude.

---

### Step 5 - La strada 2: la sintesi AI via routine Claude (il cuore del sistema)

**Cosa stiamo facendo**: i 100 titoli grezzi sono utili ma sono ancora da leggere. La strada 2 prende quei titoli e li trasforma in **idee per video YouTube** gia' pronte, divise per format. Questo lo fa **Claude (Opus 4.8)** eseguendo il ciclo descritto nel file `CLAUDE.md`.

Questa parte gira come **routine schedulata** (vedi `ROUTINE.md`): non la lanci a mano ogni volta, parte da sola alla cadenza che hai impostato. A ogni esecuzione Claude:

1. lancia i 10 scraper (Fase 1),
2. apre **10 sub-agenti in parallelo** — la nuova feature **Dynamic Workflows** di Opus 4.8 — uno per piattaforma, che filtrano i trend secondo `ARGOMENTI.md` e generano idee video (Fase 2),
3. **valuta** se la raccolta e' abbastanza ricca e, se no, rilancia mirato (Fase 3),
4. scrive il report e rigenera la dashboard con la sezione **"Idee video sintetizzate dai 10 agenti"** in cima (Fase 4).

**Per cambiare cosa cerca**: modifica `ARGOMENTI.md` (i temi) e, se serve, `CLAUDE.md` (il ciclo). Tutto in linguaggio naturale.

**Se la sezione sintesi non compare**: probabilmente la versione di Opus 4.8 in uso non ha ancora abilitato Dynamic Workflows (e' in research preview). La strada 1 continua a funzionare e ti da' comunque i 100 titoli.

---

## Adattarlo al tuo settore (la cosa importante)

Il sistema cosi' com'e' monitora il mondo AI. Ma la logica e' generale: **10 piccoli script che leggono 10 fonti e producono una vista unificata**.

Se ti occupi di vino, sostituisci i 10 scraper con 10 che monitorano: Vivino, Tannico, Wine-Searcher, blog di settore, canali YouTube di sommelier, Google News "vino", ecc.

Se ti occupi di immobiliare: Immobiliare.it, Idealista, gruppi Facebook di settore, Google News "mercato immobiliare", ecc.

Per ogni scraper nuovo che vuoi scrivere:

1. Copia uno degli scraper esistenti (`scrapers/google_news.py` e' il piu' semplice).
2. Cambia l'URL dentro la variabile `URL =`.
3. Cambia la funzione `fetch_trends()` adattandola al formato della nuova fonte.
4. Aggiungi il nuovo scraper alla lista `SCRAPERS` dentro `orchestrator.py`.
5. Aggiorna `ARGOMENTI.md` con i temi del tuo settore (e' quello che guida la sintesi).

In due ore di lavoro ti porti il sistema sul tuo settore.

---

## Concetti spiegati semplici

- **Scraper**: un piccolo programma che apre una pagina web e ne tira fuori i dati che ti interessano (titoli, prezzi, ecc.). Non e' magia: e' come quando tu apri il browser e leggi una pagina, solo che lo fa lui in automatico.
- **Orchestratore**: il "direttore d'orchestra" che decide chi parte quando, raccoglie i risultati, e costruisce l'output finale. Nel nostro caso lancia 10 scraper in parallelo.
- **Sub-agente**: un'istanza temporanea di Claude che lavora su una sola cosa precisa e poi torna con il risultato. Pensalo come uno stagista con un compito specifico: legge i risultati di Reddit, sintetizza 3 idee video, fine.
- **Dynamic Workflows**: la feature nuova di Claude Opus 4.8 (rilasciata il 28 maggio 2026) che permette di lanciare decine di sub-agenti in parallelo da un solo prompt. Prima si poteva, ma con codice scritto da te. Adesso lo fa Claude orchestrando tutto.
- **Dashboard**: l'output finale, una pagina HTML statica che si apre nel browser. Niente server, niente database — solo un file che puoi aprire anche offline una volta generato.

---

## Cosa fare adesso

Hai due strade:

- **Strada A - copia uguale**: lancia `python orchestrator.py`, usa la dashboard cosi' com'e' per il mondo AI. Buon punto di partenza per capire il flusso.
- **Strada B - adatta al tuo settore**: segui la sezione "Adattarlo al tuo settore" qui sopra. Sostituisci i 10 scraper con 10 fonti che ti interessano davvero.

In entrambi i casi, se hai Claude Code con Opus 4.8, la strada 2 (la routine che legge `CLAUDE.md`) aggiunge la sintesi AI. La differenza tra "100 titoli grezzi" e "idee gia' impacchettate" si sente.

---

## Dubbi o problemi?

- Commenta sotto il video YouTube - rispondo a tutti.
- Se uno scraper smette di funzionare (es. la piattaforma cambia layout): la dashboard ti mostra una badge rossa "vuoto" su quella card. Apri il file dello scraper, vedi cosa e' cambiato, sistema. La struttura e' fatta apposta perche' un singolo scraper rotto non blocchi gli altri 9.

Buon lavoro.
