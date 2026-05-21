# Setup automatico — Claude Code, leggi qui

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali-variante-1/START_HERE.md` — sincronizzare ogni modifica.

Sei stato lanciato dentro la cartella materiali della **Newsletter AI personale — Variante 1 (Claude Agent SDK)**. Tu fai solo: verifica prerequisiti + venv + dipendenze + chiave API + primo run. ~5 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
python --version    # deve essere ≥ 3.10
# (oppure python3 --version su Mac/Linux)
```

Se manca: indirizza l'utente a https://www.python.org/downloads/

### 2. Mostra all'utente cosa farà il sistema

In 3 frasi:
- Ogni mattina (quando schedulato), lo script Python visita le 3 fonti Anthropic in `fonti.json`
- Usa Claude Agent SDK per generare un riassunto markdown delle novità in `newsletter/`
- Aggiorna `state.json` per non riproporre articoli già visti

### 3. Setup ambiente Python

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
# oppure: .venv\Scripts\activate    su Windows
pip install -r requirements.txt
```

### 4. Configura la chiave API

```bash
cp .env.example .env
```

Chiedi all'utente la sua API key Anthropic (formato `sk-ant-...`). Se non ce l'ha: https://console.anthropic.com → Settings → API Keys → Create Key.

Apri `.env`, sostituisci il placeholder con la chiave reale. **Verifica che `.gitignore` esista già** e contenga `.env`.

### 5. (Opzionale) Personalizza fonti e tono

Chiedi:
- "Vuoi cambiare le fonti?" → apri `fonti.json` e aiuta a modificare
- "Vuoi cambiare il tono?" → apri `CLAUDE.md`, sezione `## Tono della newsletter`

Se l'utente dice "lascia tutto e fai il primo run", salta allo step 6.

### 6. Primo run di test

```bash
python newsletter.py
```

Aspetta ~1-2 minuti. Lo script stampa progress in console mentre l'Agent lavora. Quando finisce, mostra:
- Il file generato in `newsletter/YYYY-MM-DD.md`
- La modifica a `state.json`

### 7. (Opzionale) Schedulazione cron

Chiedi: "Vuoi che parta da solo ogni mattina?"

Se sì:
- Apri `scheduling/crontab-example.txt` e mostra all'utente la riga adatta al suo OS
- Su Mac/Linux: aiutalo con `crontab -e`, incolla la riga sostituendo i path placeholder
- Su Windows: spiega l'attivazione via Utilità di pianificazione

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: questa cartella È il progetto.
- **Non commettere `.env`**: è in `.gitignore`, ma se l'utente lancia `git add -A` segnala il rischio.
- **Verifica che `claude-agent-sdk` si installi senza errori** — è il pacchetto critico. Se fallisce, suggerisci `pip install --upgrade pip` e ritenta.
- Tono diretto, conciso.
- Se un comando fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
