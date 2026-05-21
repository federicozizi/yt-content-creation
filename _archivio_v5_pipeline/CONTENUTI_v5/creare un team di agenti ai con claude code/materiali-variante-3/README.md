# Team di agenti AI — Metodo C (Claude Agent SDK)

**Tutto pronto per l'uso.** Configura `.env` + `competitors.json` e lancia.

## Prerequisiti

- Python ≥ 3.10
- Node ≥ 18 con Claude Code CLI installato (`npm install -g @anthropic-ai/claude-code`)
- API key Anthropic ([console.anthropic.com](https://console.anthropic.com))
- App Password Gmail ([myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)) — opzionale, solo per ricevere il brief via mail

## Quick start (5 comandi)

```bash
# 1. Crea il virtual env e installa le dipendenze
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Configura le credenziali
cp .env.example .env
# Apri .env e compila i 4 valori (API key + Gmail)

# 3. Modifica competitors.json coi tuoi 3 competitor

# 4. Lancia
python team_agenti.py
```

Il brief finisce in `briefs/<data>.md` e arriva via email.

## Cosa c'è in questa cartella

```
.
├── README.md              ← stai leggendo questo
├── INIZIO_QUI.md          ← alternativa: lascia che Claude Code faccia il setup
├── .env.example           ← template credenziali (copia in .env)
├── .gitignore             ← protegge .env dal commit accidentale
├── requirements.txt       ← dipendenze Python
├── competitors.json       ← lista dei 3 competitor (da modificare)
├── team_agenti.py         ← lo script principale
├── .claude/agents/        ← i 4 sub-agent (stessi del Metodo A)
│   ├── pricing-watcher.md
│   ├── feature-watcher.md
│   ├── social-watcher.md
│   └── synthesizer.md
├── esempio-brief.md       ← come si presenta l'output atteso
└── scheduling/            ← file per schedulare il brief automaticamente
    ├── crontab-example.txt
    └── .github/workflows/daily-brief.yml
```

## Setup automatico (alternativa)

Non vuoi fare i comandi a mano? Lancia `claude` dentro questa cartella e scrivi:

> esegui il setup leggendo INIZIO_QUI.md

Claude Code fa tutto da solo, ti chiede solo le credenziali una alla volta.

## Sicurezza credenziali

Il file `.gitignore` esclude già `.env` dai commit. **Non rimuoverlo**: se committi `.env` per sbaglio, le credenziali sono compromesse anche dopo averle rimosse dalla storia git. Vanno revocate e ricreate.

## Schedulazione (opzionale)

Quando il test locale funziona, vai in `scheduling/` per schedulare il brief ogni mattina alle 7 via cron locale o (consigliato) GitHub Actions. Le istruzioni sono nel README della cartella `scheduling/`.
