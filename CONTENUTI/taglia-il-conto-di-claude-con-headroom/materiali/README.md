# Headroom — la stessa domanda a Claude Opus, ma con molti meno token

Questo mini-progetto serve a **vederlo coi tuoi occhi**: prendiamo un "pacchetto
incidente" (un misto di testo, dati JSON e codice), lo mandiamo a **Claude Opus**
in due modi — *intero* e dopo averlo passato in **Headroom** — e confrontiamo
quanti token (cioè quanti soldi) servono nei due casi. La risposta del modello è
la stessa; il conto, no.

**Headroom** è uno strato che si mette *davanti* al modello e comprime il testo
che gli mandi. Non "riassume con un'altra AI": riconosce il **tipo** di ogni
pezzo (JSON, codice, prosa) e applica a ciascuno un taglia-su-misura, in locale,
in pochi millisecondi.

---

## Quick start (5 passi)

> Ti serve **Python 3.10+** installato e **VS Code** per aprire i file.

1. **Apri questa cartella con VS Code** e apri il terminale integrato
   (menù *Terminale → Nuovo terminale*).

2. **Installa tutto** (un comando solo):
   ```
   pip install -r requirements.txt
   ```

3. **Crea il file `.env`** copiando l'esempio, e incollaci la tua chiave:
   ```
   copy .env.example .env
   code .env
   ```
   La chiave gratuita la prendi da **https://openrouter.ai/keys**.
   (Se salti questo passo il progetto funziona lo stesso, ma ti mostra solo la
   compressione locale, senza chiamare davvero Opus.)

4. **Avvia il server:**
   ```
   python app.py
   ```

5. **Apri il browser** su **http://localhost:8000** e premi il pulsantone.
   I numeri appaiono sulla pagina; i **log riga per riga** li vedi nel
   **terminale** e nella **console del browser** (tasto `F12`).

---

## Cosa vedi quando premi il pulsante

- Due colonne affiancate: **Senza Headroom** e **Con Headroom**, con i token in
  input, i token in output e il costo stimato.
- Una riga di verdetto: **quanti token in input hai risparmiato** (di solito
  un taglio enorme) e quanto costo.
- Le **due risposte di Opus** una accanto all'altra: servono a dimostrare che,
  pur mandando molti meno token, il modello trova **la stessa causa** (l'errore
  FATAL nei log).
- Nel terminale, il **dettaglio per tipo**: quanto è stato tagliato il JSON, il
  codice e il testo, e con quale compressore.

---

## I file della cartella (cosa fa ognuno)

| File | A cosa serve |
|---|---|
| `app.py` | Il server web. Lo lanci con `python app.py`. Serve la pagina e, al click, esegue il confronto. |
| `index.html` | La pagina con il **pulsante** e le due colonne dei risultati. |
| `headroom_demo.py` | Il **cuore**: comprime il pacchetto con Headroom e fa le due chiamate a Opus, calcolando la differenza di token. |
| `dati_esempio.py` | Costruisce il pacchetto incidente realistico: **testo** (runbook) + **JSON** (eventi) + **codice** (il servizio col bug). |
| `requirements.txt` | L'elenco delle librerie da installare. |
| `.env.example` | Il modello del file `.env` (con una chiave finta). |
| `.env` | **Lo crei tu.** Contiene la tua chiave vera. Non si condivide mai. |
| `DISCLAIMER.md` | Le regole di sicurezza sulla chiave: **leggilo**. |
| `GUIDA-PROXY.md` | Come mettere Headroom **in sottofondo a Claude Code** (modalità proxy): un comando e Claude Code spende meno mentre lavori. |

Come si parlano: `index.html` (pulsante) → `app.py` (server) → `headroom_demo.py`
(compressione + Opus) → usa i dati di `dati_esempio.py` → rimanda i numeri alla
pagina.

---

## Come funziona la compressione (e da dove arriva il risparmio)

Headroom riconosce il **tipo** di ogni pezzo e lo manda al compressore adatto:

- Il **JSON** (un array lungo di eventi quasi identici) → *SmartCrusher*. È qui
  che avviene il taglio enorme — nel nostro esempio **circa il 99%** — e
  **senza perdere informazione**: trasforma l'array ripetitivo in uno schema
  compatto + righe, tenendo struttura ed eventi anomali (incluso il FATAL).
- Il **testo** del runbook → riconosciuto come prosa. Con l'extra ML
  (`headroom-ai[ml]`) Headroom lo accorcia; senza, lo lascia leggibile.
- Il **codice** → Headroom lo lascia **intatto di proposito**: non rischia di
  rompere la logica del tuo programma. È una scelta di sicurezza, non un limite.

Il punto vero, ed è il motivo per cui Headroom funziona: **il grosso di quello
che un agente legge sono dati strutturati** — log, telemetria, risposte di API,
risultati di ricerca. Sono ripetitivi e voluminosi, ed è lì che il conto dei
token si gonfia. Comprimendo *quelli* (in locale, senza chiamare nessun modello,
in millisecondi) si taglia la spesa senza toccare il significato. Codice e prosa
li lascia stare: meno spettacolare a parole, molto più affidabile nei fatti.

---

## Se qualcosa non va

- **"Comprime tantissimo il JSON ma non il testo/codice"** → è il comportamento
  atteso (vedi sopra: il codice resta intatto per sicurezza, la prosa serve
  l'extra ML). Il risparmio grosso arriva comunque dai dati, che sono il grosso
  del conto. Se vuoi provare anche la prosa: `pip install "headroom-ai[ml]"`.
- **"Nessuna OPENROUTER_API_KEY"** → non hai creato il `.env` (passo 3). Il
  progetto gira comunque e ti mostra la compressione locale.
- **La porta 8000 è occupata** → cambia `port=8000` in fondo a `app.py`.

> ⚠️ Sicurezza: la tua chiave sta solo nel `.env`, che non va mai condiviso.
> Dettagli in **DISCLAIMER.md**.
