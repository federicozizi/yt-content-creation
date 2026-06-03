# CLAUDE.md — Serie "Startup gestita da agenti AI" + prodotto Competitor Analyzer

> **Cos'è questa cartella.** Quartier generale di una **serie YouTube** + le **bozze del sistema/prodotto**
> che la serie racconta. Deviazione voluta dalla struttura standard di `CONTENUTI/<slug>/` (che prevede
> 1 video = PRINCIPALE.html + PRINCIPALE_ENG.html + materiali/): qui c'è una serie multi-episodio **e** il
> codice di un prodotto reale. Non forzare la struttura a 3 file: vedi "Struttura della cartella" sotto.
>
> **Fonte di verità delle decisioni.** Questo file traccia TUTTO ciò che abbiamo deciso. Aggiornalo a ogni
> sessione. Le sezioni "DECISO" sono vincolanti; le sezioni "DA DECIDERE" sono aperte.
>
> Ultimo aggiornamento: 2026-05-31.

---

## 0. In una frase

Una **serie YouTube** in cui il canale lancia, sotto gli occhi del pubblico, una **vera micro-startup in
abbonamento** — un servizio di *competitor intelligence via email* — il cui lavoro operativo è svolto quasi
interamente da **agenti AI**, riusando il sistema a 10 agenti già costruito nel canale.

---

## 1. La serie

### Concept
Tema portante: **"È possibile lanciare e far girare una startup gestita (quasi) solo da agenti AI, partendo da zero?"**
Risposta onesta che esploriamo: il founder resta l'**orchestratore**, gli agenti fanno il lavoro operativo;
il valore del racconto è mostrare **dove gli agenti arrivano e dove crollano**.

### Format
- È un **ombrello "Storia personale"** (il format più potente del canale, vedi `../../CLAUDE.md`).
- I **singoli episodi cambiano format** (Listicle / Build / Problem-solver / Storia personale) → così si
  rispetta la rotazione del canale e non si satura un solo format.

### Patto col pubblico (spina di credibilità — NON NEGOZIABILE)
- **VIETATO** il claim clickbait "Startup 100% AI, zero umani".
- Framing corretto: *"Quanto lontano posso spingere la delega agli agenti? Io resto founder-orchestratore;
  scopriamo dove reggono e dove falliscono."*
- Ogni episodio DEVE contenere un momento **"qui ho dovuto salvare io la situazione"**.

### Valore durevole (da dichiarare nel pilot)
*"Anche se non aprirai mai QUESTA startup, alla fine saprai esattamente quali pezzi della TUA attività puoi
delegare a un'AI oggi — con gli strumenti veri, non le promesse."*

### Il "cruscotto" / scoreboard (meccanismo di retention — ricorrente in OGNI episodio)
Apertura fissa di ogni episodio con la stessa schermata, i cui numeri salgono nel tempo:
```
GIORNO X / 90  ·  CLIENTI: N  ·  CASSA: +€___ / −€___
ALERT/REPORT UTILI CONSEGNATI: N  ·  LAVORO FATTO DAGLI AGENTI: __%  ·  VOLTE CHE HO SALVATO IO: __
```
È il "conta gli item" del Listicle applicato a una storia: lo spettatore torna per vedere il numero salire.

### Bozza scaletta puntate (DRAFT — da rifinire)
> Apertura definita dall'utente (P1 = claim forte + tema + nascita brand). Resto proposto da Claude.
> 10 puntate è il draft pieno; comprimibile a ~8 unendo P6+P7 e P9+P10 (vedi note sotto la tabella).

| # | Titolo di lavoro | Format | Cuore + cosa avanza nella storia |
|---|------------------|--------|----------------------------------|
| 1 | **"Sto lanciando una startup gestita da agenti AI"** | Storia personale (claim forte) | Hook forte/clickbait; il tema (si può davvero, partendo da zero?); il patto di onestà; **gli agenti aiutano a definire il brand** (nome, positioning, dominio). *Fine: il brand è nato. Scoreboard a zero.* |
| 2 | **"Cosa vende un'azienda gestita da agenti AI (e a chi)"** | Build/Storia | Gli agenti validano nicchia, offerta e prezzo → si fissa: **competitor analyzer in abbonamento, report settimanale via email**. *Fine: offerta + prezzo definiti, pitch pronto.* |
| 3 | **"La pagina di iscrizione del mio SaaS ad agenti AI (senza essere web developer)"** | Build dimostrativa | Landing + form (email + consensi GDPR) + signup Supabase. "Un SaaS che parte senza app." *Fine: landing online, prime iscrizioni.* |
| 4 | **"Costruisco gli agenti AI che analizzano i miei competitor"** | Build dimostrativa | Il sistema a 10 agenti → BRIEF, fonti competitor, **diff**, swarm di interpretazione → primo report vero. *Fine: report in mano.* |
| 5 | **"Il problema che ha quasi fermato i miei agenti AI: non leggevano i siti"** | Problem-solver | La **scoperta cloud reale** (scraper KO in CCR, vedi §4) → soluzione (VPS o WebSearch/API). *Fine: collection robusta.* |
| 6 | **"Iscrizione automatica: l'utente scrive una mail, gli agenti AI fanno il resto"** | Build/Problem-solver | Conferma + onboarding via email + **parsing competitor** (agente legge le risposte). *Fine: funnel chiuso end-to-end.* |
| 7 | **"Come ho reso il report dei miei agenti AI degno di essere pagato"** | Problem-solver | Il layer **"e quindi?"** (segnale→significato→azione) + il **cancello umano** dove l'AI sbaglia. *Fine: report vendibile.* |
| 8 | **"Il primo cliente pagante della mia startup ad agenti AI"** | Storia personale | Outreach fatto dagli agenti → chiusura primo cliente reale. *Fine: cassa > 0, lo scoreboard si accende.* |
| 9 | **"L'azienda ad agenti AI che lavora mentre dormo"** | Storia + nerd | Routine settimanale che monitora-scrive-consegna-fattura in autonomia (+ template finanziari Anthropic di maggio). *Fine: gira da sola per N giorni.* |
| 10 | **"Il verdetto: un'azienda di soli agenti AI ce l'ha fatta?"** | Listicle/Storia | Numeri veri + *"Le 5 cose che gli agenti AI NON hanno saputo fare"* + lo rifarei? |

**Note sulla scaletta:**
- Versione compatta a ~8: unire **P6+P7** (onboarding + qualità report) e **P9+P10** (autonomia + verdetto).
- Il **brand** (nome, dominio) ora si definisce **in P1, on-camera** — quindi §6 "DA DECIDERE / nome brand" si scioglie dentro la puntata 1 (gli agenti propongono, si sceglie in video).
- Ogni puntata apre col **cruscotto/scoreboard** (vedi sopra) e contiene il momento **"qui ho salvato io"**.
- Distribuzione format nell'arco: prevalenza Build (3) + Problem-solver (3), incorniciati da Storia personale (apertura/chiusura/primo cliente) → coerente con la rotazione del canale.

### Materiali scaricabili (modello canale: uno per episodio)
Template `BRIEF.md`, repo dell'analyzer adattato, template di report, guida VPS (Ep4), rubrica per le
raccomandazioni "e quindi?", schema Supabase, ecc.

### Nome della serie — DA DECIDERE (candidati)
- "Founder: io. Dipendenti: agenti."
- "L'azienda che si gestisce da sola"
- "Startup a Zero Umani (quasi)"

---

## 2. Il prodotto — Competitor Analyzer (SaaS in abbonamento)

### Cos'è
Servizio in **abbonamento** che invia **report settimanali via email** sui competitor scelti dall'utente.
Pitch di lavoro: *"Hai un concorrente che vuoi seguire da vicino? Ogni settimana il report nella tua inbox."*

### DECISO
- **Posizionamento: SOLO report settimanale.** Niente alert in tempo reale. **Il claim "tempo reale" è
  abbandonato** (era in conflitto con la cadenza settimanale; scelta la semplicità).
- **Iscrizione via SITO** (landing page con form): l'utente inserisce **email + consenso privacy + consenso
  termini** (checkbox separate, non pre-spuntate — regola GDPR). Il sito serve: raccoglie il consenso al
  momento giusto, migliora la deliverability (dominio pro), e spiega l'offerta.
- **Inserimento competitor via EMAIL, full-auto dal giorno 1**: dopo l'iscrizione, l'utente riceve una mail
  che chiede i siti dei competitor; un **agente legge la risposta, estrae e valida gli URL, conferma**.

### Le 3 regole di design specifiche (qui sta il valore)
1. **Il diff, non lo snapshot.** Il valore è *"il competitor X ha abbassato il prezzo del 10% giovedì"*, non
   "ecco i prezzi". Serve salvare lo stato precedente e confrontarlo. Gli **alert sul cambiamento** sono il prodotto.
2. **Il layer "e quindi?".** Output = *segnale → significato → azione suggerita*. È ciò che il cliente paga
   (non i dati grezzi che troverebbe da solo).
3. **Il cancello umano.** Gli agenti a volte leggono male (un A/B test sul prezzo ≠ cambio listino). Il founder
   valida prima della consegna. È anche la spina di onestà della serie.

### Flusso UX end-to-end (DECISO)
```
[1] LANDING PAGE  →  form: email + ☑ privacy + ☑ termini
        │ submit
        ▼
[2] SUPABASE  →  tabella `iscritti` (stato: pending)  +  email di conferma (doppio opt-in)
        │ utente conferma
        ▼
[3] EMAIL ONBOARDING  →  "Elenca i siti dei tuoi competitor, uno per riga"
        │ l'utente risponde
        ▼
[4] AGENTE PARSING  →  estrae+valida URL  →  conferma all'utente  →  salva in `competitor`
        │
        ▼
[5] ROUTINE SETTIMANALE (il sistema a 10 agenti)  →  raccolta + diff + interpretazione  →  REPORT via email
```
Solo i blocchi **[1]** e **[3]-[4]** sono nuovi rispetto al sistema già esistente.

### Gestione post-iscrizione (comandi via email)
`AGGIUNGI <url>`, `RIMUOVI <url>`, `STOP` (disiscrizione — obbligatoria per legge).

---

## 3. Architettura tecnica

### Mappatura: il sistema esistente → il competitor analyzer
Riusa `CONTENUTI/claude-4-8-dynamic-workflows-10-agenti-paralleli/materiali/`:
| Sistema oggi | Diventa |
|---|---|
| `ARGOMENTI.md` (5 categorie) | `BRIEF.md` per cliente (chi sono i competitor, quali segnali contano) |
| 10 scraper (HN, Reddit…) | Fonti dei competitor: sito/pricing, blog/news, LinkedIn, recensioni (Trustpilot/Google/G2), annunci di lavoro, Product Hunt, Google News sul nome |
| Sub-agenti filtra-trend | Sub-agenti che leggono un competitor a testa ed estraggono le mosse |
| Valutatore (soglie + rilancio) | Identico: coperti tutti i competitor? fonte caduta? rilancia |
| Report in `IDEE/ricerche-auto/` | Report competitor per il cliente |
| Routine schedulata | Identica: gira settimanale, scrive, consegna |

### Stack scelto (DECISO a livello di indirizzo, dettagli in §6 "DA DECIDERE")
- **Landing**: pagina statica HTML/CSS self-contained → hosting su Netlify/Vercel (da scegliere).
- **Backend dati**: **Supabase** (connettore MCP **già collegato** alla sessione). Tabelle previste:
  - `iscritti` (email, consenso_privacy, consenso_termini, stato [pending|confirmed|active|stopped], token_conferma, created_at)
  - `competitor` (iscritto_id, url, nome, stato)
  - `snapshot` (competitor_id, data, hash_contenuto, dati) — serve per i diff settimanali
- **Signup**: Edge Function Supabase (valida email, salva iscritto, invia mail di conferma).
- **Email in entrata** (per il parsing competitor): provider con inbound webhook **oppure** lettura IMAP da un agente.
- **Email in uscita** (conferme + report): ESP con dominio configurato **SPF/DKIM/DMARC** (deliverability).
- **Pipeline agenti**: il sistema esistente (scraper/WebSearch + sub-agenti + valutatore).
- **Orchestratore**: routine schedulata (come quella già attiva per la ricerca idee).

### Ordine di costruzione (DECISO)
1. **Landing + form + signup Supabase** (l'ingresso, il pezzo più visibile)
2. **Email di conferma + onboarding** (doppio opt-in)
3. **Parsing competitor in entrata** (l'agente)
4. **Report settimanale** (il sistema già pronto, adattato)

---

## 4. Scoperta tecnica REALE da tenere a mente (e da trasformare in Ep 4)

Il 2026-05-31, la routine cloud di ricerca idee ha rivelato che **nell'ambiente cloud (CCR) 9 scraper su 10
falliscono**: l'ambiente blocca le richieste HTTP dirette (solo GitHub Trending ha funzionato). La routine ha
**ripiegato da sola su WebSearch/WebFetch** (proxati dall'infra Anthropic) e ha comunque prodotto un ottimo report.

**Implicazione per il prodotto** (la collection deve essere robusta):
- **Strada A**: collection via **WebSearch/WebFetch + RSS + API ufficiali** (funziona in cloud).
- **Strada B**: **scraper veri su un VPS dedicato** (non il sandbox CCR) — ricicla anche il vecchio contenuto
  "Claude Code in un server di produzione".
- **DA DECIDERE** quale strada (vedi §6). Non è una rogna: è il materiale onesto dell'**Ep 4**.

---

## 5. Vincoli legali / etici (NON NEGOZIABILI)
- **GDPR**: consenso esplicito al signup (checkbox separate), **doppio opt-in**, **disiscrizione** sempre
  possibile (STOP), **Privacy Policy + Termini** linkati prima di raccogliere email, dati del **titolare del
  trattamento** nel footer.
- **Dati personali nelle recensioni** (nomi): trattare con cautela / anonimizzare dove possibile.
- **Scraping**: solo informazioni **pubbliche**. Mai dietro login, mai account falsi. Rispettare robots.txt e ToS.
- **Onestà sui limiti** (da dire anche in video): l'analyzer vede solo segnali pubblici, non legge le intenzioni
  del competitor, e può generare **falsi positivi** (es. A/B test scambiato per cambio prezzo) → il cancello umano serve.

---

## 6. DA DECIDERE (decisioni aperte — NON ancora prese)
- [ ] **Nome della serie** (3 candidati in §1)
- [ ] **Nome/brand del prodotto** + **dominio**
- [ ] **Primo cliente / nicchia reale** ← input umano necessario per scrivere un `BRIEF.md` non finto
- [ ] **Prezzo** dell'abbonamento (ipotesi di lavoro: €200-600/mese su 3-5 competitor)
- [ ] **Giorno** di invio del report settimanale
- [ ] **Collection: Strada A (WebSearch/API) o Strada B (VPS)** — vedi §4
- [ ] **ESP** per invio/ricezione email (deliverability)
- [ ] **Hosting** landing (Netlify vs Vercel)
- [ ] **Realismo**: confermato "reale ma contenuto" (business vero, clienti/€ veri, piccola scala, basso rischio)

---

## 7. Struttura della cartella

```
serie-startup-agenti-ai/
├── CLAUDE.md            <- questo file (bibbia serie + log decisioni + spec prodotto)
├── episodi/             <- un sottocartella per episodio (PRINCIPALE.html ecc.) — da popolare
│   └── ep0-manifesto/   (futuro)
└── sistema/             <- bozze del prodotto Competitor Analyzer
                            (landing, schema Supabase, edge function, BRIEF.md, pipeline adattata)
                            TEMPORANEO: verrà spostato in una repo GitHub dedicata
```

> **Nota sul sistema**: `sistema/` è staging. Quando il prodotto prende forma, si sposta in una **repo GitHub
> dedicata** (separata da `yt-content-creation`). Fino ad allora si sviluppa qui.

---

## 8. Origine / contesto
- Nasce dal canale `yt-content-creation` (AI applicata al business, audience non tecnica).
- Riusa il sistema costruito in `CONTENUTI/claude-4-8-dynamic-workflows-10-agenti-paralleli/` (scraper +
  orchestrator + sub-agenti + valutatore + routine schedulata + Supabase).
- Connettori MCP già collegati alla sessione: **Supabase**, **Google Drive**.

## 9. Prossimo passo operativo
Costruire il **blocco [1]**: landing page con form (email + consensi) → primo artefatto reale, ingresso del
funnel, e contenuto dell'Ep 2. In parallelo, definire lo **schema Supabase** (§3). Sblocco necessario prima di
un `BRIEF.md` reale: il **primo cliente/nicchia** (§6).
