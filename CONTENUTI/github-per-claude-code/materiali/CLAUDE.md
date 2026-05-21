# Istruzioni persistenti per Claude Code

Questo file viene letto **automaticamente** da ogni sessione Claude Code che parte dentro questo repo. È il "cervello esterno" che dà contesto persistente all'agente: regole del progetto, convenzioni, do/don't.

> Quando lavori in questo repo, segui le regole sotto. Se l'utente ti chiede qualcosa che le contraddice, chiedi conferma.

## Cosa fa questo repo

Mini-sistema di **competitor intelligence**: ogni mattina alle 7 una GitHub Action lancia te (Claude Code) per produrre un brief sui 3 competitor elencati in `competitors.json`. Il brief finisce in `briefs/<data>.md` e viene committato nel repo.

## Convenzioni

- **Lingua output**: italiano
- **Formato brief**: markdown, max 400 parole, struttura definita in `prompts/daily-brief.md`
- **Niente segreti committati**: API key, password, token vivono solo in GitHub Secrets (`ANTHROPIC_API_KEY`, `GMAIL_APP_PASSWORD`, ecc.)
- **Branch policy**: lavora su feature branch `auto/<data>-<slug>`, mai direttamente su `main`
- **Commit message**: `daily brief YYYY-MM-DD` per i brief generati. `fix:`, `feat:`, `docs:` per modifiche al sistema.

## File chiave

| File | Cosa è | Quando toccarlo |
|---|---|---|
| `competitors.json` | Lista 3 competitor da monitorare | Quando l'utente vuole cambiare i competitor |
| `prompts/daily-brief.md` | Prompt orchestratore | Solo se l'utente chiede di cambiare la struttura del brief |
| `.github/workflows/daily-brief.yml` | Action schedulata 7:05 ogni giorno | Solo se l'utente chiede di cambiare cron o trigger |
| `.github/workflows/issue-task.yml` | Action che processa issue con label `claude-task` | Solo se l'utente chiede di cambiare il flow |
| `briefs/` | Output dei brief giornalieri | Solo per leggere, mai modificare a mano i file passati |

## Stile

- Tono diretto, asciutto, italiano colloquiale
- Niente paragrafi accademici
- Quando produci un brief, segui ESATTAMENTE la struttura in `prompts/daily-brief.md`
