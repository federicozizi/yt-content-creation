# Come schedulare la routine cloud

Una volta che il test in locale funziona, è il momento di passare al cloud.

## Opzione A — Da CLI (consigliato)

Dentro una sessione Claude Code (anche fresh), chiedi al lead di creare una routine:

```text
Schedula una routine cloud che ogni giorno alle 7:05 (Europe/Rome) esegua il prompt 
contenuto in daily-brief.md su questo progetto. Nome routine: "Daily Competitor Brief".
```

Claude userà i tool interni (CronCreate equivalente per cloud) e confermerà:
- ID routine
- Cadenza
- Prossima esecuzione

## Opzione B — Da web (se la CLI non è disponibile o vuoi vederlo a colpo d'occhio)

1. Apri https://claude.ai/code o claude.com/code
2. Sidebar sinistra → **Routines**
3. Click **New Routine** (in alto a destra)
4. Compila i campi:

| Campo | Valore |
|---|---|
| Name | `Daily Competitor Brief` |
| Source | Scegli `Remote task` (workspace cloud — non serve GitHub) |
| Schedule | `5 7 * * *` (ogni giorno alle 7:05) |
| Timezone | `Europe/Rome` |
| Prompt | Incolla il contenuto di `prompt-routine.md` (al root della cartella materiali) |
| Permissions | Lascia "Run autonomously" (default) |

5. Click **Save**

## Test della routine (run on demand)

Subito dopo aver creato la routine, fai un **Run now** per testare il flusso cloud senza aspettare il giorno dopo:

- Da CLI: `Esegui la routine "Daily Competitor Brief" adesso`
- Da web: nella lista Routines, click sull'icona "play" (Run now) della tua routine

Aspetta 3-5 minuti. Verifica:
- [ ] Stato passa Running → Completed
- [ ] Log della run è leggibile (mostra spawn agenti, completamento task, sintesi)
- [ ] Il file `briefs/<oggi>.md` è apparso nel workspace cloud

## Configurazione del cron

Lo schedule `5 7 * * *` significa: minuto 5, ora 7, ogni giorno, ogni mese, ogni giorno della settimana.

**Perché `:05` invece di `:00`?**
Le routine cloud applicano un jitter di max 30 minuti per evitare colli di bottiglia API. Se imposti `:00`, il job potrebbe partire fino alle 7:30. Impostando `:05` (o un altro minuto non rotondo), il jitter si applica comunque ma puoi essere ragionevolmente sicuro che parta tra le 7:05 e le 7:35.

**Variazioni utili:**

| Scenario | Cron |
|---|---|
| Solo giorni lavorativi | `5 7 * * 1-5` |
| 2 volte al giorno (mattina + pomeriggio) | crei 2 routine: `5 7 * * *` e `0 15 * * *` |
| Solo il lunedì | `5 7 * * 1` |
| Ogni 6 ore | `0 */6 * * *` |

## Limiti per piano

| Piano | Routines/giorno | Adatto per |
|---|---|---|
| Free | 0 (non disponibile) | — |
| Pro ($20/mese) | 5 | Use case singolo (questo team) |
| Max ($100/$200) | 15 | Più team paralleli (es. competitor-intel + sales-prospecting + content-radar) |
| Team / Enterprise | 25 | Use case aziendale multipli |

## Modificare i competitor o gli agenti

Se cambi `competitors.json` o uno dei file `.claude/agents/*.md`:

- Vai sul workspace cloud da claude.ai/code → upload del file modificato. La routine alla prossima run prenderà la versione aggiornata.

Nessuna modifica alla routine stessa è richiesta.

## Disabilitare temporaneamente

Da web: nella lista Routines, toggle off accanto al nome → la routine resta salvata ma non parte fino a quando non la riattivi.

Da CLI: `Disabilita la routine "Daily Competitor Brief"` (o il suo ID).

## Cancellare definitivamente

Da web: click sui 3 puntini → Delete.
Da CLI: `Cancella la routine [ID]` (l'ID è visibile dalla lista).
