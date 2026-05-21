# SCRIPT.md — Claude Code for Small Business: the 3 essential components

> ⚠️ Gemello italiano: `CONTENUTI/claude-code-piccoli-business-3-componenti/SCRIPT.md`.
> Solo le righe `🎙️ DIRE` qui sono in inglese — il resto (PRE-REC, MOSTRARE, LIVE/PRE-COTTO/MISTO, POST-REC, montaggio) resta **in italiano** perché sono note per il regista.

Durata target: **18-22 minuti**.
Stile: pratico, conversazionale. Tre strati nettamente distinti (Supabase via MCP, pacchetto Anthropic Small Business, Agent View custom), un caso d'esempio (studio commercialisti), una sezione finale che li orchestra.

---

## 0. SETUP UNA TANTUM

- Account Supabase attivo, progetto "studio-demo" con schema caricato.
- Account Claude Cowork con piano Team attivo. Plugin Small Business installato via `/smb-onboard`. 2 connettori collegati: QuickBooks sandbox + Google Workspace demo.
- Claude Code installato globalmente.
- Profilo Chrome "youtube-demo".
- OBS con 3 scene: `BROWSER`, `TERMINALE`, `CAMERA`.
- Microfono testato, -12dB di picco.

---

## 1. PRE-REC GIORNATA (45 min prima)

### Cartella demo
- [ ] `~/demo/infrastruttura/materiali/` con tutti i file IT (gli inglesi sono solo per il sito/repo template, in locale lavoriamo sul progetto già configurato).
- [ ] `.env` con valori TEST di un Supabase di prova.

### Supabase
- [ ] Progetto Supabase "studio-demo" attivo, 4 tabelle pre-popolate con dati finti.
- [ ] Pannello Supabase aperto in tab Chrome dedicata.

### Claude Cowork
- [ ] Login a `claude.com/cowork` col profilo demo. Plugin Small Business attivo. QuickBooks sandbox + Google Workspace collegati.

### Tab del browser in ordine fisso
1. PRINCIPALE.html (EN)
2. Supabase dashboard
3. Claude Cowork

### Terminale
- [ ] Cwd in `~/demo/infrastruttura/materiali/`
- [ ] History pulita

### Artefatti pre-cotti (BACKUP)
- [ ] Screenshot momenti chiave in `~/demo/backup/screenshots/`.

---

## 2. CLIP — elenco completo

| # | Schermata | Durata | Modalità |
|---|---|---|---|
| 01 | CAMERA | ~30s | LIVE (hook) |
| 02 | PRINCIPALE.html `#cosa-e` | ~70s | LIVE |
| 03 | PRINCIPALE.html `#cosa-costruiremo` | ~80s | LIVE |
| 04 | PRINCIPALE.html `#come-funziona` | ~60s | LIVE |
| 05 | PRINCIPALE.html `#setup` | ~30s | LIVE |
| 06 | PRINCIPALE.html `#step-1` (Supabase + MCP concept) | ~70s | LIVE |
| 07 | BROWSER Supabase | ~90s | LIVE |
| 08 | TERMINALE | ~70s | LIVE |
| 09 | PRINCIPALE.html `#step-2` (Package concept) | ~70s | LIVE |
| 10 | PRINCIPALE.html `#step-2` (workflows table) | ~70s | LIVE |
| 11 | PRINCIPALE.html `#step-2` (4 guarantees) | ~45s | LIVE |
| 12 | BROWSER Claude Cowork | ~90s | LIVE |
| 13 | PRINCIPALE.html `#step-3` (Agent View concept) | ~50s | LIVE |
| 14 | PRINCIPALE.html `#step-3` (sub-agent anatomy) | ~60s | LIVE |
| 15 | TERMINALE | ~80s | LIVE |
| 16 | PRINCIPALE.html `#integrazione` | ~100s | LIVE |
| 17 | BROWSER + TERMINALE split | ~75s | MISTO |
| 18 | PRINCIPALE.html `#oltre` | ~60s | LIVE |
| 19 | CAMERA | ~35s | LIVE (recap) |
| 20 | CAMERA | ~40s | LIVE (CTA verbatim) |

**Totale stimato**: ~19-21 min.

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`. Postura aperta, sguardo dritto.

**🎙️ DIRE (verbatim):**
> "You have a small business and you already use Claude Code for experiments, but you haven't built a real system yet. A real system has three pieces: a database for the data that's only yours, a workflow package Anthropic pre-cooked last week for small businesses, and custom agents for what the pre-built can't do. In twenty minutes I'll build all three live and show you how they talk to each other."

**🖥️ MOSTRARE:** Solo CAMERA.

**🎬 LIVE**

---

## CLIP 02 — Cos'è un'infrastruttura AI

**🧰 Cosa preparare prima della camera:**
- PRINCIPALE.html scrollato a `#cosa-e`. Box giallo visibile.

**🎙️ DIRE:**
> "An AI infrastructure for a small business isn't a tool. It's three pieces that talk to each other. If even one is missing, the AI stays a toy. Three layers. One: the data specific to your business — how you categorize clients, your deadlines, your industry's quirks. That goes in a database. Two: the workflows common to all small businesses — payroll, invoices, monthly close, briefings. Anthropic has already written those for you. Three: custom agents for the things only you do, when the pre-built isn't enough. Three layers. Period."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-e`. Punta col cursore il box giallo.

**🎬 LIVE**

---

## CLIP 03 — Cosa costruiremo (case study)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#cosa-costruiremo`. Diagramma ASCII ben visibile.

**🎙️ DIRE:**
> "Concrete case: an accounting firm. Fifty clients, each with their own tax peculiarities — different regimes, different VAT schedules. Today the junior does the monthly close in three days. Tomorrow the infrastructure does it in thirty minutes and the junior reviews it. Look at the diagram: three components on top, Monday morning flow on the bottom. Component one, Supabase, holds data that no standard tax software knows about. Component two, the Anthropic package inside Cowork, does the common things — month close, briefings, reminders. Component three, Agent View in Claude Code, does the three custom things the package can't do. The same schema works for any small business where you have your own quirks plus common operations plus something that's only yours."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-costruiremo`. Soffermati sul diagramma ~25s.

**🎬 LIVE**

---

## CLIP 04 — Architettura

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#come-funziona`. Lista numerata + box giallo finale visibili.

**🎙️ DIRE:**
> "The three layers have distinct roles, no overlap. Supabase via MCP — MCP is the open protocol that lets Claude talk to external services; Supabase has an official MCP connector, once installed Claude reads and writes directly to your DB with no code. Claude for Small Business — the Anthropic package released May 13, 2026, inside Cowork: fifteen workflows, fifteen skills, seven connectors for QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365. Agent View — the Claude Code dashboard that launches custom agents in parallel. Division rule, read the yellow box: custom data goes to Supabase, common operation goes to the package, custom operation goes to Agent View. Knowing this, you know where to put anything."

**🖥️ MOSTRARE:** PRINCIPALE.html `#come-funziona`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 05 — Setup

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#setup`. Lista checks visibile.

**🎙️ DIRE:**
> "Three accounts: Claude Code, which you already use. Supabase, free. Claude Cowork Team plan for the package. The Team plan is about twenty-five dollars per user per month — not free, but for a small business it's the price of a coffee a day. For operational setup in the materials: run claude in the materials folder and tell it to run the setup by reading CLAUDE.md. It guides you through, thirty minutes."

**🖥️ MOSTRARE:** PRINCIPALE.html `#setup`. Punta la lista `ul.checks`.

**🎬 LIVE**

---

## CLIP 06 — Step 1: Supabase via MCP (concept)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#step-1`. Box giallo + tabella visibili.

**🎙️ DIRE:**
> "First layer: the database for your custom data. Supabase is a cloud service that gives you a ready-to-use Postgres, accessible from the browser, with a visual panel to create tables without writing SQL. Free up to five hundred megs — for a small business that's essentially unlimited. MCP — Model Context Protocol — is the open protocol that lets Claude talk to external services; Supabase has an official MCP connector: once installed, Claude reads and writes directly to the DB. Five reasons it's better than Excel: queries in fifty milliseconds across fifty thousand rows, multi-user with no conflicts, automatic audit log, AI writes to it in real time via MCP, and it scales without crashing. For serious data, no contest."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-1`. Soffermati ~20s sulla tabella.

**🎬 LIVE**

---

## CLIP 07 — Supabase live (creazione + schema)

**🧰 Cosa preparare prima della camera:**
- Tab Supabase, logout. Dashboard "New project".
- Secondo monitor: `schema-aziendale.sql` aperto.

**🎙️ DIRE (libero, da commento):**
> "I go to supabase.com, click New project, name it studio-demo, region Frankfurt for Europe, password — I put it in a password manager, never on camera. Twenty seconds to provision. SQL Editor, New query, paste the schema from the materials: four tables — clients, tax regimes, custom deadlines, internal notes. Click Run. Four tables created, no SQL written by hand."

**🖥️ MOSTRARE:** BROWSER Supabase: New project → SQL Editor → paste → Run → verifica in Table Editor.

**🎬 LIVE** (accelerare 2x i 20s di attesa).

---

## CLIP 08 — Supabase MCP nel terminale

**🧰 Cosa preparare prima della camera:**
- Scena `TERMINALE`. Cwd `~/demo/infrastruttura/materiali/`.
- Credenziali Supabase a portata di mano.

**🎙️ DIRE (libero, da commento):**
> "Now we connect Claude Code to the database via MCP. Command: claude mcp add supabase. It asks for URL and key — I paste from the Supabase panel. Heads up, the service role key gives total access to the DB, never on camera. Verify: run claude and tell it 'show me the tables in the Supabase DB and how many rows they have'. It sees four tables, rows present. MCP connector active. Now Claude can SELECT and INSERT directly into our DB in real time, without me writing a single line of code."

**🖥️ MOSTRARE:** TERMINALE comando + verifica.

**🎬 LIVE**
> ⚠️ Censura frame-by-frame se la Service Role key è apparsa.

---

## CLIP 09 — Step 2: Claude for Small Business (concept)

**🧰 Cosa preparare prima della camera:**
- PRINCIPALE.html `#step-2`. Box giallo "What it is in practice" visibile.

**🎙️ DIRE:**
> "Second layer, and here's the big news. On May thirteen, twenty twenty-six, last week as of this video, Anthropic released Claude for Small Business. A package of workflows and skills already written for the common things every small business does. What used to cost weeks of custom scripting is now a toggle inside Claude Cowork. You activate it with slash smb-onboard, a guided procedure starts, it asks which tools your business already pays for, connects them with one click each, and ten minutes later you have fifteen workflows ready, talking to QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 10 — Step 2: tabella workflow

**🧰 Cosa preparare prima della camera:**
- Resta su `#step-2`, scorri alla `table.compare` dei 6 workflow.

**🎙️ DIRE:**
> "The fifteen workflows are slash commands inside Cowork. The six most used. Slash monday-brief: Monday morning summary — current cash reading QuickBooks, invoices due, new CRM leads reading HubSpot, suggested next action. Slash close-month: monthly close — invoice reconciliation, entries, P&L narrative which is the natural-language comment on why the numbers are what they are. Slash invoice-chaser: automatic reminders for overdue invoices, but you approve BEFORE it sends, no blind automated sends. Slash plan-payroll for payroll. Slash run-campaign: marketing campaigns — drafts copy, generates Canva graphics, segments the HubSpot list, you approve before publishing. Slash contract-review: reads a DocuSign PDF, highlights risky clauses, suggests changes. Below, fifteen smaller skills that activate automatically — cash flow, margins, lead triage, sentiment, tax prep."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2` tabella. Scorri lentamente, una riga alla volta.

**🎬 LIVE**

---

## CLIP 11 — Step 2: le 4 garanzie

**🧰 Cosa preparare prima della camera:**
- Resta su `#step-2`, scorri alla `ul.checks` delle 4 garanzie.

**🎙️ DIRE:**
> "Four guarantees that make it small-business-ready — read them on screen. One: your permissions carry over. If a teammate can't see something in QuickBooks with their account, they can't see it through Claude. No security holes created by AI. Two: mandatory human approval before anything goes out. No automatic emails, payments, posts without your OK. Three: Anthropic doesn't train on your business data on Team and Enterprise plans. Your numbers stay yours. Four: zero extra cost beyond the Cowork Team plan you're paying anyway. Free plugin inside a plan you already have."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Lista `ul.checks`.

**🎬 LIVE**

---

## CLIP 12 — Cowork live

**🧰 Cosa preparare prima della camera:**
- Tab Cowork, profilo demo loggato. Plugin Small Business attivato. QuickBooks sandbox + Google Workspace collegati.

**🎙️ DIRE (libero, da commento):**
> "Let's see the package at work. First command, slash smb-onboard, I already ran it in a previous session — you can see the plugin is active in the sidebar. The procedure asks which tools to connect, takes you through standard OAuth flows for Google, QuickBooks, HubSpot. No Google Cloud console, no manual credentials.json: Anthropic pre-registered the app, you just give consent. Now let me try a real workflow: slash monday-brief. It reads QuickBooks for cash, reads HubSpot for leads, gives me an operational summary. See the Approve button at the bottom? If I tell it to proceed, the proposed reminder email goes out; if I don't click, nothing goes. Human approval at the center."

**🖥️ MOSTRARE:** BROWSER Cowork: plugin attivo → `/monday-brief` → output → mostra (ma NON premi) il bottone Approve.

**🎬 LIVE**

---

## CLIP 13 — Step 3: Agent View (concept)

**🧰 Cosa preparare prima della camera:**
- PRINCIPALE.html `#step-3`. Box giallo "What Agent View is" visibile.

**🎙️ DIRE:**
> "Third layer. The pre-built package covers a lot, but not everything. The things that are yours — how you categorize clients, your industry's quirks, document types only you handle — you have to write those yourself. Fortunately writing here means writing markdown in plain English, not code. Agent View is the Claude Code dashboard that launches custom agents in parallel. You open it with the command claude agents. Each agent is a markdown file in dot-claude slash agents, with a name, description, tools it can use, and instructions in plain English. They work simultaneously, you see them all in the same dashboard."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3`. Punta il box giallo.

**🎬 LIVE**

---

## CLIP 14 — Anatomia di un sub-agent

**🧰 Cosa preparare prima della camera:**
- Resta su `#step-3`, scrolla al blocco `.action` con regime-checker.

**🎙️ DIRE:**
> "For the accounting firm, we write three custom sub-agents. Document classifier to classify ambiguous documents — simplified invoices or fiscal receipts for example. Regime checker that weekly checks if a client has crossed their tax regime threshold — eighty-five thousand for the forfettario for instance. Deadline alerter that every morning prepares the day's deadline list for each partner. Look at the anatomy of one — regime-checker. Top: metadata — name, description, tools it can use — Read, Write, Bash, and the Supabase MCP connector. Below: instructions in plain English. Read the clients table, compare against the regime limit, if any is past eighty percent write an alert to internal notes. It's markdown, it's plain English, your aunt who never programmed could read it."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3` blocco `.action`. Soffermati sul contenuto.

**🎬 LIVE**

---

## CLIP 15 — Agent View live

**🧰 Cosa preparare prima della camera:**
- Scena `TERMINALE`. Cwd `~/demo/infrastruttura/materiali/`.
- I 3 sub-agent in `.claude/agents/` esistono.

**🎙️ DIRE (libero, da commento):**
> "I open Agent View. Command claude agents. I see the three defined agents: document-classifier, regime-checker, deadline-alerter, all in ready state. I launch regime-checker. It runs, reads clients from Supabase via MCP, compares against each regime's limit, sees that the client Bianchi reached eighty-three percent of the forfettario. Writes an alert to internal_notes. While it does that, in parallel I launch document-classifier on a couple of ambiguous documents — runs simultaneously in the same dashboard, I see real-time logs for both. When the two are done, I go to Supabase to verify: one new row in internal_notes, two new rows in documents."

**🖥️ MOSTRARE:** TERMINALE → dashboard agents → lancio regime-checker → log → lancio document-classifier in parallelo → switch breve a Supabase.

**🎬 LIVE** (accelera 3x se lente).

---

## CLIP 16 — Integrazione (flusso end-to-end narrato)

**🧰 Cosa preparare prima della camera:**
- PRINCIPALE.html `#integrazione`. Diagramma temporale + box giallo visibili.

**🎙️ DIRE:**
> "Let's see how all three talk to each other. Typical Monday morning after the infrastructure is up. Nine AM: you open Cowork, type slash monday-brief. The package reads QuickBooks for cash and reads Supabase via MCP for alerts from regime-checker from last week. It tells you: twelve thousand in cash, four invoices due, and heads up, two clients close to the forfettario limit. Nine fifteen: you open Claude Code, run claude agents. Launch document-classifier on the PDFs clients uploaded over the weekend. In parallel regime-checker rechecks updated revenues. Nine forty-five: back in Cowork, slash invoice-chaser. The package reads unpaid invoices from QuickBooks but BEFORE writing emails it checks internal_notes on Supabase — if a client has notes like 'rough patch, don't chase', it skips. Proposes three personalized emails, you approve, they go. End of month: slash close-month. The package does standard close, QuickBooks plus entries, then reads custom_deadlines from Supabase to add firm-specific items, and saves the report to Drive via the Google Workspace connector. It all holds together thanks to the yellow box below: Supabase is your source of truth, the package is the engine for common workflows, Agent View is the engine for custom workflows. The bridge between all three is Supabase's MCP connector, which works the same in Claude Code and in Cowork. Same DB, no silos."

**🖥️ MOSTRARE:** PRINCIPALE.html `#integrazione`. Diagramma temporale ~30s, poi punta il box giallo.

**🎬 LIVE**

---

## CLIP 17 — Demo flusso end-to-end (split screen)

**🧰 Cosa preparare prima della camera:**
- Split screen: sinistra TERMINALE con `claude agents` aperto, destra BROWSER su Claude Cowork.

**🎙️ DIRE (libero, da commento):**
> "Real-flow mini-demo. Start in Cowork: slash monday-brief — the output reads both QuickBooks and Supabase via MCP, you can see it cites the two regime-checker alerts. Now I switch to Claude Code: launch document-classifier on two new PDFs — in parallel regime-checker re-runs. Back to Cowork: slash invoice-chaser — see that in the proposed text it cites the Supabase notes to modulate the tone. Without our Supabase, the package alone wouldn't know these things."

**🖥️ MOSTRARE:** Split screen TERMINALE + BROWSER. Sequenza Cowork → Code → Cowork.

**🎬 MISTO**
> Time-lapse 5x sui passaggi di attesa.

---

## CLIP 18 — Oltre il caso

**🧰 Cosa preparare prima della camera:**
- PRINCIPALE.html `#oltre`. 5 box `.use-case`.

**🎙️ DIRE:**
> "The schema works for any industry — Supabase tables and custom sub-agents change, but the three layers remain. Law firm: Supabase with contracts and custom critical clauses, package with standard contract-review, custom sub-agent for country-specific clauses the generic doesn't flag. Small e-commerce: Supabase with suppliers and price history, package with margin-analyzer and run-campaign, custom sub-agent that parses your specific suppliers' PDF lists. Communication agency: Supabase with briefs and brand guidelines, package with run-campaign, custom sub-agent that verifies creatives respect the client's guidelines. B and B: Supabase with bookings and tourist tax by municipality, package with close-month and monday-brief, custom sub-agent calculating tourist tax with your municipality's rates. Trades: Supabase with jobs and historical timing, package with plan-payroll and invoice-chaser, custom sub-agent estimating a new job's time by comparing with similar historical jobs."

**🖥️ MOSTRARE:** PRINCIPALE.html `#oltre`. Scorri i 5 box.

**🎬 LIVE**

---

## CLIP 19 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- Scena `CAMERA`. Sguardo dritto.

**🎙️ DIRE (verbatim):**
> "Recap. An AI infrastructure for a small business is three layers, not a tool. Supabase via MCP for your custom data — the MCP connector is the bridge. Claude for Small Business for common workflows — pre-cooked by Anthropic last week, free with the Cowork Team plan. Agent View for parallel custom agents — plain English markdown, no code. The three paths don't exclude each other, they talk: the Supabase DB is readable both by custom agents in Code and by package workflows in Cowork, because MCP is the same protocol. If you take one thing away: custom data to Supabase, common operation to the package, custom operation to Agent View. Never mix."

**🖥️ MOSTRARE:** CAMERA.

**🎬 LIVE**

---

## CLIP 20 — CTA Skool + consulting

**🧰 Cosa preparare prima della camera:**
- Resta su CAMERA.

**🎙️ DIRE (verbatim — non improvvisare):**
> "If you want to see other infrastructures built like this — real Supabase schemas for various industries, working custom sub-agents, Claude for Small Business configurations tuned to your model — come find me in the Skool community. Link in the description. That's where I share the real setups, with prompts and configs. If instead you have a specific business case and want us to design it together — which Supabase tables you actually need, which custom sub-agents are worth writing, which Anthropic package workflows fit your business model — there's also direct consulting. We start from your real business, not a generic tutorial. Link in the description for that too. See you in the next video."

**🖥️ MOSTRARE:** CAMERA. Sorriso a fine frase, taglio.

**🎬 LIVE**

---

## 3. POST-REC (sicurezza — CRITICO)

- [ ] **REVOCA Service Role key** del progetto Supabase demo.
- [ ] **Disconnetti i tool** collegati a Cowork del profilo demo (QuickBooks sandbox, Google Workspace).
- [ ] **Cancella `.env`** dalla cartella materiali.
- [ ] Verifica raw OBS per credenziali a video, marca i frame da censurare.
- [ ] Logout da Cowork e Supabase.

---

## 4. CHECKLIST MONTAGGIO

- [ ] Ordine clip: 01 → 20.
- [ ] **Censure obbligatorie** frame-by-frame nelle CLIP 07, 08, 12: chiavi API, token, ID privati.
- [ ] Time-lapse CLIP 07: 2x. CLIP 15: 3x. CLIP 17: 5x sui passaggi di attesa.
- [ ] Lower-third sui link Skool/consulenza nella CLIP 20.
- [ ] Audio: noise gate, EQ, compressione leggera. -14 LUFS.
- [ ] Sottotitoli EN autogenerati + correzione manuale di: Supabase, MCP, Claude Code, Claude Cowork, Claude for Small Business, Agent View, OAuth, QuickBooks, forfettario.
- [ ] Thumbnail (versione EN): split frame — logo Supabase | logo Anthropic + badge "Small Business" | terminale `claude agents`. Testo: "Your AI Business in 3 Pieces".
- [ ] Descrizione video EN: link al repo template, link Skool, link consulenza, link annuncio Anthropic (anthropic.com/news/claude-for-small-business).
- [ ] End screen: card al video precedente + iscriviti.
