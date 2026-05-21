<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-and-antigravity/materiali/README.md -->

# Claude Code + Antigravity — materiali del video

Workflow combinato: Antigravity esplora in parallelo (cloud), tu scegli, Claude Code integra in locale.

**Niente da installare oltre a Claude Code e un account Google.** I file qui dentro sono prompt e regole: si copia-e-incolla.

## Cosa c'è in questa cartella

```
.
├── README.md                                  ← stai leggendo questo
├── CLAUDE.md                                  ← Claude Code lo legge da solo: è la memoria del progetto
├── .gitignore                                 ← protegge eventuali artefatti privati
├── PRINCIPALE.html                            ← copia della guida video, comoda offline
├── prompts/
│   ├── antigravity-parallel-draft.md          ← prompt da incollare in Antigravity
│   └── claude-code-handoff.md                 ← prompt da dare a Claude Code in locale
└── esempio-output.md                          ← come si presenta il risultato dopo il workflow
```

## Quick start (3 mosse)

```
# 1. Apri Antigravity nel browser (antigravity.google.com),
#    carica il tuo index.html nel workspace e spawna 3 sessioni.
#    In ognuna incolla il prompt da prompts/antigravity-parallel-draft.md
#    cambiando solo la parola STILE.

# 2. Quando i 3 agenti finiscono, scegli la preview migliore,
#    scarica l'artefatto come "landing-vincitrice.html"
#    e mettilo in questa cartella.

# 3. Lancia Claude Code dentro la cartella del tuo sito reale:
cd ~/percorso/al/tuo-sito
claude
#    e incolla il prompt da prompts/claude-code-handoff.md
```

Tutto qui. Niente venv, niente API key, niente pip install: il workflow è due tool che già usi, in ordine.

## Setup automatico (alternativa)

Lancia `claude` dentro questa cartella e scrivi:

> "Esegui il setup leggendo CLAUDE.md."

Claude Code legge le regole del progetto e ti guida a (a) verificare che hai un sito su cui lavorare, (b) preparare la struttura per ricevere l'artefatto da Antigravity, (c) caricare il prompt di handoff quando torni dal cloud.

## Sicurezza

- Antigravity lavora in sandbox isolata, quindi non vede i tuoi file locali. Carica solo file che ti senti di esporre al cloud (tipicamente l'`index.html` di una landing pubblica va benissimo).
- L'artefatto che scarichi da Antigravity è HTML statico. Aprilo in VS Code prima di passarlo a Claude Code per controllare a colpo d'occhio che non ci siano script esterni sospetti.
- Il `.gitignore` in questa cartella esclude la sottocartella `_archivio/` dove finiscono gli artefatti scartati: niente di sensibile, ma niente neanche da committare.

## Per il pubblico del video

Nel video ho mostrato il caso "refresh di una home page". Il pattern vale per qualunque cosa fatta di file: email in N toni, proposte cliente in N angoli, documentazione in N voci. La parte di Antigravity cambia solo il prompt, la parte di Claude Code cambia solo "in che file integrare l'artefatto".
