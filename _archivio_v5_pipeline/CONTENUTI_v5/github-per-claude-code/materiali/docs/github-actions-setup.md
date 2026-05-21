# Setup GitHub Actions con Claude Code

Come far girare Claude Code in cloud (anche col tuo PC spento), schedulato o triggered da eventi GitHub.

## 1. Aggiungi i secret al repo

Vai su **Settings → Secrets and variables → Actions → New repository secret** e crea:

| Nome | Valore | Come averlo |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-...` | https://console.anthropic.com → Settings → API Keys |
| `GMAIL_APP_PASSWORD` (opz.) | `xxxx xxxx xxxx xxxx` | https://myaccount.google.com/apppasswords (richiede 2FA) |

> **Importante**: i secret di GitHub sono **write-only** una volta creati. Non riesci più a leggerli. Salvali in un password manager prima di incollarli.

## 2. I 2 workflow inclusi

### `daily-brief.yml` — Brief schedulato

Trigger: ogni giorno alle 7:05 UTC (`cron: "5 7 * * *"`) + manuale.

Cosa fa:
1. Checkout del repo
2. Installa Node + Claude Code CLI
3. Esegue Claude Code col prompt in `prompts/daily-brief.md`
4. Apre una PR con il brief generato (`peter-evans/create-pull-request`)

Tu lo mergi quando hai 30 secondi.

### `issue-task.yml` — Issue → PR automatica

Trigger: ogni volta che a una issue viene aggiunta la label `claude-task`.

Cosa fa:
1. Legge il body della issue
2. Lo passa a Claude Code come prompt
3. Claude implementa la modifica + apre una PR che chiude l'issue

Workflow tipico:
- Apri issue: *"Aggiungi anche Delta Corp ai competitor"*
- Aggiungi label `claude-task`
- 1 minuto dopo trovi una PR pronta da revisionare

## 3. Permessi del `GITHUB_TOKEN`

Nel workflow vedi:

```yaml
permissions:
  contents: write
  pull-requests: write
```

Servono perché Claude deve poter committare e aprire PR. **Niente `admin`** — Claude non deve cancellare repo o gestire user.

## 4. Costi

GitHub Actions su repo pubblici è **gratis e illimitato**. Su repo privati hai 2.000 minuti/mese gratis nel piano Free, 3.000 nel Pro.

Una run del `daily-brief.yml` consuma ~30-60 secondi → **~3 minuti/mese** se gira ogni giorno. Trascurabile.

I costi veri sono lato Anthropic API: ~$0.01-0.05 per run a seconda della complessità del prompt e del modello scelto.

## 5. Debugging quando una run fallisce

Tab **Actions** → click sulla run rossa → click sullo step fallito → leggi il log.

Errori comuni:
| Errore | Causa | Fix |
|---|---|---|
| `ANTHROPIC_API_KEY: not found` | Secret non creato | Settings → Secrets → crea `ANTHROPIC_API_KEY` |
| `claude: command not found` | Step di install saltato | Verifica che lo step `Install Claude Code CLI` sia presente |
| `Permission denied for github-actions` | Mancano `permissions:` | Aggiungi `contents: write, pull-requests: write` |
| Claude non apre la PR | Branch già esistente | Lo step `peter-evans/create-pull-request` ha `delete-branch: true` — verifica |

## 6. Limitare quando gira (per non sprecare API credit)

Se vuoi che giri solo nei giorni lavorativi:

```yaml
on:
  schedule:
    - cron: "5 7 * * 1-5"   # lun-ven
```

Se vuoi disabilitarlo temporaneamente senza cancellarlo:
- Tab **Actions** → click sul workflow → **Disable workflow**
