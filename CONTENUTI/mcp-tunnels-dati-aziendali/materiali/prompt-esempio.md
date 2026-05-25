# Prompt di esempio da provare in chat Claude (con Supabase MCP collegato)

Tutti i prompt qui sotto presuppongono che tu abbia:
1. Eseguito gli script `schema-magazzino.sql` e `esempio-magazzino.sql` sul tuo Supabase
2. Collegato Supabase a Claude da [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)

Copia e incolla ogni prompt in una **nuova chat** su [https://claude.ai](https://claude.ai).

> **Nota importante**: il dataset contiene **5 anomalie deliberate** che Claude scopre rispondendo ai prompt da #3 in avanti. Vediamo come stare dietro alla salute reale di un magazzino — non un esercizio teorico.

---

## Livello 1 — Esplorare il magazzino

> "Che tabelle ho nel database collegato? Spiegami a cosa servono."

> "Quanti vini ho nel catalogo e qual e' il valore totale del magazzino, calcolato a prezzo di vendita?"

> "Mostrami la ripartizione del catalogo per regione di provenienza, con numero di referenze e valore totale per regione."

---

## Livello 2 — Bestseller e tendenze

> "Quali sono i 5 vini che hanno venduto di piu' negli ultimi 30 giorni? Mostrami quantita' totale, numero di ordini, ricavo."

> "Confronta le vendite degli ultimi 30 giorni con i 30 giorni precedenti. Quali prodotti stanno crescendo e quali stanno calando?"

> "Quanto incido tramite ogni canale (sito / amazon / enoteca / wholesale)? Percentuali sul totale ultimi 90 giorni."

---

## Livello 3 — Bestseller a rischio di rottura stock

> "Ho prodotti che stanno per esaurirsi senza che me ne accorga? Confronta vendite recenti (ultimi 30 giorni) e giacenza attuale. Considera 'a rischio' i prodotti dove la giacenza coprira' meno di 21 giorni di vendita."

Cosa scopre: Chianti, Vermentino, Lambrusco — vendite intense, scorte sotto soglia. Da riordinare entro la settimana per non perdere fatturato.

---

## Livello 4 — Errori tariffari (vendi sotto costo)

> "Verifica se ci sono prodotti dove sto vendendo sotto costo. Mostrami nome, prezzo di vendita, costo di acquisto, perdita per bottiglia, e quante bottiglie ho gia' venduto a perdere negli ultimi 90 giorni."

Cosa scopre: Barolo e Champagne hanno prezzo < costo. Calcolo della perdita gia' generata + suggerimento di re-pricing.

---

## Livello 5 — Esauriti che il sito sta promettendo lo stesso

> "Ci sono prodotti esauriti (giacenza zero) che pero' risultano ancora ordinabili online (visibile_online = TRUE)? Questi sono casi dove sto promettendo vendite impossibili. Lista completa."

Cosa scopre: Prosecco, Pinot Grigio Friulano, Moscato d'Asti — andati esauriti ma ancora visibili sul sito. Se non li nascondi, accetti ordini che non puoi consegnare.

---

## Livello 6 — Magazzino morto (capitale immobilizzato)

> "Quali prodotti sono fermi senza vendite da piu' di 180 giorni? Voglio sapere il capitale immobilizzato totale (giacenza per costo di acquisto) e suggerimenti su cosa fare (es. promozione svuotamagazzino, dismissione, ecc.)."

Cosa scopre: Aglianico, Cannonau, Ribolla Gialla, Marsala (mai venduto!), Refosco. Calcolo del capitale fermo + idee per liberare cassa.

---

## Livello 7 — Sintesi-azione "lunedi' mattina"

> "Generami un'analisi 'salute magazzino' completa in formato dashboard markdown. Voglio le 5 cose piu' importanti da sistemare questa settimana, in ordine di impatto economico, con il dato in euro per ognuna. Aggiungi un riassunto da 3 righe da mandare al mio commercialista."

Questo prompt e' il piu' utile in assoluto: chiede a Claude di mettere insieme tutto e darti un piano operativo settimanale. Output: una pagina con priorita', euro coinvolti, azioni concrete.

---

## Livello 8 — Combinazioni con altri MCP (richiede Gmail / Google Workspace collegato)

> "Per ogni prodotto in esaurimento del livello 3, scrivi una bozza di email al produttore — tono professionale ma cordiale — per ordinare le scorte. Salva ogni email come bozza Gmail nella cartella Drafts. NON inviare."

> "Per ogni prodotto del magazzino morto del livello 6, suggerisci un'azione di marketing concreta (es. offerta in newsletter, sconto a clienti vip, dismissione). Genera per i primi 3 un draft di email newsletter con titolo + corpo, salvato in Gmail Drafts."

---

## Cose che il modello NON dovrebbe fare (e perche')

- **Scrivere/modificare/cancellare dati** se hai scelto "solo lettura" durante il primo collegamento. Resta cosi' per le prime settimane.
- **Mandare email vere ai produttori senza la tua revisione.** Le email sono SEMPRE come bozza nella cartella Drafts. Tu riguardi una per una e clicchi Invia.
- **Sostituirsi al tuo giudizio commerciale.** Claude trova le anomalie nei numeri. Tu decidi cosa fare con quei numeri (es. dismissione di un vino e' decisione tua, non sua).
