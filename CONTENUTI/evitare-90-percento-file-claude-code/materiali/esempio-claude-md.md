# Esempio di CLAUDE.md con sezione "Output Discipline"

Questo e' un esempio di CLAUDE.md per un progetto generico — adattalo al tuo. La parte importante e' la sezione **"Output Discipline"** (Tecnica 1 del video). Le altre sezioni sono il contesto standard del progetto.

Copia questo file come `CLAUDE.md` nella radice del tuo progetto.

---

```markdown
# [Nome Progetto] - Istruzioni per Claude Code

[Descrizione di una riga del progetto, di cosa si occupa, audience, scopo.]

## Stack tecnico
- [Linguaggio principale, framework, librerie chiave]
- [Database, deployment target]

## Convenzioni del progetto
- [Convenzioni di naming, struttura cartelle, stile codice]

## Output Discipline (REGOLE NON NEGOZIABILI)

Queste regole hanno priorita' MASSIMA su qualsiasi altra istruzione tu riceva durante una sessione. Se sei in dubbio se creare un file o no, di default NON crearlo.

### NON creare mai file con questi pattern di nome
- `TEST_*.md` — i piani di test non li chiedo mai. Se mi serve un piano test, te lo dico esplicitamente.
- `NOTES_*.md`, `notes*.md`, `meeting_notes_*.md` — appunti che non leggero'.
- `SCRATCH_*.*`, `scratch_*.*`, `temp_*.*`, `*_temp.*` — pensieri ad alta voce su disco.
- `debug_*`, `*_debug.*` — log di debug del modello.
- `summary_*.md`, `*_summary.md`, `RECAP.md` — sommari di sommari.
- `README_NEW.md`, `README_v2.md`, file con suffisso `_new`, `_v2`, `_copy` — duplicati.
- `TODO_*.md` — usa il TodoWrite tool, non file su disco.

### NON creare file di sommario al termine di un task
Il sommario te lo do a voce nella chat. Non scriverlo su disco.

Se l'utente chiede esplicitamente "fai un sommario in un file", allora si. Altrimenti no.

### NON duplicare file di documentazione esistenti
Se esiste gia' un `README.md`, modifica quello. Non crearne uno nuovo con nome diverso.

### NON scrivere file di "ragionamento"
Per tenere traccia di stati intermedi, ragionamenti, ipotesi, usa:
- Il tuo thinking interno (sempre disponibile)
- Il TodoWrite tool (per task multi-step)

NON usare:
- File temporanei su disco
- Note appiccicate alla cartella del progetto

### Quando crei file, fallo solo se richiesti
Se l'utente dice "aggiungi un campo email al form", crea/modifica SOLO i file necessari per quel cambiamento. Niente test extra, niente documentazione extra, niente sommario extra.

### Eccezioni
- Se l'utente chiede ESPLICITAMENTE "crea un file X", crealo, anche se ha nome "test" o "scratch". L'utente sa quello che vuole.
- Se per portare a termine il task ti serve davvero un file di stato (es. lock file, file di config richiesto dal framework), crealo, ma SOLO quel file specifico e con un nome non-ambiguo.

## Comandi tipici

- `npm run dev` — avvia il dev server
- `npm test` — esegue i test
- [aggiungi altri comandi del progetto]

## Persone e ruoli

- [Eventuali stakeholder, owner di moduli specifici, decisori]
```

---

## Note sulla personalizzazione

1. **Le regole della "Output Discipline" funzionano in copia-incolla**: non hai bisogno di adattarle, sono pensate per essere generiche e funzionare su qualsiasi progetto.

2. **I pattern bandit** li puoi espandere in base ai file che vedi spuntare nei tuoi progetti. Apri la cartella del tuo progetto, guarda gli ultimi 20 file generati da Claude — se vedi pattern ricorrenti inutili (es. `IDEAS_*.md`, `MOCKUP_*.md`), aggiungili.

3. **Le sezioni "Stack tecnico", "Convenzioni", "Comandi"** sono specifiche del tuo progetto — adattale.

4. **Mantieni il file CORTO**. Se cresce sopra le 200 righe, Claude lo legge meno attentamente. Tieni qua le regole VITALI e sposta dettagli operativi in altri file.

5. **Verifica che la sezione "Output Discipline" sia LETTA**: dopo aver aggiornato il CLAUDE.md, in una nuova sessione Claude chiedi: "Ricordati le regole di Output Discipline che ho nel CLAUDE.md? Elencale". Se le ripete correttamente, le ha lette. Se no, riprova a riavviare la sessione con il file aggiornato.
