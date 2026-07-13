# Agenti AI sostenibili — Analizza centinaia di recensioni spendendo pochi centesimi

Serie **"Agenti AI per aziende veri, zero fuffa"** — Episodio 2.

In questa cartella hai un sistema che analizza un mucchio di recensioni di clienti
**senza svuotarti il portafoglio**. Il trucco non è usare l'AI più potente per tutto:
è usare **il modello giusto al posto giusto**.

> **L'idea in una frase.** Per leggere centinaia di recensioni che si assomigliano ti
> serve un dipendente veloce ed economico, non un dirigente strapagato. Il dirigente lo
> chiami solo per i due o tre casi spinosi. Qui dentro facciamo esattamente questo, con
> tre "strati" che lavorano insieme.

---

## I tre strati (spiegato semplice)

1. **Il modello economico** (Claude Haiku) → lo *stagista veloce*. Legge **ogni**
   recensione e la inquadra in una scheda: che voto esprime, di che tema parla (pulizia,
   colazione, rumore...), se il tono è positivo o negativo. Costa pochissimo, ed è
   perfetto per il lavoro di volume.
2. **Lo script** (codice normale, Python) → la *calcolatrice e le procedure*. Fa le cose
   meccaniche che non richiedono intelligenza: somma, calcola la media, conta i temi, e
   **decide quali pochi casi meritano il modello potente**. Gira sul tuo PC: costo zero,
   e non sbaglia mai i conti.
3. **Il modello smart** (Claude Opus) → il *senior che chiami solo per i casi difficili*.
   Interviene **solo** sulle poche recensioni gravi o ambigue (un reclamo, una minaccia,
   un rimborso): le valuta con calma, ragionando, e ti propone come rispondere. Costa di
   più, ma lo usi su pochissimi casi, quindi il conto resta leggero.

**Perché "sostenibile"?** Perché un agente che costa pochi centesimi a giro lo puoi
davvero tenere acceso tutti i giorni, in azienda, sul serio — non solo per una demo. La
sostenibilità non è un dettaglio tecnico: è ciò che separa il giocattolo dallo strumento
di lavoro.

---

## Quick start (5 passi)

1. **Installa Python** (versione 3.10 o successiva) da [python.org](https://www.python.org/downloads/). Su Windows, durante l'installazione spunta *"Add Python to PATH"*.
2. **Apri questa cartella** con VS Code e apri il terminale integrato (menu *Terminale → Nuovo terminale*).
3. **Installa i pacchetti**: nel terminale scrivi `pip install -r requirements.txt`.
4. **Crea la chiave** (vedi sotto "La chiave che ti serve"), poi copia `.env.example` in `.env` e incolla il tuo valore.
5. **Avvia l'analisi**: `python analizza_recensioni.py`. Guarda scorrere i tre strati e, alla fine, il conto dei costi.

---

## La chiave che ti serve

Il programma usa **OpenRouter**: una sola chiave che dà accesso a *tutti* i modelli, così
puoi cambiare modello quando vuoi (per questo episodio usiamo modelli **Anthropic**). La
metti nel file `.env` (mai a video, mai su GitHub).

1. Vai su [openrouter.ai/keys](https://openrouter.ai/keys), accedi e crea una chiave.
2. Copia la chiave (inizia con `sk-or-v1-...`).
3. In VS Code, fai una copia di `.env.example` e rinominala in `.env` (togli `.example`).
4. Apri `.env` e incolla la tua chiave al posto del valore di esempio (riga `OPENROUTER_API_KEY=`).

> Pensa a questa chiave come al **PIN del bancomat**: chi ce l'ha può spendere i tuoi soldi. Tienila segreta. Leggi `DISCLAIMER.md`.
>
> Nota: su OpenRouter carichi un piccolo credito e paghi a consumo. L'analisi di esempio costa pochi centesimi.

---

## Cosa c'è nella cartella

- `analizza_recensioni.py` → il programma con i tre strati.
- `recensioni.csv` → le recensioni di esempio (un B&B inventato). **Sostituiscile con le tue**: stessa struttura, due colonne `autore` e `testo`.
- `.env.example` → il modello del file delle credenziali.
- `requirements.txt` → i pacchetti da installare.
- `report.md` → **lo crea il programma** quando lo lanci: è il riepilogo leggibile (medie, temi, casi delicati con la risposta suggerita).

---

## Come si legge il "conto" alla fine

Quando il programma finisce, stampa una tabellina come questa (i numeri variano):

```
                IL CONTO (quello che conta)
========================================================
Recensioni analizzate: 30
  Strato 1 - anthropic/claude-haiku-4-5: $0.0131
  Strato 2 - script (sul tuo PC):      $0.0000
  Strato 3 - anthropic/claude-opus-4-8:  $0.0487
  --> TOTALE del sistema:              $0.0618
--------------------------------------------------------
  Se usassi il modello smart per OGNI recensione: ~$0.4900
  --> Così costa circa 8 volte di meno.
```

Lo "strato 2" costa **zero**: è codice che gira sul tuo computer. Ed è proprio lì il
risparmio nascosto — un sacco di lavoro (contare, fare medie, decidere) non ha bisogno di
nessuna AI, basta uno script.

> Il confronto "se usassi il modello potente per OGNI recensione" è una **stima onesta**:
> prende quanto costa in media un caso trattato dal modello smart e lo moltiplica per
> tutte le recensioni. È lo scenario di chi, per pigrizia, dà il trattamento di lusso a
> tutto. Il numero esatto dipende da quante recensioni finiscono dal modello smart.

---

## Personalizza (le 3 leve)

Apri `analizza_recensioni.py` con VS Code. In cima trovi tre cose facili da cambiare:

- **`MODELLO_ECONOMICO` / `MODELLO_SMART`** → quali due modelli usare (nomi in stile
  OpenRouter, es. `anthropic/claude-haiku-4-5`). Per l'Ep2 restiamo su modelli Anthropic;
  puoi comunque sceglierne un altro (es. più economico o più recente) cambiando solo la riga.
- **`MAX_CASI_SMART`** → il tetto massimo di recensioni che possono finire dal modello
  smart. È il tuo freno a mano sui costi: anche se qualcosa va storto, non spenderai più
  del previsto.
- **I temi nella "scheda"** (`tema_principale`) → cambia la lista dei temi con quelli del
  tuo settore (un e-commerce avrà "spedizione", "imballo", "assistenza"...).

Poi sostituisci `recensioni.csv` con le tue recensioni vere: stesse due colonne.

---

## Cosa fa e cosa NON fa (onestà, zero fuffa)

**Fa:**
- Inquadra centinaia di recensioni a costo bassissimo (lo strato economico).
- Aggrega e calcola senza errori e senza spendere nulla (lo strato script).
- Dà l'attenzione del modello potente solo dove serve davvero (i casi delicati).

**NON fa (e va detto):**
- "Sostenibile" non vuol dire **gratis**: ogni parola letta o scritta dall'AI si paga.
  Vuol dire che il conto è abbastanza basso da reggere nel tempo.
- Il modello economico **può sbagliare** un inquadramento: per questo lo script fa da
  rete (controlla, conta) e i casi spinosi passano comunque al modello smart.
- La bozza di risposta che il modello smart propone per i reclami è un **punto di
  partenza**, non l'ultima parola: la decisione su un cliente arrabbiato resta a un umano.

---

## Problemi comuni

- **`ModuleNotFoundError`** → hai saltato il passo `pip install -r requirements.txt`.
- **`FileNotFoundError: recensioni.csv`** → stai lanciando il programma dalla cartella
  sbagliata. Assicurati che il terminale sia aperto **dentro** la cartella `materiali`.
- **Errore di autenticazione (401)** → la `OPENROUTER_API_KEY` in `.env` è sbagliata,
  incompleta, o hai lasciato il valore di esempio.
- **Errore "insufficient credits" / 402** → ricarica un piccolo credito su
  [openrouter.ai](https://openrouter.ai) (è prepagato, paghi a consumo).
- **Il conto ti sembra alto** → hai troppe recensioni che finiscono dal modello smart.
  Abbassa `MAX_CASI_SMART`, oppure rendi più severo il criterio di `serve_revisione` nel
  testo che diamo al modello economico.
- **Vedi comparire una cartella `__pycache__`** → è normale, la crea Python da sola. È già
  esclusa da Git.
