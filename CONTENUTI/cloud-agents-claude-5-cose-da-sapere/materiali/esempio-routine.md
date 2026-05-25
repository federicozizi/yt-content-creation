# Template di Routine — Scouting news quotidiano

> Copia il blocco "Prompt completo" qui sotto e incollalo nel campo **Prompt** della tua Routine su [https://claude.ai/code/routines](https://claude.ai/code/routines).
> Personalizza i 4 placeholder marcati `<<COSI>>`.

---

## Prompt completo (copia da qui)

```
Sei l'agente remoto schedulato per la mia routine di scouting news quotidiano.

OBIETTIVO: leggere le ultime notizie/post virali sul tema <<TEMA SPECIFICO, es. AI per il marketing B2B>> e produrre un file markdown in `news/YYYY-MM-DD.md` con 3-5 spunti operativi per la mia attivita'.

STEPS:

1. Setup identita' git (sempre, idempotente):
   `git config user.email 'bot@anthropic.com' && git config user.name 'My Cloud Agent'`

2. Determina la data di oggi:
   `date -u +%Y-%m-%d`

3. Esegui WebSearch e WebFetch su queste fonti, ultimi 7 giorni:
   - <<FONTE 1, es. blog HubSpot Marketing>>
   - <<FONTE 2, es. r/marketing su Reddit, top weekly>>
   - <<FONTE 3, es. newsletter Marketing Brew>>
   - YouTube: query "<<KEYWORD DEL TUO SETTORE>>" filtrati per ultima settimana

4. Identifica 3-5 spunti realmente utili per la mia attivita'. Per ognuno:
   - Titolo dello spunto (1 riga)
   - Perche' e' utile per me (2 righe)
   - Link alla fonte originale (cliccabile)
   - Una "azione concreta" che potrei mettere in pratica questa settimana

5. Scrivi il file `news/<data>.md` con il formato:

   ```
   # News quotidiana - <data>
   
   ## Spunto 1: <titolo>
   <perche' utile>
   Fonte: <link>
   Azione: <cosa fare questa settimana>
   
   ## Spunto 2: ...
   ```

6. Commit + push autenticato con PAT:
   - `git add news/<data>.md`
   - `git commit -m 'scouting news <data>'`
   - `git push https://<<TUO_USERNAME_GITHUB>>:<<TUO_PAT>>@github.com/<<TUO_USERNAME_GITHUB>>/<<NOME_REPO>>.git HEAD:main 2>&1`

   Se il push fallisce, riporta l'errore esatto.

VINCOLI:
- Tocca SOLO i file in `news/`. Non modificare altro.
- Lingua: italiano.
- Non inventare fonti: ogni link deve venire da una WebSearch/WebFetch reale.
- Se la giornata e' povera di novita', meglio 2 spunti forti che 5 deboli.
```

---

## I 4 placeholder da sostituire

1. **`<<TEMA SPECIFICO>>`** — il tema su cui fai scouting. Esempi:
   - "AI per il marketing B2B"
   - "Nuove feature di Claude e Anthropic per le PMI italiane"
   - "Sviluppi normativi GDPR e AI Act per piccole imprese"
   - "Trend e-commerce per cantine vinicole online"

2. **`<<FONTE 1/2/3>>`** — siti o community da scansionare. Suggerimenti:
   - **Newsletter di settore**: HubSpot Marketing Blog, Marketing Brew, Ben's Bites
   - **Subreddit pertinenti**: r/marketing, r/Entrepreneur, r/smallbusiness
   - **Blog AI**: anthropic.com/news, openai.com/blog
   - **Hacker News**: thehackernews.com (per tech) o news.ycombinator.com

3. **`<<KEYWORD DEL TUO SETTORE>>`** — query YouTube. Esempi:
   - `"AI marketing automation"` (per marketer)
   - `"claude code workflow"` (per chi usa Claude)
   - `"small business AI"` (per imprenditori PMI)

4. **`<<TUO_USERNAME_GITHUB>>`, `<<TUO_PAT>>`, `<<NOME_REPO>>`** — le tue credenziali GitHub. Esempi:
   - `username`: `mario-rossi`
   - `PAT`: `ghp_xxxxxxxxxxxxxxxxxxxxxx` (quello che hai creato seguendo lo Step 2 del README)
   - `repo`: `claude-routines-personali`

---

## Configurazione cron consigliata

Per scouting **mattutino** (vedi il report appena svegli):
- Cron: `0 6 * * *` (ogni giorno alle 06:00 UTC = 08:00 ora italiana CEST estate / 07:00 CET inverno)

Per scouting **serale** (vedi il report a fine giornata):
- Cron: `0 18 * * *` (ogni giorno alle 18:00 UTC = 20:00 CEST / 19:00 CET)

Per scouting **solo settimanale** (meno consumo quota):
- Cron: `0 6 * * 1` (ogni lunedi' alle 06:00 UTC)

Ricorda: cron e' sempre in **UTC**. Usa [crontab.guru](https://crontab.guru) per verifica.

---

## Allowed tools da spuntare nella UI

Quando crei la routine, nella sezione "Allowed tools" spunta:

- ✅ `Bash` — per comandi git
- ✅ `Read` — per leggere file dal repo
- ✅ `Write` — per creare il file di news
- ✅ `Edit` — opzionale, per modificare file esistenti
- ✅ `Glob` — per cercare file
- ✅ `Grep` — per cercare contenuti
- ✅ `WebSearch` — per cercare news
- ✅ `WebFetch` — per leggere pagine specifiche

NON spuntare:
- ❌ `NotebookEdit` (non serve)
- ❌ Tool MCP "extra" che non ti servono (riducono il rischio di azioni impreviste)

---

## Variante per altri tipi di routine

Lo stesso template puoi adattarlo per:

- **Newsletter personale settimanale**: cambia path da `news/` a `newsletter/` e schedule a lunedi'
- **Monitor competitor**: cambia il prompt per scansionare 3-5 siti competitor invece di fonti news
- **Customer support digest**: aggiungi la lettura via WebFetch dei ticket pubblici (es. forum, recensioni Google) e sintesi settimanale

La struttura del prompt (steps 1, 2, 6 — commit) resta sempre quella. Cambia solo l'obiettivo e le fonti.
