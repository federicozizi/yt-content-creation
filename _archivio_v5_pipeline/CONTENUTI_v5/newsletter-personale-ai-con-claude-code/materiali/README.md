# Newsletter AI personale — template

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali/README.md` — sincronizzare ogni modifica.

**Tutto pronto per essere usato.** Sistema minimale che ogni mattina visita le fonti che decidi tu, riassume le novità nel tono che preferisci, salva un file markdown sulla scrivania. Niente Python, niente API esterne, solo Claude Code.

## Prerequisiti

- [Claude Code installato](https://claude.com/code) e loggato (Pro/Max o API key)

Nient'altro.

## Quick start (3 comandi)

```bash
# 1. Entra nella cartella
cd materiali

# 2. Lancia Claude col prompt orchestratore
claude --print "$(cat prompts/newsletter-daily.md)"

# 3. Apri il file generato
# (apparirà in newsletter/YYYY-MM-DD.md)
```

Fine. La prima newsletter è in `newsletter/`.

## Setup automatico (consigliato per non-tecnici)

Lancia Claude Code dentro questa cartella:

```bash
claude
> esegui il setup leggendo INIZIO_QUI.md
```

Claude Code fa tutto da solo: verifica i prerequisiti, ti chiede 1-2 conferme, lancia il primo run, ti mostra il risultato.

## Cosa c'è in questa cartella

```
.
├── README.md                          ← stai leggendo questo
├── INIZIO_QUI.md                      ← setup guidato per Claude Code
├── CLAUDE.md                          ← STEP 2: tono e regole della newsletter
├── .gitignore                         ← protegge state.json e output
├── fonti.json                         ← STEP 1: lista fonti primarie da monitorare
├── fonti-fallback.json                ← STEP 5: fonti secondarie per giorni vuoti
├── state.json                         ← memoria URL già visti (Claude lo aggiorna)
├── esempio-output.md                  ← come si presenta una newsletter generata
├── prompts/
│   └── newsletter-daily.md            ← STEP 3: prompt orchestratore
├── .claude/
│   └── agents/
│       ├── empty-day-rescue.md        ← STEP 5: sub-agent per giorni vuoti
│       └── major-update-spotter.md    ← STEP 5: sub-agent per major update
├── scheduling/
│   ├── claude-routines.md             ← STEP 4: scheduling con Routines
│   └── crontab-example.txt            ← STEP 4: fallback cron locale
└── docs/
    └── email-opzionale.md             ← opzionale — ricevere via email
```

## I 5 step in sintesi

| # | Step | File | Cosa fai |
|---|---|---|---|
| 1 | Definisci le fonti | `fonti.json` | Aggiungi/togli URL dei siti da monitorare |
| 2 | Definisci il tono | `CLAUDE.md` | Modifichi le regole di scrittura |
| 3 | Primo run | `prompts/newsletter-daily.md` | Lanci Claude col prompt |
| 4 | Schedula | `scheduling/claude-routines.md` | Una riga: parte da sola ogni mattina |
| 5 | Team di agenti | `.claude/agents/*.md` + `fonti-fallback.json` | 2 sub-agent: gestione giorni vuoti + spotlight major update |

## Cosa modificare per riadattarlo al tuo caso

- **Cambi argomento** (es. da Anthropic a competitor): modifichi `fonti.json` con nuovi URL
- **Cambi tono** (es. più tecnico, più colloquiale, lingua diversa): modifichi `CLAUDE.md`
- **Cambi orario** (es. da 8 a 18): modifichi la routine in `claude routines edit`
- **Cambi formato output** (es. da markdown a HTML email-ready): modifichi `prompts/newsletter-daily.md`

## Cosa NON deve essere committato in git

- `state.json` → contiene URL che hai consultato, è "privato"
- `newsletter/*.md` → output personale, non lo vuoi su GitHub pubblico

Il `.gitignore` li esclude già di default. Non rimuoverlo se intendi versionare la cartella.
