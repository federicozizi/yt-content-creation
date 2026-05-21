# Setup automatico — Claude Code, leggi qui

Sei stato lanciato dentro la cartella materiali del **Metodo C — Claude Agent SDK**. Tutto il necessario è già qui dentro al root: lo script, i 4 sub-agent in `.claude/agents/`, il template `.env.example`, il `.gitignore`. Il tuo compito è solo: prerequisiti + venv + credenziali. ~3 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
python --version    # ≥ 3.10
node --version      # ≥ 18 (serve per il binario claude che l'SDK chiama sotto)
claude --version    # se manca: npm install -g @anthropic-ai/claude-code
```

Se manca qualcosa, segnalalo all'utente coi link giusti (python.org, nodejs.org).

### 2. Crea il virtual env e installa le dipendenze

Lavoriamo **direttamente in questa cartella** (no progetto separato — tutto è già pronto qui).

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configura le credenziali

Copia il template e chiedi i valori uno alla volta:

```bash
cp .env.example .env
```

Poi chiedi all'utente:
- **API key Anthropic** (`sk-ant-...`) — se non ce l'ha, mandalo su https://console.anthropic.com → Settings → API Keys
- **Email mittente** (Gmail) — quella da cui parte il brief
- **App Password Gmail** (16 caratteri tipo `abcd efgh ijkl mnop`) — se non ce l'ha, mandalo su https://myaccount.google.com/apppasswords (richiede 2FA attiva)
- **Email destinatario** — può essere uguale alla mittente

Scrivi i 4 valori in `.env`. **Verifica che `.gitignore` esista già** (c'è di default) e contenga `.env` — è il caso.

### 4. Configura i competitor

Apri `competitors.json`, mostralo all'utente, e aiutalo a sostituire i 3 placeholder coi suoi competitor reali. Per ognuno servono: `name`, `pricing_url`, `blog_url`, `linkedin_url`.

### 5. Test

```bash
python team_agenti.py
```

Aspetta 30-60 secondi. Vedrai lo stream di eventi: l'orchestrator spawna i 3 watcher in parallelo, poi il synthesizer. Il brief finisce in `briefs/<data>.md` e arriva via email.

Se l'email non arriva: lo script comunque scrive il brief su file. Apri `briefs/<data>.md` per verificare.

### 6. Schedulazione (opzionale)

Quando il test è OK, suggerisci all'utente di andare in `scheduling/` e seguire le istruzioni per attivare GitHub Actions (gratis, autonomo, anche col PC spento).

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: la cartella materiali stessa È il progetto. Tutto è già qui.
- **Non rimuovere `.gitignore`**: protegge `.env` dai commit accidentali.
- Tono diretto, conciso. Niente paragrafi accademici.
- Se qualcosa fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
