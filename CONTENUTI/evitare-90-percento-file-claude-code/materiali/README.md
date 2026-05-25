# Le 5 tecniche per evitare il 90% dei file che Claude Code genera (e non ti servono)

> Materiali del video YouTube **"Le 5 tecniche per evitare il 90% dei file che Claude Code genera (e non ti servono)"**.
> Trovi qui le 5 tecniche in versione operativa, un template di CLAUDE.md gia' scritto, un settings.json con i blocchi giusti, e un prompt-tipo che applica disciplina dal primo messaggio.

---

## In 30 secondi — di cosa stiamo parlando

Se hai usato Claude Code anche solo per due settimane, conosci la scena: chiedi una cosa semplice ("aggiungi un campo al form") e ti ritrovi 5 file nuovi nella cartella che NON avevi chiesto:

- `TEST_user_form.md` — un piano di test che non hai chiesto
- `scratch_calculations.py` — uno script di "pensiero ad alta voce" che non serve
- `NOTES_2026-05-22.md` — appunti che non leggerai mai
- `debug_session_log.md` — log di debug del modello
- `summary_changes.md` — un riassunto delle modifiche che hai gia' visto a video

Risultato: la cartella del progetto diventa un rumore. Difficile distinguere i file veri da quelli inutili. Difficile fare commit puliti. Difficile capire cosa hai prodotto.

Questo documento ti da' 5 tecniche per riprendere il controllo. Applicate insieme, eliminano il 90% dei file inutili.

---

## Le 5 tecniche — riassunto operativo

| # | Tecnica | Dove configurarla | Difficolta' |
|---|---------|-------------------|-------------|
| 1 | Output discipline nel CLAUDE.md | File `CLAUDE.md` del progetto | Facile (10 minuti) |
| 2 | Deny patterns nel settings.json | File `.claude/settings.json` o `~/.claude/settings.json` | Facile (5 minuti) |
| 3 | Hook PreToolUse Write | Sempre `settings.json`, sezione hooks | Medio (15 minuti) |
| 4 | Skill personalizzata "Output minimalista" | Cartella `.claude/skills/` | Medio (15 minuti) |
| 5 | Prompt iniziale rinforzato | All'inizio di ogni sessione | Sempre (10 secondi) |

Le 5 lavorano in stack. La tecnica 1 e' il fondamento, la 5 e' la cima. Piu' tecniche applichi, piu' Claude sta nei binari.

Approfondimento di ognuna sotto.

---

## Cosa ti serve prima di iniziare

- [ ] **Claude Code installato** — [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- [ ] **VS Code** — [https://code.visualstudio.com](https://code.visualstudio.com) — per editare i file di configurazione
- [ ] 30 minuti per applicare tutte e 5 le tecniche al primo progetto. Le successive sono copia-incolla.

---

## Tecnica 1 — Output discipline nel CLAUDE.md

**Cosa fa**: aggiunge regole esplicite al CLAUDE.md del progetto su cosa Claude PUO' e NON PUO' scrivere.

**Dove**: file `CLAUDE.md` nella radice del tuo progetto (oppure file globale `~/.claude/CLAUDE.md`).

**Come si fa**: apri CLAUDE.md con VS Code, aggiungi una sezione `## Output Discipline (REGOLE NON NEGOZIABILI)`. Vedi il file `esempio-claude-md.md` di questa cartella per il blocco completo da copiare.

In sintesi, le regole vanno scritte cosi':

```markdown
## Output Discipline (REGOLE NON NEGOZIABILI)

NON creare mai file con questi pattern di nome:
- TEST_*.md, NOTES_*.md, SCRATCH_*.md
- debug_*, summary_*, *_temp.*
- README aggiuntivi se ne esiste gia' uno

NON creare file di sommario al termine di un task — il sommario lo do io a video.
NON scrivere file di "pensieri" o "ragionamenti" — usa il tuo thinking interno.
NON duplicare file di documentazione esistenti — modifica quelli che ci sono.

Se hai bisogno di tenere traccia di stati intermedi, usa il TodoWrite tool, MAI file scratch su disco.
```

**Efficacia**: alta. Claude rispetta CLAUDE.md la maggior parte delle volte. Ma non e' bulletproof (a volte lo "dimentica" su task lunghi). Per questo serve la tecnica 2.

---

## Tecnica 2 — Deny patterns nel settings.json

**Cosa fa**: configura Claude Code per RIFIUTARE proattivamente la scrittura su pattern di file inutili. Anche se Claude provasse, il tool Write fallisce con "Permission denied".

**Dove**: `.claude/settings.json` (livello progetto) o `~/.claude/settings.json` (livello utente).

**Come si fa**: vedi il file `esempio-settings.json` di questa cartella per la configurazione completa. La sezione chiave:

```json
{
  "permissions": {
    "deny": [
      "Write(**/TEST_*)",
      "Write(**/NOTES_*)",
      "Write(**/SCRATCH_*)",
      "Write(**/debug_*)",
      "Write(**/summary_*)",
      "Write(**/notes*.md)",
      "Write(**/scratch*.*)",
      "Write(**/*_temp.*)"
    ]
  }
}
```

**Importante**: gli asterischi sono glob pattern. `**` significa "qualsiasi cartella ricorsivamente", `*` significa "qualsiasi nome di file". Personalizza i pattern in base ai file che vedi spuntare nei tuoi progetti.

**Efficacia**: alta. Bypassa il problema della "dimenticanza" della tecnica 1, perche' la regola e' a livello sistema, non a livello prompt.

---

## Tecnica 3 — Hook PreToolUse Write

**Cosa fa**: oltre al deny passivo della tecnica 2, aggiungi un hook che ATTIVAMENTE intercetta ogni chiamata a Write e fa controlli aggiuntivi (es. nome file, contenuto, percentuale di file gia' presenti nella cartella).

**Dove**: sempre `.claude/settings.json`, sezione `hooks.PreToolUse`.

**Come si fa**: vedi `esempio-settings.json`. In sintesi:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "node ~/.claude/check-write-discipline.js"
          }
        ]
      }
    ]
  }
}
```

Lo script `check-write-discipline.js` riceve in stdin la richiesta di Write e decide se lasciarla passare o bloccarla. Logica tipica:

- Se il filename inizia con `TEST_`, `NOTES_`, etc -> blocca
- Se nella cartella ci sono gia' > 20 file `.md` -> blocca creazione nuovo .md
- Se il file e' un duplicato di uno esistente (stesso nome con suffisso `_1`, `_v2`) -> blocca

**Efficacia**: massima. Ma richiede un po' di setup. Pratico per chi ha gia' applicato 1 e 2 e vuole il livello finale di controllo.

(Il file `check-write-discipline.js` completo non e' incluso in questi materiali perche' e' uno script un po' tecnico — nel video lo mostro a schermo e do un link al gist GitHub).

---

## Tecnica 4 — Skill personalizzata "Output minimalista"

**Cosa fa**: invece di mettere le regole dentro il CLAUDE.md del progetto specifico, crei una **skill** riutilizzabile che porti su tutti i progetti.

**Dove**: cartella `.claude/skills/output-minimalista/` (livello progetto) o `~/.claude/skills/output-minimalista/` (livello utente).

**Come si fa**:

```bash
mkdir -p ~/.claude/skills/output-minimalista
nano ~/.claude/skills/output-minimalista/SKILL.md
```

Contenuto del file `SKILL.md`:

```markdown
---
name: output-minimalista
description: Disciplina la produzione di file durante le sessioni Claude Code. Da attivare su ogni progetto dove l'utente vuole mantenere la cartella ordinata. Use this skill when working on any user codebase where file proliferation is unwanted.
---

# Output minimalista

Quando questa skill e' attiva, segui queste regole:

1. Non creare file di "pensieri", "ragionamenti", "appunti", o "stato intermedio". Usa il thinking interno o il TodoWrite tool.
2. Non scrivere file di sommario alla fine di un task. Il sommario lo dai nella risposta in chat.
3. Non creare file TEST_*, NOTES_*, SCRATCH_*, debug_*, summary_*.
4. Non duplicare file esistenti con suffissi tipo _v2, _new, _temp. Modifica l'originale o chiedi conferma all'utente.
5. Se l'utente chiede "fai X" e per fare X servono 3 file, crea solo i 3 file. Niente extra.
6. Se hai bisogno di un esempio o di un test, mostra il codice nella chat — non crearne un file.

Eccezione: se l'utente chiede esplicitamente "crea un file X", crealo senza esitazione, anche se ha nome "test" o "scratch". L'utente sa quello che vuole.
```

**Efficacia**: media-alta. Le skill si attivano automaticamente quando Claude riconosce che servono. Possono essere meno deterministiche del deny pattern. Vantaggio: portabili tra progetti.

---

## Tecnica 5 — Prompt iniziale rinforzato

**Cosa fa**: quando avvii una sessione Claude Code o lanci un task importante, inizia il prompt con un'istruzione esplicita di disciplina output.

**Dove**: nel primo messaggio della sessione, o all'inizio di task complessi.

**Come si fa**: copia/incolla questo blocco all'inizio del tuo prompt iniziale (vedi `prompt-tipo.md` di questa cartella per il template completo):

```
Per questa sessione applica disciplina output massima:
- Crea SOLO i file che ti chiedo esplicitamente di creare
- Niente file scratch, notes, debug, summary
- Niente file extra non richiesti
- Se per pensare hai bisogno di stati intermedi, usali nel tuo thinking, non su disco
- Se ti viene voglia di scrivere un README/sommario alla fine, NON farlo

Quando devi mostrarmi qualcosa (es. esempio di output, snippet di test), mostralo nella chat, non in un file.
```

**Efficacia**: media. Funziona come "reminder" continuo. E' la cima dello stack: combinata con le altre 4, raggiunge il 90%+ di riduzione.

---

## Il prima e dopo (caso reale dal video)

**PRIMA delle 5 tecniche** (cartella `progetto-cliente-XYZ/` dopo 2 settimane):

```
progetto-cliente-XYZ/
|-- src/
|-- README.md
|-- TEST_button_component.md       <- inutile, generato 3 settimane fa
|-- NOTES_2026-05-08.md             <- inutile
|-- NOTES_2026-05-15.md             <- duplicato di nulla
|-- SCRATCH_layout_ideas.md         <- pensieri ad alta voce
|-- debug_form_submit.md            <- log di debug
|-- summary_recent_changes.md       <- riassunto del riassunto
|-- summary_v2.md                   <- duplicato del riassunto
|-- README_NEW.md                   <- duplicato del README
|-- TODO_feature_payment.md         <- non chiesto, sostituibile con TodoWrite
|-- temp_calculations.py            <- script di "ho pensato"
|-- notes_meeting_2026.md           <- non chiesto
|-- ... (32 file in totale, di cui ~25 inutili)
```

**DOPO le 5 tecniche** (stesso progetto, sessioni successive):

```
progetto-cliente-XYZ/
|-- src/
|-- README.md
|-- CLAUDE.md                       <- la "costituzione" del progetto
|-- ... (8 file in totale, tutti utili)
```

Riduzione: -24 file. Ripulita la cartella, ripulita la testa.

---

## Riferimenti

- **Documentazione `permissions` in settings.json**: [https://docs.anthropic.com/en/docs/claude-code/settings](https://docs.anthropic.com/en/docs/claude-code/settings)
- **Documentazione hooks in Claude Code**: [https://docs.anthropic.com/en/docs/claude-code/hooks](https://docs.anthropic.com/en/docs/claude-code/hooks)
- **Documentazione Skills**: [https://docs.anthropic.com/en/docs/claude-code/skills](https://docs.anthropic.com/en/docs/claude-code/skills)

---

## Dubbi o problemi?

- Commenta sotto il video YouTube — rispondo a tutti.
- Errore tipico: hai applicato la tecnica 2 ma Claude continua a creare file -> verifica che il pattern in `deny` sia scritto corretto (gli asterischi e i path sono finicky). Prova prima con un solo pattern e verifica che blocchi davvero.
- Errore tipico: la skill non si attiva -> verifica che il file `SKILL.md` sia nel posto giusto (`~/.claude/skills/nome-skill/SKILL.md`) e che il `description` nel frontmatter sia chiaro.

Buon ordine.
