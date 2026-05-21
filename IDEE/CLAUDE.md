# IDEE/

Cartella che raccoglie tutte le **idee di contenuto** da cui partire per produrre un video. Due fonti:

## File

- **`manuali.md`** — idee scritte a mano dall'utente. Una sezione per idea, separate da `---`. Titolo descrittivo + descrizione libera.
- **`topics.md`** — appunti su macro-temi e angoli interessanti (campo libero).
- **`ricerche-auto/`** — cartella che contiene i file generati 2 volte al giorno dallo `/schedule` (ricerca automatica di contenuti virali rivisitati). Naming: `YYYY-MM-DD-mattina.md` e `YYYY-MM-DD-sera.md`.

## Formato delle idee in `manuali.md`

```markdown
## [Titolo sintetico, descrittivo, NON click-bait]

[Descrizione libera in parole povere: cosa vorresti mostrare, perche', tool coinvolti, eventuali POC, angolo.]

---
```

## Formato delle idee nei file di `ricerche-auto/`

Le ricerche automatiche producono ogni volta lo stesso template (vedi `RICERCA_AUTOMATICA/prompt-ricerca.md`):

```markdown
# Ricerca contenuti - YYYY-MM-DD [mattina|sera]

## Polso del momento
[3-5 bullet su cosa sta diventando virale sul settore in questo periodo, con fonte cliccabile]

## Idee proposte

### 1. [Titolo proposto]
**Angolo nuovo**: [perche' non e' una copia banale]
**Ispirato da**: [post/video/tweet virale con link]
**Format suggerito**: [build pratica / breakdown concettuale / case study / ecc.]
**Hook potenziale**: [una frase di apertura per il video]
**Target**: [chi e' lo spettatore]

### 2. ...
```

## Regole

- **Per l'utente**: nel `manuali.md` aggiungi/modifica/rimuovi liberamente. Il titolo descrive l'idea (NON e' ancora il titolo YouTube finale).
- **Non rinominare i file** — `manuali.md` e i file di `ricerche-auto/` sono cercati per nome dalle automazioni.
- **Non rimuovere il separatore `---`** tra idee in `manuali.md`.
- **Una idea per sezione**, niente sotto-idee dentro la stessa.

## Come Claude usa questa cartella

- `lavora sull'idea X` -> Claude cerca X **prima** in `manuali.md`, **poi** nei file piu' recenti di `ricerche-auto/`. Trovata l'idea, estrae titolo + descrizione (+ angolo nuovo, se viene da ricerca automatica) e procede a generare la cartella `CONTENUTI/<slug>/`.
- `che idee abbiamo` -> elenca titoli da `manuali.md` + ultimo file (per data) di `ricerche-auto/`.
- `idee di oggi` -> mostra il contenuto del file di `ricerche-auto/` di oggi (sia mattina che sera, se esistono).
