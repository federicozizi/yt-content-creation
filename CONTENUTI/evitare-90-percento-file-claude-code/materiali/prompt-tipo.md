# Prompt-tipo iniziale rinforzato (Tecnica 5 del video)

Quando avvii una nuova sessione Claude Code o lanci un task complesso, copia questo blocco come primo messaggio prima della tua richiesta vera. Funziona da "richiamo" delle regole anche se hai gia' tutto il resto configurato.

---

## Blocco da copiare all'inizio di ogni sessione importante

```
[OUTPUT DISCIPLINE - regole di sessione]

Per tutta questa sessione applica disciplina output massima. NON creare:
- File scratch, notes, debug, summary, temp
- File con prefisso TEST_, NOTES_, SCRATCH_, debug_, summary_
- File di "ragionamento" o "stato intermedio" su disco
- Sommari finali in formato file (sommario in chat, sempre)
- Documentazione duplicata (es. README aggiuntivi se ne esiste gia' uno)

Crea SOLO i file:
- Strettamente richiesti dal task che ti chiedo
- Esplicitamente chiesti da me ("crea il file X")
- Necessari al funzionamento del codice (es. config richiesti dal framework)

Se hai bisogno di tenere traccia di stati intermedi durante il task, usa il TodoWrite tool, MAI file scratch su disco.

Se ti viene voglia di scrivere un riassunto finale come file, NON farlo - dammelo nella tua risposta in chat.

---

[INIZIO TASK]

[Qui inserisci la tua richiesta vera. Esempi:]

"Aggiungi un campo email obbligatorio al form di registrazione utente. Aggiorna validazione lato client e server."

"Risolvi il bug del pulsante 'Salva' che non triggera l'evento submit su Safari."

"Refactora il modulo `auth.js` separando autenticazione e autorizzazione in due file."
```

---

## Quando vale la pena usare questo blocco

Sempre? Quasi mai? Dipende da quanto pulite sono le altre tecniche.

**Usalo SEMPRE** se:
- Non hai ancora applicato la Tecnica 1 (CLAUDE.md con output discipline) o la Tecnica 2 (deny patterns)
- Lavori su un progetto nuovo dove le configurazioni non sono ancora attive
- Stai facendo un task complesso o di lunga durata (sessioni lunghe -> piu' probabilita' che Claude "dimentichi" CLAUDE.md)

**Usalo OCCASIONALMENTE** se:
- Hai gia' CLAUDE.md + settings.json + skill configurati
- Stai facendo task brevi e ben definiti

**NON usarlo** se:
- Stai facendo un task molto piccolo, tipo "spiegami questa funzione" (e' overkill)
- L'utente con cui lavori (se sei in coppia) si lamenta che il prompt iniziale e' troppo lungo

---

## Variante "task brutale" (sessioni lunghe)

Se sai gia' che la sessione sara' lunga e complessa, una variante piu' assertiva:

```
[REGOLE DI SESSIONE - PRIORITA' ASSOLUTA]

Sono in una sessione di lavoro che sara' lunga. Mantieni queste regole per tutta la sessione, anche se le dimentichi a meta':

1. NON creare file che non ti ho chiesto esplicitamente.
2. NON scrivere sommari, notes, debug, scratch, temp - mai.
3. Se per pensare ti serve scrivere qualcosa, scrivilo nella chat, non in un file.
4. Ogni 5 messaggi, ripeti a te stesso queste regole nel thinking.
5. Se ti viene voglia di "documentare per il futuro" mettendo file extra, resisti.

Se sento che hai dimenticato queste regole, te le ricordo dicendo "DISCIPLINE". Quando lo dico, fermati e rileggi questo elenco.

---

[TASK]:

[la tua richiesta]
```

L'aggiunta della keyword "DISCIPLINE" e' utile perche' ti da' un richiamo veloce — basta scriverla nella chat per riportare Claude in carreggiata senza ripetere tutto il blocco.

---

## Tips per integrarlo nel tuo workflow

1. **Salva il blocco come snippet** nel tuo VS Code (o text expander tipo Espanso/aText). Lo lanci con due tasti.

2. **Crea un alias bash** che lo prefigge automaticamente:
   ```bash
   alias claude-disciplinato='claude --append-system-prompt "$(cat ~/.claude/output-discipline.txt)"'
   ```
   Poi `claude-disciplinato` ti apre Claude Code col blocco gia' iniettato come istruzione di sistema.

3. **Usa lo Skill** (Tecnica 4) se preferisci. Una skill ben fatta carica le regole automaticamente quando serve, senza che tu debba copia-incollare nulla.

Le tecniche 1-5 sono in ordine di permanenza. La 1 e la 2 sono "set once, work forever". La 5 e' "applica ogni volta". Mix come preferisci.
