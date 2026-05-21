# Istruzioni persistenti per Claude Code

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali/CLAUDE.md` — sincronizzare ogni modifica.

Questo file viene letto **automaticamente** da ogni sessione Claude Code che parte dentro questa cartella. Definisce: cosa fa il sistema, in che tono scrivere, cosa scartare, come gestire lo stato.

## Cosa fa questo sistema

Newsletter giornaliera personale: ogni mattina alle 8, Claude visita le fonti elencate in `fonti.json`, identifica gli articoli nuovi (confrontando con `state.json`), li riassume in `newsletter/YYYY-MM-DD.md`, aggiorna lo stato.

## Tono della newsletter

- Italiano, diretto, colloquiale (come parla un imprenditore al collega)
- Max 3-5 bullet per articolo
- Max 1 riga per bullet
- Niente intro/outro generiche ("ecco le novità di oggi…", "buona lettura!")
- Niente aggettivi marketing ("rivoluzionario", "incredibile", "game-changer")
- Sempre il link originale alla fine di ogni articolo

## Cosa enfatizzare

- Numeri concreti (versioni, percentuali, prezzi, date)
- Cosa cambia per chi usa il prodotto/servizio
- Date di disponibilità o rilascio
- Eventuali breaking changes o deprecation

## Cosa scartare

- Annunci di partnership senza dettagli concreti
- Posizioni aperte, eventi sponsor, conference recap generici
- Articoli "filler" che ripetono cose già dette
- Roba già coperta dai run precedenti (controlla `state.json` prima)

## Gestione dello stato (`state.json`)

`state.json` è la memoria di lungo termine. Struttura:

```json
{
  "articoli_visti": [
    "https://www.anthropic.com/news/claude-sonnet-4-7",
    "https://www.anthropic.com/research/constitutional-ai-v2"
  ],
  "ultimo_run": "2026-05-16T08:00:00Z"
}
```

Regole:
- Prima di processare un articolo, controlla se l'URL è in `articoli_visti`
- Se sì → scarta (anche se sembra rilevante)
- Se no → processa e aggiungi l'URL a `articoli_visti` DOPO aver scritto la newsletter
- Aggiorna `ultimo_run` a ogni esecuzione

## Output

- File: `newsletter/YYYY-MM-DD.md` (data del run, YYYY-MM-DD)
- Se la data esiste già (es. test manuale ripetuto nello stesso giorno), **sovrascrivi** — è il run più recente che vale
- Formato: vedi `esempio-output.md`

## Stile

- Nessuna sigla o termine tecnico senza spiegazione di 3 parole
- Emoji 🚀 📄 🔧 🆕 ⚠️ per separare le sezioni — niente più di 1-2 emoji per articolo
- Mai prima persona ("Anthropic ha lanciato…", non "abbiamo lanciato…")
