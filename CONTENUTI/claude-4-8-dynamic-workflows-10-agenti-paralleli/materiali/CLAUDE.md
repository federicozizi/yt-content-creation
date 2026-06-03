# CLAUDE.md — Routine di ricerca trend basata su Dynamic Workflows

> Questo file è il **cervello** del sistema. Una routine schedulata di Claude (Opus 4.8)
> lo legge a ogni esecuzione e svolge il ciclo descritto qui sotto.
> Il sistema è costruito attorno a **Dynamic Workflows**: Claude orchestra, interpreta,
> valuta e — se serve — rilancia, in autonomia.

## Cosa cerco

@ARGOMENTI.md

---

## Il ciclo (cosa fai a ogni esecuzione)

Sei l'orchestratore. Non sei tu a leggere 100 titoli a mano: tu **coordini** una squadra di
sub-agenti e **decidi**. Il ciclo ha quattro fasi.

### Fase 1 — Raccolta (lanci gli strumenti)

Esegui dal terminale, nella cartella di questo file:

```
python orchestrator.py --no-open
```

Questo lancia i 10 scraper in parallelo e scrive i risultati in `output/<piattaforma>.json`
(10 file, ~10 trend ciascuno). Gli scraper sono strumenti deterministici: non ragionano,
raccolgono. Se uno fallisce (0 item), prendine nota: servirà nella Fase 3.

### Fase 2 — Interpretazione (Dynamic Workflows: 10 agenti in parallelo)

Lancia **10 sub-agenti in parallelo**, uno per piattaforma. Ogni sub-agente:

1. legge `output/<piattaforma>.json`,
2. confronta ogni trend con le 5 categorie di `ARGOMENTI.md`,
3. tiene **solo i trend rilevanti** (scarta tutto il resto), assegnando a ognuno:
   - `categoria` (1-5)
   - `rilevanza` (alta / media / bassa)
4. per i trend ad alta/media rilevanza, genera **1-3 idee video** con:
   - `titolo` (sotto 70 caratteri, click-worthy, niente format banditi)
   - `format` (Listicle / Build / Problem-solver / Storia personale)
   - `razionale` (2 righe: perché funziona per l'audience)
   - `fonte` (titolo + URL del trend originale)

Output di ogni agente: un blocco JSON strutturato. Niente prosa.

### Fase 3 — Valutazione (decidi se rilanciare)

Aggrega i risultati dei 10 agenti e applica le **soglie di qualità** di `ARGOMENTI.md`:

- almeno 3 categorie su 5 con segnale,
- categoria 5 (feature di Claude) coperta se c'è stata novità nelle 48h,
- totale match rilevanti ≥ 12.

**Se le soglie sono raggiunte** → vai alla Fase 4.

**Se NON sono raggiunte** → rilancia in modo mirato (non tutto: solo ciò che è debole):
- piattaforma con 0 item (scraper fallito) → riprova una volta; se rifallisce, annota e prosegui.
- categoria scoperta → rilancia gli scraper più adatti a quella categoria con parametri allargati:
  - categoria 5 (Claude) debole → in `scrapers/reddit.py` punta a `r/ClaudeAI`, e in
    `scrapers/google_news.py` allarga la query a `Claude Anthropic`.
  - categoria 3 (modelli) debole → in `scrapers/hackernews.py` e `scrapers/huggingface_papers.py`
    aumenta il numero di item raccolti.
- **massimo 2 rilanci.** Dopo il secondo, procedi comunque con quello che hai e dichiara nel
  report cosa è rimasto scoperto. **Mai loop infinito.**

Questa fase è il cuore di Dynamic Workflows: Claude non esegue una pipeline fissa, **valuta il
proprio output e decide se serve un altro giro**. È la differenza tra uno script e un agente.

### Fase 4 — Consegna

1. Scrivi `output/synthesis.html` con le idee aggregate. È un frammento HTML (non un documento intero):
   l'orchestratore lo inietta dentro la dashboard. Usa questo schema per ogni idea:

   ```html
   <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;">
     <!-- per ogni idea, una card: bordo viola (#bc8cff) se categoria 5 (Claude), ambra (#f59e0b) altrimenti -->
     <div style="background:#21262d;border:1px solid #30363d;border-left:3px solid #bc8cff;border-radius:10px;padding:18px 20px;">
       <span style="font-size:11px;font-weight:700;color:#bc8cff;text-transform:uppercase;">{FORMAT} · {CATEGORIA}</span>
       <h4 style="margin:8px 0;font-size:16px;color:#e6edf3;">{TITOLO}</h4>
       <p style="margin:0;color:#8b949e;font-size:13px;line-height:1.5;">{RAZIONALE}</p>
       <small style="color:#6e7681;font-size:11px;">Fonte: {PIATTAFORMA}</small>
     </div>
   </div>
   ```
   Apri con una riga di riepilogo (match totali, categorie coperte, decisione del valutatore).
2. Rigenera la dashboard: `python orchestrator.py --no-open --skip-scrape`
   (riusa i JSON esistenti e include la sintesi).
3. Scrivi il report giornaliero in `../../../IDEE/ricerche-auto/YYYY-MM-DD-{mattina|sera}.md`
   usando il **formato canonico** atteso dal resto del sistema (lo stesso definito in
   `RICERCA_AUTOMATICA/prompt-ricerca.md`, sezione "Formato obbligatorio del file"):

   ```markdown
   # Ricerca contenuti — YYYY-MM-DD [mattina|sera]

   > Esecuzione automatica (sistema a 10 agenti). Fonti: Hacker News, Reddit, Dev.to,
   > Product Hunt, Medium, GitHub Trending, Lobste.rs, YouTube, Google News IT, Hugging Face Papers.

   ## Polso del momento
   - **[Trend]**: descrizione 1-2 righe + 1 fonte cliccabile REALE (URL dal JSON o da WebSearch). (3-5 trend)

   ## Idee proposte

   ### 1. [Titolo che segue una delle 4 template format]
   - **Format**: Listicle / Storia personale / Problem-solver / Build dimostrativa (uno solo)
   - **Angolo nuovo**: perché non è una copia banale
   - **Ispirato da**: [link reale]
   - **Hook potenziale**: una frase di apertura
   - **Cosa costruisce concretamente lo spettatore**: 1-2 righe
   - **Target**: chi è lo spettatore
   ### 2. ... (5-8 idee; distribuzione ~40% Listicle, 30% Build, 20% Problem-solver, 10% Storia personale)

   ## Note esecuzione
   - Distribuzione format nelle idee proposte (conteggio esplicito)
   - Match per categoria + eventuali rilanci effettuati + categorie rimaste scoperte
   - Idee scartate e perché
   ```

   Prima di scrivere, leggi i 3 file più recenti in `IDEE/ricerche-auto/` per non duplicare idee già proposte.

---

## Regole non negoziabili

- **Mai inventare trend.** Se un JSON è vuoto, dillo. Non riempire con idee a memoria.
- **Mai più di 2 rilanci.** La routine deve sempre terminare.
- **Scarta in modo aggressivo.** Meglio 12 match veri che 40 forzati. La rilevanza viene prima del volume.
- **Categoria 5 (Claude) ha priorità.** A parità di spazio, un'idea su una feature di Claude batte le altre.
- **Audience non tecnica.** Ogni idea deve superare il test: "un imprenditore non tecnico capisce il titolo e lo trova interessante?".
- **Niente file di troppo.** Scrivi solo: `output/*.json`, `output/synthesis.html`, `dashboard.html`, il report in `IDEE/ricerche-auto/`. Nient'altro.

## Come viene lanciata questa routine

Una routine schedulata (cloud) esegue il prompt:
> "Sei nella cartella materiali/. Esegui il ciclo descritto in CLAUDE.md, dalla Fase 1 alla Fase 4."

La cadenza è definita nello scheduling (vedi `ROUTINE.md`).
