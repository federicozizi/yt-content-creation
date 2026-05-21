# Disclaimer - Credenziali e sicurezza

> **Includi questo file SOLO se il contenuto usa `.env`, API key, token o qualsiasi credenziale.**
> Se il video e' puramente concettuale e non tocca credenziali, **elimina questo file** dalla cartella `materiali/` prima di consegnarla al pubblico.

---

## Importante prima di iniziare

In questa cartella **non ci sono mai credenziali vere**. Tutti i file `.env`, le chiavi API, i token che vedi sono **placeholder fittizi** (es. `API_KEY=metti-la-tua-qui`). Devi sostituirli con le tue.

Se nel video ho mostrato un file `.env`, lo trovi in versione **`.env.example`** dentro questa cartella - senza i miei valori veri.

---

## Cosa fare con i tuoi valori

1. **Copia `.env.example` in `.env`** (stesso file, nome diverso):
   - Su Windows: tasto destro sul file -> Copia -> Incolla -> rinomina in `.env`
   - Su Mac/Linux da terminale: `cp .env.example .env`

2. **Apri `.env` con VS Code** e sostituisci i placeholder con i tuoi valori veri (API key che ti sei procurato sul sito del servizio, token, ecc.).

3. **Salva il file.** Non chiudere VS Code se devi ancora lavorarci.

---

## Se condividi questi materiali con altri

Prima di mandare la cartella a qualcuno (collega, cliente, repository GitHub, drive condiviso):

1. **Cancella il file `.env`** (quello con i tuoi valori veri). Tieni solo `.env.example`.
2. Verifica che dentro la cartella non ci siano altre tracce delle tue credenziali in file diversi (cerca con VS Code la stringa della tua API key per essere sicuro).

---

## Se hai pubblicato per errore le credenziali su GitHub

**Cancellare il file dal repository NON basta.** I bot scansionano GitHub in tempo reale e archiviano tutto. Anche se cancelli il commit, le tue credenziali restano nella history e probabilmente sono gia' state lette da qualcuno.

**Cosa fare subito:**

1. **Vai sul sito del servizio** da cui hai preso la chiave (es. Anthropic Console, OpenAI Platform, Stripe Dashboard, ecc.).
2. **Revoca la chiave compromessa.** Cerca "Revoke", "Delete", "Disable" accanto alla chiave.
3. **Genera una chiave nuova.**
4. **Aggiorna il tuo `.env` locale** con la nuova chiave.

Tempo che ti ci vuole: 2 minuti. Tempo che ci mette un bot a sfruttare la vecchia chiave: secondi. Non saltare questo passaggio.

---

## Promemoria - `.gitignore`

Se hai messo questi materiali in un repository Git, controlla che `.env` sia listato nel file `.gitignore` della radice del progetto. Cosi' Git **non** lo committera' mai per sbaglio.

Esempio minimo di `.gitignore`:

```
.env
.env.local
.env.*.local
*.key
*.pem
```

Se non c'e' un `.gitignore`, creane uno con questi contenuti **prima** del primo `git add`.
