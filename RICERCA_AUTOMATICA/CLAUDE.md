# RICERCA_AUTOMATICA/

> **AGGIORNAMENTO (2026-05-30): meccanismo sostituito.** Le 2 routine cloud legacy
> (`yt-ricerca-idee-mattina` + `-sera`, basate su WebSearch + `prompt-ricerca.md`, su Sonnet 4.6)
> sono state **disabilitate**. Le sostituisce **una sola routine** — `Ricerca idee YouTube — 10 agenti (mattina)`
> (Sonnet 4.6, 1x/giorno ~8:00) — basata sul sistema a 10 scraper + sub-agenti in
> `CONTENUTI/claude-4-8-dynamic-workflows-10-agenti-paralleli/materiali/`.
> L'output finisce sempre in `IDEE/ricerche-auto/YYYY-MM-DD-mattina.md` nello **stesso formato**
> (definito qui in `prompt-ricerca.md`), quindi il resto del sistema (`lavora sull'idea X`) non cambia.
> `prompt-ricerca.md` resta come **specifica del formato di output** (ancora la fonte di verità del template).
> Le routine legacy restano archiviate su claude.ai e si possono riattivare se serve.

La descrizione sotto si riferisce al **meccanismo legacy** (storico, ora disattivato).

---

Configurazione dello **scheduling remoto** che 2 volte al giorno (mattina + sera) genera nuove idee di contenuto basate sulla scansione di cosa sta diventando virale online nel mio settore.

## Cosa fa

Lo `/schedule` esegue il prompt definito in `prompt-ricerca.md`. Il prompt:

1. **Scansiona fonti** del settore (Twitter/X, YouTube, Reddit, Hacker News, blog di riferimento, newsletter, release notes Anthropic/OpenAI/Google) per individuare cosa sta funzionando in questo momento.
2. **Identifica pattern virali** — non singoli post ma medie e tendenze (es. "questa settimana stanno tirando i video brevi su Claude Skills", "su Reddit r/ClaudeAI il thread piu' upvotato e' sui sub-agent per email").
3. **Genera 5-8 idee rivisitate** — non copie ma varianti, combinazioni, angoli inediti applicati alla mia audience (non tecnica, business-oriented).
4. **Salva il file** in `IDEE/ricerche-auto/YYYY-MM-DD-{mattina|sera}.md`.

## Topic da coprire (REGOLA GLOBALE)

Il prompt cerca contenuti su:
- **AI per automazioni** (n8n, Make, Zapier + AI, custom agents)
- **Software AI** (nuovi tool/SaaS, release di modelli, plugin)
- **Claude Code** (workflow, plugin, MCP, skills, hooks, sub-agent, integrazioni)
- **Intelligenza artificiale per il business** (use case settoriali, case study, ROI, integrazione enterprise)

## Cadenza

- **Mattina**: ~08:00 ora italiana — cattura cosa e' diventato virale la sera prima (USA fuso orario)
- **Sera**: ~20:00 ora italiana — cattura cosa e' diventato virale durante la giornata europea

## File

- `prompt-ricerca.md` — il prompt completo che lo `/schedule` esegue. **Non modificarlo senza pensarci**: e' la spec dell'output. Se cambi questo, cambia il template atteso in `IDEE/CLAUDE.md`.

## Come e' stato configurato lo /schedule

Vedi la routine registrata via `/schedule` (gestita con la skill omonima). Per modificare cadenza o prompt:

- `gestisci lo schedule` -> Claude usa la skill `/schedule` per listare/aggiornare le routine attive.
- `aggiorna il prompt di ricerca` -> apri `prompt-ricerca.md`, modifica, salva. Lo `/schedule` lo rileggera' alla prossima esecuzione (perche' lo script remoto fa `Read` del file ogni volta — non e' incorporato statico).

## Cosa NON fare in questa cartella

- Non scrivere idee qui. Le idee finiscono in `IDEE/ricerche-auto/` (non qui).
- Non duplicare il prompt in piu' file. C'e' un solo `prompt-ricerca.md`.
