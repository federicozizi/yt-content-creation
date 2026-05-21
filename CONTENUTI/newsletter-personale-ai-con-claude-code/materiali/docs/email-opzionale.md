# Ricevere la newsletter via email (opzionale)

Di default la newsletter è un file markdown in `newsletter/YYYY-MM-DD.md`. Se preferisci riceverla in casella email — così la apri dal telefono, dal tablet, ovunque — segui questa guida.

Richiede 5 minuti di setup una tantum.

## Cosa serve

- Un account Gmail (qualsiasi, anche quello personale)
- Una **App Password** Gmail (NON la tua password normale)

## 1. Crea l'App Password Gmail

L'App Password è una password speciale a 16 caratteri che Gmail genera per gli script esterni. È più sicura della password normale: la puoi revocare in qualsiasi momento senza cambiare la tua password vera, e funziona solo per app autorizzate.

Prerequisito: avere la **verifica in 2 passaggi** attiva sul tuo account Google.

1. Vai su https://myaccount.google.com/apppasswords
2. Login con la tua password Google normale
3. Nome dell'app: scrivi `Claude Newsletter`
4. Click "Crea"
5. Google ti mostra una password di 16 caratteri tipo: `abcd efgh ijkl mnop`
6. **Copia subito la password** in un posto sicuro — non te la mostra mai più

## 2. Crea il file `.env`

Nella cartella `materiali/` crea un file `.env` (copia da `.env.example` se preferisci):

```
GMAIL_USER=tuoindirizzo@gmail.com
GMAIL_APP_PASSWORD=abcd efgh ijkl mnop
DESTINATARIO=tuoindirizzo@gmail.com
```

`DESTINATARIO` può anche essere diverso da `GMAIL_USER` (es. la tua email aziendale).

**Importante**: `.env` è già escluso da `.gitignore`. Non rimuoverlo dall'elenco — se committi `.env` per sbaglio, devi revocare l'App Password e crearne una nuova (Gmail rivoca, in https://myaccount.google.com/apppasswords).

## 3. Aggiorna il prompt orchestratore

Apri `prompts/newsletter-daily.md` e aggiungi alla fine, dopo lo step 7:

```markdown
### 8. (Opzionale) Manda la newsletter via email

Se nella cartella esiste un file `.env` con `GMAIL_USER`, `GMAIL_APP_PASSWORD`, `DESTINATARIO`:
- Leggi i valori dal `.env`
- Manda il contenuto del file appena generato (`newsletter/YYYY-MM-DD.md`) come email HTML al `DESTINATARIO`
- Subject: `🧠 La tua AI Brief — <data leggibile>`
- Body: contenuto markdown convertito in HTML (usa una libreria standard tipo `marked` o equivalente)
- SMTP server: `smtp.gmail.com`, port 587, TLS

Se l'invio email fallisce, NON fallire l'intero run: la newsletter resta nel file system, segnala solo l'errore nel riepilogo finale.
```

## 4. Test

Rilancia il prompt orchestratore:

```bash
claude --print "$(cat prompts/newsletter-daily.md)"
```

Tra qualche secondo dovresti ricevere l'email. Se non arriva, controlla:
- Cartella spam
- Che `GMAIL_USER` e `DESTINATARIO` siano scritti senza errori
- Che l'App Password sia ancora attiva (https://myaccount.google.com/apppasswords)

## Quando NON serve l'email

Se sei una persona che ha sempre il PC aperto e ti basta aprire un file ogni mattina, salta tutto questo: il file markdown in `newsletter/` è già perfetto.

L'email serve se:
- Vuoi leggerla dal telefono mentre fai colazione
- Vuoi inoltrarla facilmente a colleghi
- Vuoi storicizzarla nella tua casella email come fai con le newsletter normali
