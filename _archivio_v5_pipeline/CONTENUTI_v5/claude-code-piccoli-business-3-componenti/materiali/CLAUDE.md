<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/CLAUDE.md -->

# CLAUDE.md — Regole del progetto

Sei Claude Code, lanciato dentro la cartella `materiali/` del video "Claude Code per piccoli business: le 3 componenti imprescindibili". Questa cartella **È IL progetto** — non creare cartelle progetto separate.

Il progetto monta 3 componenti che devono parlarsi:
1. **Supabase via MCP connector** — DB dei dati custom dello studio
2. **Claude for Small Business** (Anthropic) — pacchetto di workflow pre-cotti, vive in Cowork
3. **Agent View** — sub-agent custom in `.claude/agents/`, vivono in Claude Code

## Cosa fai quando l'utente dice "esegui il setup leggendo CLAUDE.md"

Lavora in 3 fasi sequenziali. Ogni fase corrisponde a un prompt in `prompts/`.

### Fase 1 — Supabase via MCP

Esegui le istruzioni di `prompts/01-supabase-mcp-setup.md`. Sono già state scritte pensando a questo flusso, applicale parola per parola. Al termine la verifica deve passare ("4 tabelle viste").

### Fase 2 — Claude for Small Business

NON è una cosa che puoi fare tu. È un'attivazione che l'utente fa nel browser, dentro Claude Cowork.

Cosa fai tu:
- Spiega all'utente chi è e dove vive (`docs/claude-for-small-business-howto.md` ha tutto).
- Indicagli di aprire `prompts/02-claude-cowork-smb-onboard.md` e seguire i passi.
- Quando l'utente conferma "fatto", aggiorna `README.md` sezione "Stato setup" segnando Step 2 ✓.

### Fase 3 — Sub-agent custom

Esegui le istruzioni di `prompts/03-launch-custom-agents.md`. Lancia almeno regime-checker per dimostrare che gli agenti funzionano. Mostra all'utente le righe nuove generate in `note_interne` su Supabase.

### Fase 4 (bonus, se l'utente chiede) — Integrazione end-to-end

Apri `prompts/04-integrazione-end-to-end.md` e guida l'utente nel flusso che alterna terminale e browser. Mostra il punto di verifica finale: il pacchetto Anthropic legge `note_interne` di Supabase quando lanci `/invoice-chaser` in Cowork.

## Tono

Diretto, asciutto, da pari a pari. Niente "ottimo, procedo", niente "ho preparato per te". Mostra cosa stai facendo, fallo, basta. L'utente è un piccolo imprenditore — usa il tempo che usa lui.

## Cose da NON fare

- **Non committare `.env`** — è già in `.gitignore`, verificalo prima di qualsiasi `git add`.
- **Non eseguire `git init` da solo** — questo progetto non è necessariamente un repo git; se l'utente vuole versionarlo, glielo lascia decidere.
- **Non installare dipendenze npm/pip** — l'unica cosa che ci serve è il server MCP di Supabase, che `claude mcp add supabase` installa via `npx` al volo. Niente venv, niente requirements.txt.
- **Non scrivere codice middleware** — tutta la comunicazione Claude↔Supabase passa per MCP. Niente Python wrapper, niente API custom.
- **Non sovrascrivere i file in `prompts/`, `docs/`, `.claude/agents/`** durante un'esecuzione — sono i materiali di base, devono restare quelli del video. Eccezione: l'utente che dice esplicitamente "modifica `regime-checker.md` aggiungendo X".
- **Non eseguire azioni esterne** (email, pagamenti, post pubblicati) dagli agenti custom. Quelle passano dal pacchetto Anthropic in Cowork, con approvazione umana.

## Quando qualcosa fallisce

Mostra l'errore in chiaro, ipotizza la causa (URL Supabase sbagliato? Service role key revocata? Progetto in stato Paused?), proponi il fix. NON ripartire da zero senza dirlo all'utente.

## Riferimenti

- Guida video: `PRINCIPALE.html` in questa cartella (copia di quella nel parent).
- Schema SQL: `schema-aziendale.sql`.
- Sub-agent: `.claude/agents/document-classifier.md`, `regime-checker.md`, `scadenza-allerter.md`.
- Annuncio Anthropic: https://www.anthropic.com/news/claude-for-small-business
