# Prompt orchestratore — Daily Competitor Brief

Stai eseguendo il **Daily Competitor Brief** di oggi.

## Cosa fare

1. Leggi `competitors.json` (3 competitor con `pricing_url`, `blog_url`, `linkedin_url`).
2. Per ogni competitor, in parallelo:
   - **Pricing**: apri `pricing_url`, estrai i piani correnti coi prezzi
   - **Features**: apri `blog_url`, estrai i blog post degli ultimi 7 giorni
   - **Social**: apri `linkedin_url`, estrai i top post (>50 reazioni, ≤7 giorni)
3. Sintetizza in `briefs/<data-oggi YYYY-MM-DD>.md` seguendo la struttura sotto.
4. Committa: branch `auto/<data>-brief`, messaggio `daily brief YYYY-MM-DD`. Apri PR contro `main`.

## Struttura output (`briefs/YYYY-MM-DD.md`)

```markdown
# Daily Competitor Brief — <data leggibile>

## TOP INSIGHT
1. ...
2. ...
3. ...

## Per competitor

### <Nome>
- 🟢/🔴/⚪ **Pricing**: <riga>
- 🟢/🟡 **Features**: <riga>
- 🔵/🟢 **Social**: <riga>

## Suggerimento azione (opzionale)
<1 frase, solo se emerge un'azione concreta>
```

## Regole

- Lingua: italiano
- Lunghezza max: 400 parole
- Niente prezzi/post inventati: se una pagina è inaccessibile, scrivi `N/D` e prosegui
- Niente narrazione lunga: bullet di fatti
