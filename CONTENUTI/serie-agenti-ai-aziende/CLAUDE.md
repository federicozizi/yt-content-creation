# CLAUDE.md — Serie "Agenti AI per le aziende (Zero fuffa)"

> **Cos'è questa cartella.** Quartier generale di una **serie YouTube didattica**: insegnare a costruire
> **agenti AI veri per le aziende**, partendo dagli strumenti reali (Claude SDK) e arrivando ogni volta a un
> agente che fa qualcosa di concreto. Deviazione voluta dalla struttura standard `CONTENUTI/<slug>/`: qui c'è
> una serie multi-episodio, quindi gli episodi vivono in sottocartelle. Ogni **episodio** però resta una cartella
> a 3 cose standard (PRINCIPALE.html + PRINCIPALE_ENG.html + materiali/), vedi `../../CLAUDE.md`.
>
> **Distinta da `serie-startup-agenti-ai`**: quella racconta il *lancio di una startup gestita* da agenti
> (storia personale). Questa **insegna a costruirli** (build dimostrative didattiche). Non confonderle.
>
> Ultimo aggiornamento: 2026-06-11.

---

## 0. In una frase

Una serie in cui, episodio dopo episodio, lo spettatore impara a costruire **agenti AI veri** che fanno un
lavoro concreto in azienda — non chatbot-giocattolo, non demo da palco. Filo conduttore ripetuto a ogni
puntata: **"Agenti AI per aziende veri, zero fuffa."**

---

## 1. Il key topic (la promessa-ombrello)

Ogni contenuto della serie, qualunque sia il titolo, rimanda sempre allo stesso concetto-chiave:

> **"Agenti AI per aziende veri, zero fuffa."**

Cosa vuol dire "vero" e cosa vuol dire "zero fuffa" (da ribadire in ogni episodio):
- **Vero** = un agente che *fa* qualcosa (legge, decide, agisce con strumenti), non solo che *risponde*.
- **Zero fuffa** = strumenti ufficiali e reali (Claude SDK), codice che gira davvero, caso d'uso aziendale
  concreto, e onestà sui limiti (cosa l'agente NON sa fare).

L'agente "vero" si distingue dal chatbot perché ha **strumenti** (in inglese *tool*) — chiamiamoli a voce
**"le mani dell'agente"**: il chatbot parla, l'agente parla *e fa* (registra una richiesta, apre un ticket,
scrive su un file, manda una notifica).

---

## 2. Format della serie

- **Ombrello**: Build dimostrativa ("Costruisco X") — il format più adatto a una serie tecnica-ma-accessibile.
- I singoli episodi possono variare format (Listicle / Problem-solver / Storia) per rispettare la rotazione
  del canale (vedi `../../CLAUDE.md`), ma il cuore resta sempre: **si costruisce un agente vero, in chiaro**.

### Struttura ricorrente di ogni episodio (per coerenza di serie)
1. **Richiamo al key topic** nei primi secondi: "Agenti AI per aziende veri, zero fuffa."
2. **Promessa visibile**: l'agente finito mostrato (anche 5 secondi) entro il primo minuto.
3. **Build progressivo**: ogni step aggiunge qualcosa di visibile.
4. **Il momento "ecco perché è un agente VERO"**: quando l'agente usa uno strumento, non solo risponde.
5. **Onestà sui limiti**: cosa NON fa, dove serve ancora l'umano.
6. **Consegna**: file pronti nei materiali, lo spettatore replica.

---

## 3. Roadmap episodi (DRAFT — si rifinisce strada facendo)

| # | Titolo di lavoro | Cuore tecnico | Agente che si costruisce |
|---|------------------|---------------|--------------------------|
| 1 | **"Ecco come si creano Agenti AI per le aziende (Zero fuffa)"** (FATTO) | Cos'è il Claude SDK e cos'è un agente *vero* (Claude + strumenti) | Agente che gestisce le **comunicazioni interne su Telegram**: risponde alle domande dei dipendenti dal "manuale aziendale" e **protocolla** richieste (ferie/assenze/IT) usando uno strumento |
| 2 | **"Come creare agenti AI sostenibili per le aziende (Guida pratica reale)"** (FATTO) | Il modello giusto al posto giusto: **modello economico + script + modello smart** solo sui casi critici (model routing / cascade) | Agente che analizza **centinaia di recensioni** a costo bassissimo: Haiku inquadra tutto, lo script aggrega e seleziona i casi delicati, Opus li valida e propone le risposte |
| 3 | (proposta) "Il mio agente AI gira da solo ogni mattina" | Routine schedulata (Claude Routines) | Agente che produce un report e lo consegna da solo — allineato alla CTA dell'Ep2 |
| 4 | (proposta) "Il mio agente AI legge le email / parla col gestionale" | Lettura dati reali (posta o database) | Agente che triagga la posta o risponde su ordini/magazzino |

> La roadmap oltre l'Ep1 è proposta da Claude: confermare/riscrivere con l'utente prima di produrre.

---

## 4. Decisioni tecniche dell'Ep1 (DECISO)

- **SDK**: SDK ufficiale Anthropic per Python — pacchetto `anthropic`. Si usa il **tool runner**
  (`client.beta.messages.tool_runner`) che è il vero ciclo agentico: Claude decide, chiama lo strumento,
  riceve il risultato, continua, da solo. Verificato contro la doc ufficiale (skill `claude-api`).
- **Modello**: `claude-opus-4-8` nel codice (default più capace). Nota nei materiali: per volumi alti e
  costi bassi si può passare a `claude-haiku-4-5` cambiando una sola riga.
- **Canale**: Telegram via `python-telegram-bot` (gratis, immediato, niente server da esporre — il bot
  fa *polling* in uscita, quindi gira anche dal PC senza aprire porte).
- **Caso d'uso**: comunicazioni interne. L'agente (a) risponde dalle info aziendali in un file
  `azienda_knowledge.md`, (b) ha **uno strumento vero** `registra_richiesta` che protocolla ferie/assenze/IT
  in un file di log. È questo strumento che lo rende un *agente* e non un chatbot.
- **Credenziali**: `.env` con `ANTHROPIC_API_KEY` e `TELEGRAM_BOT_TOKEN`. Solo `.env.example` nei materiali
  → **DISCLAIMER.md obbligatorio**.

---

## 4-bis. Decisioni tecniche dell'Ep2 (DECISO)

- **Architettura a tre strati** (in gergo *model routing / cascade*; a voce: "il modello giusto al posto giusto"):
  1. **Modello economico** per il lavoro di volume — inquadra ogni recensione.
  2. **Script Python deterministico** (gratis) per aggregare, contare e **selezionare** i pochi casi critici.
  3. **Modello smart** solo sui casi delicati — li valida e propone la risposta.
- **Modelli**: `claude-haiku-4-5` (economico, $1/$5 per Mtok) per inquadrare tutte le recensioni;
  `claude-opus-4-8` (smart, $5/$25 per Mtok) solo sui casi delicati. Prezzi verificati contro la doc
  ufficiale (skill `claude-api`).
- **Structured output**: il modello economico compila una "scheda" (Pydantic + `client.messages.parse`).
  Output corto = costo basso + risultato subito usabile dallo script. Supportato da Haiku 4.5.
- **Thinking/effort**: NIENTE su Haiku (non lo supporta, e non serve); **thinking adattivo** su Opus
  (`thinking={"type": "adaptive"}`) — si paga il ragionamento solo sui pochi casi difficili. Niente
  `temperature`/`budget_tokens` (rimossi su Opus 4.8).
- **Freno a mano sui costi**: la costante `MAX_CASI_SMART` limita quante recensioni finiscono a Opus —
  decisione deterministica dello **script**, non dell'AI. È il punto narrativo forte dello Step 4.
- **Caso d'uso**: analisi delle recensioni di un B&B (`recensioni.csv`, colonne `autore`/`testo`).
  Output: `report.md` + il **conto dei costi** stampato a terminale (token reali via `usage`),
  confrontato con lo scenario "tutto Opus". Il conto è il momento "wow" dello Step 6.
- **Credenziali**: `.env` con `ANTHROPIC_API_KEY`. Solo `.env.example` nei materiali →
  **DISCLAIMER.md obbligatorio**. `.gitignore` esclude `.env`, `__pycache__/`, `report.md`.

---

## 5. Voice & sicurezza

Valgono integralmente le regole globali di `../../CLAUDE.md`:
- **Voice Guide** (analogie sempre, niente gergo dev nelle frasi da pronunciare, hook-storia non hook-funnel).
  - Glossario rapido per questa serie: *tool/strumento* → "le mani dell'agente"; *SDK* → "la cassetta degli
    attrezzi ufficiale per far lavorare Claude dentro i tuoi programmi"; *API key* → "una chiave personale che
    sblocca Claude, da tenere segreta come il PIN del bancomat"; *polling* → "il bot che ogni secondo chiede a
    Telegram: ci sono messaggi nuovi per me?".
- **Sicurezza credenziali**: mai chiavi vere nei materiali, `.env` mai a schermo, DISCLAIMER dove ci sono
  credenziali, `.gitignore` prima di `git init`.

---

## 6. Struttura della cartella

```
serie-agenti-ai-aziende/
├── CLAUDE.md                       <- questo file (bibbia serie + roadmap + decisioni)
├── ep1-claude-sdk-telegram/        <- episodio di esordio (cartella a 3 cose standard)
│   ├── PRINCIPALE.html
│   ├── PRINCIPALE_ENG.html
│   └── materiali/
│       ├── README.md
│       ├── DISCLAIMER.md
│       ├── .env.example
│       ├── requirements.txt
│       ├── agente_telegram.py
│       └── azienda_knowledge.md
└── ep2-agenti-ai-sostenibili/      <- episodio sui costi (modello economico + script + giudice smart)
    ├── PRINCIPALE.html
    ├── PRINCIPALE_ENG.html
    └── materiali/
        ├── README.md
        ├── DISCLAIMER.md
        ├── .env.example
        ├── .gitignore
        ├── requirements.txt
        ├── analizza_recensioni.py
        └── recensioni.csv
```
