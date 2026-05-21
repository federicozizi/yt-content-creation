<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/docs/connettori-pacchetto-vs-custom.md -->

# Pacchetto pre-cotto vs sub-agent custom — quando usare cosa

La domanda ricorrente, quando hai messo in piedi i 3 componenti, è: "questa cosa la faccio col pacchetto Anthropic o con un sub-agent custom?"

Questa guida ti dà i criteri operativi.

## La regola in una frase

> **Se la cosa che devi fare la fanno anche gli altri piccoli business** del tuo settore o trasversalmente (paghe, fatture, briefing, chiusura mese, marketing) → **pacchetto**.
>
> **Se la cosa è specifica del tuo modello di business**, della tua nicchia, di una regola italiana, o dei tuoi dati custom in Supabase → **sub-agent custom**.

## I 5 criteri per decidere

### 1. La cosa esiste già come workflow del pacchetto?

Apri la lista dei 15 workflow (`docs/claude-for-small-business-howto.md`). Se trovi qualcosa che assomiglia: parti da lì. Lo eviti di reinventare la ruota, e Anthropic lo manterrà aggiornato.

### 2. La cosa usa dati che vivono solo in Supabase?

Esempio: il regime fiscale dei tuoi clienti, le note interne dello studio, le scadenze custom che ti sei tracciato tu.

→ **Sub-agent custom**. Il pacchetto vede QuickBooks, HubSpot, Gmail — non Supabase, a meno che tu non l'abbia collegato come MCP custom (vedi `claude-for-small-business-howto.md` sezione "Come collegare Supabase via MCP al pacchetto"). Anche dopo averlo collegato, il pacchetto NON ha la logica di business custom per il tuo settore — l'usa solo come lookup table.

### 3. La cosa ha regole italiane specifiche?

Esempio: clausole vessatorie ex art. 1341 c.c., soglie del forfettario, aliquote IVA agevolate per settori specifici, tasse di soggiorno per comune.

→ **Sub-agent custom**. Il pacchetto è generico e US-first. Le regole italiane specifiche te le devi scrivere.

### 4. La cosa coinvolge un'azione esterna?

Esempio: mandare email, fare pagamenti, pubblicare un post, firmare contratti.

→ **Pacchetto**, sempre. Il pacchetto ha l'integrazione OAuth pulita coi tool che fanno l'azione (Gmail, PayPal, ecc.) e soprattutto ha l'approvazione umana built-in. Scrivere un sub-agent custom che manda email è masochismo: devi gestire SMTP, deliverability, OAuth, ecc.

Se hai bisogno di logica custom PRIMA dell'invio (es. "leggi note Supabase per modulare il tono"): combina i due. Sub-agent custom prepara i dati su Supabase, il pacchetto legge da Supabase via MCP e fa l'invio.

### 5. La cosa è destinata a cambiare spesso?

Esempio: le regole di una promozione che cambia ogni 3 mesi, la struttura di un report che ti chiedono di rivedere ogni trimestre.

→ **Sub-agent custom**, perché lo modifichi tu in markdown in 30 secondi. Il pacchetto è meno flessibile su microaggiustamenti.

## Tabella di decisione (riassunto)

| Cosa devi fare | Pacchetto | Custom | Entrambi |
|---|---|---|---|
| Chiusura mese contabile standard | ✅ /close-month | | |
| Sollecito fatture standard | ✅ /invoice-chaser | | |
| Sollecito fatture con tono diversificato in base a note Supabase | | | ✅ Custom riempie Supabase, pacchetto legge e invia |
| Briefing del lunedì | ✅ /monday-brief | | |
| Classificare un tipo di scontrino italiano ambiguo | | ✅ document-classifier | |
| Controllare soglia forfettario | | ✅ regime-checker | |
| Scadenze custom dello studio (rinnovo albo, ecc.) | | ✅ scadenza-allerter | |
| Campagna marketing con grafiche | ✅ /run-campaign | | |
| Campagna marketing con regole di branding tue | | | ✅ Custom controlla guidelines, pacchetto esegue |
| Revisione contratto generico | ✅ /contract-review | | |
| Revisione contratto con clausole vessatorie italiane | | | ✅ Pacchetto fa la revisione formale, custom controlla le clausole specifiche |
| Cash flow forecast | ✅ /cash-flow | | |
| Calcolo tasse di soggiorno per comune | | ✅ Custom | |

## Pattern di combinazione comuni

### Pattern 1: "Custom arricchisce, pacchetto esegue"

- Sub-agent custom legge documenti caricati e arricchisce Supabase con classificazioni/note.
- Pacchetto (es. `/close-month`) legge Supabase + tool standard e produce l'output finale.

Esempio: document-classifier classifica gli scontrini ambigui → /close-month li conteggia correttamente nel totale deducibile.

### Pattern 2: "Custom controlla, pacchetto bloccato"

- Sub-agent custom controlla che una condizione sia vera prima che un workflow del pacchetto parta.
- Se la condizione è falsa, blocca o modifica il comportamento del pacchetto.

Esempio: regime-checker scrive `flag_per_invoice_chaser = 'non_sollecitare'` in note_interne se un cliente ha appena superato il limite → quando lanci /invoice-chaser, il pacchetto legge il flag e salta quel cliente.

### Pattern 3: "Pacchetto schedulato, custom on-demand"

- I workflow del pacchetto girano a frequenza fissa (lunedì mattina, fine mese).
- I sub-agent custom girano quando ti servono, da Agent View, con un click.

Esempio: /monday-brief automatico ogni lunedì alle 8, scadenza-allerter on-demand prima di una riunione di studio.

## Cosa NON combinare

- **Non duplicare logica**: se /close-month già sa chiudere il mese, non scrivere `close-month-custom.md`. Modifica invece il prompt che dai a /close-month con istruzioni aggiuntive.
- **Non bypassare l'approvazione umana**: se hai un sub-agent custom che manda email senza passare dal pacchetto, ti stai facendo male da solo. Passa sempre dai tool del pacchetto per le azioni esterne.
- **Non mettere logica di business in entrambi i posti**: se la regola "il cliente Bianchi non si solleciterebbe" sta sia nel pacchetto come prompt-rule sia nel sub-agent come flag su Supabase, prima o poi divergeranno. Decidi UN posto, lì la metti, l'altro la legge.
