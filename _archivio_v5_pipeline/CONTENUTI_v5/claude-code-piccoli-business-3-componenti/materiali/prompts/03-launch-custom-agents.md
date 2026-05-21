<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/prompts/03-launch-custom-agents.md -->

# Prompt 03 — Lanciare gli agenti custom via Agent View

Questo step si svolge in **Claude Code** dentro la cartella `materiali/`. Lancia gli agenti custom dello studio in parallelo.

## Prerequisiti

- Step 1 completato (Supabase MCP funzionante).
- Step 2 idealmente completato, ma non obbligatorio: gli agenti custom lavorano su Supabase indipendentemente dal pacchetto Anthropic.

## Setup

```bash
cd materiali
claude
```

E incolla:

```
Vediamo gli agenti custom in azione. Prima di lanciarli, voglio capire cosa c'è.

PASSAGGI:

1. Mostra l'elenco dei sub-agent
   - Lista i file in .claude/agents/ con il loro nome (dal frontmatter) e la
     descrizione (sempre dal frontmatter).
   - Atteso: document-classifier, regime-checker, scadenza-allerter.

2. Apri Agent View
   - Spiega all'utente: "Adesso ti faccio vedere la dashboard. Aprila tu in un
     altro terminale col comando: claude agents. Vedrai i 3 agenti elencati,
     ognuno in stato 'ready'. Da lì potresti lanciarli con un click. Io invece
     te li lancio direttamente da questa sessione per farti vedere l'output."
   - Conferma che l'utente ha visto la dashboard (o accetta di skippare e
     procedere via questa sessione).

3. Lancia regime-checker (è il più semplice e veloce da vedere in azione)
   - Esegui le istruzioni del file .claude/agents/regime-checker.md.
   - Usa il connettore MCP Supabase per la query sulla view
     v_clienti_vicini_limite.
   - Per ogni cliente trovato, fai l'INSERT in note_interne come da
     istruzioni del sub-agent.
   - Mostra all'utente: quante righe ha trovato la view, quanti alert hai
     generato, quanti hai saltato per evitare duplicati negli ultimi 7 giorni.

4. (Opzionale) Lancia scadenza-allerter in parallelo
   - Se l'utente vuole vedere il parallelismo: lancia anche scadenza-allerter
     "in coda" dopo regime-checker (i sub-agent in Claude Code sono asincroni
     ma non veri thread paralleli quando lanciati da CLI; per vero parallelismo
     usa la dashboard `claude agents` o il Task tool).
   - Mostra il report markdown generato in logs/scadenze-YYYY-MM-DD.md.

5. document-classifier — lascia per quando hai documenti veri
   - Spiega all'utente: "document-classifier ha bisogno di documenti caricati
     dai clienti in Drive (collegato via il pacchetto Small Business). Per
     testarlo simulato, puoi passargli del testo di una fattura finta. Ma il
     suo uso vero è in produzione, quando il pacchetto Anthropic ti notifica
     'arrivato file da cliente X', tu inneschi document-classifier su quel
     file. Vedi prompts/04-integrazione-end-to-end.md per il flusso completo."

6. Mostra cosa è successo
   - Fai una query Supabase per leggere note_interne degli ultimi 5 minuti,
     ordinate per created_at DESC. Mostra le righe nuove generate dagli agenti.
   - Atteso: alcune righe con autore = 'agente:regime-checker' o
     'agente:scadenza-allerter'.

REGOLE:

- Non modificare i file dei sub-agent durante l'esecuzione. Se vedi un bug
  nelle istruzioni, fermati e segnalalo all'utente.
- Non lanciare gli agenti più di una volta per sessione senza permesso —
  altrimenti rischi di duplicare gli alert (anche se le istruzioni dei
  sub-agent prevedono la deduplicazione, meglio essere espliciti).
- Non eseguire azioni esterne (email, file caricati altrove, ecc.) — i
  sub-agent custom scrivono SOLO su Supabase.

Procedi.
```
