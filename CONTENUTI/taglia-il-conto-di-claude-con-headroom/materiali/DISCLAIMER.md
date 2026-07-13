# ⚠️ Prima di condividere o caricare su GitHub — leggi

Questo progetto usa una **chiave API** (la tua chiave OpenRouter), scritta nel file `.env`.

## Regole, in ordine di importanza

1. **Non committare mai il file `.env`.**
   C'è già un `.gitignore` che lo esclude: lascialo dov'è. Il file da condividere è
   `.env.example`, che contiene solo un valore finto.

2. **La chiave vera sta SOLO nel tuo `.env`, sul tuo computer.**
   Non incollarla nel codice, nei messaggi, negli screenshot del video.

3. **Se la chiave finisce per sbaglio su GitHub: revocala e rigenerala subito.**
   Vai su [openrouter.ai/keys](https://openrouter.ai/keys), cancella quella vecchia e creane
   una nuova. Cancellarla dalla cronologia di git **non basta**: dei bot scansionano
   GitHub in continuazione e una chiave esposta va considerata già compromessa.

4. **Ogni chiamata a Opus costa qualche centesimo.**
   La demo fa due chiamate per click. Su OpenRouter puoi mettere un tetto di spesa.
