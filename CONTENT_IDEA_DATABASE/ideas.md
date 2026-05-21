# Idee di contenuto

Una sezione per idea, separate da `---`. Titolo sintetico (non click-bait) + descrizione libera.

---

## Creare un team di agenti AI con Claude Code

L'idea è creare un insieme di file sui quali è possibile avviare N esecuzioni simultanee di Claude Code, ciascun file contiene le istruzioni per fare una cosa specifica. Il video deve mostrare un esempio di un team di agenti che fa cose in contemporanea. Infine, andrò a mettere uno scheduling tramite "Claude Routines" affinché possano lavorare a quella attività ogni tot tempo.

---

## GitHub per Claude Code: come usarlo al meglio

Un contenuto che descriva un numero di trucchi per usare GitHub al fine di massimizzare l'utilizzo di Claude Code. Idea: mostrare i pattern concreti con cui GitHub potenzia il workflow di Claude Code — gestione di branch e worktree per parallelizzare task, integrazione con GitHub Actions per schedulare run in cloud (anche col PC spento), uso delle pull request come "review point" tra agenti, gestione delle issue come backlog di task per Claude, hooks pre-commit per validare l'output prima del merge, e altri trucchi pratici tipo l'uso di `.github/instructions/` per dare contesto persistente al modello. Pubblico target: utente non tecnico che già usa Claude Code ma non sfrutta GitHub come "infrastruttura" attorno. Format: build di un mini-setup replicabile, con repo template scaricabile.

---

## Claude Agents View: il centro di comando per agenti AI in parallelo

La nuova funzionalità di Claude Code che permette di lanciare e gestire più agenti AI contemporaneamente da una sola schermata. Si apre con `claude agents` e mostra una dashboard con lo stato di ogni sessione: chi sta lavorando, chi ha bisogno di input, chi ha finito. Il video mostra come dispatchare 4 task in parallelo, monitorarli, rispondere alle domande, e raccogliere i risultati. Focus su uso pratico per chi deve fare più cose alla volta senza impazzire tra finestre. Video corto ad alto valore.

---

## Come creare una newsletter personale AI con Claude Code

Sistema che ogni mattina pesca le nuove uscite dal sito di Anthropic (model release, news, research papers, changelog) e te le consegna in un file markdown ben formattato — la tua newsletter AI privata, fatta per te, filtrata sui tuoi interessi. Caso study di esempio: monitorare anthropic.com/news. L'idea generale è "newsletter personale automatizzata" — il pattern vale per qualunque fonte (competitor, news di settore, blog preferiti, paper accademici). Stack: solo Claude Code (no Python, no API esterne, usa i tool built-in WebFetch + file write). Scheduling: Claude Routines. State tracking: file `state.json` aggiornato da Claude stesso per non duplicare articoli già letti. Output: file markdown in `newsletter/YYYY-MM-DD.md`; email opzionale in docs separato. Pubblico: chi vuole restare aggiornato senza scrollare Twitter/Hacker News ogni mattina, non sa programmare, vuole un sistema minimale che fa una cosa sola e bene.

---

## Claude Code + Antigravity: come usarli insieme in 7 minuti

Video di integrazione tra due tool AI. Premessa: alle persone piacciono le integrazioni tra tool. Antigravity (il nuovo agent IDE di Google in cloud) lavora bene quando deve esplorare in parallelo — spawna agenti multipli, ognuno produce un artefatto verificabile (HTML, screenshot, preview). Claude Code (locale, terminale) lavora bene quando deve cucire il risultato nel progetto reale dell'utente — legge i file veri, rispetta link e meta, fa il commit. Il pattern del video: "esplora in cloud → scegli con l'occhio → integra in locale". Case study di esempio: rifare la home page di un sito. Antigravity genera 3 varianti grafiche in parallelo (corporate / amichevole / aggressive), l'utente sceglie via preview, Claude Code in locale integra l'artefatto vincente nell'index.html reale preservando link interni, meta tag, asset, tracking. Format compatto: 7 minuti, 1 metodo solo (no varianti tecniche), focus sul pattern che generalizza a email/proposte/audit/docs. Pubblico: chi già usa Claude Code e vuole capire se ha senso aggiungere Antigravity.

---

## Claude Code per piccoli business: le 3 componenti imprescindibili (Step by step)

Video "step by step" che monta l'infrastruttura AI minima per un piccolo business (studio professionale, e-commerce, agenzia, consulenza, artigianato). Tre strati che si parlano: (1) **Supabase via MCP connector** per i dati custom — il connettore MCP ufficiale permette a Claude di leggere/scrivere direttamente nel DB Postgres senza scrivere codice middleware. Confronto col foglio Excel (query, multi-utente, audit, scalabilità). (2) **Claude for Small Business**, il pacchetto Anthropic rilasciato il 13 maggio 2026 dentro Claude Cowork: 15 workflow pronti (`/monday-brief`, `/close-month`, `/invoice-chaser`, `/plan-payroll`, `/run-campaign`, `/contract-review` ecc.) + 15 skill + 7 connettori (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365). Approvazione umana obbligatoria, permessi che si propagano, no training sui dati business. (3) **Agent View** di Claude Code per i sub-agent custom in markdown che fanno le cose specifiche del settore che il pre-cotto non sa fare. Case study: studio commercialisti con tabelle Supabase per regimi fiscali e scadenze custom, sub-agent `regime-checker`, `document-classifier`, `scadenza-allerter`. Il ponte tra i 3 strati è l'MCP di Supabase, leggibile sia da Code che da Cowork. Sezione finale "tutto insieme" mostra il flusso lunedì-mattina end-to-end. Durata: 18-22 minuti. Pubblico: piccoli imprenditori non-developer che usano già Claude Code.

---
