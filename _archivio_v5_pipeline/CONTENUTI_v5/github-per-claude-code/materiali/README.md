# GitHub per Claude Code — repo template

**Tutto pronto per essere usato come template GitHub.** Dentro trovi 5 trucchi pratici già configurati: contesto persistente, scheduling cloud, issue → PR automatica, code review pre-commit, pattern worktree per task paralleli.

## Prerequisiti

- Account GitHub
- [GitHub CLI `gh`](https://cli.github.com/) installato e autenticato (`gh auth login`)
- Claude Code CLI installato (`npm install -g @anthropic-ai/claude-code`)
- API key Anthropic (https://console.anthropic.com)

## Quick start

```bash
# 1. Crea un nuovo repo GitHub partendo da questa cartella
gh repo create my-claude-repo --private --source . --push

# 2. Aggiungi il secret ANTHROPIC_API_KEY al repo
gh secret set ANTHROPIC_API_KEY

# 3. Modifica competitors.json coi tuoi 3 competitor reali

# 4. Trigger manuale del primo brief (per testare)
gh workflow run daily-brief.yml

# 5. Aspetta 1-2 minuti, poi:
gh run watch
gh pr list  # dovresti vedere la PR del brief
```

Da domani alle 7:05 UTC il brief arriva da solo come PR ogni mattina.

## Setup automatico (consigliato per non-tecnici)

Lancia Claude Code dentro questa cartella:

```bash
claude
> esegui il setup leggendo INIZIO_QUI.md
```

Claude Code fa tutto da solo: crea il repo GitHub, imposta il secret, fa il primo test, ti spiega cosa è successo.

## Cosa c'è in questa cartella

```
.
├── README.md                                  ← stai leggendo questo
├── INIZIO_QUI.md                              ← setup guidato per Claude Code
├── CLAUDE.md                                  ← TRUCCO #1: contesto persistente nel repo
├── .gitignore                                 ← protegge .env e file sensibili
├── .env.example                               ← template credenziali (per test locale)
├── competitors.json                           ← lista competitor (modificabile)
├── esempio-output.md                          ← come si presenta il risultato atteso
├── prompts/
│   └── daily-brief.md                         ← prompt orchestratore del brief
├── .github/
│   ├── workflows/
│   │   ├── daily-brief.yml                    ← TRUCCO #3: Claude schedulato in cloud
│   │   └── issue-task.yml                     ← TRUCCO #4: issue → PR automatica
│   └── hooks/
│       └── pre-commit-claude-review.sh        ← TRUCCO #5: review pre-commit
└── docs/
    ├── worktree-pattern.md                    ← TRUCCO #2: 3 Claude in parallelo
    └── github-actions-setup.md                ← guida ai secret e permessi
```

## I 5 trucchi in sintesi

| # | Trucco | File | Cosa risolve |
|---|---|---|---|
| 1 | `CLAUDE.md` nel repo | `CLAUDE.md` | Contesto persistente per ogni sessione |
| 2 | Worktree paralleli | `docs/worktree-pattern.md` | 3 Claude in parallelo senza conflitti |
| 3 | GitHub Actions schedulato | `.github/workflows/daily-brief.yml` | Claude gira anche col PC spento |
| 4 | Issue → PR automatica | `.github/workflows/issue-task.yml` | Backlog di task gestito da labels |
| 5 | Pre-commit review | `.github/hooks/pre-commit-claude-review.sh` | Auto-review prima del commit |

## Sicurezza credenziali

- **Mai committare `.env`**: il `.gitignore` lo esclude. In produzione, le credenziali vivono nei **GitHub Secrets** del repo, non in file locali.
- **Mai stampare i secret nei log delle Action**: GitHub li maschera in automatico, ma evita comunque `echo $ANTHROPIC_API_KEY`.
- Se per sbaglio committi `.env`: revoca subito la chiave su https://console.anthropic.com e ricreane una nuova. Rimuoverla dalla storia git **non basta** — i bot scansionano GitHub costantemente.
