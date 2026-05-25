# Claude for Small Business — La mia settimana operativa, raccontata in 3 momenti

> Materiali del video YouTube **"Le quindici automazioni di Claude per piccole imprese: quello che paghi gia' senza saperlo"**.
> Trovi qui un riassunto fedele del pacchetto, una guida step-by-step per attivarlo, e checklist pratiche per i workflow che uso davvero nella mia settimana lavorativa.

---

## In 30 secondi — di che si tratta

Il 13 maggio 2026 Anthropic ha rilasciato dentro Claude Cowork un pacchetto che si chiama **Claude for Small Business**. E' pensato per piccole imprese, freelance, consulenti — chi non lavora con codice ma con clienti, fatture, contratti, email.

Cosa c'e' dentro: **quindici automazioni gia' costruite** (le chiamano "workflow"), con nomi tipo `/monday-brief`, `/invoice-chaser`, `/contract-review`. Sono comandi che digiti in chat e che fanno cose specifiche — non chiedi a Claude di pensare da zero, gli chiedi di eseguire un protocollo gia' pensato.

E sette **connettori** per parlare coi tool che usi davvero: HubSpot, QuickBooks, Google Workspace, Microsoft 365, PayPal, DocuSign, Canva.

Risultato pratico: in venti minuti hai automazioni che ti tolgono ore di lavoro a settimana. E le paghi gia' col tuo abbonamento Pro o Max — non costano extra. Probabilmente non sapevi che esistessero.

---

## Cosa ti serve prima di iniziare

- [ ] **Claude Pro o Max** — [https://claude.ai/upgrade](https://claude.ai/upgrade) — il pacchetto Small Business vive qui
- [ ] Almeno **un account aziendale** dei sette supportati: HubSpot, Google Workspace, QuickBooks, Microsoft 365, PayPal, DocuSign, Canva. Per partire bastano 1-2 tool — io nel video uso **HubSpot free tier** + **Google Workspace personale**.
- [ ] **VS Code** — [https://code.visualstudio.com](https://code.visualstudio.com) — opzionale, per leggere i file di questa cartella
- [ ] 20 minuti

---

## Quick start (5 passi per chi va veloce)

1. Vai su [https://claude.ai/cowork](https://claude.ai/cowork) e cerca il pacchetto **Small Business**. Click **Activate**.
2. Apri il pannello **Connectors** e collega almeno **HubSpot** + **Google Workspace** (procedura OAuth: 30 secondi per ognuno, sempre con chiavi di lettura).
3. Apri una nuova chat Cowork. Digita `/monday-brief`. Claude legge calendario + email + HubSpot e ti consegna il riassunto della settimana.
4. Quando arriva un lead nuovo, digita `/lead-qualifier`. Claude lo arricchisce con informazioni pubbliche sul cliente potenziale.
5. Venerdi' sera, prima di chiudere, digita `/invoice-chaser`. Claude prepara le bozze di sollecito per i clienti in ritardo (le salva come bozze, non invia).

Se sei alle prime armi con Claude Cowork, vai alla **guida completa** qui sotto.

---

## Guida completa passo-passo

### Step 1 — Capire dove vivono i quindici workflow (Cowork, non Code)

Prima di toccare il setup, una nota che evita confusione. Esistono due Claude per il lavoro: **Claude Code** e **Claude Cowork**. Sono cugini, fanno cose diverse.

- **Claude Code** e' lo strumento da terminale — gira sul tuo PC e lavora coi file, col codice, con la struttura tecnica del tuo progetto. Audience: developer, power user.
- **Claude Cowork** e' l'ambiente di lavoro via chat collegato ai tuoi tool aziendali — HubSpot, QuickBooks, Gmail. Audience: team non-tecnici, freelance, PMI.

Il pacchetto Small Business — i quindici workflow — vive **dentro Cowork**, non dentro Code. La logica e' semplice: i workflow servono per parlare coi tool aziendali, e quei tool li raggiungi via Cowork.

Pratica: apri [https://claude.ai/cowork](https://claude.ai/cowork) dal browser. Se sei abituato a Claude Code col terminale, non confondere i due — i comandi tipo `/monday-brief` funzionano **solo in Cowork**. In Code ti dice "comando non trovato".

Cowork e' incluso nel tuo abbonamento Pro o Max. Niente costi aggiuntivi.

---

### Step 2 — Attivare il pacchetto Small Business

1. Apri [https://claude.ai/cowork](https://claude.ai/cowork). Loggati col tuo account Pro o Max.
2. Sidebar a sinistra -> **Packages** (in alcune versioni si chiama **Marketplace**).
3. Cerca **Small Business** nella lista. Vedi una card col logo.
4. Click sulla card. Si apre un riassunto:
   - 15 workflow (i comandi `/monday-brief`, `/invoice-chaser`, eccetera)
   - 15 skill (sono pacchetti di expertise che Claude usa automaticamente quando serve — non li vedi, lavorano dietro)
   - 7 connettori richiesti (puoi collegarne anche solo 1-2, gli altri quando ti servono)
5. Click **Activate**. E' gratis se hai gia' Pro o Max.
6. Badge verde "Active" appare sulla card.

Da questo momento, in qualsiasi nuova chat Cowork, hai a disposizione i quindici comandi. Ma sono "vuoti" finche' non colleghi almeno un connettore — perche' devono avere qualcosa da leggere e con cui lavorare.

---

### Step 3 — Collegare HubSpot e Google Workspace

Sempre dentro Cowork, sidebar -> **Connectors** (oppure direttamente [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)).

I sette connettori del pacchetto e cosa abilitano:

| Connettore | Workflow che abilita | Difficolta' setup |
|---|---|---|
| **HubSpot** | `/monday-brief`, `/invoice-chaser`, `/lead-qualifier`, `/run-campaign` | Facile (free tier OK) |
| **Google Workspace** | `/monday-brief`, `/meeting-followup`, tutti i workflow che producono email/calendar | Facile (account personale OK) |
| **Microsoft 365** | Stesso ruolo di Google Workspace se usi Outlook | Facile |
| **QuickBooks** | `/close-month`, `/invoice-chaser`, `/expense-categorizer` | Medio (serve account QuickBooks attivo) |
| **PayPal** | `/expense-categorizer`, `/close-month` | Facile |
| **DocuSign** | `/contract-review` (pre-signing) | Medio (account business) |
| **Canva** | `/run-campaign`, `/pitch-builder` | Facile (free tier OK) |

Per il video colleghiamo solo **HubSpot** + **Google Workspace**. Bastano per coprire 4-5 workflow su 15. Gli altri li aggiungi mano a mano che ti servono.

Procedura per ogni connettore:
1. Click sulla card del connettore -> **Connect**
2. Si apre la finestra OAuth del servizio (HubSpot, Google, ecc.)
3. **Sempre solo lettura la prima volta.** Stessa regola del nuovo stagista: prima vedi come si comporta, dopo gli dai anche le chiavi per scrivere.
4. Conferma -> torni a Cowork col connettore "Connected"

Per HubSpot (gratuito):
- Se non hai un account, crealo su [https://hubspot.com](https://hubspot.com) — free tier praticamente illimitato per gestire contatti
- Aggiungi 10-20 contatti realistici come prova (nome, email, magari settore e ultima interazione)
- Se hai gia' HubSpot attivo, collega quello — nessuna preoccupazione, Claude legge solo

Per Google Workspace:
- Funziona anche con un account Gmail personale
- Concedi accesso a Gmail (lettura), Calendar (lettura), Drive (lettura per i file allegati ai meeting)

---

### Step 4 — Lunedi' mattina con `/monday-brief`

Lunedi'. Apri Cowork. Una nuova chat. Digita:

```
/monday-brief
```

Cosa fa: Claude legge il tuo calendario della settimana, le email non lette degli ultimi sette giorni, e i deal/contatti recenti in HubSpot. Sintetizza tutto in un report con quattro sezioni:

- **Priorita' della settimana** — le 3-5 cose che davvero contano
- **Meeting in calendario** — con suggerimenti su cosa preparare per quelli importanti
- **Conversazioni pendenti** — clienti che aspettano risposta, follow-up da fare
- **Numeri della settimana scorsa** — quanti deal aperti, response time, KPI base

Tempo di elaborazione: 30-60 secondi. Risultato: una pagina markdown che puoi salvare, stampare, o lasciare aperta sul secondo schermo per la giornata.

**La prima volta** Claude ti chiedera' qualche dato di contesto: che lavoro fai, quali sono le tue priorita' tipiche, in che lingua vuoi il brief. Rispondi una volta — dopo le settimane successive partono autonome.

**Personalizzazione**: dopo il primo run, prova:
```
/monday-brief solo focus su vendite, tono italiano informale
```

Claude calibra. Le settimane successive seguono il nuovo tono.

---

### Step 5 — Mercoledi' pomeriggio, arriva un lead nuovo

Scenario: hai un sito web col form contatti. Mercoledi' pomeriggio arriva un lead nuovo — nome dell'azienda, email aziendale, eventualmente sito o LinkedIn. Prima della call, vorresti capire chi hai dall'altra parte senza spendere mezz'ora a googlare.

Salvi il contatto in HubSpot (basta nome + email + un campo "ultimo touch"). Poi su Cowork apri una chat e digita:

```
/lead-qualifier
```

Claude prende l'ultimo lead caricato in HubSpot (o gli dici esplicitamente quale) e fa il lavoro di **arricchimento**:

- Cerca il sito web aziendale, lo legge
- Stima settore, dimensione, fascia di fatturato
- Cerca presenza LinkedIn della persona contatto (se inferibile dall'email)
- Verifica se l'azienda ha presenza pubblica significativa (news recenti, recensioni)
- Calcola un **punteggio MQL/SQL** — quanto e' interessante come lead e perche'

Output: scheda di 1 pagina pronta per essere letta in 2 minuti prima della call. Sai con chi stai parlando, in che fase di vita e' l'azienda, dove andare a parare.

**Disclaimer onesto**: Claude lavora con informazioni pubbliche. Non e' un'agenzia di intelligence. Su aziende molto piccole o appena nate, l'output sara' magro — non e' colpa di Claude, sono informazioni che non esistono nemmeno in rete.

---

### Step 6 — Venerdi' sera, recupero crediti

Venerdi', diciassette e mezza. Stanno per chiudere. Prima di staccare, hai una mezz'ora per il recupero crediti — i clienti con fatture in ritardo da contattare. Su Cowork apri una chat e digita:

```
/invoice-chaser
```

Claude (con HubSpot collegato, oppure QuickBooks se lo usi per la contabilita') scansiona alla ricerca di fatture in stato "scaduto" o "non pagato". Per ognuna classifica per anzianita':

- 0-30 giorni
- 31-60 giorni
- 61-90 giorni
- 91+ giorni

E per ogni cliente genera una **bozza di email di sollecito** con tono calibrato in base all'anzianita':

- 15 giorni: tono cordiale, "promemoria gentile"
- 45 giorni: tono fermo, propone soluzioni (es. rateizzazione)
- 80+ giorni: tono di escalation, menziona conseguenze

Le bozze vengono salvate **nella cartella Drafts di Gmail** (o Outlook). Importante: **Claude non le invia**. Tu apri Gmail, rileggi una a una, eventualmente correggi qualche tono, e clicchi Invia tu.

Tempo che ti costa il lavoro tradizionale: 45-60 minuti per cinque-sei clienti. Tempo col workflow: 5 minuti per generare + 10 minuti per rivedere = 15 minuti. Recuperati 30 minuti, e — soprattutto — il lavoro si fa anche le settimane in cui non avresti avuto voglia di farlo.

---

### Step 7 — E gli altri 12 workflow?

I tre che hai visto sono quelli che io uso davvero ogni settimana. Gli altri dodici li trovi tutti documentati in `workflow-tutti.md` di questa cartella, organizzati per categoria. Cito i piu' utili per chi inizia:

- **`/contract-review`** — analisi pre-firma di un contratto PDF. Dodici punti di controllo standard. Per pre-screenare prima di mandarlo all'avvocato.
- **`/meeting-followup`** — dopo un meeting, da' a Claude le tue note e ti restituisce sommario + action item + bozza email di follow-up.
- **`/weekly-report`** — il fratello quantitativo del `/monday-brief`. Numeri della settimana per te o per il team.
- **`/close-month`** — chiusura contabile mensile. Riconcilia movimenti PayPal + QuickBooks, identifica anomalie.

Strategia che consiglio: NON collegare tutti i sette connettori subito. Aggiungi mano a mano. Mantieni l'attenzione sui pochi workflow che ti restituiscono il novanta percento del valore.

---

### Step 8 — Schedulare ricorrente con Claude Routines (opzionale ma potente)

Una volta che `/monday-brief` ti funziona bene manualmente, puoi schedularlo automatico — ogni lunedi' mattina, sandbox cloud Anthropic, niente PC da accendere.

1. Vai su [https://claude.ai/code/routines](https://claude.ai/code/routines)
2. Crea una nuova Routine:
   - Schedule: ogni lunedi' alle 07:30 ora italiana
   - Prompt: "Esegui /monday-brief con il mio contesto consueto e inviami il risultato via email"
3. Salva.

Risultato: ogni lunedi' alle 8 trovi il brief gia' nella casella mail. Hai delegato un pezzo del tuo lunedi' mattina al cloud Anthropic.

---

## Concetti spiegati semplici

- **Claude Cowork**: ambiente di lavoro Claude separato da Claude Code, pensato per chi non lavora con codice ma con tool aziendali. Vive su claude.ai/cowork.
- **Workflow (o slash command)**: comando che digiti in chat (es. `/monday-brief`) che innesca una sequenza di azioni precostruita. Sono "macro intelligenti" — fanno cose ben definite invece di "pensare da zero".
- **Skill**: pacchetto di expertise che Claude carica automaticamente quando serve. Es. la skill di "scrittura email commerciali in italiano" si attiva dentro `/invoice-chaser` senza che tu la richieda. Lavorano dietro le quinte.
- **Connector**: l'interruttore che colleghi una volta sola per dare a Claude accesso a un servizio. Click, autorizzazione OAuth, fine.
- **OAuth**: protocollo standard con cui un servizio (HubSpot, Google, ecc.) da' a Claude una chiave limitata senza che tu condivida la tua password.
- **Solo lettura / anche scrittura**: durante OAuth scegli cosa puo' fare Claude. Sempre solo lettura per cominciare.

---

## Riferimenti

- **Annuncio ufficiale Claude for Small Business**: [https://www.anthropic.com/news/claude-for-small-business](https://www.anthropic.com/news/claude-for-small-business)
- **Documentazione workflow**: dentro Cowork, sidebar -> Help -> Workflows
- **Lista connettori ufficiali**: [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)
- **HubSpot free tier**: [https://hubspot.com](https://hubspot.com)

---

## Dubbi o problemi?

- Commenta sotto il video YouTube — rispondo a tutti.
- Errore tipico: "Workflow not found" -> verifica di essere su [https://claude.ai/cowork](https://claude.ai/cowork) (NON su claude.ai normale) e che il pacchetto Small Business sia "Active".
- Errore connector: "Token expired" -> vai su Connectors, disconnetti e riconnetti. La chiave scade dopo periodi di inattivita'.

Buon lavoro.
