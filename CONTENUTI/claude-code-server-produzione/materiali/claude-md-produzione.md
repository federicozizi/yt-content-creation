# CLAUDE.md di esempio per Claude Code in produzione (scraper prezzi)

Questo file e' la "costituzione" del progetto. Quando Claude Code parte sul server, lo legge per primo, e tutto cio' che fa segue queste regole.

Copia questo intero file come `CLAUDE.md` nella cartella del tuo progetto sul VPS.

---

```markdown
# Scraper Prezzi Competitor - Production CLAUDE.md

Sistema di scraping notturno che monitora 3 siti competitor e segnala variazioni prezzi.
Gira su VPS DigitalOcean, schedulato via cron alle 04:00 ogni notte.

## REGOLE OPERATIVE (NON NEGOZIABILI)

### Regola 1 - Azioni distruttive vietate
NON eseguire mai:
- `rm`, `rmdir`, `mv` su file fuori da `/home/claude/scraper/` e `/var/log/claude-scraper.log`
- `sudo` qualsiasi comando (l'utente claude NON ha sudo in produzione)
- `chmod`, `chown` su file di sistema
- Comandi di rete come `iptables`, `ufw`, `nc`
- Modifica di crontab, systemd, file in `/etc/`

Se ti viene chiesto di fare una di queste cose, rifiuta esplicitamente e scrivi nel log:
`REFUSED: <comando> per regola di produzione`

### Regola 2 - Sempre log
Ogni esecuzione, prima di fare qualsiasi cosa, apri il file `/var/log/claude-scraper.log` in append e scrivi:
```
=== RUN START <timestamp ISO> ===
Trigger: cron / manual / dry-run
Goal: <descrizione goal>
```

Alla fine, indipendentemente da successo/fallimento:
```
=== RUN END <timestamp ISO> | status: <success|partial|failed> | comandi eseguiti: <N> ===
```

Tra inizio e fine, ogni decisione importante (es. "ho deciso di saltare il sito X perche' risponde 503", "ho trovato variazione prezzo > 5% per prodotto Y") va loggata.

### Regola 3 - Mai dati personali nei log
I log finiscono su disco e potrebbero essere consultati. Nei log:
- ✅ OK: URL visitati (sono pubblici)
- ✅ OK: prezzi e variazioni
- ✅ OK: errori tecnici
- ❌ NO: contenuti di email
- ❌ NO: API key, token, password (mai)
- ❌ NO: dati personali di clienti

### Regola 4 - Dry-run mode
Se ti viene passato il flag `--dry-run`, esegui TUTTA la logica ma NON:
- Scrivere nel database
- Inviare email
- Modificare file fuori dalla cartella `/tmp/`

In dry-run, scrivi nel log un riassunto di "cosa avrei fatto" per ogni operazione skippata.

### Regola 5 - Budget protection
Stima il consumo di token a inizio esecuzione (in base a quanti siti devi scrappare e a quante chiamate WebFetch sono necessarie). Se la stima supera 100k token totali, scrivi nel log un alert:
`WARNING: stima consumo elevato (X token), considera ottimizzazione`
E procedi.

Se durante l'esecuzione ricevi un errore HTTP 429 (rate limit) dall'API Anthropic, **ferma immediatamente** e scrivi nel log:
`ABORT: rate limit Anthropic. Eseuzione fermata per protezione budget.`

## STRUTTURA PROGETTO

```
/home/claude/scraper/
|-- CLAUDE.md                 (questo file)
|-- scraper-prompt.md         (prompt operativo del task)
|-- competitors.json          (lista URL e prodotti chiave)
|-- prezzi.db                 (database SQLite con storia prezzi)
|-- last_run_state.json       (stato dell'ultima esecuzione)
`-- reports/
    `-- YYYY-MM-DD.md         (report giornaliero, generato dal task)
```

## TOOL DISPONIBILI

- `WebFetch` - per scaricare pagine HTML dei competitor
- `Bash` (limitato dalla Regola 1) - per interagire col database SQLite, per inviare email via `mail` command
- `Read`, `Write` - per file di stato e report

NON sono disponibili:
- `Edit` - perche' modificare file in produzione e' rischioso, sempre meglio scrivere file nuovi
- Tool MCP esterni - aggiungerli solo se davvero necessari

## CONTESTO DI BUSINESS

Cliente: e-commerce di articoli sportivi. Ha 3 competitor diretti che bisogna monitorare.
Prodotti chiave: 20 prodotti per categoria, totale 60 prodotti monitorati.
Sensibilita': variazioni > 5% sono interessanti. Variazioni > 10% sono URGENTI.

## QUANDO RIFERIRE A UN UMANO

Se durante l'esecuzione succede una di queste cose, NON cercare di risolvere autonomamente — scrivilo nel report come `BLOCKING ISSUE`:

- Un sito competitor cambia struttura HTML radicalmente (i selettori non funzionano piu')
- Errori HTTP 5xx persistenti per piu' di 3 tentativi
- Variazioni di prezzo > 50% (sospette: o e' un errore di parsing, o e' una promozione enorme da verificare)
- Il database SQLite non risponde

Il report con `BLOCKING ISSUE` viene letto da un umano la mattina dopo. Tu non devi risolvere magicamente — devi solo segnalare bene.
```

---

## Personalizzazione

Per adattare questo CLAUDE.md al tuo caso d'uso (es. non scraper ma altro task in produzione):

1. **Sezione "STRUTTURA PROGETTO"**: aggiorna i path e i file specifici del tuo progetto
2. **Sezione "TOOL DISPONIBILI"**: aggiungi/rimuovi tool in base al tuo task
3. **Sezione "CONTESTO DI BUSINESS"**: spiega il tuo settore, dati sensibili, KPI
4. **Sezione "QUANDO RIFERIRE A UN UMANO"**: definisci tu i casi che devono escalare

Mantieni invariate le **5 regole operative**: sono i guardrail di sicurezza, validi per qualsiasi task in produzione.
