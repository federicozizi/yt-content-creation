# Setup automatico — Claude Code, leggi qui

Sei stato lanciato dentro la cartella materiali del **Metodo B — Anthropic SDK raw**. Tutto è già qui dentro al root: lo script, i 4 prompt in `prompts/`, il template `.env.example`, il `.gitignore`. Tu fai solo: prerequisiti + venv + credenziali. ~3 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
python --version    # ≥ 3.10
```

Se manca o è < 3.10, manda l'utente su https://python.org/downloads e fermati.

### 2. Crea il virtual env e installa le dipendenze

Lavoriamo **direttamente in questa cartella** (no progetto separato — tutto è già pronto qui).

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configura le credenziali

```bash
cp .env.example .env
```

Chiedi all'utente i 4 valori uno alla volta:
- **API key Anthropic** (`sk-ant-...`) — se non ce l'ha: https://console.anthropic.com → Settings → API Keys
- **Email mittente** (Gmail)
- **App Password Gmail** (16 caratteri) — se non ce l'ha: https://myaccount.google.com/apppasswords (richiede 2FA)
- **Email destinatario**

Scrivi i 4 valori in `.env`. **Verifica che `.gitignore` esista già** (c'è di default) e contenga `.env` — è il caso.

### 4. Configura i competitor

Apri `competitors.json` e aiuta l'utente a sostituire i 3 placeholder coi suoi competitor reali. Per ognuno servono: `name`, `pricing_url`, `blog_url`, `linkedin_url`.

### 5. Test

```bash
python team_agenti.py
```

A terminale vedrai i 3 watcher partire nello stesso secondo (timestamp identici), finire in tempi diversi, poi il synthesizer. Il brief finisce in `briefs/<data>.md` e arriva via email. Tempo totale: ~30 secondi.

### 6. Schedulazione (opzionale)

Quando il test è OK, suggerisci all'utente di andare in `scheduling/` e seguire le istruzioni per attivare GitHub Actions.

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: la cartella materiali stessa È il progetto.
- **Non rimuovere `.gitignore`**.
- Tono diretto, conciso.
