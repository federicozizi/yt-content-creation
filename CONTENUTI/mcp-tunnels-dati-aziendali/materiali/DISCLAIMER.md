# Disclaimer - Credenziali e sicurezza

In questa cartella **non ci sono credenziali vere**. Gli script SQL (`schema-clienti.sql`, `esempio-clienti.sql`) inseriscono **dati clienti completamente inventati** - non c'e' alcuna corrispondenza con aziende reali. Le partite IVA, le email e i telefoni sono finti.

Tuttavia, la build del video coinvolge **diverse credenziali sensibili** che tu produrrai durante il setup:

1. **Password del database Supabase** (generata automaticamente in step 2 della guida)
2. **Token OAuth** che Claude usa per accedere a Supabase (gestito dietro le quinte da claude.ai)
3. Eventualmente **API key Anthropic** se decidi di automatizzare anche tu via API

## Regole d'oro

### 1. Password Supabase
- Quando generi la password del database, **annotala subito** in un gestore di password (1Password, Bitwarden, KeePass). Supabase **non la mostra una seconda volta** completa.
- Se la perdi, dovrai resettare la password dal pannello Supabase (Settings -> Database -> Reset database password).
- **Non scriverla mai in file di codice o file `.env` committati su Git.**

### 2. Token OAuth Claude <-> Supabase
- Sono gestiti automaticamente da [claude.ai](https://claude.ai). **Non li vedi mai, non devi copiarli, non devi salvarli.** Bene cosi'.
- Per **revocarli** (es. se vendi/chiudi il progetto Supabase): vai su Supabase -> Settings -> API -> revoca i token attivi. Su Claude -> Settings -> Connectors -> disconnetti Supabase.

### 3. Database con dati veri (non demo)
Se al posto del database demo colleghi un **database aziendale vero**:

- **Inizia sempre con scope read-only.** Solo dopo aver verificato che il comportamento di Claude e' affidabile sui tuoi dati, valuta lo scope read-write.
- **Mai dati personali sensibili senza GDPR check.** Dati medici, dati di minori, dati finanziari sensibili = serve valutazione DPO prima di collegare.
- **Backup attivo prima del primo collegamento read-write.** Anche se Claude e' affidabile, una query sbagliata su un database produttivo senza backup e' rovinosa.

### 4. Se hai pubblicato per errore credenziali su Git/GitHub

**Cancellare i file dal repository NON basta.** I bot scansionano GitHub in tempo reale.

- **Vai sul servizio che ha emesso la credenziale** (Supabase, Anthropic Console, GitHub, ecc.)
- **Revoca la credenziale compromessa**
- **Genera una credenziale nuova**
- **Aggiorna i sistemi che la usavano**

Tempo che ti serve: 2 minuti. Tempo che ci mette un bot a sfruttare la vecchia: secondi.

### 5. `.gitignore` obbligatorio

Se hai messo questi materiali in un repository Git, controlla che il `.gitignore` contenga almeno:

```
.env
.env.local
.env.*.local
*.key
*.pem
secrets/
credentials/
```

Crealo **prima** del primo `git add`.
