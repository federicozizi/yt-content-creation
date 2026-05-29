# CLAUDE.md — checkpoint del contenuto "Claude 4.8 + Dynamic Workflows + 10 agenti"

> Questo file e' la **fonte di verita'** per qualsiasi sessione Claude che lavora su questa cartella, in particolare durante il `/loop /esegui` programmato fino alle 22:30 di oggi (2026-05-28).
>
> Ogni volta che vieni invocato qui: **leggi prima questo file, esegui il prossimo task non completato, aggiorna lo stato in fondo, fine.**

---

## Contesto del contenuto

- **Titolo del video**: *Claude 4.8: faccio lavorare 10 agenti in parallelo sul mio business (la nuova feature "Dynamic Workflows")*
- **Format**: Build dimostrativa (vedi `../../CLAUDE.md` paragrafo "Format YouTube ad alta performance")
- **Audience**: imprenditori / manager / freelance non tecnici
- **Durata target**: 15 minuti
- **Data registrazione prevista**: 2026-05-29 mattina (l'utente apre la cartella, legge PRINCIPALE.html, registra)
- **Lingua di produzione**: italiano (PRINCIPALE.html), traduzione inglese in PRINCIPALE_ENG.html

## La demo (cuore del video)

Il sistema gira come **routine schedulata di Claude** (vedi `materiali/ROUTINE.md`). A ogni esecuzione Claude (Opus 4.8):

1. lancia i 10 scraper (`python orchestrator.py --no-open`) → 100 trend grezzi in `output/*.json`
2. apre **10 sub-agenti in parallelo** (Dynamic Workflows), uno per piattaforma: filtrano i trend secondo `materiali/ARGOMENTI.md` e generano idee video
3. **valuta** se la raccolta basta e, se no, rilancia mirato (max 2 volte)
4. scrive `output/synthesis.html`, rigenera `dashboard.html` e il report in `IDEE/ricerche-auto/`

Tutta la logica vive in `materiali/CLAUDE.md` (il cervello) + `materiali/ARGOMENTI.md` (i temi).

**Fallback (se Dynamic Workflows fa storie)**: si lancia direttamente `python orchestrator.py` — la dashboard si apre comunque con i 100 trend grezzi e senza sintesi. Non può fallire catastroficamente.

> Nota: il percorso **on-demand** (incollare un prompt a mano in Claude Code) è stato **rimosso**. Il sistema gira solo via routine schedulata. `PROMPT_DEMO.md` non esiste più (recuperabile da git).

---

## Stato dei task (aggiornare a ogni passaggio)

| # | Task | Stato | Note |
|---|------|-------|------|
| 1 | Folder scaffolding | DONE | Cartella + sottocartelle create |
| 2 | 10 scraper Python no-API | DONE | Testati: 10/10 ritornano dati validi |
| 3 | `orchestrator.py` + dashboard auto-open | DONE | Testato end-to-end: dashboard 49KB, 10/10 OK |
| 4 | Routine schedulata (CLAUDE.md + ARGOMENTI.md + ROUTINE.md) | DONE | On-demand/PROMPT_DEMO.md rimosso — solo routine |
| 5 | `materiali/README.md` (audience non tech) | DONE | Quick start + step-by-step + concetti |
| 6 | `materiali/DISCLAIMER.md` | N/A | Nessun .env / credenziale → file non necessario |
| 7 | `PRINCIPALE.html` (italiano) | DONE | **Presentazione cliente** (hero + 4 fasi + ciclo Claude + architettura + requisiti). Non più script video |
| 8 | `PRINCIPALE_ENG.html` (traduzione) | DONE | Traduzione fedele della presentazione IT — sincronizzata (117/117 div) |
| 9 | Polish voice guide su PRINCIPALE.html | DONE | Ristrutturato 7→5 step; rimossa apertura difensiva Step 1; allineata promessa intro con struttura |
| 10 | Test orchestrator (smoke) | DONE | 10/10 piattaforme verdi — 2026-05-28 |
| 11 | Verifica sync IT ↔ ENG | DONE | Entrambi i file a 5 step, allineati |
| 12 | Re-leggi PRINCIPALE.html a voce alta (mentale) | DONE | Voice guide check PASS — nessun termine-blog, analogie ok, niente ref. temporali |

---

## Task #9 — Polish voice guide su PRINCIPALE.html (checklist da rifare a ogni loop)

Apri `PRINCIPALE.html` e applica la **checklist voice guide** del CLAUDE.md radice (`../../CLAUDE.md` → "Voice Guide"):

- [ ] **Niente termini-da-blog-tecnico** nelle frasi "Cosa dire". Vietati: "standard de facto", "attack surface", "sandbox", "scope read-only", "endpoint/payload/API", "self-hosted", "setup un filo piu' tecnico"
- [ ] **Analogie ricorrenti** per ogni concetto astratto. In particolare:
  - Dynamic Workflows = "10 stagisti specializzati che lavorano in parallelo mentre tu segui il cliente"
  - Sub-agente = "stagista con un compito preciso, torna con un risultato"
  - Scraper = "un piccolo addetto che ti sbircia una piattaforma e ti torna i titoli importanti"
- [ ] **Hook personalizzato non-funnel**. Storia vera che apre. Mai "in questo video ti mostro X" piatto
- [ ] **Wow dal pratico-utile** (calendario editoriale generato in pochi minuti, valore concreto) NON dal drammatico-clickbait ("ho risparmiato 18 ore!" se non e' verificato)
- [ ] **Sano effetto nerd** = ammirazione per la magia del processo. Es: "guarda cosa sta succedendo — 10 cervelli che lavorano insieme su 10 piattaforme diverse, in parallelo, e in qualche minuto hai sul tavolo un mese di idee"
- [ ] **Niente riferimenti temporali** nelle frasi da pronunciare. No "per 30 secondi", no "ora prendi 2 minuti"
- [ ] **Intro sotto 1 minuto**: leggila a voce mentale, se supera ~70 secondi tagliala

Se trovi qualcosa da migliorare, modifica il file e **riallinea immediatamente PRINCIPALE_ENG.html** (regola sync IT↔EN dal CLAUDE.md di `CONTENUTI/`).

---

## Task #10 — Smoke test orchestrator

Ogni passaggio del loop deve garantire che la demo funzioni ancora. Esegui:

```bash
cd materiali
python orchestrator.py
```

Atteso:
- output: "10/10 piattaforme con dati validi"
- `dashboard.html` rigenerato e dimensione > 30KB
- Il browser apre il file (nei loop non interattivi puoi patchare `webbrowser.open` come nel test precedente)

Se < 10 piattaforme tornano dati, **investiga lo scraper rotto**:
- Probabilmente UA bloccato, rate limit, o endpoint cambiato
- Fixa lo scraper in `materiali/scrapers/<nome>.py`
- Re-esegui finche' torna verde

**Non procedere con altri task se la demo non gira.** La regola dell'utente: "il test deve funzionare".

---

## Task #11 — Sync IT ↔ ENG

Regola dal `CONTENUTI/CLAUDE.md`: PRINCIPALE.html e PRINCIPALE_ENG.html non possono divergere.

Se PRINCIPALE.html viene modificato in qualsiasi modo:
- riallinea PRINCIPALE_ENG.html mantenendo:
  - stessa struttura (intro + step N + CTA)
  - traduzione naturale (non letterale) delle analogie (es. "stagisti" → "interns")
  - vincolo intro <1 min anche in inglese

---

## Task #12 — Re-lettura finale a voce (mentale)

Prima di marcare il contenuto "ready to record":
- Leggi mentalmente ogni blocco "Cosa dire" del PRINCIPALE.html
- Domanda: *"se lo dicessi questa sera a cena a un amico imprenditore non tecnico, lui mi capirebbe e penserebbe che e' interessante?"*
- Se la risposta e' no, riscrivi

---

## Vincoli del contenuto (REGOLE NON NEGOZIABILI)

- **NON aggiungere file di troppo**. Solo i 3 artefatti previsti dal CLAUDE.md radice (materiali/, PRINCIPALE.html, PRINCIPALE_ENG.html) + i file demo dentro materiali/ (scraper, orchestrator, dashboard).
- **NON modificare la struttura della cartella**. Niente SCRIPT.md, niente _revisione.md, niente varianti tecniche.
- **NON aggiungere DISCLAIMER.md** — non ci sono .env / credenziali in questa demo.
- **NON cambiare i 10 nomi delle piattaforme** una volta scelti — sono referenziati in scraper + orchestrator + prompt + dashboard.

---

## Quando si considera il contenuto "ready to record"

Tutti questi punti sono veri:

- [ ] Task 9, 10, 11, 12 sono DONE
- [ ] `python orchestrator.py` gira con 10/10 (ultimo smoke test entro 1 ora dalla registrazione prevista)
- [ ] PRINCIPALE.html e PRINCIPALE_ENG.html allineati
- [ ] README.md di materiali/ leggibile da un imprenditore senza chiedere niente

Quando sono tutti DONE, scrivere in fondo a questo file una riga:
`READY TO RECORD - YYYY-MM-DD HH:MM`

---

READY TO RECORD - 2026-05-28 22:10
