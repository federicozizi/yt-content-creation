# Setup automatico — Claude Code, leggi qui

Sei stato lanciato dentro la cartella materiali del **Metodo A — Claude Code Agent Teams**. Tutto il necessario è già qui dentro al root: i 4 sub-agent in `.claude/agents/`, le settings in `.claude/settings.json`, il prompt orchestratore in `daily-brief.md`. Il tuo compito è solo: prerequisiti + configurare i competitor + primo test. ~3 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
bash verifica-prerequisiti.sh
```

Lo script controlla Node, Claude Code CLI, e la presenza dei file chiave. Se qualcosa manca, segnala all'utente cosa installare.

> Non fare `git init`: per il Metodo A non serve GitHub. Lo scheduling avviene tramite Anthropic Routines (cloud).

### 2. Configura i competitor

Apri `competitors.json`, mostralo all'utente, e aiutalo a sostituire i 3 placeholder coi suoi competitor reali. Per ognuno servono: `name`, `website`, `pricing_url`, `blog_url`, `linkedin_url`.

### 3. Test locale

Esegui il prompt contenuto in `daily-brief.md`:

- Crea il team di 4 teammates dalle definizioni in `.claude/agents/`
- Crea i 3 task A/B/C in parallelo per i watcher
- Crea il task D del synthesizer con dipendenza su A/B/C
- Aspetta il completamento e verifica che `briefs/<data-oggi>.md` esista

### 4. Schedulazione cloud (opzionale)

Quando il test locale è OK, suggerisci all'utente di seguire `docs/scheduling-routines.md` per creare la routine cloud Anthropic (gira ogni mattina alle 7, anche col PC spento, niente VPS).

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: la cartella materiali stessa È il progetto. Tutto è già qui.
- **Non rimuovere `.gitignore`** anche se non usiamo git: è un'abitudine di sicurezza.
- **Non fare git init**: per il Metodo A non serve. Lo scheduling è cloud.
- Tono diretto, conciso. Niente paragrafi accademici.
- Se qualcosa fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
