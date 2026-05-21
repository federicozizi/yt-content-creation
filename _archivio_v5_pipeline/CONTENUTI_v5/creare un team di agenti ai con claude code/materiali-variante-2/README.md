# Team di agenti AI — Metodo B (Anthropic SDK raw)

**Tutto pronto per l'uso.** Configura `.env` + `competitors.json` e lancia.

## Prerequisiti

- Python ≥ 3.10
- API key Anthropic ([console.anthropic.com](https://console.anthropic.com))
- App Password Gmail ([myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords))

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
├── requirements.txt       ← dipendenze Python (anthropic + python-dotenv)
├── competitors.json       ← lista dei 3 competitor (da modificare)
├── team_agenti.py         ← lo script principale (~150 righe commentate)
├── prompts/               ← i 4 system prompt dei ruoli
│   ├── pricing.txt
│   ├── features.txt
│   ├── social.txt
│   └── synthesizer.txt
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

## Modificare i prompt dei ruoli

Apri `prompts/pricing.txt`, `prompts/features.txt`, ecc. — sono testo puro, modifichi e rilanci. Lo script li ricarica ad ogni run.

## Schedulazione (opzionale)

Quando il test locale funziona, vai in `scheduling/` per schedulare il brief ogni mattina alle 7 via cron locale o (consigliato) GitHub Actions.
