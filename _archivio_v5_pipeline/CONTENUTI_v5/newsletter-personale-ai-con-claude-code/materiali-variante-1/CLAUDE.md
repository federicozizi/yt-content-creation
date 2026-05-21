# Istruzioni persistenti per la newsletter

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali-variante-1/CLAUDE.md` — sincronizzare ogni modifica.

Questo file è caricato dallo script `newsletter.py` e concatenato al prompt di sistema dell'Agent Claude. Definisce: tono, cose da enfatizzare, cose da scartare, gestione stato.

## Cosa fa il sistema

Newsletter giornaliera personale: ogni mattina, l'Agent visita le fonti elencate in `fonti.json`, identifica articoli nuovi (confrontando con `state.json`), li riassume in `newsletter/YYYY-MM-DD.md`.

## Tono della newsletter

- Italiano, diretto, colloquiale (come parla un imprenditore al collega)
- Max 3-5 bullet per articolo
- Max 1 riga per bullet
- Niente intro/outro generiche
- Niente aggettivi marketing
- Sempre il link originale alla fine di ogni articolo

## Cosa enfatizzare

- Numeri concreti (versioni, percentuali, prezzi, date)
- Cosa cambia per chi usa il prodotto
- Date di disponibilità o rilascio
- Breaking changes o deprecation

## Cosa scartare

- Annunci di partnership senza dettagli concreti
- Posizioni aperte, eventi sponsor, conference recap generici
- Articoli filler che ripetono cose già dette
- Roba già coperta dai run precedenti (controlla `state.json` prima)

## Gestione dello stato (`state.json`)

```json
{
  "articoli_visti": ["url1", "url2"],
  "ultimo_run": "2026-05-16T08:00:00Z"
}
```

Regole:
- Prima di processare → controlla se l'URL è in `articoli_visti`
- Se sì → scarta
- Se no → processa, aggiungi a `articoli_visti` DOPO aver scritto la newsletter
- Aggiorna `ultimo_run` a ogni esecuzione

## Output

- File: `newsletter/YYYY-MM-DD.md`
- Se la data esiste già → sovrascrivi
- Formato: vedi `esempio-output.md`

## Stile

- Niente sigle senza spiegazione di 3 parole
- Emoji 🚀 📄 🔧 🆕 per categorie — max 1-2 per articolo
- Mai prima persona ("Anthropic ha lanciato…", non "abbiamo lanciato…")
