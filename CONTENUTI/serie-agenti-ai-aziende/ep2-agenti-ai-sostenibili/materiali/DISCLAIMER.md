# ⚠️ Importante — credenziali e sicurezza

Questo progetto usa una **chiave segreta** (`OPENROUTER_API_KEY`) salvata nel file `.env`.
Trattala come il PIN del bancomat: chi ce l'ha può spendere i tuoi soldi.

## Regole d'oro

1. **Non condividere mai il file `.env`.** Quando zippi o passi questa cartella a
   qualcuno, togli prima il `.env` (lascia solo `.env.example`, che contiene un valore
   finto).

2. **Non caricare mai `.env` su GitHub.** In questa cartella c'è già un file `.gitignore`
   che lo esclude: tienilo. Crea il `.gitignore` **prima** di fare `git init`, non dopo.

3. **Se la chiave finisce per sbaglio online — revocala e rigenerala subito.**
   Cancellarla dalla cronologia di Git **non basta**: dei programmi automatici (bot)
   scansionano GitHub in continuazione e copiano le chiavi nel giro di pochi secondi.
   L'unica cosa che ti mette al sicuro è andare su
   [openrouter.ai/keys](https://openrouter.ai/keys), **cancellare quella chiave** e
   crearne una nuova.

## Una nota sui dati delle recensioni

Le recensioni vengono inviate a OpenRouter, che le inoltra al modello scelto per
l'analisi. Se contengono **dati personali** dei tuoi clienti (nomi, contatti, dettagli
sensibili), valuta se anonimizzarle prima — è buona prassi e in molti casi è anche un
obbligo di legge (es. GDPR). Le politiche su come vengono trattati i dati dipendono dal
provider a cui OpenRouter instrada la richiesta: puoi controllarle e impostarle nel tuo
account OpenRouter. La responsabilità su *cosa* invii resta tua.
