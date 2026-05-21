<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/docs/claude-for-small-business-howto.md -->

# Claude for Small Business — how-to dettagliato

Tutto quello che ti serve per usare al meglio il pacchetto Anthropic per piccoli business.

## Stato del rilascio

- **Data di lancio**: 13 maggio 2026.
- **Annuncio ufficiale**: https://www.anthropic.com/news/claude-for-small-business
- **Pagina plugin**: https://claude.com/plugins/small-business
- **Disponibilità geografica**: per ora US-first, ma i connettori Google Workspace, Microsoft 365, HubSpot, DocuSign, Canva funzionano da subito anche dalla UE. QuickBooks e PayPal richiedono account US per alcune funzioni avanzate; in UE funzionano in modalità base.

## Prerequisiti

- **Piano Claude Cowork Team** (non funziona con Pro singolo).
- **Almeno un tool collegato**. Anche solo Google Workspace basta per partire — molti workflow leggono Drive e Gmail.

## Attivazione

In una chat Cowork:

```
/smb-onboard
```

Parte la procedura guidata. Domande tipiche:

1. **Settore del business** (commercialisti, studio legale, e-commerce, agenzia, ecc.).
2. **Strumenti che già paghi**: spunta solo quelli che usi davvero. NON tutto.
3. **Permessi per ciascun tool**: per ogni tool spuntato parte un OAuth nel browser. Tu autorizzi col tuo account.

Alla fine vedi una nuova sezione "Small Business" in sidebar.

## I 15 workflow (slash commands)

Al momento del rilascio (maggio 2026), i 15 comandi documentati sono:

| Comando | Cosa fa | Tool che usa |
|---|---|---|
| `/monday-brief` | Riassunto del lunedì: cassa, fatture, lead, prossima azione | QuickBooks, HubSpot, Supabase MCP (se config) |
| `/close-month` | Chiusura mese: riconciliazione + P&L narrative | QuickBooks, Excel/Google Sheets |
| `/invoice-chaser` | Solleciti automatici fatture scadute | QuickBooks, Gmail/Outlook |
| `/plan-payroll` | Pianificazione paghe + cedolini | Gestionale paghe, QuickBooks |
| `/run-campaign` | Campagna marketing: testo + grafiche + lista | HubSpot, Canva, Gmail |
| `/contract-review` | Revisione contratti, evidenzia clausole rischiose | DocuSign |
| `/business-pulse` | Dashboard live di KPI chiave | tutti i connettori |
| `/lead-triage` | Smista i lead in arrivo per priorità | HubSpot |
| `/tax-prep` | Preparazione dichiarazione, raggruppa documenti | QuickBooks, Google Drive |
| `/hiring-packet` | Pacchetto onboarding per nuova assunzione | DocuSign, Google Workspace |
| `/customer-sentiment` | Sintesi opinioni clienti da email/messaggi | Gmail, Slack |
| `/cash-flow` | Forecasting cash flow 30/60/90 giorni | QuickBooks |
| `/margin-analyzer` | Analisi margini per prodotto/servizio | QuickBooks, Excel |
| `/expense-categorizer` | Categorizzazione automatica spese | QuickBooks, Drive |
| `/vendor-payments` | Pianifica pagamenti fornitori | QuickBooks, PayPal |

Ogni comando si lancia in chat Cowork. La prima volta che lo lanci, parte un mini-wizard ("quale periodo? quale conto? approvi prima di inviare?"). Le volte successive ricorda le tue scelte.

## I 15 skill

I "skill" sono mattoni più piccoli che si attivano AUTOMATICAMENTE dentro i workflow. Non li chiami con uno slash command, ma li vedi citati nell'output dei workflow:

- cash-flow forecasting
- margin analysis
- lead triage
- invoice chasing
- contract review
- customer sentiment
- tax prep
- hiring packet builder
- expense categorization
- vendor payment scheduling
- (e altri 5 al momento non interamente documentati nell'annuncio)

## Connettori disponibili

### Inclusi nel pacchetto base

- **Intuit QuickBooks** — contabilità
- **PayPal** — pagamenti
- **HubSpot** — CRM
- **Canva** — design grafico
- **DocuSign** — contratti e firma elettronica
- **Google Workspace** — Gmail, Drive, Calendar, Sheets, Docs
- **Microsoft 365** — Outlook, OneDrive, Teams, Excel, Word

### Opzionali (vanno aggiunti manualmente)

- Slack
- Stripe
- Square
- **MCP custom** — qualunque server MCP che esponi (es. il nostro Supabase!). Questo è il modo in cui il pacchetto vede i tuoi dati custom.

## Come collegare Supabase via MCP al pacchetto

Questa è la parte importante per l'integrazione coi sub-agent custom in Claude Code.

1. In Cowork: Settings → Connectors → "Add custom MCP".
2. Inserisci:
   - **URL**: lo stesso `SUPABASE_URL` di `.env`.
   - **Auth**: la stessa `SUPABASE_SERVICE_ROLE_KEY` di `.env`.
3. Dai un nome al connettore (es. "Studio DB").
4. Salva.

Da questo momento, i workflow del pacchetto che leggono il "tuo DB" (es. `/monday-brief` quando cita "alert dalle note_interne") vedono Supabase via MCP, esattamente come fa Claude Code.

## Garanzie di sicurezza (di nuovo)

- **Permission inheritance**: il pacchetto NON vede mai più di quello che il tuo account collegato vede. Se un collaboratore non ha accesso a una cartella Drive col suo account, non lo vede neanche tramite Claude.
- **Approvazione umana obbligatoria** per qualunque azione esterna (invio email, pagamento, post). Niente è automatico.
- **Anthropic non si allena sui tuoi dati di business** nei piani Team/Enterprise. Garanzia contrattuale.

## Cosa fare quando un workflow non fa quello che vorresti

Tre opzioni in ordine di preferenza:

1. **Cambia il prompt dentro il workflow**: ogni comando accetta argomenti naturali. Es: `/monday-brief con focus solo sui clienti del settore retail`. Il workflow obbedisce.
2. **Usa uno skill da solo**: invece di lanciare il workflow grande, chiami lo skill singolo. Es: `/cash-flow per i prossimi 60 giorni`.
3. **Scrivi un sub-agent custom in Claude Code**: se la cosa che ti serve è strutturalmente diversa da quello che il pacchetto fa (es. parsare un tipo di documento italiano specifico), passa ad Agent View. Quella è la regola "quando A, quando B" del video.

## Cosa NON fare

- Non collegare TUTTI i connettori al primo onboard. Sicurezza+chiarezza ne soffrono. Aggiungili man mano.
- Non testare workflow che mandano email/pagamenti in produzione la prima volta. Sandbox prima.
- Non aspettarti che il pacchetto conosca le particolarità del diritto italiano (regimi forfettari, IVA agevolata, ecc.) al 100%. Quelle restano competenza dei tuoi sub-agent custom.
