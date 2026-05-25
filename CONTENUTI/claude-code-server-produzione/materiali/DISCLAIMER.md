# Disclaimer - Sicurezza VPS, API key, dati di produzione

Mettere Claude Code in produzione su un server vero significa avere a che fare con **credenziali sensibili** (API key Anthropic, SSH key, eventuali password di database) e con **azioni che girano in autonomia 24/7**. Le regole qui sotto sono quelle che ho imparato sulla mia pelle nei primi 30 giorni del progetto.

## Punto critico 1 — La API key Anthropic

Nel file `~/.claude/env` sul VPS c'e' la tua API key. Se compromessa, qualcuno puo' consumare quota dal tuo account fino al limit budget che hai impostato.

### Mitigazioni obbligatorie
1. **Crea una API key dedicata per il VPS** — separata dalla tua personale per sviluppo. Cosi' se devi revocarla, non rompi niente altro.
2. **Imposta un budget mensile soft + hard limit** nella Anthropic Console. Soft limit (es. 50 USD): ti manda email. Hard limit (es. 200 USD): la key smette di funzionare. Anche col peggior bug possibile, il danno e' contenuto.
3. **Notifications attive**: email al 50% e all'80% del soft limit.
4. **NON committare mai `~/.claude/env` su Git**. Anche se il repo e' privato. Anche se sei sicuro. Mai.
5. **Rotazione periodica**: ogni 3-6 mesi, genera una nuova API key, aggiorna il VPS, revoca la vecchia. Disciplina semplice, ti protegge da leak dimenticati nel tempo.

### Se la API key trapela
1. Vai su [https://console.anthropic.com](https://console.anthropic.com) -> API Keys
2. Click **Revoke** sulla key compromessa (immediato)
3. Crea una nuova key
4. Aggiornala nel VPS: `nano ~/.claude/env`, sostituisci la stringa, salva
5. Audita la fatturazione delle ultime 24h per spese anomale

## Punto critico 2 — Sicurezza del VPS stesso

Il VPS e' una macchina connessa a Internet. Va protetta da intrusioni.

### Checklist minima di sicurezza VPS
- [ ] **SSH solo con chiave** (no password). Configura in `/etc/ssh/sshd_config`: `PasswordAuthentication no`
- [ ] **Disabilita login root via SSH**. Stessa configurazione: `PermitRootLogin no`
- [ ] **Firewall attivo**: `sudo ufw allow OpenSSH && sudo ufw enable`. Apri SOLO la porta 22 (SSH). Niente HTTP/HTTPS a meno che tu non serva qualcosa di pubblico.
- [ ] **Aggiornamenti automatici**: `sudo apt install unattended-upgrades`
- [ ] **Fail2ban** per bloccare tentativi di brute-force: `sudo apt install fail2ban`
- [ ] **Audit periodico dei log**: `last`, `who`, `journalctl -u sshd`. Se vedi login da IP sconosciuti, allarme rosso.

### NON salvare nulla di personalmente identificabile sul VPS
Il VPS dovrebbe contenere SOLO:
- Codice del task
- Database con dati di lavoro (prezzi competitor, log scraping, ecc.)
- File di stato

NON dovrebbe contenere:
- Liste clienti con nome/email/telefono
- Email private
- Documenti contrattuali
- Foto, file personali

Se hai bisogno di dati personali per il task, valuta GDPR e usa minimizzazione (es. solo l'email del cliente, niente di piu').

## Punto critico 3 — Claude in autonomia 24/7

Anche con le 5 regole del CLAUDE.md applicate, Claude resta un sistema che esegue codice. Alcuni rischi residui:

### Rischio loop infinito
Se il prompt e' mal scritto e Claude entra in loop ("riprova lo scraping, riprova ancora, riprova ancora..."), brucia token velocemente.

**Mitigazione**: budget hard limit nella Anthropic Console + monitoring dei log al mattino. La Regola 5 e' il guardrail di ultima istanza.

### Rischio comando sbagliato non previsto
Hai bloccato `rm`, `sudo`, etc. Ma magari c'e' un comando che non avevi previsto come pericoloso (es. `chgrp`, `setfacl`, `dpkg`). Se Claude lo prova, l'hook PreToolUse non lo blocca.

**Mitigazione**: l'utente `claude` ha permessi minimi a livello OS. Anche se Claude eseguisse un comando inaspettato, il sistema operativo dovrebbe rifiutarlo. Ridondanza al di sopra dell'hook.

### Rischio "data poisoning" dei competitor
Un competitor che capisce di essere scrappato potrebbe mostrare prezzi falsi al tuo IP. Lo scraping diventa inaffidabile.

**Mitigazione**: ruota IP usando un servizio di proxy (es. ScrapingBee, Bright Data), o usa solo competitor di cui hai accesso autorizzato ai dati.

## Punto critico 4 — Conformita' legale dello scraping

Lo scraping di siti web e' una zona grigia legale. Prima di partire:

1. **Leggi i Terms of Service del competitor**: se vietano scraping esplicitamente, lo stai facendo a tuo rischio
2. **Rispetta `robots.txt`** del sito (anche se non e' legalmente vincolante, e' buona pratica)
3. **Frequenza moderata**: non fare scraping ogni 5 minuti. Una volta al giorno alle 4 del mattino e' il giusto compromesso
4. **Identificati come bot**: usa uno User-Agent che dice "il mio scraper, contact info@..." invece di mascherarti da browser. Trasparenza riduce rischi
5. **Solo dati pubblici**: scarica solo ci0' che vedrebbe un visitatore normale. Mai login fittizi per accedere a sezioni private

Se hai dubbi legali specifici per il tuo settore, consulta un avvocato esperto in diritto digitale prima di metterlo in produzione.

## In caso di emergenza

Se sospetti compromissione del VPS, della API key, o del sistema:

1. **Revoca subito la API key Anthropic** ([https://console.anthropic.com](https://console.anthropic.com)) -> taglia l'accesso istante
2. **Disabilita cron** sul VPS: `crontab -r` (rimuove tutti i cron job)
3. **Audita i log**: `cat /var/log/claude-scraper.log`, `last`, `journalctl -u sshd`
4. **Rigenera SSH key** se sospetti compromissione del VPS
5. **Considera ricostruzione del VPS da zero** se i log mostrano accessi non autorizzati

Costo della ricostruzione: 1 ora di setup, 6 USD del nuovo droplet. Costo di non farla in caso di compromissione: incalcolabile.

---

Le regole sopra sembrano paranoiche. Lo sono. Dopo un mese di Claude Code in produzione, ti garantisco che non te ne pentirai.
