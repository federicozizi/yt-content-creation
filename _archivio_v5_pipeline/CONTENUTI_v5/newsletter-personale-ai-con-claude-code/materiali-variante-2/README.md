# Newsletter AI personale — Variante 2 (Anthropic API + parsing HTML/RSS)

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali-variante-2/README.md` — sincronizzare ogni modifica.

**Lo stesso pattern degli altri 2 metodi, ridotto all'osso.** ~80 righe di Python che scaricano HTML/RSS delle fonti, estraggono articoli con BeautifulSoup/feedparser, mandano a Claude API solo il testo pulito, salvano il markdown.

## Prerequisiti

- Python ≥ 3.10
- Una API key Anthropic (https://console.anthropic.com)

## Quick start (4 comandi)

```bash
cd materiali-variante-2
python -m venv .venv && source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # poi compila ANTHROPIC_API_KEY
python newsletter.py
```

Il file appare in `newsletter/YYYY-MM-DD.md`.

## Setup automatico (consigliato)

```bash
claude
> esegui il setup leggendo INIZIO_QUI.md
```

## Cosa c'è in questa cartella

```
.
├── README.md              ← stai leggendo questo
├── INIZIO_QUI.md          ← setup guidato per Claude Code
├── .gitignore             ← protegge .env, state.json, output
├── .env.example           ← template ANTHROPIC_API_KEY
├── requirements.txt       ← anthropic, requests, beautifulsoup4, feedparser, python-dotenv
├── newsletter.py          ← LO SCRIPT (~80 righe)
├── fonti.json             ← fonti HTML + RSS
├── prompt.txt             ← prompt di sintesi per Claude
├── state.json             ← memoria URL già visti
├── esempio-output.md      ← esempio newsletter generata
└── scheduling/
    └── crontab-example.txt ← esempi cron Mac/Linux/Windows
```

## Differenze chiave dai metodi precedenti

| Aspetto | Principale | Variante 1 | Variante 2 (questa) |
|---|---|---|---|
| Stack | Claude Code CLI | Claude Agent SDK | Anthropic API + Python stdlib + requests |
| Loader CLAUDE.md | automatico | manuale (open in Python) | il "tono" vive in `prompt.txt` puro |
| Agent loop | sì (CLI fa tutto) | sì (Agent SDK) | NO (codice procedurale) |
| Tool use | sì (WebFetch) | sì (web_fetch) | NO (richiede `requests` esplicito) |
| Token Claude per run | alti | medi | bassi (passi solo testo pulito) |
| Costo/run | $0 (abbonamento) o ~$0.05 (API) | ~$0.05 | ~$0.005-0.01 |
| Server headless | no | sì | sì (anche Raspberry Pi) |
| Magia | molta | media | zero |

## Costi

API Anthropic: ~$0.002-0.01 per run (passi solo i testi puliti, non gli HTML grezzi).
Per un run/giorno → ~$0.10-0.30/mese.

## Sicurezza credenziali

- `.env` è in `.gitignore`. Non rimuoverlo.
- Se committi `.env` per sbaglio, **revoca la chiave** su console.anthropic.com.
