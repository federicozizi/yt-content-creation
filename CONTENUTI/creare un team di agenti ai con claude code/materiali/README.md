# Team di agenti AI — Metodo A (Claude Code Agent Teams)

**Tutto pronto per l'uso.** Configura `competitors.json` coi tuoi 3 competitor e lancia.

## Prerequisiti

- Node ≥ 18 con Claude Code CLI installato (`npm install -g @anthropic-ai/claude-code`)
- Abbonamento Claude Pro o Max (Agent Teams + Routines sono inclusi)

> Per il Metodo A **non** serve API key Anthropic separata né Python: Claude Code usa il tuo abbonamento.

## Quick start

```bash
# 1. Verifica i prerequisiti
bash verifica-prerequisiti.sh

# 2. Modifica competitors.json coi tuoi 3 competitor reali

# 3. Lancia Claude Code dentro questa cartella e incolla:
#    "esegui il prompt in daily-brief.md"
claude
```

Il brief finisce in `briefs/<data>.md`.

## Setup automatico (consigliato)

Se non vuoi pensare a niente, lancia `claude` dentro questa cartella e scrivi:

> esegui il setup leggendo INIZIO_QUI.md

Claude Code fa il check dei prerequisiti, ti aiuta a configurare i competitor e lancia il primo test.

## Cosa c'è in questa cartella

```
.
├── README.md                    ← stai leggendo questo
├── INIZIO_QUI.md                ← setup guidato per Claude Code
├── .gitignore                   ← protegge .env e file sensibili
├── .env.example                 ← placeholder credenziali (non obbligatorio per il Metodo A)
├── competitors.json             ← lista dei 3 competitor (da modificare)
├── daily-brief.md               ← prompt orchestratore (per il test locale)
├── prompt-routine.md            ← prompt per la routine cloud schedulata
├── esempio-brief.md             ← come si presenta l'output atteso
├── verifica-prerequisiti.sh     ← check rapido dei prerequisiti
├── .claude/
│   ├── settings.json            ← attiva Agent Teams + permessi
│   └── agents/                  ← i 4 sub-agent (3 watcher + synthesizer)
│       ├── pricing-watcher.md
│       ├── feature-watcher.md
│       ├── social-watcher.md
│       └── synthesizer.md
└── docs/                        ← guide aggiuntive
    ├── test-locale.md
    └── scheduling-routines.md
```

## Schedulazione (opzionale)

Quando il test locale funziona, segui `docs/scheduling-routines.md` per attivare la routine cloud Anthropic (gira anche col PC spento, niente VPS, niente GitHub).
