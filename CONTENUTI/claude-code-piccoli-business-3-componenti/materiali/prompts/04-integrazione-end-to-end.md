<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/prompts/04-integrazione-end-to-end.md -->

# Prompt 04 — Orchestrazione end-to-end dei 3 componenti

Questo prompt mostra il "lunedì mattina tipico" dello studio commercialisti — il punto in cui tutti e 3 i componenti lavorano insieme.

## Prerequisiti

- Step 1, 2, 3 completati e funzionanti separatamente.
- Almeno qualche cliente in `clienti` su Supabase con `regime_fiscale_codice` e `fatturato_anno_corrente` popolati (per far girare regime-checker e produrre alert reali).
- Pacchetto Claude for Small Business attivo in Cowork, con almeno QuickBooks (sandbox) e Google Workspace collegati.

## Flusso

Il flusso alterna **Cowork (browser)** e **Claude Code (terminale)**, perché il pacchetto vive in Cowork e gli agenti custom vivono in Code. Il ponte è Supabase via MCP, leggibile da entrambi.

### Step A — In Cowork (browser)

Apri Cowork, nuova chat, digita:

```
/monday-brief
```

Output atteso: riassunto operativo del lunedì che include:
- Cassa attuale (letta da QuickBooks)
- Fatture in scadenza questa settimana (QuickBooks)
- Lead nuovi nel CRM (HubSpot se collegato, altrimenti la riga viene omessa)
- **+ Alert dalle note_interne di Supabase**, perché il pacchetto legge anche il tuo DB custom via MCP

Verifica nell'output che ci siano righe del tipo:
> ⚠️ 2 clienti vicini al limite del forfettario (alert da regime-checker della settimana scorsa)

Se non vedi righe da Supabase, il pacchetto potrebbe non avere ancora il connettore MCP Supabase configurato a livello workspace Cowork. Se è il tuo caso: in Cowork → Settings → Connectors → Add custom MCP → URL e key di Supabase (stessi di .env). Anthropic supporta MCP custom nei workspace Team da maggio 2026.

### Step B — In Claude Code (terminale)

Apri il terminale, dentro `materiali/`:

```bash
claude
```

E incolla:

```
Lancia regime-checker e scadenza-allerter in sequenza, come faresti il lunedì
mattina prima della riunione di studio.

Dopo:
1. Mostra il report di scadenza-allerter (file logs/scadenze-YYYY-MM-DD.md).
2. Mostra quante note_interne nuove ha generato regime-checker in totale.

Procedi.
```

Aspetta che finisca. Vai a controllare in Supabase Table Editor che `note_interne` abbia le righe nuove generate.

### Step C — Di nuovo in Cowork

Torna in Cowork, digita:

```
/invoice-chaser
```

Il pacchetto:
1. Legge da QuickBooks le fatture insolute oltre 30 giorni.
2. **Per ogni cliente con fattura insoluta, prima di scrivere l'email controlla note_interne su Supabase** cercando righe con `flag_per_invoice_chaser` non-null per quel cliente.
3. Se trova `flag_per_invoice_chaser = 'non_sollecitare'` → salta quel cliente.
4. Se trova `flag_per_invoice_chaser = 'sollecitare_modo_morbido'` → adatta il tono.
5. Ti propone le email risultanti.

**NON cliccare "Approve" se sei in produzione** — fermati a leggere quello che proporrebbe, decidi se va bene, e solo allora invialo. Per il test, lascia le email proposte senza inviarle.

### Step D — Verifica integrazione

Il punto di questo step è dimostrare che **il pacchetto Anthropic ha letto Supabase**. Per verificarlo:

1. Prendi un cliente dal report `/invoice-chaser`.
2. Vai in Supabase Table Editor → `note_interne` → filtra per quel `cliente_id` con `flag_per_invoice_chaser` non-null.
3. Conferma che il tono dell'email proposta dal pacchetto sia coerente con il flag (se "non_sollecitare", il cliente NON doveva essere nell'elenco; se "sollecitare_modo_morbido", il testo deve essere meno aggressivo del default).

Se la coerenza c'è: **i 3 componenti si parlano**. Hai un'infrastruttura, non 3 tool slegati.

## Cosa segna che il flusso funziona

- `/monday-brief` cita righe sia da QuickBooks (cassa) sia da Supabase (alert).
- regime-checker scrive in `note_interne` senza duplicare.
- `/invoice-chaser` legge `flag_per_invoice_chaser` da Supabase e modula i testi.
- Tutti gli output finali (email, report) passano dall'approvazione umana — niente azione automatica.

## Cosa fare se qualcosa non si parla

- **Pacchetto non vede Supabase**: aggiungi MCP custom in Cowork (Settings → Connectors).
- **Agenti custom non scrivono note_interne**: verifica che `.env` sia presente e che `claude mcp add supabase` sia stato eseguito con successo. Test diretto: `claude` + "fai un INSERT di test in note_interne".
- **Pacchetto e agenti scrivono in modo incoerente** (es. duplicano gli alert): in genere è un problema di deduplicazione nel sub-agent custom. Vedi le istruzioni di deduplicazione in `.claude/agents/regime-checker.md`.
