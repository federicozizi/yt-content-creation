# Mettere Headroom "in sottofondo" a Claude Code

Finora abbiamo chiamato Headroom dentro il codice. Ma c'è un modo molto più
comodo: lasciarlo girare **in sottofondo** come un casello tra Claude Code e i
server di Claude. Tu usi Claude Code **esattamente come sempre** — stessi
comandi, stessa schermata — e Headroom, senza che tu faccia niente, schiaccia i
contenuti pesanti prima che partano. Il conto scende da solo.

> **L'analogia:** è come un addetto che, all'imbarco, comprime sottovuoto i tuoi
> bagagli mentre passi. Tu non te ne accorgi; paghi meno di stiva.

---

## Come funziona, in un disegno

```
   Claude Code  (lo usi normalmente)
        │
        ▼
   Headroom proxy   ← gira in sottofondo sul tuo PC (porta 8787)
        │              comprime gli output pesanti, al volo
        ▼
   Server di Claude (Anthropic)
```

Headroom si mette **in mezzo**. Non cambia cosa fa Claude: cambia solo *quanto
testo* gli arriva. Meno testo = meno token = meno spesa, a parità di risultato.

---

## Setup — il modo facile (un comando)

### 1. Installa Headroom con il proxy
Apri **PowerShell** e lancia:
```powershell
pip install "headroom-ai[proxy]"
```

### 2. Avvia Claude Code "avvolto" da Headroom
Invece di scrivere `claude`, scrivi:
```powershell
headroom wrap claude
```
Questo comando fa **due cose insieme**: accende il proxy in sottofondo e lancia
Claude Code già collegato. Da qui in poi usi Claude Code come sempre — la
compressione avviene da sola.

Per smettere: chiudi Claude Code normalmente. Il proxy si spegne con lui.

> **"headroom : termine non riconosciuto"?** È normalissimo: Windows ha
> installato il comando ma non sa ancora dov'è. Due rimedi:
>
> - **Al volo** (vale per la finestra aperta): chiamalo come modulo Python —
>   funziona sempre:
>   ```powershell
>   python -m headroom.cli wrap claude
>   ```
> - **Per sempre** (una volta sola, poi chiudi e riapri PowerShell):
>   ```powershell
>   [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path","User") + ";$env:APPDATA\Python\Python313\Scripts", "User")
>   ```
>   Da qui in poi `headroom` viene riconosciuto come un comando normale.
>   (Il numero `Python313` dipende dalla tua versione di Python: se è diversa,
>   correggilo.)

---

## Setup — il modo manuale (proxy sempre acceso)

Utile se vuoi tenere il proxy acceso in modo stabile e collegarci anche altri
strumenti, non solo Claude Code.

### 1. Apri un terminale "dedicato" al proxy e avvialo
```powershell
headroom proxy
```
Lascialo aperto: questo terminale è il motore in sottofondo. Quando è pronto
vedi `Running on http://127.0.0.1:8787`.

### 2. In un ALTRO terminale, di' a Claude Code di passare dal proxy
```powershell
$env:ANTHROPIC_BASE_URL = "http://127.0.0.1:8787"
claude
```
Fatto: questo Claude Code ora passa da Headroom. Quando chiudi il terminale,
la variabile sparisce e Claude Code torna a collegarsi normalmente.

> Per renderlo **permanente** (vale per tutti i terminali nuovi):
> ```powershell
> setx ANTHROPIC_BASE_URL "http://127.0.0.1:8787"
> ```
> Da disfare con `setx ANTHROPIC_BASE_URL ""` quando non lo vuoi più.

---

## Come verifichi che sta davvero lavorando

Con il proxy acceso, in un terminale qualsiasi:

```powershell
# È vivo e in salute?
curl http://localhost:8787/health

# Quanti token ha risparmiato finora?
curl http://localhost:8787/stats
```

In `stats` vedi crescere `tokens_saved` e `savings_percent` man mano che usi
Claude Code. È lì la prova in euro del lavoro fatto in sottofondo.

---

## Una cosa importante da dire (onestà)

Headroom **non comprime quello che scrivi tu** a Claude: comprime quello che
Claude **legge per lavorare** — file aperti, log, risultati di ricerca, risposte
di API, output dei comandi. Ed è giusto così, perché è *lì* che si accumulano i
token: quando Claude Code legge un file da 2.000 righe o l'output di un comando
lunghissimo, quello pesa molto più della tua domanda.

In pratica:
- ✅ Comprime tantissimo: log, dati, JSON, file letti, output di strumenti
- 🔒 Lascia intatto il **codice** (per non rischiare di romperti la logica)
- 🔒 Non tocca i **tuoi messaggi** (sono corti e sono "il punto")

Risultato: spendi meno proprio dove si spreca di più, senza che la qualità delle
risposte cambi.

---

## Spegnere tutto e tornare come prima

- Modo facile (`wrap`): chiudi Claude Code.
- Modo manuale: chiudi il terminale del proxy (o `Ctrl+C`), e se avevi usato
  `setx`, azzera la variabile con `setx ANTHROPIC_BASE_URL ""` e riapri i
  terminali.

Da quel momento Claude Code torna a collegarsi diretto, come sempre.
