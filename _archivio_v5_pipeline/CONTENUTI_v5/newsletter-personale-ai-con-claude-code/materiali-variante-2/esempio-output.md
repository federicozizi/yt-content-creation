# Esempio newsletter prodotta da `newsletter.py` (Variante 2)

Output identico ai 2 metodi precedenti — è il punto: cambia solo come.

---

# 🧠 La tua AI Brief — venerdì 16 maggio 2026

## 3 novità di oggi

### 🚀 Claude Sonnet 4.7 disponibile in beta
- Aumento del 15% nelle prestazioni sui task di reasoning
- Nuovo modello "thinking" attivabile su richiesta
- Disponibile da subito su API e Claude.ai per i piani Pro e Max
- 🔗 https://www.anthropic.com/news/claude-sonnet-4-7

### 📄 Paper: "Constitutional AI v2"
- Aggiornamento al sistema di principi alla base del training
- Focus sulla trasparenza dei trade-off di sicurezza
- 🔗 https://www.anthropic.com/research/constitutional-ai-v2

### 🆕 [HN] Show HN: lightweight RSS aggregator in Rust
- Alternativa open source a Feedly, ~5MB binario
- Self-hosted, supporta sync via WebDAV
- 🔗 https://news.ycombinator.com/item?id=12345678

---

## Output di `python newsletter.py` in console

```
🚀 Avvio newsletter per 2026-05-16
📖 Anthropic News...
📖 Anthropic Research...
📖 Hacker News front page...

✅ Newsletter generata: newsletter/2026-05-16.md
   - 3 fonti consultate
   - 8 articoli letti
   - 3 articoli inclusi
   - 5 articoli scartati
   - 38.2 secondi totali
```

Nota: 38 secondi totali — più veloce della Variante 1 perché non c'è agent loop. Lo script controlla esplicitamente ogni passaggio.
