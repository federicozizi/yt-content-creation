# CONTENT_IDEA_DATABASE

Lista di **idee di contenuto** scritte e mantenute manualmente dall'utente. È il punto di partenza della pipeline.

## Cosa contiene

`ideas.md` — file unico in formato markdown con TUTTE le idee. Una sezione per ogni idea, separate da `---`.

## Formato di ogni idea

```markdown
## [Titolo sintetico, NON click-bait, descrittivo]

[Descrizione in parole povere di cosa l'utente vorrebbe fare in quel video. Può essere lunga o breve, in linguaggio naturale, senza struttura rigida. Spiega l'obiettivo, l'angolo, eventuali tool da usare, se è già stato fatto un POC, ecc.]

---
```

**Esempio:**

```markdown
## Come creare un team di agenti AI con Claude Code

Vorrei mostrare come si crea un team di sub-agenti specializzati che collaborano tra loro. Tipo un agente per la ricerca, uno per la scrittura, uno per il review. Vogliamo dimostrare che si può con Claude Code in modo pulito, ognuno fa il suo pezzo. L'aspetto pratico mi interessa molto: quali file creare, come orchestrarli, esempi reali. Il pubblico deve capire che è una cosa che possono replicare.

---
```

## Regole

- **Per l'utente**: aggiungi/modifica/rimuovi liberamente. Il titolo deve essere descrittivo dell'idea (NON ancora il titolo finale del video — quello sarà più punchy/click-friendly e verrà generato dopo). La descrizione è in linguaggio naturale, conta il senso non la forma.
- **Non rinominare il file**: deve restare `ideas.md`. Le automazioni lo cercano per nome.
- **Non rimuovere il separatore `---`** tra idee diverse.
- **Una idea per sezione**, niente sotto-idee dentro la stessa sezione (se ci sono varianti, fanne 2 idee separate).

## Come Claude (le automazioni) usa questo file

- Quando l'utente dice "lavora sull'idea X" o "fai il giro completo per X":
  - Claude apre `ideas.md`, identifica l'idea (per match parziale del titolo)
  - Estrae **titolo** + **descrizione**
  - Passa entrambi all'AUTOMAZIONE_GUIDA come input

- Quando l'utente dice "che idee ci sono?":
  - Claude legge il file e mostra la lista dei titoli
