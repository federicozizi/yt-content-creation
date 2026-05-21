<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/docs/supabase-mcp-howto.md -->

# Supabase via MCP — how-to dettagliato

Come funziona il connettore MCP di Supabase, cosa fare quando si rompe, e quali sono le buone pratiche di sicurezza.

## Cos'è MCP

**MCP** = Model Context Protocol. È un protocollo aperto pubblicato da Anthropic nel novembre 2024 che permette ai modelli AI di parlare con servizi esterni in modo strutturato.

Funziona così:
- Un servizio (Supabase, GitHub, Slack, ecc.) espone un "MCP server" — un piccolo processo che dichiara: "ecco le funzioni che posso fare, ecco i parametri, ecco i tipi di output".
- Claude (Code o Cowork) si collega al server e usa quelle funzioni come tool aggiuntivi, esattamente come usa Read/Write/Bash.

Per noi piccoli imprenditori: vuol dire che Claude può fare query SQL sul tuo DB senza che tu scriva codice di middleware.

## Setup del connettore Supabase

### 1. Installa il server MCP Supabase

Anthropic e Supabase distribuiscono il server ufficiale come pacchetto npm:

```bash
claude mcp add supabase
```

Il comando aggiunge una voce nel registro MCP di Claude Code (`~/.claude/mcp.json` di solito, o nel progetto se hai un `.claude/mcp.json` come in questa cartella materiali).

### 2. Configura le credenziali

Il server ha bisogno di:
- `SUPABASE_URL`: il Project URL del tuo progetto (es. `https://abcdefghij.supabase.co`)
- `SUPABASE_SERVICE_ROLE_KEY`: la service role key (segreta!)

In questa cartella, le mettiamo in `.env` e il file `.claude/mcp.json` le pesca via `${SUPABASE_URL}` e `${SUPABASE_SERVICE_ROLE_KEY}`. Vedi `.env.example` per il template.

### 3. Verifica

```bash
claude
> "Lista le tabelle nel DB Supabase"
```

Output atteso: lista delle tabelle + numero righe.

Se vedi un errore tipo "MCP server not found" o "connection refused", probabilmente:
- L'`SUPABASE_URL` è sbagliato (es. hai messo l'URL del dashboard `https://supabase.com/dashboard/project/xxxxx` invece dell'URL API `https://xxxxx.supabase.co`).
- La service role key è scaduta o revocata.
- Il progetto Supabase è "Paused" (succede se è inattivo per >7 giorni nel piano free). Riattivalo dal dashboard.

## Cosa può fare il server MCP Supabase

Le funzioni esposte (al momento di questo video):

- **list_tables**: elenco tabelle del DB
- **execute_sql**: esegue una query SQL (sia SELECT che INSERT/UPDATE/DELETE)
- **list_migrations**: storico migrazioni applicate
- **apply_migration**: applica una migrazione (versionata)
- **list_extensions**: elenco extensions Postgres attive
- **generate_typescript_types**: genera tipi TS dallo schema (utile se hai un frontend)
- **list_branches**, **create_branch**, **merge_branch**: gestione branch Supabase (feature beta)
- **get_advisors**: suggerimenti automatici di Supabase su sicurezza/performance
- **get_logs**: log del progetto

In Claude Code, queste funzioni appaiono come tool del tipo `mcp__supabase__<nome>`. Gli agenti custom che dichiarano `tools: mcp__supabase` ne ereditano l'accesso.

## Buone pratiche di sicurezza

### Service Role Key vs Anon Key

La **service role key** bypassa Row Level Security (RLS) e ha accesso totale al DB. Usala SOLO per agenti backend (come il nostro Claude Code locale), MAI per applicazioni esposte al pubblico.

La **anon key** rispetta RLS e dà accesso solo a ciò che le policy permettono. Usala se vuoi che Claude veda solo un subset dei dati (es. solo le tabelle pubbliche, solo il cliente loggato).

**Per il setup di questo video**: service role key va bene perché siamo in un ambiente locale dello studio. Ma se metterai Claude su un server condiviso o farai vedere lo schermo a terzi, considera di passare a anon key + RLS appropriate.

### Mai committare .env

`.gitignore` in questa cartella esclude già `.env` (con eccezione di `.env.example`). Verifica con:

```bash
git check-ignore .env
```

Output atteso: `.env` (significa che è ignorato). Se non lo è, controlla il `.gitignore`.

### Cosa fare se hai esposto la service role key per sbaglio

(Es: l'hai messa in un commit pubblico, in uno screenshot social, l'hai incollata in un canale Slack sbagliato.)

1. **Subito**: Supabase Dashboard → Settings → API → "Reset service_role secret". La vecchia chiave smette di funzionare immediatamente.
2. **Aggiorna `.env`** col nuovo valore.
3. **Verifica i log Supabase** (Dashboard → Database → Logs) per query sospette negli ultimi giorni — se trovi traffico che non riconosci, valuta di esportare lo schema, rimuovere il progetto e ricrearlo.

## Query frequenti per il caso "studio commercialisti"

Esempi che puoi dare direttamente a `claude` una volta che MCP funziona:

```
"Mostrami tutti i clienti in regime forfettario che hanno fatturato oltre l'80% del limite"

"Inserisci un nuovo cliente con ragione_sociale 'Studio Rossi SRL', P.IVA '12345678901', regime_fiscale_codice 'ordinario'"

"Per il cliente con ID X, aggiungi una nota interna di tipo 'commento' con testo 'rivedere posizione fiscale per il 2027' e autore 'mario'"

"Quante scadenze custom abbiamo in arrivo nei prossimi 7 giorni?"
```

Tutte queste girano via MCP — niente SQL scritto a mano, Claude lo genera lui.
