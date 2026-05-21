# Esempio di newsletter prodotta dal sistema

Quello che vedi sotto è un esempio reale di come si presenta un file in `newsletter/YYYY-MM-DD.md` dopo un run riuscito. È esattamente quello che ti arriva sulla scrivania ogni mattina (o nella casella email, se hai attivato l'opzione email).

---

# 🧠 La tua AI Brief — venerdì 16 maggio 2026

## 3 novità di oggi

### 🚀 Claude Sonnet 4.7 disponibile in beta
- Aumento del 15% nelle prestazioni sui task di reasoning rispetto a 4.6
- Nuovo modello "thinking" attivabile su richiesta (parametro `enable_extended_thinking`)
- Disponibile da subito su API e Claude.ai per i piani Pro e Max
- 🔗 https://www.anthropic.com/news/claude-sonnet-4-7

### 📄 Paper: "Constitutional AI v2"
- Aggiornamento al sistema di principi alla base del training dei modelli
- Focus sulla trasparenza dei trade-off di sicurezza (safety vs helpfulness)
- Introduce nuove metriche di valutazione open-source
- 🔗 https://www.anthropic.com/research/constitutional-ai-v2

### 🔧 Claude Code 2.4.0 — nuova "Plan Mode"
- Modalità che separa pianificazione ed esecuzione del task
- Particolarmente utile per task complessi multi-step (refactoring, migrazioni)
- Attivabile con Shift+Tab durante una sessione
- 🔗 https://docs.claude.com/en/release-notes/claude-code

---
Generato in 47 secondi · 3 fonti consultate · 3 articoli nuovi · 2 articoli scartati (già visti nei run precedenti)

---

## Note su questo esempio

- **Giornata "media"**: 3 articoli rilevanti. In giornate scariche puoi avere 0-1 articolo. In giornate piene (lanci grossi, conferenze) puoi averne 8-10.
- **Tempo totale**: ~30-60 secondi per run, dipende dal numero di fonti e dalla velocità della rete.
- **Articoli scartati**: il sistema NON ti dice quali ha scartato (per non sporcare la newsletter), solo quanti. Se vuoi vederli, controlla `state.json` — gli URL aggiunti nell'ultimo run sono tutti quelli processati, sia inclusi sia scartati.

## Come si presenta una "giornata morta"

Se nessuna delle fonti ha novità nelle ultime 48 ore:

```markdown
# 🧠 La tua AI Brief — sabato 17 maggio 2026

Nessuna novità rilevante oggi. Tutte le 3 fonti consultate non hanno pubblicato nulla nuovo nelle ultime 48 ore.

---
Generato in 12 secondi · 3 fonti consultate
```

Sintetico e onesto. Niente news inventate per "riempire".
