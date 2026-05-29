# La routine schedulata

Il sistema è pensato per girare **da solo, in cloud, su una cadenza fissa**, senza che tu apra niente.

## Cosa fa, in una frase

A ogni esecuzione, Claude (Opus 4.8) legge `CLAUDE.md`, lancia gli scraper, interpreta i risultati
con 10 agenti in parallelo, **valuta se la raccolta è abbastanza ricca e — se no — rilancia**,
poi scrive un report di idee video in `IDEE/ricerche-auto/`.

## Il prompt della routine

È volutamente corto: tutta l'intelligenza sta in `CLAUDE.md`.

```
Sei nella cartella materiali/ del progetto yt-content-creation.
Assicurati di usare il modello Opus 4.8.
Esegui il ciclo descritto in CLAUDE.md, dalla Fase 1 alla Fase 4.
Al termine, scrivi il report in IDEE/ricerche-auto/ e fermati.
```

## Come si schedula

Con Claude Code, dal terminale del progetto:

```
/schedule
```

e descrivi la cadenza desiderata.
La routine remota eseguirà il prompt qui sopra alla cadenza scelta, anche a PC spento.

> Cadenza attiva: **1 volta al giorno, al mattino (ore 8:00)**. Un solo report giornaliero,
> leggero e pulito. I trend non cambiano ogni ora: uno scatto al mattino cattura le novità
> della notte e del giorno prima. Per aumentare la frequenza basta modificare lo scheduling.

## Perché una routine, e non un click manuale

Il valore non è "raccogliere trend" — quello lo fa anche uno script. Il valore è che **un agente
guarda i risultati e decide**: se mancano novità su Claude, allarga la ricerca; se uno scraper è
caduto, riprova; se la raccolta è povera, fa un altro giro. Si sveglia, lavora, valuta, consegna,
si ferma. Tu trovi il report pronto, già filtrato sui tuoi argomenti.
