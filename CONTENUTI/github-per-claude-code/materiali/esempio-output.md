# Esempio di esecuzione — cosa vedi quando il sistema gira

## 1. La GitHub Action parte da sola alle 7:05

Vai sul tab **Actions** del repo. Vedi la run `Daily Competitor Brief` con stato 🟢:

```
✓ Checkout repo
✓ Setup Node
✓ Install Claude Code CLI
✓ Run Claude Code with daily-brief prompt
✓ Open PR with the brief
```

## 2. Trovi una PR aperta automaticamente

Tab **Pull requests** del repo:

```
📊 Daily Competitor Brief — auto                    #42
   auto/daily-brief-7821 → main
   bot: github-actions
```

## 3. Apri la PR e leggi il brief

Il diff mostra un nuovo file: `briefs/2026-05-08.md`:

```markdown
# Daily Competitor Brief — giovedì 8 maggio 2026

## TOP INSIGHT
1. Acme ha alzato Pro €49 → €56 (+15%)
2. Beta Inc ha lanciato l'integrazione Notion ieri
3. Gamma Co ha pubblicato un case study con 310 reazioni

## Per competitor

### Acme
- 🔴 **Pricing**: Pro €49 → €56 (+15%)
- 🟡 **Features**: nessun annuncio ultimi 7gg
- 🔵 **Social**: 2 post settimanali, engagement medio

### Beta Inc
- ⚪ **Pricing**: invariato
- 🟢 **Features**: integrazione Notion live dal 7 maggio
- 🔵 **Social**: top post Notion (180 reactions)

### Gamma Co
- ⚪ **Pricing**: invariato
- 🟡 **Features**: nessun annuncio
- 🟢 **Social**: case study "ABC Corp" (310 reactions)

## Suggerimento azione
Pubblica oggi un confronto pricing vs Acme: il loro +15% è un'apertura.
```

## 4. Lo mergi (se OK)

Click `Merge pull request`. Il brief entra in `main`. Il giorno dopo, alle 7:05, ne arriva uno nuovo.

---

## Esempio del flusso "issue → task automatico"

1. Apri una issue: *"Aggiungi anche Delta Corp come 4° competitor"*
2. Aggiungi label `claude-task`
3. 30-60 secondi dopo, GitHub Action ha aperto una PR che modifica `competitors.json` aggiungendo Delta Corp
4. Tu revisioni la PR e mergi
