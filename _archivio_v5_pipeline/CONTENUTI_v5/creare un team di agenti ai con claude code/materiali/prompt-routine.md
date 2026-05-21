# Prompt routine — Daily Competitor Brief (versione cloud)

Da configurare nel campo "Prompt" della routine cloud (claude.ai/code → New Routine).

È una versione leggermente adattata del prompt orchestratore: include un cenno al fatto che si è in ambiente cloud (no UI, no laptop), per disambiguare eventuali fallback.

---

Stai eseguendo una routine cloud schedulata. Il tuo job: produrre il **Daily Competitor Brief** di oggi.

## Step 1 — Crea il team

Crea un agent team di 4 teammates usando le subagent definitions presenti in `.claude/agents/`:

1. teammate "**pricing**" — agent type `pricing-watcher` (model: claude-sonnet-4-6)
2. teammate "**features**" — agent type `feature-watcher` (model: claude-sonnet-4-6)
3. teammate "**social**" — agent type `social-watcher` (model: claude-sonnet-4-6)
4. teammate "**synthesizer**" — agent type `synthesizer` (model: claude-opus-4-7)

Modalità: in-process (siamo in ambiente cloud, niente UI tmux/iterm).

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
- Termina la routine con stato success

## Gestione errori

- Se un watcher fallisce su un competitor specifico (es. pagina down): l'agente deve scrivere `N/D` nel suo file `_partial` e proseguire con gli altri competitor. NON bloccare il task.
- Se TUTTI i 3 file `_partial` sono vuoti (improbabile): il synthesizer scrive un brief minimal con "[dati non disponibili oggi - verificare gli URL in competitors.json]", così la presenza del file conferma che la routine è girata.

## Lingua e formato

- Lingua: italiano
- Formato output: markdown
- Lunghezza brief: max 400 parole
