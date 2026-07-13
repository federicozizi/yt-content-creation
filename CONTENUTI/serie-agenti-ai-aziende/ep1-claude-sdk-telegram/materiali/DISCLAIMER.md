# ⚠️ Disclaimer sicurezza — leggi prima di tutto

Questo progetto usa **credenziali segrete** nel file `.env`:
- `ANTHROPIC_API_KEY` — la chiave che sblocca Claude (e che ti viene addebitata in base all'uso).
- `TELEGRAM_BOT_TOKEN` — il token che controlla il tuo bot Telegram.

## Regole d'oro

1. **Mai mettere le chiavi vere a video** in un eventuale video/registrazione. Nei materiali condividi solo
   `.env.example` con valori finti.
2. **Mai committare il file `.env`** su GitHub o altri repository. Nei materiali è **già incluso** un file
   `.gitignore` che esclude `.env` e `richieste.log` (quest'ultimo può contenere dati dei dipendenti): prima
   di `git init` verifica solo che ci sia (è un file nascosto, attiva la visualizzazione dei file nascosti).
3. **Se per sbaglio una chiave finisce online** (anche solo per un minuto): considerala compromessa.
   - **Chiave Anthropic** → vai su console.anthropic.com e **revocala/rigenerala** subito.
   - **Token Telegram** → su @BotFather usa `/revoke` per generarne uno nuovo.
   - Cancellarla solo dalla storia di git **non basta**: i bot scansionano i repository in pochi secondi.

## Dati dei dipendenti

Il file `richieste.log` contiene nomi e richieste delle persone. Trattalo come un dato sensibile: non
condividerlo pubblicamente e conservalo secondo le regole privacy della tua azienda (GDPR).

## .gitignore (già fornito)

Nei materiali trovi già un file `.gitignore` con dentro:

```
.env
richieste.log
__pycache__/
```

Se parti da una cartella tua (non da questi materiali), crealo con lo stesso contenuto prima di `git init`.
