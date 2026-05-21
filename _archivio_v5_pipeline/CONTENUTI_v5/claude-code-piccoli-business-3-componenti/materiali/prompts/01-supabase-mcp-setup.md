<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/prompts/01-supabase-mcp-setup.md -->

# Prompt 01 — Setup Supabase via MCP connector

Questo prompt si usa **dentro la cartella `materiali/`**, lanciando `claude` e incollandolo subito dopo. Claude Code esegue tutta la procedura, guidandoti dove serve un input umano (creazione progetto Supabase, copia delle chiavi).

## Quando usarlo

Subito, prima di tutti gli altri. Senza Supabase + MCP nessun sub-agent custom può girare.

## Setup

```
cd materiali
claude
```

Poi incolla il prompt sotto.

---

## PROMPT

```
Setup completo del primo componente: Supabase via MCP connector.

CONTESTO:
Stiamo montando l'infrastruttura "Claude Code per piccoli business — 3 componenti".
Componente 1 = database Supabase via connettore MCP, dove finiranno i dati CUSTOM
dello studio (clienti, regimi fiscali, scadenze custom, note interne).

PASSAGGI:

1. Verifica che lo schema sia presente
   - Conferma l'esistenza di ./schema-aziendale.sql in questa cartella materiali.
   - Aprilo brevemente e mostra all'utente le 4 tabelle definite (clienti,
     regimi_fiscali, scadenze_custom, note_interne) + le 2 viste comode.

2. Guida l'utente alla creazione del progetto Supabase
   - Spiegagli: "vai su supabase.com, crea un account se non ce l'hai (gratis),
     click su 'New project', dai un nome (es. 'studio-demo' o il nome del tuo
     studio), regione 'Frankfurt' o 'eu-central-1' se sei in Europa, password
     del DB salvata in un gestore di password (non in chiaro)".
   - Attendi conferma che il progetto è stato creato.

3. Carica lo schema
   - Spiega: "pannello Supabase → SQL Editor → New query → incolla TUTTO il
     contenuto di schema-aziendale.sql → click su Run".
   - Attendi conferma che ha visto le 4 tabelle in Table Editor.

4. Configura le credenziali in .env
   - Verifica che esista .env (se no, copialo da .env.example).
   - Chiedi all'utente:
     a) "Vai in Settings → API del tuo progetto Supabase, copia il Project URL,
        incollalo qui (lo metto io in .env, non in chiaro a video)"
     b) "Stessa pagina, copia la service_role key. ⚠️ Questa chiave dà
        accesso totale al DB, non condividerla mai con nessuno e non
        committarla."
   - Salva i due valori in .env nelle variabili SUPABASE_URL e
     SUPABASE_SERVICE_ROLE_KEY. Conferma il salvataggio senza ri-stampare i
     valori a schermo.

5. Installa il connettore MCP Supabase
   - Verifica che ./.claude/mcp.json esista (è già nella cartella materiali).
   - Esegui in shell:
     claude mcp add supabase
   - Se il comando chiede URL e key interattivamente, prendi i valori da .env.
   - Se il setup è già stato fatto in passato (esistono già le voci nel
     registro MCP di Claude Code), conferma all'utente e procedi al test.

6. Test del connettore
   - Esegui mentalmente (come se fossi una nuova sessione Claude):
     "mostrami le tabelle del DB Supabase e quante righe hanno"
   - Mostra il risultato. Atteso: 4 tabelle, di cui regimi_fiscali con 5 righe
     (dal seed), le altre 3 con 0 righe.
   - Se vedi le 4 tabelle: ✅ Step 1 completo. Riporta il fatto all'utente.
   - Se vedi errori: diagnostica (chiave sbagliata? URL sbagliato? progetto
     ancora in inizializzazione?) e proponi il fix.

7. Prossimo passo
   - Avvisa l'utente: "Step 1 fatto. Step 2 è l'attivazione di Claude for
     Small Business dentro Claude Cowork — non è una cosa che faccio io,
     la fai tu nel browser. Apri prompts/02-claude-cowork-smb-onboard.md
     per le istruzioni quando sei pronto."

REGOLE:

- Non stampare mai la service_role key a schermo dopo averla salvata.
- Non creare cartelle progetto separate: questa cartella materiali È IL
  progetto, lavoriamo qui dentro.
- Se qualcosa fallisce, mostra l'errore e proponi il fix. Non ripartire da
  zero senza dirlo all'utente.

Procedi.
```
