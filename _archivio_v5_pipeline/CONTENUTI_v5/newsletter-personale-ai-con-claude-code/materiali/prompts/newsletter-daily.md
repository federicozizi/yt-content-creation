# Prompt orchestratore — Newsletter AI personale

Stai generando la newsletter personale di oggi. Segui i passi sotto in ordine. Ricorda: `CLAUDE.md` definisce tono, formato e cose da scartare — leggilo se non lo hai già in contesto.

## Cosa fare

### 1. Carica lo stato corrente

Leggi `state.json`. Memorizza:
- `articoli_visti`: la lista di URL già processati nei run precedenti
- `ultimo_run`: timestamp dell'ultimo run riuscito

### 2. Carica le fonti

Leggi `fonti.json`. Memorizza l'elenco di fonti con `nome`, `url`, `categoria`.

### 3. Visita ogni fonte (in parallelo)

Per ogni fonte in `fonti.json`:
- Apri l'URL (`WebFetch`)
- Estrai la lista degli articoli pubblicati con: titolo, URL, data
- Filtra: tieni solo articoli pubblicati nelle ultime 48 ore E NON presenti in `articoli_visti`

### 4. Approfondisci ogni nuovo articolo

Per ogni articolo che ha superato il filtro:
- Apri il suo URL completo (`WebFetch`)
- Estrai il contenuto rilevante (saltando navigation, footer, related links)
- Riassumi in 3-5 bullet seguendo le regole di `CLAUDE.md` (sezione "Tono")
- Applica i criteri "Cosa enfatizzare" e "Cosa scartare" di `CLAUDE.md`

Se un articolo, dopo lettura, ricade nei criteri di scarto (filler, partnership senza dettagli, ecc.): salta. Non includerlo, ma aggiungilo comunque a `articoli_visti` per non riprocessarlo domani.

### 5. Componi il file newsletter

Crea `newsletter/YYYY-MM-DD.md` (data del run, formato ISO).

Struttura:

```markdown
# 🧠 La tua AI Brief — <giorno> <data leggibile in italiano>

## <N> novità di oggi

### <emoji categoria> <Titolo articolo 1>
- <bullet 1>
- <bullet 2>
- <bullet 3>
- 🔗 <URL originale>

### <emoji categoria> <Titolo articolo 2>
...

---
Generato in <X> secondi · <N> articoli letti · <M> articoli scartati (già visti o filtrati)
```

Emoji per categoria:
- 🚀 product (lanci, feature, model release)
- 📄 research (paper, white paper)
- 🔧 changelog (note di rilascio)
- 🆕 altre categorie aggiunte dall'utente in `fonti.json`

Se non ci sono novità da riportare oggi:

```markdown
# 🧠 La tua AI Brief — <data>

Nessuna novità rilevante oggi. Tutte le <N> fonti consultate non hanno pubblicato nulla nuovo nelle ultime 48 ore.

---
Generato in <X> secondi · <N> fonti consultate
```

Non inventare news per "riempire" — se è giornata morta, è giornata morta.

### 6. Aggiorna lo stato

Modifica `state.json`:
- Aggiungi a `articoli_visti` TUTTI gli URL processati oggi (sia quelli inclusi nella newsletter sia quelli scartati post-lettura — l'importante è non riproporli)
- Aggiorna `ultimo_run` al timestamp ISO 8601 corrente (es. `"2026-05-16T08:00:00Z"`)

### 7. Chiama i sub-agent del team

A questo punto, il file `newsletter/YYYY-MM-DD.md` esiste. Adesso passi il testimone al team di sub-agent specializzati che vivono in `.claude/agents/`:

**Se K (articoli inclusi) == 0** → chiama il sub-agent `empty-day-rescue`:
> "Lancia empty-day-rescue. Il file newsletter di oggi è vuoto. Pesca 1-2 approfondimenti dalle fonti secondarie in fonti-fallback.json e aggiungili al file."

Aspetta che finisca. Lui leggerà il suo file istruzioni in `.claude/agents/empty-day-rescue.md`, farà il lavoro, modificherà il file newsletter aggiungendo una sezione "📚 Approfondimenti del giorno", aggiornerà `state.json`.

**Sempre, anche se K > 0** → chiama il sub-agent `major-update-spotter`:
> "Lancia major-update-spotter sul file newsletter/YYYY-MM-DD.md. Verifica se c'è almeno un major update (nuovo modello, nuovo tool/servizio, breaking change) e, in caso, evidenzialo in cima al file."

Aspetta che finisca. Lui leggerà il suo file istruzioni in `.claude/agents/major-update-spotter.md`, classificherà i contenuti, e se troverà major update aggiungerà un box `🚨 MAJOR UPDATE` in cima al file.

### 8. Stampa riepilogo finale

Dopo che entrambi i sub-agent hanno finito, in console stampa:

```
✅ Newsletter generata: newsletter/YYYY-MM-DD.md
   - N fonti primarie consultate
   - M articoli nuovi trovati
   - K articoli inclusi
   - L articoli scartati (filler/già visti)
   - <empty-day-rescue: invocato/saltato — eventuali contenuti aggiunti>
   - <major-update-spotter: N major update evidenziati / nessun major update>
   - Tempo totale: <X> secondi
```

## Regole assolute

- **Lingua output**: italiano (a meno che `CLAUDE.md` non dica diversamente)
- **Mai inventare contenuti**: se non puoi leggere un articolo, segnalalo nel riepilogo finale ma non scriverne il riassunto
- **Mai duplicare**: prima di processare, controlla `articoli_visti`
- **Mai modificare manualmente `fonti.json`**: è l'utente che lo modifica, tu lo leggi e basta
- **Sub-agent obbligatori**: lo step 7 NON è opzionale. Il team di sub-agent è parte integrante del flow. Se Claude Code non riconosce i sub-agent (es. cartella `.claude/agents/` mancante), segnalalo nel riepilogo finale ma non bloccare l'esecuzione del resto.
