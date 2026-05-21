# Setup automatico — Claude Code, leggi qui

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali-variante-2/START_HERE.md` — sincronizzare ogni modifica.

Sei stato lanciato dentro la cartella materiali della **Newsletter AI personale — Variante 2 (Anthropic API + parsing HTML/RSS)**. Tu fai solo: prerequisiti + venv + dipendenze + chiave API + primo run. ~5 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
python --version    # deve essere ≥ 3.10
```

Se manca: indirizza a https://www.python.org/downloads/

### 2. Mostra cosa farà il sistema

In 3 frasi:
- Lo script scarica HTML/RSS delle 3 fonti in `fonti.json`
- Per ogni articolo nuovo (non in `state.json`), passa il testo pulito a Claude API per il riassunto
- Salva un file markdown in `newsletter/YYYY-MM-DD.md`

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

Chiedi all'utente l'API key Anthropic (`sk-ant-...`). Se non ce l'ha: https://console.anthropic.com → Settings → API Keys.

### 5. (Opzionale) Personalizza fonti e prompt

- "Vuoi cambiare le fonti?" → apri `fonti.json`. Spiega la differenza tra `tipo: html` (serve selettore CSS) e `tipo: rss` (più stabile, niente selettore).
- "Vuoi cambiare il tono?" → apri `prompt.txt`. È testo puro, lo modifichi senza vincoli.

### 6. Primo run di test

```bash
python newsletter.py
```

Aspetta ~1-2 minuti. Mostra a fine:
- Il file generato in `newsletter/YYYY-MM-DD.md`
- La modifica a `state.json`

### 7. (Opzionale) Schedulazione

Apri `scheduling/crontab-example.txt`, mostra all'utente la riga adatta al suo OS.

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**.
- **Verifica installazione dipendenze**: `pip install` può fallire su Windows per BeautifulSoup/lxml. Se succede, suggerisci `pip install --upgrade pip` prima.
- Tono diretto.
- Se un comando fallisce, mostra l'errore e suggerisci la correzione.
