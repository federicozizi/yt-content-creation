# Newsletter AI personale — Variante 1 (Claude Agent SDK Python)

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali-variante-1/README.md` — sincronizzare ogni modifica.

**Stesso pattern del metodo principale, ma sotto forma di script Python.** Usa la libreria ufficiale `claude-agent-sdk` per orchestrare un Agent Claude con tool di web fetching, generare la newsletter, salvarla.

## Prerequisiti

- Python ≥ 3.10
- Una API key Anthropic (https://console.anthropic.com)

## Quick start (4 comandi)

```bash
cd materiali-variante-1
python -m venv .venv && source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # poi compila ANTHROPIC_API_KEY
python newsletter.py
```

Il file della prima newsletter appare in `newsletter/YYYY-MM-DD.md`.

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
├── CLAUDE.md              ← tono e regole newsletter (identico al PRINCIPALE)
├── .gitignore             ← protegge .env, state.json, output
├── .env.example           ← template ANTHROPIC_API_KEY
├── requirements.txt       ← claude-agent-sdk, python-dotenv
├── newsletter.py          ← LO SCRIPT principale
├── fonti.json             ← lista fonti da monitorare
├── state.json             ← memoria URL già visti (lo script lo aggiorna)
├── esempio-output.md      ← esempio di newsletter generata
└── scheduling/
    └── crontab-example.txt ← esempi cron Mac/Linux/Windows
```

## Differenze chiave dal metodo principale

| Aspetto | Metodo principale | Variante 1 (questa) |
|---|---|---|
| Linguaggio | nessuno (solo prompt MD) | Python ~50 righe |
| Loader CLAUDE.md | automatico (CLI) | manuale nello script |
| Esecuzione | `claude` CLI | `python newsletter.py` |
| API key | non serve se hai abbonamento | sempre necessaria |
| Scheduling | Claude Routines | cron / Task Scheduler |
| Logica custom | difficile | facile (modifichi Python) |
| Server headless | no | sì |

## Costi

API Anthropic: ~$0.01-0.05 per run a seconda della dimensione del prompt. Per un run/giorno → ~$0.30-1.50/mese.

## Sicurezza credenziali

- `.env` è in `.gitignore`. Non rimuoverlo.
- Se committi `.env` per sbaglio, **revoca la chiave** su console.anthropic.com e creane una nuova: rimuoverla dalla git history non basta (i bot scansionano GitHub).
