<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/esempio-output.md -->

# Esempio: come si presenta una giornata-tipo dopo che il sistema gira

Lunedì mattina, studio commercialisti "Studio Demo & Associati". I 3 componenti sono attivi da una settimana. Ecco cosa vede l'utente in 3 schermate.

## Schermata 1 — Claude Cowork: `/monday-brief`

```
> /monday-brief

📊 Monday Brief — Lunedì 18 maggio 2026

💰 Cassa attuale: €12.450 (fonte: QuickBooks)
📑 Fatture in scadenza questa settimana: 4 (totale €3.200)
🆕 Lead nuovi nel CRM: 7 (fonte: HubSpot)

⚠️ Alert dal DB studio (Supabase MCP):
  • Cliente "Bianchi SRL" arrivato all'83% del limite forfettario
    (alert da regime-checker, 2 giorni fa, non ancora letto)
  • Cliente "Verdi Costruzioni" arrivato al 91% del limite forfettario
    (alert da regime-checker, 5 giorni fa)
  • 3 scadenze custom dello studio nei prossimi 7 giorni
    (alert da scadenza-allerter di stamattina)

📌 Suggerimento prossima azione:
  Chiamare per primo "Mario Bianchi" (lead caldo nel CRM da 3 giorni)
  e pianificare un appuntamento con "Verdi Costruzioni" per discutere
  il cambio regime fiscale per il 2027.

OK a procedere con l'invio del riepilogo email ai soci dello studio?
[ Approva ] [ Modifica ] [ Annulla ]
```

L'utente clicca **Approva**. Parte un'email interna ai 3 soci dello studio con il brief.

## Schermata 2 — Claude Code (Agent View): regime-checker

```
$ claude agents

  ┌─────────────────────────────────────────────────────────────────┐
  │  AGENT VIEW — claude-code-piccoli-business                       │
  ├─────────────────────────────────────────────────────────────────┤
  │                                                                  │
  │  ▼ document-classifier      [ready]                              │
  │     Classifica documenti italiani ambigui                       │
  │                                                                  │
  │  ▼ regime-checker           [running] — partito 09:15            │
  │     Controlla soglie regime fiscale                              │
  │                                                                  │
  │  ▼ scadenza-allerter        [completed] — terminato 09:08        │
  │     Report scadenze in logs/scadenze-2026-05-18.md               │
  │                                                                  │
  └─────────────────────────────────────────────────────────────────┘
```

Apri lo stream di `regime-checker`:

```
[09:15:03] Inizio esecuzione regime-checker
[09:15:04] Query v_clienti_vicini_limite via MCP Supabase…
[09:15:05]   → 2 clienti restituiti
[09:15:05] Cliente "Bianchi SRL": 83% del limite forfettario
[09:15:06]   Check duplicati ultimi 7gg → nessun alert recente
[09:15:06]   INSERT note_interne (tipo=alert_soglia, autore=agente:regime-checker)
[09:15:07] Cliente "Verdi Costruzioni": 91% del limite forfettario
[09:15:08]   Check duplicati ultimi 7gg → alert esistente di 5gg fa
[09:15:08]   SKIP — duplicato, non rigenero
[09:15:09] Fine esecuzione regime-checker
[09:15:09] Riepilogo: 2 clienti controllati, 1 alert nuovo, 1 saltato
[09:15:09] Log salvato in logs/regime-checker-2026-05-18.log
```

## Schermata 3 — Supabase: la riga appena inserita

Apri Table Editor → `note_interne` → ordina per `created_at` DESC. Prima riga:

| campo | valore |
|---|---|
| `id` | `f8a3b2c1-...` |
| `cliente_id` | `<id di Bianchi SRL>` |
| `tipo` | `alert_soglia` |
| `testo` | `Cliente Bianchi SRL arrivato a 83% del limite del regime forfettario. Considerare il passaggio anticipato.` |
| `autore` | `agente:regime-checker` |
| `flag_per_invoice_chaser` | `null` |
| `letto` | `false` |
| `created_at` | `2026-05-18 09:15:06+00` |

Più tardi, quando lanci `/invoice-chaser` in Cowork, il pacchetto Anthropic farà una query a questa stessa tabella (via il connettore MCP custom configurato in Cowork Settings) e vedrà queste righe per modulare i solleciti.

## Cosa NON vedi (e va bene così)

- **Nessuna email inviata in automatico**. Il `/monday-brief` ha proposto un riepilogo interno; tu l'hai approvato. Il `/invoice-chaser` di più tardi proporrà 3 email di sollecito; tu deciderai se inviarle.
- **Nessuna modifica al regime fiscale** dei clienti. regime-checker ha solo generato un alert. Il cambio regime è una decisione del commercialista titolare.
- **Nessuna scrittura su QuickBooks o HubSpot dagli agenti custom**. I tool del pacchetto le possono fare (con approvazione umana). Gli agenti custom toccano solo Supabase.

## Il punto di vista del cliente esterno (es. "Bianchi SRL")

Il cliente:
1. Riceve un'email dal commercialista che gli chiede di fissare un appuntamento per discutere il cambio regime fiscale.
2. NON riceve un'email automatica. Il commercialista ha deciso di scriverla manualmente dopo aver letto l'alert.
3. Vede uno studio organizzato, sul pezzo, proattivo.

L'infrastruttura è invisibile. Quello che il cliente sente è solo "lo studio si è ricordato di me prima che fossi io a chiederglielo".
