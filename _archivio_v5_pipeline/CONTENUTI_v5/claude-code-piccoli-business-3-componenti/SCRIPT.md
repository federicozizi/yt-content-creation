# SCRIPT.md — Claude Code per piccoli business: le 3 componenti imprescindibili

> ⚠️ Gemello inglese: `CONTENUTI/claude-code-small-business-3-components/SCRIPT.md`.

Durata target: **18-22 minuti**.
Stile: pratico, conversazionale. Tre strati nettamente distinti (Supabase via MCP, pacchetto Anthropic Small Business, Agent View custom), un caso d'esempio (studio commercialisti), una sezione finale che li orchestra.

---

## 0. SETUP UNA TANTUM

Cose della vita, da fare una sola volta:

- Account Supabase attivo (`supabase.com`), progetto "studio-demo" già creato e con lo schema caricato.
- Account Claude Cowork con piano Team attivo. Plugin Small Business installato via `/smb-onboard`. Almeno 2 connettori collegati: QuickBooks sandbox e Google Workspace del profilo demo.
- Claude Code installato globalmente (`claude --version`).
- Profilo Chrome dedicato "youtube-demo".
- OBS con 3 scene: `BROWSER`, `TERMINALE`, `CAMERA`.
- Microfono testato, livello -12dB di picco.

---

## 1. PRE-REC GIORNATA (45 min prima)

### Cartella demo
- [ ] `~/demo/infrastruttura/materiali/` esiste e contiene: `schema-aziendale.sql`, `.env` compilato con valori di TEST (mai produzione), `.claude/agents/` coi 3 sub-agent, `.claude/mcp.json`, `prompts/`, `docs/`.
- [ ] `.env` ha `SUPABASE_URL` e `SUPABASE_SERVICE_ROLE_KEY` di un progetto Supabase di test.

### Supabase
- [ ] Progetto Supabase "studio-demo" attivo, con tabelle `clienti`, `regimi_fiscali`, `scadenze_custom`, `note_interne` pre-popolate con dati finti (5 clienti, regimi assortiti, ~10 scadenze, ~5 note interne tra cui 2 alert da regime-checker della "settimana scorsa" finta).
- [ ] Pannello Supabase aperto in tab Chrome dedicata, già loggato.

### Claude Cowork
- [ ] Login a `claude.com/cowork` col profilo demo. Plugin Small Business già attivo. QuickBooks sandbox + Google Workspace già collegati.
- [ ] Tab di Cowork aperta in `/monday-brief` (chat pronta).

### Tab del browser in ordine fisso
1. PRINCIPALE.html locale (per le clip slide)
2. Supabase dashboard (`studio-demo` aperto)
3. Claude Cowork (tab dedicata)

### Terminale
- [ ] Cwd in `~/demo/infrastruttura/materiali/`
- [ ] Prompt leggibile (es. `PS1='\W $ '`)
- [ ] History pulita

### Artefatti pre-cotti (BACKUP)
- [ ] Screenshot dei 3 momenti chiave (Supabase con tabelle popolate, `/monday-brief` output, Agent View con 3 agenti running) in `~/demo/backup/screenshots/`.
- [ ] Log finto `regime-checker-output.txt` se la run live è lenta.

---

## 2. CLIP — elenco completo

| # | Schermata | Durata | Modalità |
|---|---|---|---|
| 01 | CAMERA | ~30s | LIVE (hook) |
| 02 | PRINCIPALE.html `#cosa-e` | ~70s | LIVE |
| 03 | PRINCIPALE.html `#cosa-costruiremo` | ~80s | LIVE |
| 04 | PRINCIPALE.html `#come-funziona` | ~60s | LIVE |
| 05 | PRINCIPALE.html `#setup` | ~30s | LIVE |
| 06 | PRINCIPALE.html `#step-1` (Supabase + MCP concetto) | ~70s | LIVE |
| 07 | BROWSER Supabase | ~90s | LIVE (creazione progetto + run schema) |
| 08 | TERMINALE | ~70s | LIVE (`claude mcp add supabase` + verifica) |
| 09 | PRINCIPALE.html `#step-2` (Pacchetto Anthropic concetto) | ~70s | LIVE |
| 10 | PRINCIPALE.html `#step-2` (tabella workflow) | ~70s | LIVE |
| 11 | PRINCIPALE.html `#step-2` (4 garanzie) | ~45s | LIVE |
| 12 | BROWSER Claude Cowork | ~90s | LIVE (collegare un connettore + `/monday-brief`) |
| 13 | PRINCIPALE.html `#step-3` (Agent View concetto) | ~50s | LIVE |
| 14 | PRINCIPALE.html `#step-3` (esempio sub-agent regime-checker) | ~60s | LIVE |
| 15 | TERMINALE | ~80s | LIVE (`claude agents` + lancio sub-agent custom) |
| 16 | PRINCIPALE.html `#integrazione` | ~100s | LIVE |
| 17 | BROWSER + TERMINALE split | ~75s | MISTO (flusso end-to-end accelerato) |
| 18 | PRINCIPALE.html `#oltre` | ~60s | LIVE |
| 19 | CAMERA | ~35s | LIVE (riepilogo) |
| 20 | CAMERA | ~40s | LIVE (CTA verbatim) |

**Totale stimato**: ~19-21 min. CAMERA solo per hook + riepilogo + CTA.

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`.
- Postura aperta, sguardo dritto.

**🎙️ DIRE (verbatim):**
> "Hai un piccolo business e usi Claude Code per esperimenti, ma non hai ancora messo in piedi un sistema vero. Un sistema vero ha tre pezzi: un database dei dati che sono solo tuoi, un pacchetto di workflow che Anthropic ha pre-cotto la settimana scorsa per le piccole imprese, e degli agenti custom per quello che il pre-cotto non sa fare. In venti minuti monto tutti e tre, dal vivo, e ti faccio vedere come si parlano."

**🖥️ MOSTRARE:** Solo CAMERA.

**🎬 LIVE**

---

## CLIP 02 — Cos'è un'infrastruttura AI

**🧰 Cosa preparare prima della camera:**
- Switcha a tab PRINCIPALE.html, scrolla a `#cosa-e`. Box giallo `.concetto-chiave` visibile.

**🎙️ DIRE:**
> "Un'infrastruttura AI per piccolo business non è un tool. Sono tre pezzi che si parlano. Se ne manca uno, l'AI resta un giochino. Tre strati. Uno: i dati specifici del tuo business — come categorizzi i clienti tu, le scadenze tue, le particolarità del tuo settore. Quelli vanno in un database. Due: i workflow comuni a tutti i piccoli business — paghe, fatture, chiusura mese, briefing. Quelli li ha già scritti Anthropic per te. Tre: gli agenti custom per le cose che fai solo tu, quando il pre-cotto non basta. Tre strati. Punto."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-e`. Punta col cursore il box giallo mentre lo leggi.

**🎬 LIVE**

---

## CLIP 03 — Cosa costruiremo (case study)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#cosa-costruiremo`. Il diagramma ASCII (3 componenti + flusso lunedì) ben visibile a schermo intero.

**🎙️ DIRE:**
> "Caso concreto: studio di commercialisti. Cinquanta clienti, ognuno con le sue particolarità — regime forfettario, ordinario, scadenze IVA diverse. Oggi il junior fa la chiusura mensile in tre giorni. Domani la fa l'infrastruttura in trenta minuti, e il junior la revisiona. Guarda lo schema: in alto i tre componenti, in basso il flusso del lunedì mattina. Componente uno, Supabase, ci finiscono i dati che nessun software fiscale standard conosce. Componente due, il pacchetto Anthropic dentro Cowork, fa le cose comuni — chiusura mese, briefing, solleciti. Componente tre, Agent View di Claude Code, fa le tre cose custom dello studio che il pacchetto non sa fare. Lo stesso schema vale per qualsiasi piccolo business in cui hai particolarità tue più operazioni comuni più qualcosa che è solo tuo."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-costruiremo`. Soffermati sul diagramma ~25s — è la mappa di tutto il video.

**🎬 LIVE**

---

## CLIP 04 — Architettura

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#come-funziona`. Lista numerata + box giallo finale visibili.

**🎙️ DIRE:**
> "I tre strati hanno ruoli netti, non si sovrappongono. Supabase via MCP — MCP è il protocollo aperto che permette a Claude di parlare coi servizi esterni; Supabase ha un connettore MCP ufficiale, una volta installato Claude legge e scrive direttamente nel tuo DB senza scrivere codice. Claude for Small Business — il pacchetto Anthropic rilasciato il tredici maggio duemilaventisei dentro Cowork: quindici workflow, quindici skill, sette connettori per QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365. Agent View — la dashboard di Claude Code che lancia gli agenti custom in parallelo. Regola di divisione, leggi il box giallo: dato custom va in Supabase, operazione comune va nel pacchetto, operazione custom va in Agent View. Sapendo questo, sai dove mettere qualunque cosa."

**🖥️ MOSTRARE:** PRINCIPALE.html `#come-funziona`. Punta il box giallo `.concetto-chiave` quando arrivi alla regola di divisione.

**🎬 LIVE**

---

## CLIP 05 — Setup

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#setup`. Lista checks visibile.

**🎙️ DIRE:**
> "Tre account: Claude Code che già usi, Supabase gratuito, Claude Cowork piano Team per il pacchetto. Il piano Team costa attorno ai venticinque euro per utente al mese — non è gratis, ma per un piccolo business è il prezzo di un caffè al giorno. Per il setup operativo: lanci claude nella cartella materiali e gli dici esegui il setup leggendo CLAUDE.md. Ti guida lui, trenta minuti."

**🖥️ MOSTRARE:** PRINCIPALE.html `#setup`. Punta la lista `ul.checks`.

**🎬 LIVE**

---

## CLIP 06 — Step 1: Supabase via MCP (concetto)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#step-1`. Box giallo "Cos'è Supabase + MCP" + tabella Excel vs Supabase ben visibili.

**🎙️ DIRE:**
> "Primo strato: il database dei tuoi dati custom. Supabase è un servizio cloud che ti dà un Postgres pronto all'uso, accessibile dal browser, con pannello visuale per creare tabelle senza scrivere SQL. Gratuito fino a cinquecento mega — per un piccolo business significa essenzialmente illimitato. MCP — Model Context Protocol — è il protocollo aperto che permette a Claude di parlare coi servizi esterni; Supabase ha un MCP connector ufficiale: una volta installato, Claude legge e scrive direttamente nel DB. Cinque motivi per cui è meglio di Excel: query in cinquanta millisecondi anche su cinquantamila righe, multi-utente senza conflitti, audit log automatico, l'AI ci scrive sopra in tempo reale via MCP, e cresce senza piantarsi. Per dati seri non c'è gara."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-1`. Soffermati ~20s sulla tabella `table.compare`.

**🎬 LIVE**

---

## CLIP 07 — Supabase live (creazione + schema)

**🧰 Cosa preparare prima della camera:**
- Switcha a tab Supabase, logout dal progetto demo. Torna in dashboard "New project".
- Apri in secondo monitor `materiali/schema-aziendale.sql`.

**🎙️ DIRE (libero, da commento mentre fai):**
> "Vado su supabase.com, clic New project, nome studio-demo, regione Francoforte per l'Italia, password — la metto in un gestore di password, mai a video. Aspetta venti secondi che lo prepara. Pannello SQL Editor, New query, incollo lo schema dai materiali: quattro tabelle — clienti, regimi fiscali, scadenze custom, note interne. Click Run. Quattro tabelle create, niente SQL scritto a mano."

**🖥️ MOSTRARE:** BROWSER Supabase. Creazione progetto → SQL Editor → paste schema → Run → verifica tabelle in Table Editor.

**🎬 LIVE** (accelerare 2x i 20s di attesa creazione progetto).

---

## CLIP 08 — Supabase MCP nel terminale

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `TERMINALE`. Cwd in `~/demo/infrastruttura/materiali/`.
- Tieni a portata le credenziali Supabase (URL + Service Role key) dal progetto appena creato.

**🎙️ DIRE (libero, da commento):**
> "Ora colleghiamo Claude Code al database via MCP. Comando: claude mcp add supabase. Mi chiede URL e key — le incollo dal pannello Supabase. Attenzione, la service role key dà accesso totale al DB, mai a video. Verifica: lancio claude e gli dico 'mostrami le tabelle del DB Supabase e quante righe hanno'. Lui le vede: quattro tabelle, righe presenti. MCP connector attivo. Adesso Claude può fare SELECT e INSERT direttamente nel nostro DB, in tempo reale, senza che io scriva una riga di codice."

**🖥️ MOSTRARE:** TERMINALE: `claude mcp add supabase` (campi sensibili da censurare in editing), poi `claude` + prompt verifica, output con 4 tabelle.

**🎬 LIVE**
> ⚠️ Censura frame-by-frame se la Service Role key è apparsa anche per 1 frame.

---

## CLIP 09 — Step 2: Claude for Small Business (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-2`. Box giallo "Cos'è in pratica" visibile.

**🎙️ DIRE:**
> "Secondo strato, e qui c'è la novità grossa. Il tredici maggio duemilaventisei, la settimana scorsa al momento di questo video, Anthropic ha rilasciato Claude for Small Business. Un pacchetto di workflow e skill già scritti per le cose comuni a tutti i piccoli business. Quello che prima costava settimane di scripting custom, adesso è un toggle dentro Claude Cowork. Si attiva col comando barra smb-onboard, parte una procedura guidata, ti chiede quali tool del tuo business già paghi, li collega con un click ciascuno, e dopo dieci minuti hai quindici workflow pronti che parlano con QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 10 — Step 2: tabella workflow

**🧰 Cosa preparare prima della camera:**
- Resta su PRINCIPALE.html `#step-2`, scorri alla `table.compare` dei 6 workflow principali.

**🎙️ DIRE:**
> "I quindici workflow sono comandi slash dentro Cowork. I sei più usati. Barra monday-brief: lunedì mattina ti dà un riassunto — cassa attuale leggendo QuickBooks, fatture in scadenza, lead nuovi nel CRM leggendo HubSpot, suggerimento prossima azione. Barra close-month: chiusura del mese — riconciliazione fatture, scritture, P&L narrative cioè il commento in linguaggio naturale sul perché i numeri sono quelli. Barra invoice-chaser: solleciti automatici delle fatture scadute, ma tu approvi PRIMA che parta l'email, niente invii alla cieca. Barra plan-payroll per le paghe. Barra run-campaign: campagne marketing — drafta testi, genera grafiche con Canva, segmenta lista in HubSpot, tu approvi prima di pubblicare. Barra contract-review: legge un PDF DocuSign, evidenzia clausole rischiose, suggerisce modifiche. Sotto, quindici skill più piccoli che si attivano automaticamente — cash flow, margini, lead triage, sentiment, tax prep."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2` tabella `table.compare`. Scorri lentamente, soffermati su ogni riga.

**🎬 LIVE**

---

## CLIP 11 — Step 2: le 4 garanzie

**🧰 Cosa preparare prima della camera:**
- Resta su PRINCIPALE.html `#step-2`, scorri alla `ul.checks` con le 4 garanzie.

**🎙️ DIRE:**
> "Quattro garanzie che lo rendono adatto a un piccolo business — leggile a schermo. Uno: i tuoi permessi si propagano. Se un collaboratore non vede una cosa in QuickBooks col suo account, non la vede neanche tramite Claude. Niente buchi di sicurezza creati dall'AI. Due: approvazione umana obbligatoria prima che esca qualcosa. Niente email, pagamenti, post automatici senza il tuo OK. Tre: Anthropic non si allena sui tuoi dati di business nei piani Team e Enterprise. I tuoi numeri restano tuoi. Quattro: costo zero in più rispetto al piano Cowork Team che paghi comunque. Plugin gratuito dentro un piano che hai già."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Lista `ul.checks` con le 4 garanzie.

**🎬 LIVE**

---

## CLIP 12 — Cowork live (`/smb-onboard` + `/monday-brief`)

**🧰 Cosa preparare prima della camera:**
- Switcha a tab Claude Cowork, profilo demo loggato. Plugin Small Business già attivato (non ri-eseguire smb-onboard live, fai vedere il risultato come "già attivato").
- Connettori già collegati: Google Workspace + QuickBooks sandbox.

**🎙️ DIRE (libero, da commento):**
> "Vediamo il pacchetto al lavoro. Il primo comando, barra smb-onboard, l'ho già eseguito in una sessione precedente — vedi che il plugin è attivo nella sidebar. La procedura ti chiede quali tool collegare, ti porta nei flussi OAuth standard di Google, QuickBooks, HubSpot. Niente console Google Cloud, niente credentials.json a mano: Anthropic ha pre-registrato l'app, tu dai solo il consenso. Adesso provo un workflow vero: barra monday-brief. Lui legge QuickBooks per la cassa, legge HubSpot per i lead, e mi tira fuori un riassunto operativo. Vedi il bottone Approve in basso? Se gli dico procedi, manda l'email di sollecito proposta; se non clicco, non manda niente. Approvazione umana al centro."

**🖥️ MOSTRARE:** BROWSER Cowork: vista del plugin attivo → comando `/monday-brief` → output → mostra (ma NON premi) il bottone di approvazione.

**🎬 LIVE**

---

## CLIP 13 — Step 3: Agent View (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-3`. Concetto-chiave "Cos'è Agent View" visibile.

**🎙️ DIRE:**
> "Terzo strato. Il pacchetto pre-cotto copre tantissimo, ma non tutto. Le cose tue — come categorizzi i clienti, particolarità del tuo settore, tipi di documento che gestisci solo tu — quelle te le devi scrivere tu. Per fortuna scrivere qui significa scrivere markdown in italiano, non codice. Agent View è la dashboard di Claude Code che lancia agenti custom in parallelo. La apri col comando claude agents. Ogni agente è un file markdown in cartella punto-claude slash agents, con nome, descrizione, tool che può usare, e istruzioni in italiano. Lavorano contemporaneamente, li vedi dalla stessa dashboard."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3`. Punta il box giallo `.concetto-chiave`.

**🎬 LIVE**

---

## CLIP 14 — Anatomia di un sub-agent

**🧰 Cosa preparare prima della camera:**
- Resta su PRINCIPALE.html `#step-3`, scrolla al blocco `.action` con il file `regime-checker.md`.

**🎙️ DIRE:**
> "Per lo studio commercialisti, scriviamo tre sub-agent custom. Document classifier per classificare documenti ambigui — fatture semplificate o scontrini fiscali per esempio. Regime checker che controlla settimanalmente se qualche cliente ha superato la soglia del proprio regime fiscale — ottantacinquemila euro per il forfettario per esempio. Scadenza allerter che ogni mattina prepara la lista delle scadenze del giorno per i singoli soci dello studio. Guarda l'anatomia di uno di questi — regime-checker. In alto i metadati: nome, descrizione, tool che può usare — Read, Write, Bash, e il connettore MCP di Supabase. Sotto le istruzioni in italiano: leggi la tabella clienti, confronta col limite del regime, se uno è oltre l'ottanta percento del limite scrivi un alert in note_interne. È markdown, è italiano, lo legge anche tua zia che non ha mai programmato."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3` blocco `.action` con regime-checker. Soffermati sul contenuto.

**🎬 LIVE**

---

## CLIP 15 — Agent View live

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `TERMINALE`. Cwd in `~/demo/infrastruttura/materiali/`.
- I 3 sub-agent in `.claude/agents/` esistono e sono configurati per il progetto demo.

**🎙️ DIRE (libero, da commento):**
> "Apro Agent View. Comando claude agents. Vedo i tre agenti definiti: document-classifier, regime-checker, scadenza-allerter, tutti in stato ready. Lancio regime-checker. Lui parte, legge clienti da Supabase via MCP, confronta col limite di ogni regime, vede che il cliente Bianchi è arrivato all'ottantatre percento del forfettario. Scrive un alert in note_interne. Mentre fa quello, lancio in parallelo document-classifier su un paio di documenti ambigui — gira contemporaneamente nella stessa dashboard, vedo i log in tempo reale di entrambi. Finiti i due, vado in Supabase a verificare: una riga nuova in note_interne, due righe nuove in documenti."

**🖥️ MOSTRARE:** TERMINALE `claude agents` → dashboard con 3 agenti → lancio regime-checker → vedi log → lancio in parallelo document-classifier → switch breve a Supabase per verifica.

**🎬 LIVE** (se le run sono lente, accelera 3x in editing).

---

## CLIP 16 — Integrazione (flusso end-to-end narrato)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#integrazione`. Diagramma "09:00, 09:15, 09:45, fine mese" visibile + box giallo.

**🎙️ DIRE:**
> "Vediamo come si parlano tutti insieme. Il lunedì mattina tipico dopo che l'infrastruttura è in piedi. Nove di mattina: apri Cowork, digiti barra monday-brief. Il pacchetto legge QuickBooks per la cassa, e legge Supabase tramite MCP per gli alert da regime-checker della settimana scorsa. Ti dice: cassa dodicimila, quattro fatture in scadenza, e attenzione, due clienti vicini al limite del forfettario. Nove e un quarto: apri Claude Code, lanci claude agents. Lanci document-classifier sui PDF caricati nel weekend dai clienti. In parallelo regime-checker ricontrolla i fatturati. Nove e quarantacinque: torni in Cowork, barra invoice-chaser. Il pacchetto legge le fatture insolute da QuickBooks ma PRIMA controlla note_interne su Supabase — se un cliente ha note 'tempo difficile, non sollecitare', salta. Ti propone tre email personalizzate, approvi, partono. Fine mese: barra close-month. Il pacchetto fa la chiusura standard QuickBooks più scritture, poi legge scadenze_custom da Supabase per aggiungere le particolarità dello studio, e salva il report su Drive via Google Workspace connector. Tutto si tiene insieme grazie al box giallo qui sotto: Supabase è la fonte di verità del tuo business, il pacchetto è il motore dei workflow comuni, Agent View è il motore dei workflow custom. Il ponte tra tutti e tre è il connettore MCP di Supabase, che funziona allo stesso modo dentro Claude Code e dentro Cowork. Stesso DB, niente silos."

**🖥️ MOSTRARE:** PRINCIPALE.html `#integrazione`. Diagramma temporale ~30s, poi punta il box giallo "Il momento in cui tutto si tiene insieme".

**🎬 LIVE**

---

## CLIP 17 — Demo flusso end-to-end (split screen)

**🧰 Cosa preparare prima della camera:**
- Set-up split screen: metà sinistra TERMINALE con `claude agents` aperto, metà destra BROWSER su Claude Cowork.

**🎙️ DIRE (libero, da commento):**
> "Mini-demo del flusso reale. Parto da Cowork: barra monday-brief — l'output legge sia QuickBooks che Supabase via MCP, vedi nell'output che cita i due alert da regime-checker. Adesso passo a Claude Code: lancio document-classifier su due nuovi PDF — in parallelo regime-checker rifà il giro. Torno in Cowork: barra invoice-chaser — vedi che nel testo proposto cita le note di Supabase per modulare il tono. Senza la nostra Supabase, il pacchetto da solo non saprebbe queste cose."

**🖥️ MOSTRARE:** Split screen TERMINALE + BROWSER. Cowork `/monday-brief` → Code `claude agents` (lancia 2 sub-agent) → Cowork `/invoice-chaser` con citazioni Supabase nell'output.

**🎬 MISTO**
> Se le run agente sono lente, time-lapse 5x in editing.

---

## CLIP 18 — Oltre il caso

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#oltre`. I 5 box `.use-case` visibili scrollando lentamente.

**🎙️ DIRE:**
> "Lo schema vale per qualunque settore — cambiano le tabelle Supabase e i sub-agent custom, ma i tre strati restano. Studio legale: Supabase con contratti e clausole critiche custom, pacchetto con contract-review standard, sub-agent custom per le clausole vessatorie del diritto italiano che il generico non flagga. E-commerce piccolo: Supabase con fornitori e listini storici, pacchetto con margin-analyzer e run-campaign, sub-agent custom che parsa i listini PDF dei tuoi fornitori specifici. Agenzia di comunicazione: Supabase con brief e brand guidelines, pacchetto con run-campaign, sub-agent custom che verifica che i creativi rispettino le brand guidelines del cliente. B&B: Supabase con prenotazioni e tasse di soggiorno per comune, pacchetto con close-month e monday-brief, sub-agent custom che calcola le tasse di soggiorno con le aliquote del tuo comune. Artigiano: Supabase con lavori e tempistiche storiche, pacchetto con plan-payroll e invoice-chaser, sub-agent custom che stima il tempo di un lavoro nuovo confrontandolo con lavori storici simili."

**🖥️ MOSTRARE:** PRINCIPALE.html `#oltre`. Scorri attraverso i 5 box `.use-case`.

**🎬 LIVE**

---

## CLIP 19 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`. Sguardo dritto.

**🎙️ DIRE (verbatim):**
> "Riepilogo. Un'infrastruttura AI per piccolo business sono tre strati, non un tool. Supabase via MCP per i tuoi dati custom — il connettore MCP è il ponte. Claude for Small Business per i workflow comuni — pre-cotti da Anthropic la settimana scorsa, gratuiti col piano Cowork Team. Agent View per gli agenti custom in parallelo — markdown italiano, niente codice. Le tre strade non si escludono, si parlano: il DB Supabase è leggibile sia dagli agenti custom in Code che dai workflow del pacchetto in Cowork, perché MCP è lo stesso protocollo. Se ti porti a casa una cosa sola: dato custom in Supabase, operazione comune nel pacchetto, operazione custom in Agent View. Mai mischiare."

**🖥️ MOSTRARE:** CAMERA.

**🎬 LIVE**

---

## CLIP 20 — CTA Skool + consulenza

**🧰 Cosa preparare prima della camera:**
- Resta su CAMERA.

**🎙️ DIRE (verbatim — non improvvisare):**
> "Se vuoi vedere altre infrastrutture montate così — schemi Supabase reali per i vari settori, sub-agent custom funzionanti, configurazioni di Claude for Small Business adattate al tuo modello — vienimi a trovare nella community Skool. Link in descrizione. È dove condivido i setup veri, con prompt e configurazioni. Se invece hai un caso aziendale specifico e vuoi che lo disegniamo insieme — quali tabelle Supabase ti servono, quali sub-agent custom valgono la pena scrivere, quali workflow del pacchetto Anthropic ti convengono — c'è anche la consulenza diretta. Partiamo dal tuo business reale, non da un tutorial generico. Link in descrizione anche per quello. Ci vediamo nel prossimo video."

**🖥️ MOSTRARE:** CAMERA. Sorriso a fine frase, poi taglio.

**🎬 LIVE**

---

## 3. POST-REC (sicurezza — CRITICO)

Subito dopo aver fermato la registrazione:

- [ ] **REVOCA la Service Role key di Supabase** del progetto demo. Supabase Settings → API → "Reset service_role secret". L'hai usata a video.
- [ ] **Disconnetti i tool collegati a Cowork** del profilo demo (QuickBooks sandbox, Google Workspace demo). Cowork → Settings → Connectors → Revoke ciascuno.
- [ ] **Cancella il file `.env`** dalla cartella materiali (conteneva le credenziali).
- [ ] Verifica nelle raw OBS che nessuna credenziale sia visibile, marca i frame da censurare in editing.
- [ ] Logout da Cowork e da Supabase.

---

## 4. CHECKLIST MONTAGGIO

- [ ] Ordine clip: 01 → 20.
- [ ] **Censure obbligatorie** (frame-by-frame nelle clip 07, 08, 12): qualunque chiave API, qualunque token, qualunque ID di progetto privato.
- [ ] Time-lapse CLIP 07 (creazione progetto Supabase, ~20s): 2x.
- [ ] Time-lapse CLIP 15 (parsing PDF agenti, ~60s): 3x.
- [ ] Time-lapse CLIP 17 (split screen end-to-end, possibili attese): 5x sui passaggi di attesa.
- [ ] Lower-third sui link Skool/consulenza nella CLIP 20.
- [ ] Audio: noise gate, EQ, compressione leggera. -14 LUFS.
- [ ] Sottotitoli IT autogenerati + correzione manuale di: Supabase, MCP, Claude Code, Claude Cowork, Claude for Small Business, Agent View, OAuth, QuickBooks.
- [ ] Thumbnail: split frame in 3 — logo Supabase | logo Anthropic (con badge "Small Business") | terminale `claude agents`. Testo: "Il tuo business AI in 3 pezzi".
- [ ] Descrizione video: link al repo template materiali, link Skool, link consulenza, link annuncio Anthropic Claude for Small Business (anthropic.com/news/claude-for-small-business).
- [ ] End screen: card al video precedente su Agent View + iscriviti.
