# Setup automatico — Claude Code, leggi qui

Sei stato lanciato dentro la cartella materiali del template **GitHub per Claude Code**. Tutto è già qui: workflow Actions, hook pre-commit, prompt orchestratore, `CLAUDE.md` di contesto. Tu fai solo: prerequisiti + creazione repo GitHub + secret + primo test. ~5 minuti.

## Cosa fare

### 1. Verifica prerequisiti

```bash
gh --version            # GitHub CLI: https://cli.github.com
gh auth status          # deve dire "Logged in"
claude --version        # se manca: npm install -g @anthropic-ai/claude-code
```

Se manca qualcosa, segnalalo all'utente coi link giusti.

### 2. Chiedi il nome del nuovo repo

Chiedi all'utente:
- Nome del repo (es. `competitor-intel`)
- Privato o pubblico? (default: privato)

### 3. Crea il repo GitHub partendo dalla cartella corrente

```bash
gh repo create <nome> --private --source . --push
```

Questo: inizializza git locale, fa il primo commit, crea il repo su GitHub, fa il push. Tutto in un comando.

### 4. Aggiungi il secret ANTHROPIC_API_KEY

Chiedi all'utente la sua API key Anthropic (`sk-ant-...`). Se non ce l'ha, mandalo su https://console.anthropic.com → Settings → API Keys.

```bash
gh secret set ANTHROPIC_API_KEY
# (incolla la chiave quando te la chiede)
```

### 5. Configura i competitor

Apri `competitors.json`, mostralo all'utente, e aiutalo a sostituire i 3 placeholder coi suoi competitor reali.

Committa e push:

```bash
git add competitors.json
git commit -m "config: competitor reali"
git push
```

### 6. Test manuale del workflow

```bash
gh workflow run daily-brief.yml
gh run watch
```

Aspetta 1-2 minuti. Quando finisce:

```bash
gh pr list
```

Dovresti vedere la PR del brief. Mostrala all'utente:

```bash
gh pr view --web
```

### 7. (Opzionale) Attiva il pre-commit hook localmente

Se l'utente vuole il TRUCCO #5 (review pre-commit) anche in locale:

```bash
cp .github/hooks/pre-commit-claude-review.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 8. Tutto pronto

Da domani alle 7:05 UTC arriverà una PR ogni mattina con il brief.

Per disabilitare: tab Actions su GitHub → workflow → Disable.
Per cambiare orario: modifica `cron:` in `.github/workflows/daily-brief.yml`.

## Note per te (Claude Code)

- **Non creare cartelle progetto separate**: questa cartella È il repo del progetto.
- **Non rimuovere `CLAUDE.md`**: è il file che ti dà contesto persistente nel repo. Se lo cancelli, le sessioni future partiranno alla cieca.
- Tono diretto, conciso. Niente paragrafi accademici.
- Se un comando fallisce, mostra l'errore e suggerisci la correzione invece di ripartire da zero.
