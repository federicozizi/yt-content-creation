# Argomenti di ricerca — cosa cerco davvero

> File importato da `CLAUDE.md`. Definisce **cosa conta come segnale rilevante**
> quando gli agenti interpretano i trend raccolti dalle 10 piattaforme.
> Modificalo per cambiare il focus della routine: la logica del sistema resta identica.

## Il filtro mentale

Un trend è **rilevante** solo se rientra in una di queste cinque categorie.
Tutto il resto (gossip tech, finanza pura, politica AI, hardware di consumo, ecc.) va **scartato**.

### 1. Nuove feature nel mondo AI
Funzionalità appena rilasciate da qualsiasi attore (Anthropic, OpenAI, Google, Microsoft, Meta, startup).
Esempi di cosa cerco: nuovi tool agentici, nuove modalità (voice, vision, computer use),
nuove capacità di automazione, nuovi modi di integrare l'AI nel lavoro quotidiano.
**Domanda guida:** "C'è qualcosa che ieri non si poteva fare e oggi sì?"

### 2. Nuove uscite e annunci
Lanci di prodotto, release note importanti, anteprime, beta pubbliche.
Esempi: una nuova app, un nuovo SDK, una nuova integrazione, un changelog rilevante.
**Domanda guida:** "È appena uscito qualcosa di cui la gente parlerà questa settimana?"

### 3. Nuovi modelli
Rilasci di modelli AI (LLM, modelli multimodali, modelli specializzati) e i loro benchmark.
Esempi: una nuova versione di un modello noto, un modello open-weight nuovo, un modello verticale.
**Domanda guida:** "È uscito un modello nuovo o un upgrade che sposta l'asticella?"

### 4. Gente che fa cose interessanti con Claude
Casi d'uso reali, progetti, esperimenti, automazioni costruite con Claude (o Claude Code).
Esempi: qualcuno che ha automatizzato un processo di business, un workflow creativo,
un'integrazione ingegnosa, un risultato sorprendente ottenuto con Claude.
**Domanda guida:** "Qualcuno ha fatto con Claude una cosa che vale la pena raccontare/replicare?"

### 5. Nuove feature di Claude (priorità massima)
Tutto ciò che riguarda specificamente Claude e l'ecosistema Anthropic.
Esempi: nuove funzioni di Claude Code, MCP, sub-agenti, Dynamic Workflows, skill, connettori,
nuove modalità, aggiornamenti dell'app, novità della Console/API.
**Domanda guida:** "Riguarda direttamente Claude e i miei spettatori lo vorrebbero sapere?"
> Questa categoria pesa **doppio**: è il cuore del canale.

## Audience di destinazione (per tarare le idee video)

- **Chi**: imprenditori, manager, marketer, freelance, curiosi. **Non** developer.
- **Cosa li accende**: applicazioni pratiche al business, risparmio di tempo concreto,
  "guarda cosa si può fare adesso", vantaggio competitivo accessibile senza essere tecnici.
- **Cosa li spegne**: gergo tecnico, benchmark astratti, dibattiti accademici, hype senza uso pratico.

## Format video ammessi (per ogni idea generata)

Ogni idea deve essere etichettata con UNO di questi quattro format:
- **Listicle** — "Le N cose / errori / tecniche…"
- **Build dimostrativa** — "Costruisco X in N minuti…"
- **Problem-solver** — "Come evitare / risolvere / sistemare X…"
- **Storia personale** — "Hai mai…? Io l'ho fatto…"

Format banditi: "Tutorial completo", "Guida definitiva", "X spiegato semplice", "X in 60 secondi".

## Soglie di qualità per la valutazione (loop "rilancia se serve")

Una raccolta è **sufficiente** quando:
- almeno **3 delle 5 categorie** hanno trovato segnale rilevante,
- la categoria 5 (feature di Claude) ha **almeno 1 match** se nelle ultime 48h c'è stato qualcosa,
- il totale dei match rilevanti è **≥ 12** su 100 trend grezzi.

Se la raccolta è **insufficiente**, la routine deve rilanciare gli scraper deboli con parametri
allargati (vedi `CLAUDE.md`, sezione "Loop di valutazione").
