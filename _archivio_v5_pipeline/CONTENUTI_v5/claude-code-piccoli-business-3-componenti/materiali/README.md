<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/README.md -->

# Claude Code per piccoli business — materiali del video

Le 3 componenti imprescindibili: Supabase via MCP, Claude for Small Business (pacchetto Anthropic), Agent View con sub-agent custom.

**Niente di esotico da installare oltre a Claude Code, un account Supabase gratuito, e un piano Claude Cowork Team.**

## Cosa c'è in questa cartella

```
.
├── README.md                                  ← stai leggendo questo
├── CLAUDE.md                                  ← Claude Code lo legge da solo: regole del progetto
├── .gitignore                                 ← protegge .env e altri file sensibili
├── .env.example                               ← template credenziali Supabase
├── PRINCIPALE.html                            ← copia della guida video, offline
├── schema-aziendale.sql                       ← 4 tabelle Supabase pronte
├── esempio-output.md                          ← come si presenta il risultato finale
├── .claude/
│   ├── mcp.json                               ← config connettore MCP Supabase
│   └── agents/
│       ├── document-classifier.md             ← sub-agent: classifica documenti italiani
│       ├── regime-checker.md                  ← sub-agent: alert soglie regime fiscale
│       └── scadenza-allerter.md               ← sub-agent: scadenze custom mattutine
├── prompts/
│   ├── 01-supabase-mcp-setup.md               ← setup Step 1
│   ├── 02-claude-cowork-smb-onboard.md        ← setup Step 2 (nel browser)
│   ├── 03-launch-custom-agents.md             ← setup Step 3
│   └── 04-integrazione-end-to-end.md          ← flusso completo dei 3 componenti
└── docs/
    ├── supabase-mcp-howto.md                  ← MCP nel dettaglio, troubleshooting, sicurezza
    ├── claude-for-small-business-howto.md     ← il pacchetto Anthropic A-Z
    └── connettori-pacchetto-vs-custom.md      ← quando usare uno vs l'altro
```

## Quick start (3 step in ~30 minuti)

```
# 1. Step 1 — Supabase via MCP
cp .env.example .env             # poi compila SUPABASE_URL e SUPABASE_SERVICE_ROLE_KEY
claude
# Incolla il prompt da prompts/01-supabase-mcp-setup.md.

# 2. Step 2 — Claude for Small Business
# Tutto nel browser, NON in terminale. Apri claude.com/cowork (richiede piano Team),
# digita /smb-onboard nella chat, segui le istruzioni del prompt 02.

# 3. Step 3 — Agent View con sub-agent custom
claude
# Incolla il prompt da prompts/03-launch-custom-agents.md.

# 4. (Bonus) Vedi tutti e 3 lavorare insieme
# Segui prompts/04-integrazione-end-to-end.md (alterna terminale e browser).
```

## Setup automatico (alternativa)

Lancia `claude` dentro questa cartella e scrivi:

> "Esegui il setup leggendo CLAUDE.md."

Claude Code parte da Step 1, ti guida step by step, ti chiede gli input umani quando servono (creazione progetto Supabase, attivazione pacchetto in Cowork) e prosegue da solo dove può.

## Stato setup

Aggiorna queste voci man mano che completi gli step (Claude Code lo può fare per te al termine di ciascuno):

- [ ] Step 1 — Supabase via MCP attivo
- [ ] Step 2 — Pacchetto Claude for Small Business attivo in Cowork
- [ ] Step 3 — Sub-agent custom funzionanti in Agent View
- [ ] Integrazione — Supabase visibile sia da Code che da Cowork (vedi prompts/04)

## Per il pubblico del video

Nel video ho usato lo studio commercialisti come case study. Lo schema è agnostico del settore — vedi la sezione "Oltre lo studio commercialisti" del PRINCIPALE.html per come applicarlo a studio legale, e-commerce, agenzia, B&B, artigiano.

## Sicurezza credenziali

- `.env` con la service_role key di Supabase è già protetto da `.gitignore`. Non rimuovere.
- Il pacchetto Anthropic gestisce i suoi OAuth dentro Cowork — non vengono mai salvati in questa cartella.
- Se hai esposto la service_role key per sbaglio (commit pubblico, screenshot, ecc.), vai SUBITO in Supabase Settings → API → "Reset service_role secret" e aggiorna `.env`. Dettagli in `docs/supabase-mcp-howto.md` sezione sicurezza.
