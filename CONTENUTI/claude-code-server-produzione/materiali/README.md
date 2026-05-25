# Hai mai messo Claude Code in un vero server di produzione? Io l'ho fatto.

> Materiali del video YouTube **"Hai mai messo Claude Code in un vero server di produzione? Io l'ho fatto."**.
> Trovi qui il setup completo del sistema che ho costruito (uno scraper prezzi competitor che gira 30 giorni di fila su un VPS), le 5 regole che ho imparato sulla mia pelle, e tutto il materiale per replicarlo a casa tua.

---

## In 30 secondi — la storia in breve

Quattro mesi fa ho deciso di provare una cosa che la maggior parte degli utenti di Claude Code non fa mai: **mettere Claude Code in un server di produzione che gira ventiquattro ore su ventiquattro**.

Caso d'uso scelto: uno scraper di prezzi competitor — ogni notte alle quattro del mattino, il server visita 3 siti di competitor di un mio cliente, estrae i prezzi dei prodotti chiave, salva in un database, e manda un report email se ci sono variazioni significative.

Cose che ho scoperto:
- ✅ Funziona — il sistema gira da 30 giorni di fila, ha trovato 7 variazioni di prezzo che avrebbero perso ore di analisi manuale
- ⚠️ Ho sbattuto la testa 3 volte (selettori CSS, banning IP, consumi token)
- 📚 Ho imparato 5 regole che ora applico SEMPRE quando metto Claude in produzione

Questo documento ti spiega come replicare il setup + le 5 regole.

---

## Cosa ti serve prima di iniziare

- [ ] **VPS economico** (DigitalOcean, Hetzner, Linode, Vultr) — 5-10 USD/mese. Nel video uso DigitalOcean da 6 USD/mese.
- [ ] **API key Anthropic** — [https://console.anthropic.com](https://console.anthropic.com) — necessaria per Claude Code in modalita' non-interattiva
- [ ] **Conoscenza minima di SSH e terminale Linux** — se non sai cos'e' SSH, comincia da un tutorial base prima di tornare qui
- [ ] **VS Code** — [https://code.visualstudio.com](https://code.visualstudio.com) — per modificare i file di configurazione
- [ ] 45-60 minuti per il primo setup. Dopo, il sistema gira solo.

---

## Le 5 regole che ho imparato (lista completa)

Le 5 regole sono il cuore del video. Le metto qui in cima per chi cerca un riferimento veloce.

### Regola 1 — Mai eseguire Claude Code come utente `root`
Sul VPS crea un utente dedicato con permessi minimi. Se Claude Code combina un errore (e in 30 giorni e' successo una volta), il danno e' contenuto. Se lo lasci girare come root, un comando sbagliato e' catastrofe.

### Regola 2 — Hook bloccanti per i comandi distruttivi
Aggiungi a `~/.claude/settings.json` un hook `PreToolUse` per `Bash` che blocca pattern come `rm -rf`, `sudo`, `> /dev/`, `mkfs`. Mai gli dai questi comandi, mai succedono per errore.

### Regola 3 — Logging aggressivo, sempre
Ogni esecuzione di Claude Code scrive su un file di log con: timestamp, prompt iniziale, decisioni prese, comandi eseguiti, output. In caso di problema, hai la storia di cosa e' successo. In caso di tutto bene, hai metriche per ottimizzare.

### Regola 4 — Dry-run mode prima di ogni deploy
Quando modifichi il prompt o il setup, **gira sempre prima in dry-run** (Claude pensa ma NON esegue comandi distruttivi). Lo vedi cosa farebbe. Solo se ti convince, lo lanci sul serio.

### Regola 5 — Budget API con alert
Imposta un alert nell'Anthropic Console su un budget mensile preciso. Quando supera l'80%, ricevi mail. Cosi' non ti svegli col conto da 400 EUR dopo un loop infinito del modello.

Approfondimento di ogni regola sotto, nella Guida completa.

---

## Quick start (per chi vuole partire subito)

1. Crea un VPS DigitalOcean da 6 USD/mese, Ubuntu 22.04, regione Frankfurt
2. SSH al VPS, crea utente `claude` non-root (`sudo adduser claude`)
3. Installa Node.js e Claude Code come utente `claude`
4. Copia il file `claude-md-produzione.md` di questa cartella come `/home/claude/scraper/CLAUDE.md`
5. Copia `scraper-prompt.md` come istruzione del task ricorrente
6. Schedula con cron: `0 4 * * * claude --headless -f /home/claude/scraper/scraper-prompt.md`
7. Guarda il log al mattino in `/var/log/claude-scraper.log`

Per dettagli, leggi la guida completa.

---

## Guida completa passo-passo

### Step 1 — Setup del VPS (10 minuti)

1. Vai su [https://digitalocean.com](https://digitalocean.com), iscriviti (codice promo per nuovi: 200 USD di credito gratuito).
2. Click **Create -> Droplet**.
3. Opzioni:
   - **Image**: Ubuntu 22.04 LTS
   - **Size**: Basic, Regular, 6 USD/mese (1 GB RAM, 25 GB SSD — basta per lo scraper)
   - **Region**: Frankfurt (vicino all'Italia)
   - **Authentication**: SSH key (carica la tua chiave pubblica, vedi [https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/create-with-openssh/](https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/create-with-openssh/))
   - **Hostname**: `claude-scraper-vps`
4. Click **Create Droplet**. Aspetta 1 minuto.
5. Copia l'IP pubblico del droplet (te lo mostra DO).

Apri terminale locale, connettiti via SSH:

```bash
ssh root@TUO_IP_VPS
```

Sei dentro il VPS come root. Adesso applichiamo subito la **Regola 1**: crea un utente dedicato.

```bash
sudo adduser claude
sudo usermod -aG sudo claude          # opzionale, solo per setup iniziale - poi lo togli
su - claude                           # ti logghi come claude
```

Da ora in poi, tutto il setup successivo lo fai come `claude`, non come root.

### Step 2 — Installa Node.js e Claude Code

Come utente `claude`:

```bash
# Installa NVM (Node Version Manager) - modo pulito per gestire Node senza sudo
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20

# Installa Claude Code (CLI)
npm install -g @anthropic-ai/claude-code

# Verifica
claude --version
```

### Step 3 — Configura l'API key

Crea un file delle variabili d'ambiente:

```bash
mkdir -p ~/.claude
nano ~/.claude/env       # ti apre l'editor nano
```

Incolla (sostituisci `sk-ant-...` con la tua chiave da [https://console.anthropic.com](https://console.anthropic.com)):

```
export ANTHROPIC_API_KEY="sk-ant-XXXXXXXXXXXXXXXXXXXXXXXXX"
```

Salva (Ctrl+O, Invio, Ctrl+X).

Aggiungi a `~/.bashrc`:

```bash
echo 'source ~/.claude/env' >> ~/.bashrc
source ~/.bashrc
```

Adesso `claude` ha la chiave per parlare con l'API.

**Importante**: il file `~/.claude/env` contiene la tua API key. Non condividerlo, non committarlo su Git. Vedi `DISCLAIMER.md` di questa cartella per le precauzioni.

### Step 4 — Applica le 5 regole (configurazione settings.json)

Sempre come utente `claude`:

```bash
nano ~/.claude/settings.json
```

Incolla il contenuto del file `claude-settings-produzione.json` di questa cartella. Configura:

- **Hook PreToolUse** per `Bash`: blocca pattern distruttivi (Regola 2)
- **Hook PostToolUse** per ogni tool: scrive log su `/var/log/claude-scraper.log` (Regola 3)
- **Allowed tools** ristretti: solo `Bash, Read, Write, WebFetch` (niente `Edit` se non strettamente necessario)

### Step 5 — Crea il progetto scraper

```bash
mkdir -p ~/scraper
cd ~/scraper

# Copia il file CLAUDE.md della cartella materiali
nano CLAUDE.md
# Incolla qui il contenuto del file `claude-md-produzione.md` dei materiali

# Crea il prompt del task
nano scraper-prompt.md
# Incolla il contenuto del file `scraper-prompt.md` dei materiali
# Personalizza i 3 placeholder: URL competitor 1, 2, 3
```

### Step 6 — Schedula con cron (la Regola 4 prima ti fa fare un dry-run)

Prima di schedulare per davvero, fai un **dry-run manuale** (Regola 4):

```bash
cd ~/scraper
claude --dry-run -f scraper-prompt.md
```

Claude ti mostra cosa farebbe SENZA eseguire azioni distruttive. Leggi l'output. Se ti convince, vai avanti.

Se ti convince, schedula con cron:

```bash
crontab -e
```

Aggiungi questa riga (esegue ogni notte alle 4):

```
0 4 * * * cd /home/claude/scraper && claude --headless -f scraper-prompt.md >> /var/log/claude-scraper.log 2>&1
```

Salva. Il sistema e' attivo. Domani alle 4 la routine partira'.

### Step 7 — Configura alert di budget (Regola 5)

1. Vai su [https://console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing)
2. **Usage Limits** -> imposta un soft limit a 50 USD/mese (o quello che ti senti)
3. **Notifications** -> attiva email alert al 50% e 80% del limit
4. Tieni d'occhio il consumo le prime 2 settimane

Stima realistica per il nostro scraper: 5-15 USD al mese di consumo Claude API. Se sale sopra, vai a vedere i log — probabilmente c'e' un loop o un sito ti blocca e Claude riprova all'infinito.

---

## Cosa fa lo scraper di esempio (caso reale)

Vedi `scraper-prompt.md` per il prompt completo. In sintesi:

1. Visita 3 siti di competitor (URL personalizzabili)
2. Per ogni sito, estrae prezzi dei prodotti chiave usando WebFetch
3. Confronta coi prezzi salvati nel database SQLite locale
4. Se ci sono variazioni > 5%, manda email di notifica
5. Aggiorna il database
6. Scrive log dettagliato

Tempo di esecuzione: 3-5 minuti per scraping di 3 siti con 20 prodotti ciascuno.

---

## Riferimenti

- **Documentazione Claude Code (modalita' headless)**: [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- **DigitalOcean — guida droplet**: [https://docs.digitalocean.com/products/droplets/](https://docs.digitalocean.com/products/droplets/)
- **Cron syntax**: [https://crontab.guru](https://crontab.guru)
- **Anthropic Console (per API key + billing alert)**: [https://console.anthropic.com](https://console.anthropic.com)

---

## Dubbi o problemi?

- Commenta sotto il video YouTube — rispondo a tutti.
- Errore tipico: "ANTHROPIC_API_KEY not found" -> il file `~/.claude/env` non e' stato caricato. Riavvia la sessione SSH o esegui `source ~/.claude/env`.
- Errore tipico: cron non parte -> verifica con `grep CRON /var/log/syslog` che il job sia stato schedulato. Spesso e' un problema di PATH dentro il cron — aggiungi `PATH=/home/claude/.nvm/versions/node/v20.x.x/bin:/usr/bin:/bin` all'inizio del crontab.

Buon esperimento.
