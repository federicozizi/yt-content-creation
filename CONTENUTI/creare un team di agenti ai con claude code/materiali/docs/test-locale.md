# Test locale del team

Prima di schedulare la routine cloud, verifica che il team funzioni in locale dentro Claude Code.

## Passi

1. Verifica i prerequisiti:

   ```bash
   bash verifica-prerequisiti.sh
   ```

2. Modifica `competitors.json` coi tuoi 3 competitor reali (almeno `pricing_url`, `blog_url`, `linkedin_url` validi).

3. Lancia Claude Code dentro questa cartella:

   ```bash
   claude
   ```

4. Incolla il prompt orchestratore:

   > esegui il prompt in `daily-brief.md`

5. Aspetta 2-5 minuti. Vedrai Claude:
   - Creare il team con 4 teammates (pricing, features, social, synthesizer)
   - Distribuire 3 task in parallelo ai watcher
   - Aspettare il completamento
   - Far partire il synthesizer
   - Scrivere `briefs/<data-oggi>.md`

## Cosa controllare

- [ ] Il file `briefs/<data-oggi>.md` esiste
- [ ] La sezione "TOP INSIGHT" ha 3 punti concreti (non placeholder)
- [ ] Per ogni competitor c'è almeno 1 riga compilata in pricing / features / social
- [ ] Il brief è leggibile in 30 secondi (max ~400 parole)

## Se qualcosa non funziona

| Problema | Causa probabile | Fix |
|---|---|---|
| "Agent teams not enabled" | settings.json non letto | Verifica che `.claude/settings.json` esista (non `claude-settings.json` al root) |
| Watcher restituisce solo "N/D" | URL non leggibili (403, JS-only) | Verifica gli URL in `competitors.json` aprendoli nel browser |
| Synthesizer parte prima dei watcher | Dipendenze non passate | Rilancia il prompt: `daily-brief.md` specifica `depends_on: [A, B, C]` |
| LinkedIn restituisce login wall | Bloccato per non-loggati | Il social-watcher ha un fallback su X/blog: leggi il file `briefs/_partial/social.md` |

## Quando il test passa

Procedi con `docs/scheduling-routines.md` per la routine cloud schedulata.
