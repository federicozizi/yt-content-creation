# Il tuo primo Agente AI per le aziende — Assistente interno su Telegram

Serie **"Agenti AI per aziende veri, zero fuffa"** — Episodio 1.

In questa cartella hai tutto per costruire un **agente AI vero** (non un chatbot) che gestisce le
comunicazioni interne della tua azienda su Telegram: risponde alle domande dei dipendenti leggendo il
"manuale aziendale" e **protocolla** le richieste di ferie, assenze e problemi informatici.

> **Cosa rende questo un AGENTE e non un chatbot?** Un chatbot *parla*. Un agente *parla e fa*. Il nostro
> agente, quando serve, usa uno **strumento** (lo chiamiamo "le mani dell'agente") per registrare davvero una
> richiesta in un file. Questo è il cuore della serie.

---

## Quick start (5 passi)

1. **Installa Python** (versione 3.10 o successiva) da [python.org](https://www.python.org/downloads/). Su Windows, durante l'installazione spunta *"Add Python to PATH"*.
2. **Apri questa cartella** con VS Code e apri il terminale integrato (menu *Terminale → Nuovo terminale*).
3. **Installa i pacchetti**: nel terminale scrivi `pip install -r requirements.txt`.
4. **Crea le chiavi** (vedi sotto "Le due chiavi che ti servono"), poi copia `.env.example` in `.env` e incolla i tuoi valori.
5. **Avvia l'agente**: `python agente_telegram.py`. Apri Telegram, scrivi al tuo bot, e provalo.

---

## Cosa sono le cose che usiamo (spiegato semplice)

- **Claude SDK** → la "cassetta degli attrezzi ufficiale" che permette di far lavorare Claude *dentro* un tuo
  programma, non solo nella chat del browser. In pratica: il tuo codice parla con Claude.
- **Agente con strumenti** → Claude a cui dai delle "mani". Tu descrivi cosa può fare (es. "registra una
  richiesta"), e lui decide *da solo* quando usarle. Il ciclo "Claude pensa → usa lo strumento → vede il
  risultato → continua" lo gestisce l'SDK per te.
- **Telegram bot** → il modo più veloce per dare una "faccia" all'agente. Gira anche dal tuo PC: il bot chiede
  in continuazione a Telegram "ci sono messaggi nuovi?" (si chiama *polling*), quindi non devi aprire porte né
  configurare un server.

---

## Le due chiavi che ti servono

L'agente ha bisogno di due chiavi segrete. Le metti nel file `.env` (mai a video, mai su GitHub).

### 1. La chiave Anthropic (sblocca Claude)
1. Vai su [console.anthropic.com](https://console.anthropic.com) e accedi.
2. Sezione **API Keys → Create Key**. Copia la chiave (inizia con `sk-ant-...`).
3. Incollala in `.env` alla riga `ANTHROPIC_API_KEY=`.

> Pensa a questa chiave come al **PIN del bancomat**: chi ce l'ha può spendere i tuoi soldi. Tienila segreta.

### 2. Il token del bot Telegram
1. Su Telegram cerca **@BotFather** (il bot ufficiale per creare bot).
2. Scrivi `/newbot`, scegli un nome e un username che finisce per `bot`.
3. BotFather ti dà un **token** (tipo `123456789:AA...`). Copialo.
4. Incollalo in `.env` alla riga `TELEGRAM_BOT_TOKEN=`.

---

## Come si crea il file .env (importante)

1. In VS Code, fai una copia di `.env.example` e rinominala in `.env` (togli `.example`).
2. Apri `.env` e incolla le tue due chiavi al posto dei valori di esempio.
3. **Non condividere mai questo file** e non caricarlo su GitHub. Leggi `DISCLAIMER.md`.

---

## Personalizza il "cervello" dell'agente

Apri `azienda_knowledge.md` con VS Code e sostituisci i dati di esempio (Acme S.r.l.) con le informazioni
vere della tua azienda: orari, ferie, contatti, regole. **Più questo file è chiaro e ordinato, migliori sono
le risposte dell'agente.** È la prima cosa da mettere a posto.

---

## Provalo (esempi da scrivere al bot)

- *"A che ora chiude l'ufficio venerdì?"* → risponde dal manuale.
- *"Quanti giorni di ferie ho all'anno?"* → risponde dal manuale.
- *"Vorrei prendere ferie dal 12 al 16 agosto"* → **usa lo strumento** e protocolla la richiesta.
- *"La stampante del secondo piano non funziona"* → **protocolla** una richiesta IT.

Le richieste protocollate finiscono nel file `richieste.log`, una riga per richiesta. Aprilo per vederle.

> Non devi creare tu questo file: l'agente lo genera da solo la prima volta che protocolla una richiesta. Se
> non lo vedi ancora, vuol dire che non hai ancora fatto una richiesta di ferie/assenza/IT.

---

## Cosa fa e cosa NON fa (onestà, zero fuffa)

**Fa:**
- Risponde alle domande coperte dal manuale aziendale.
- Riconosce ferie/assenze/IT e le registra in un file.

**NON fa (ancora):**
- Non approva le ferie: le *registra* soltanto. L'approvazione resta a un umano.
- Non conosce nulla che non sia scritto nel manuale (e te lo dice, invece di inventare).
- In questa versione base gira finché il programma è acceso e non ha una memoria delle conversazioni passate
  tra un riavvio e l'altro. Negli episodi successivi della serie aggiungeremo questi pezzi.

---

## Problemi comuni

- **`ModuleNotFoundError`** → hai saltato il passo `pip install -r requirements.txt`.
- **`FileNotFoundError: azienda_knowledge.md`** → stai lanciando il programma dalla cartella sbagliata.
  Assicurati che il terminale sia aperto **dentro** la cartella `materiali` (vedi passo 2 del Quick start).
- **Errore di autenticazione Anthropic** → la chiave in `.env` è sbagliata o incompleta.
- **Il bot non risponde** → controlla che `TELEGRAM_BOT_TOKEN` sia giusto e che il programma sia ancora in
  esecuzione nel terminale.
- **Risposte "non lo so"** → l'informazione non è nel `azienda_knowledge.md`: aggiungila lì.
- **Vedi comparire una cartella `__pycache__`** → è normale: la crea Python da sola, puoi ignorarla (è già
  esclusa da Git).
