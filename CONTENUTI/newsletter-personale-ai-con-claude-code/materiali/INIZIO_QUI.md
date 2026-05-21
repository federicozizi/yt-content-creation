# Setup automatico — Claude Code, leggi qui

> ⚠️ Gemello inglese: `CONTENUTI/personal-ai-newsletter-with-claude-code/materiali/START_HERE.md` — sincronizzare ogni modifica.

Sei stato lanciato dentro la cartella materiali della **Newsletter AI personale**. Tutto è già qui: `fonti.json` con 3 fonti di esempio (Anthropic news/research/changelog), `CLAUDE.md` col tono, `prompts/newsletter-daily.md` con l'orchestratore, `state.json` vuoto pronto da popolare. Tu fai solo: verifica prerequisiti + primo run di test. ~3 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
claude --version
```

Se manca: `npm install -g @anthropic-ai/claude-code` (oppure il metodo di installazione preferito su https://claude.com/code).

L'utente deve essere già loggato in Claude Code con un piano (Pro/Max) o con una API key configurata. Verificalo con:

```bash
claude /status
```

Se non è loggato, ferma il setup e chiedi di loggarsi prima.

### 2. Mostra all'utente cosa farà il sistema

In 3 frasi:
- Visiterà le 3 fonti di Anthropic in `fonti.json`
- Riassumerà gli articoli mai visti prima in un file markdown dentro `newsletter/`
- Aggiornerà `state.json` per non riproporre gli stessi articoli nei run futuri

### 3. (Opzionale) Personalizza fonti o tono

Chiedi all'utente:
- "Vuoi cambiare le fonti?" Se sì, apri `fonti.json` e aiutalo a modificare/aggiungere/togliere voci.
- "Vuoi cambiare il tono di scrittura?" Se sì, apri `CLAUDE.md` e mostragli la sezione `## Tono della newsletter`.

Se l'utente dice "lascia tutto com'è e fai il primo run", salta direttamente allo step 4.

### 4. Primo run di test

Lancia il prompt orchestratore:

```bash
claude --print "$(cat prompts/newsletter-daily.md)"
```

Aspetta che finisca (~1-2 minuti). Mostra all'utente:
- Il file creato in `newsletter/YYYY-MM-DD.md`
- La modifica a `state.json` (URL aggiunti agli articoli visti)

### 5. (Opzionale) Schedulazione

Chiedi: "Vuoi che parta da solo ogni mattina?"

Se sì:
- Mostra la guida in `scheduling/claude-routines.md`
- Aiuta l'utente a creare la routine con `claude routines add daily-newsletter --schedule "0 8 * * *" --cwd "$(pwd)" --prompt "esegui prompts/newsletter-daily.md"`
- Verifica con `claude routines list`

Se no: spiega che può sempre rilanciare manualmente il comando dello step 4.

### 6. (Opzionale) Email

Se chiede "posso riceverla via email invece che leggerla nel file?":
- Aprigli `docs/email-opzionale.md`
- La configurazione email richiede un Gmail App Password — guidalo passo passo

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: questa cartella È il progetto.
- **Non rimuovere `CLAUDE.md`**: è il tuo contesto persistente (tono, regole, gestione stato).
- **Non modificare manualmente `state.json`** durante il setup: viene popolato al primo run.
- Tono diretto, conciso. Niente paragrafi accademici.
- Se un comando fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
