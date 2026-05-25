# Prompt del task — Scraper Prezzi Competitor

Questo e' il prompt che cron lancia ogni notte alle 4. Lo trovi nel file `scraper-prompt.md` nella cartella `/home/claude/scraper/` del VPS.

Personalizza i 3 placeholder con i tuoi competitor reali prima del primo run.

---

## Prompt (copia da qui sotto)

```
Sei lo scraper di prezzi schedulato che gira sul VPS di produzione. Hai gia' letto CLAUDE.md di questo progetto e ne conosci le 5 regole operative. Le rispetti tassativamente.

OBIETTIVO: scansionare 3 siti competitor, estrarre prezzi dei prodotti monitorati, identificare variazioni > 5% rispetto al run precedente, e inviare un report via email se ci sono variazioni significative.

STEPS:

1. Apri il file di log e scrivi l'inizio della run:
   `echo "=== RUN START $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" >> /var/log/claude-scraper.log`

2. Leggi `/home/claude/scraper/competitors.json` per ottenere la lista dei competitor e dei prodotti chiave da monitorare. Il file ha questa struttura:
   ```json
   [
     {
       "name": "Competitor A",
       "url_base": "https://<<URL_COMPETITOR_1>>",
       "products": [
         { "sku": "...", "url": "https://<<URL_PRODOTTO_1_1>>", "selector_price": ".price-now" },
         ...
       ]
     },
     { "name": "Competitor B", "url_base": "https://<<URL_COMPETITOR_2>>", ... },
     { "name": "Competitor C", "url_base": "https://<<URL_COMPETITOR_3>>", ... }
   ]
   ```

3. Per ogni competitor, per ogni prodotto:
   - Usa WebFetch per scaricare la pagina prodotto
   - Estrai il prezzo usando il selettore CSS specificato
   - Salva nel database: `sqlite3 /home/claude/scraper/prezzi.db "INSERT INTO prezzi (competitor, sku, prezzo, data) VALUES ('<comp>', '<sku>', <prezzo>, '<oggi>')"`
   - Se WebFetch fallisce o il selettore non trova nulla, logga l'errore ma CONTINUA con gli altri prodotti (non bloccare la run intera)

4. Confronta i nuovi prezzi col prezzo precedente (query SQLite sulla penultima data per quello stesso sku/competitor). Calcola la variazione percentuale.

5. Identifica le variazioni > 5%. Per ognuna, prepara una riga del report:
   `[Competitor A] Prodotto X: 49.90 EUR -> 39.90 EUR (-20%)`

6. Genera un file di report `/home/claude/scraper/reports/<data>.md` con:
   - Riassunto: totale prodotti scansionati, errori, variazioni trovate
   - Sezione "Variazioni significative" con tutte le righe del punto 5
   - Sezione "BLOCKING ISSUES" se per qualche competitor il sito ha cambiato struttura HTML (selettori non funzionano per > 50% dei prodotti)

7. Se ci sono variazioni significative, invia il report via email al cliente:
   `mail -s "Report Prezzi Competitor - <data>" <<EMAIL_CLIENTE>> < /home/claude/scraper/reports/<data>.md`

8. Aggiorna `/home/claude/scraper/last_run_state.json` con:
   ```json
   {
     "last_run": "<timestamp ISO>",
     "status": "success | partial | failed",
     "products_scanned": N,
     "errors": N,
     "variations_found": N
   }
   ```

9. Chiudi il log:
   `echo "=== RUN END $(date -u +%Y-%m-%dT%H:%M:%SZ) | status: <status> | comandi: <N> ===" >> /var/log/claude-scraper.log`

REGOLE DA RICORDARE (dal CLAUDE.md):
- Mai sudo, mai rm -rf, mai modifiche fuori da /home/claude/scraper/
- Logging dettagliato (decisioni importanti, errori, variazioni trovate)
- Niente API key o password nei log
- Se rilevi BLOCKING ISSUE (es. sito cambiato radicalmente), segnalalo nel report ma NON cercare di risolverlo autonomamente

In dry-run (flag --dry-run): esegui tutta la logica ma NON scrivere nel database, NON inviare email, NON aggiornare last_run_state.json. Scrivi nel log "DRY RUN: avrei fatto X" per ogni operazione skippata.
```

---

## Placeholder da sostituire

1. **`<<URL_COMPETITOR_1>>`, `<<URL_COMPETITOR_2>>`, `<<URL_COMPETITOR_3>>`** — URL dei competitor che vuoi monitorare. Esempio: `amazon.it`, `eprice.it`, `mediaworld.it`.

2. **`<<URL_PRODOTTO_X_Y>>`** — URL specifico della pagina prodotto sul competitor. Devi prepararlo a mano la prima volta nel file `competitors.json`. Suggerimento: per 60 prodotti totali, dedica un'oretta al setup iniziale di `competitors.json` con tutti gli URL e selettori CSS.

3. **`<<EMAIL_CLIENTE>>`** — l'indirizzo email a cui mandare il report giornaliero. Puo' essere anche il tuo, all'inizio, finche' non verifichi che il report e' utile davvero.

---

## File `competitors.json` di esempio (versione minimale)

Crealo come `/home/claude/scraper/competitors.json`:

```json
[
  {
    "name": "Amazon",
    "url_base": "https://www.amazon.it",
    "products": [
      {
        "sku": "scarpa-running-nike",
        "url": "https://www.amazon.it/dp/EXAMPLE-ASIN-1",
        "selector_price": ".a-price-whole",
        "nome_leggibile": "Nike Air Zoom Pegasus 40"
      },
      {
        "sku": "scarpa-running-adidas",
        "url": "https://www.amazon.it/dp/EXAMPLE-ASIN-2",
        "selector_price": ".a-price-whole",
        "nome_leggibile": "Adidas Ultraboost 22"
      }
    ]
  }
]
```

Quando aggiungi un competitor, aggiungi un oggetto alla lista. Per ogni prodotto, l'unica cosa veramente specifica e' il selettore CSS — varia da sito a sito. Per identificarlo:

1. Apri la pagina prodotto del competitor nel browser
2. Tasto destro sul prezzo -> Inspect
3. Identifica la classe CSS che contiene il prezzo (es. `.price-now`, `.product-price`, `.a-price-whole`)
4. Inseriscila come `selector_price` nel JSON

Se il sito usa JavaScript pesante per renderizzare il prezzo, WebFetch (che fa solo HTML statico) potrebbe non vedere il prezzo. In quel caso devi cambiare strategia (es. usare un servizio di scraping piu' pesante tipo ScrapingBee). Per il 90% dei casi, WebFetch + selettore CSS funziona.
