<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-and-antigravity/materiali/prompts/antigravity-parallel-draft.md -->

# Prompt per Antigravity — drafting parallelo di varianti

Questo è il prompt che incolli **in ognuna delle 3 sessioni agente** che spawni in Antigravity. L'unica cosa che cambia tra le 3 sessioni è la parola `<<STILE>>`.

---

## Setup nel workspace Antigravity

1. Crea un nuovo workspace (es. `homepage-refresh-<nome-progetto>`).
2. Carica il file `index.html` di partenza (la home attuale che vuoi rifare).
3. Spawna 3 sessioni agente, tutte sullo stesso file di partenza.
4. In ognuna incolla il prompt sotto, sostituendo `<<STILE>>` con uno dei tre valori:
   - `corporate` (formale, monocromatico, focus su trust)
   - `amichevole` (colori caldi, immagini di persone, tono conversazionale)
   - `aggressive` (claim grossi, urgenza, CTA dominante)
5. Premi invio in tutte e tre. Lavorano in parallelo.

---

## PROMPT da incollare in ogni sessione

```
Sei un designer/copywriter senior. Hai a disposizione l'index.html caricato nel workspace, che è la home page di un sito esistente.

Il tuo compito: produrre una NUOVA versione di index.html in stile <<STILE>>.

VINCOLI:
- Mantieni il SIGNIFICATO della pagina: chi è il brand, cosa offre, perché contattarlo. Cambia tono e visual, non la sostanza.
- Mantieni la STRUTTURA semantica: header, hero, sezioni principali, footer. Non aggiungere sezioni nuove a meno che lo stile <<STILE>> non le richieda esplicitamente.
- Mantieni i NOMI dei link nel menu (es. se c'erano "Chi siamo", "Servizi", "Contatti", devono restare quelli — l'href può anche essere "#" per ora, ma le label sono fisse).
- NIENTE script esterni, NIENTE chiamate CDN, NIENTE Google Fonts. Solo CSS inline o in <style>.
- File singolo HTML self-contained. Stesso nome: index.html.

INTERPRETAZIONE DELLO STILE <<STILE>>:
- "corporate": palette monocromatica (grigi + 1 accento blu/navy), tipografia sans-serif sobria, copy autorevole, frasi corte, claim che parlano di affidabilità ed esperienza, CTA secondaria rispetto al contenuto.
- "amichevole": palette calda (rosso/arancio/giallo desaturati su sfondo crema), tipografia rounded o serif friendly, copy in seconda persona, micro-storie, claim che parlano di relazione e supporto, CTA "iniziamo insieme".
- "aggressive": palette ad alto contrasto (nero + 1 accento neon), tipografia bold e grande, copy in maiuscolo per i claim, numeri e percentuali in evidenza, sensazione di urgenza, CTA dominante e ripetuta.

DELIVERABLE:
1. L'index.html riscritto (file unico, pronto al rendering).
2. Una preview renderizzata (Antigravity lo fa di default — assicurati che sia visibile nel workspace).
3. In coda al file, in un commento HTML, scrivi 2 righe: lo stile applicato e una frase che spiega la scelta principale di tono ("ho puntato su X perché Y").

Lavora in autonomia. Quando hai finito, NON pubblicare nulla — lascia l'artefatto pronto al download nel workspace.
```

---

## Cosa aspettarsi

- Tempo medio per agente: 2-4 minuti.
- I 3 agenti girano in parallelo: il tempo totale di attesa è quello del più lento, non la somma.
- Ognuno produce 1 file HTML + 1 preview renderizzata + 1 screenshot.
- Tu non interrompi — Antigravity ti notifica quando ognuno è pronto.

## Cosa fare dopo

1. Apri le 3 preview nel workspace, affianca le finestre.
2. Scegli quella che ti convince di più (con l'occhio, non leggendo il codice).
3. Click destro sull'artefatto vincente → "Download artifact" → salvalo come `landing-vincitrice.html` nella cartella del tuo sito (sottocartella `_da_antigravity/`).
4. (Opzionale) Scarica anche gli altri 2 come `landing-<stile>.html` se vuoi archiviarli.
5. Torna sul tuo PC, apri Claude Code nella cartella del sito, e usa il prompt in `claude-code-handoff.md` per l'integrazione finale.
