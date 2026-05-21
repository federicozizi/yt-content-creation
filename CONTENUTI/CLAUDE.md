# CONTENUTI/

Output prodotto: una cartella per ogni video da registrare. Ogni cartella ha **esattamente 3 cose** (vedi `../CLAUDE.md` per le regole globali).

## Struttura di una cartella contenuto

```
CONTENUTI/<slug>/
|-- PRINCIPALE.html            <- guida regista (italiano)
|-- PRINCIPALE_ENG.html        <- traduzione inglese
`-- materiali/                 <- cartella zippabile per il pubblico
    |-- README.md              <- guida step-by-step (obbligatorio)
    |-- DISCLAIMER.md          <- solo se ci sono credenziali/.env
    `-- ... (altri file se servono al video)
```

**Niente altro.** Non aggiungere SCRIPT.md, _revisione.md, varianti tecniche, sottocartelle gemelle EN. Quella roba era v5 ed e' archiviata.

## Convenzioni slug

- Lowercase, separato da trattini
- Italiano (la lingua di produzione)
- Termini propri restano invariati (es. `claude-code` resta `claude-code`)
- Esempi validi: `agenti-ai-per-fatturazione`, `claude-skills-pratici`, `mcp-per-non-developer`

## Come si produce una nuova cartella

L'utente dice "lavora sull'idea X". Claude:

1. Cerca l'idea in `IDEE/manuali.md` o `IDEE/ricerche-auto/*.md` (per match parziale di titolo)
2. Estrae titolo + descrizione + (se ricerca-auto) angolo + hook
3. Crea `CONTENUTI/<slug>/` partendo dal template `_TEMPLATE_CONTENUTO/`
4. Compila i 3 artefatti:
   - `materiali/README.md` — guida step-by-step a prova di idiota
   - `materiali/DISCLAIMER.md` — **solo se** il contenuto usa `.env` o credenziali; altrimenti rimuovi il file
   - `PRINCIPALE.html` — intro persuasiva sotto 1 minuto + step (cosa mostrare + cosa dire) + CTA
   - `PRINCIPALE_ENG.html` — traduzione integrale del PRINCIPALE
5. Se il contenuto include file pratici (script, prompt, config), li mette al root di `materiali/`, mai in sottocartelle numerate

## Regola sync IT <-> EN

Quando rigeneri il PRINCIPALE.html devi rigenerare anche il PRINCIPALE_ENG.html (traduzione). Non lasciare mai le due versioni divergenti.

Se l'utente dice solo "rifai il PRINCIPALE", si intende **entrambi**.

## Regola DISCLAIMER

Il file `materiali/DISCLAIMER.md`:

- **Esiste** se nei materiali c'e' un `.env` o `.env.example`, o se la guida menziona credenziali API, token, password
- **NON esiste** altrimenti (cancellalo se l'avevi creato e poi hai capito che non serve)

Contenuto tipo (template): vedi `_TEMPLATE_CONTENUTO/materiali/DISCLAIMER.md`.
