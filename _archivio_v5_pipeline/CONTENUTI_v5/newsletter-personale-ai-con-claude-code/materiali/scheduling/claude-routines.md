# Schedulare la newsletter con Claude Routines

Claude Routines è il sistema di scheduling integrato in Claude Code. Esegue prompt a orari ricorrenti senza che il PC debba avere qualcosa di particolare aperto — basta che sia acceso e che Claude Code sia installato.

## Quick start

```bash
# Dalla cartella materiali
cd /path/to/materiali

# Crea la routine "daily-newsletter": ogni giorno alle 8:00
claude routines add daily-newsletter \
  --schedule "0 8 * * *" \
  --cwd "$(pwd)" \
  --prompt "esegui prompts/newsletter-daily.md"
```

Spiegazione dei parametri:
- `daily-newsletter` → nome della routine (deve essere unico)
- `--schedule "0 8 * * *"` → sintassi cron: minuti, ore, giorno-del-mese, mese, giorno-settimana. `"0 8 * * *"` = ogni giorno alle 8:00
- `--cwd "$(pwd)"` → directory di lavoro (deve essere la cartella materiali, dove vivono `fonti.json` e gli altri file)
- `--prompt "..."` → il prompt da eseguire

## Verifiche

```bash
# Lista routine attive
claude routines list
```

Output atteso:
```
📋 Active routines:
   • daily-newsletter — every day at 08:00 — next: tomorrow 08:00
```

```bash
# Run manuale (per testare senza aspettare l'orario)
claude routines run daily-newsletter
```

## Cambiare orario

```bash
# Esempio: spostare a 18:00
claude routines edit daily-newsletter --schedule "0 18 * * *"
```

## Disattivare temporaneamente

```bash
claude routines pause daily-newsletter
# riattivare:
claude routines resume daily-newsletter
```

## Cancellare definitivamente

```bash
claude routines remove daily-newsletter
```

## Esempi di schedule più comuni

| Quando | Espressione cron |
|---|---|
| Ogni giorno alle 8:00 | `"0 8 * * *"` |
| Solo nei giorni lavorativi (lun-ven) alle 8 | `"0 8 * * 1-5"` |
| Ogni lunedì alle 9 | `"0 9 * * 1"` |
| Due volte al giorno (8 e 18) | `"0 8,18 * * *"` |
| Ogni 3 ore | `"0 */3 * * *"` |

Se non sei sicuro, usa https://crontab.guru/ per verificare l'espressione.

## Quando NON usare Claude Routines

- **Se il tuo PC è spento**: Routines gira solo se Claude Code è attivo sulla tua macchina. Se vuoi un sistema che gira anche a PC spento, serve scheduling cloud (es. GitHub Actions — vedi video dedicato).
- **Se sei su un server senza Claude Code installato**: usa cron Linux direttamente. Vedi `crontab-example.txt`.
