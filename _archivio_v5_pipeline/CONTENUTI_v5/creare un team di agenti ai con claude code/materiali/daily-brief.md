# Prompt orchestratore — Daily Competitor Brief

Questo è il prompt che lanci dentro Claude Code (locale) per testare il sistema. Per la versione cloud schedulata vedi `prompt-routine.md`.

---

Stai eseguendo il **Daily Competitor Brief** di oggi.

## Step 1 — Crea il team

Crea un agent team di 4 teammates usando le subagent definitions presenti in `.claude/agents/`:

1. teammate "**pricing**" — agent type `pricing-watcher` (model: claude-sonnet-4-6)
2. teammate "**features**" — agent type `feature-watcher` (model: claude-sonnet-4-6)
3. teammate "**social**" — agent type `social-watcher` (model: claude-sonnet-4-6)
4. teammate "**synthesizer**" — agent type `synthesizer` (model: claude-opus-4-7)

Modalità: in-process.

## Step 2 — Distribuisci i task in parallelo

Crea 3 task indipendenti nella shared task list:

- **task A** (assigned: pricing): "Leggi `competitors.json` e per ogni competitor estrai i prezzi correnti dalla loro pagina pricing. Output in `briefs/_partial/pricing.md`. Segui le regole del system prompt."
- **task B** (assigned: features): "Leggi `competitors.json` e per ogni competitor estrai gli ultimi blog post pubblicati negli ultimi 7 giorni. Output in `briefs/_partial/features.md`. Segui le regole del system prompt."
- **task C** (assigned: social): "Leggi `competitors.json` e per ogni competitor estrai i top post LinkedIn aziendali (≤7gg, >50 reazioni). Output in `briefs/_partial/social.md`. Segui le regole del system prompt."

I 3 watcher lavorano in parallelo.

## Step 3 — Synthesizer (con dipendenza)

Crea il task D con dipendenza esplicita su A, B, C:

- **task D** (assigned: synthesizer, depends_on: [A, B, C]): "Quando A, B, C sono `completed`, leggi i 3 file `briefs/_partial/*.md`, produci il brief finale in `briefs/<data-oggi-YYYY-MM-DD>.md`. Segui la struttura del system prompt."

## Step 4 — Cleanup

Dopo che task D è completed:
- Verifica che il file `briefs/<data>.md` esiste
- Esegui cleanup del team

## Lingua e formato

- Lingua: italiano
- Formato output: markdown
- Lunghezza brief: max 400 parole
