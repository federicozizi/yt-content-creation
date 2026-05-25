# Disclaimer - Connettori OAuth e dati aziendali

In questa cartella **non ci sono credenziali**. Le guide si limitano a indicarti la procedura. Tuttavia, **attivare Claude for Small Business significa collegare a Claude i tuoi tool aziendali** (HubSpot, Google Workspace, QuickBooks, ecc.) e questo merita attenzione.

## Regole d'oro

### 1. Scope sempre minimo possibile
Quando colleghi un connector tramite OAuth, ti viene chiesto di scegliere lo **scope** (cosa Claude puo' fare sul servizio):

- **Read-only**: Claude legge i dati ma NON puo' modificare, creare, cancellare. **Sempre questo per la prima settimana**.
- **Read-write**: Claude puo' anche modificare. Attiva SOLO dopo che hai verificato il comportamento read-only per almeno qualche giorno.
- **Admin / full access**: praticamente mai - lo richiedono solo workflow molto specifici (es. setup automatici). Se il workflow te lo chiede, verifica DUE volte di sapere cosa stai facendo.

Eccezione: `/invoice-chaser` ha bisogno di scope write su Gmail/Outlook per **salvare bozze**. Anche in quel caso le email **non vengono inviate** - solo bozze. Le invii tu manualmente dopo revisione.

### 2. Dati personali sensibili - check GDPR
Claude **non addestra modelli sui tuoi dati business** quando usi Cowork col tuo abbonamento Pro/Max (clausola contrattuale Anthropic). Pero':

- I dati passano comunque attraverso i server Anthropic per essere processati
- Se hai dati di clienti minori, dati sanitari, dati finanziari sensibili (es. transazioni bancarie con saldi), valuta col tuo DPO o legale prima di collegare connector che li espongono
- Per dati standard B2B (nomi aziende, email business, fatturati aggregati, scadenze contratti) generalmente non ci sono problemi

### 3. Revoca dei token quando necessario

Scenari in cui devi disconnettere immediatamente un connector:

- **Smetti di usare un servizio** (es. cambi CRM da HubSpot a Pipedrive) -> disconnetti HubSpot
- **Vendi/chiudi attivita'** -> disconnetti tutti i connector
- **Cambia ruolo aziendale** (es. da admin a contributor) -> rinegozia gli scope
- **Notifica di breach** dal servizio fornitore -> disconnetti per precauzione + rinnova credenziali sul servizio

Procedura: [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors) -> trova il connector -> click **Disconnect** -> conferma. I token vengono invalidati immediatamente.

### 4. Bozze prima di invii reali

I workflow Small Business che producono comunicazioni (`/invoice-chaser`, `/meeting-followup`, `/run-campaign`) **salvano sempre come bozze**, mai inviano direttamente. Questo per design - non e' una limitazione, e' una scelta di sicurezza.

**NON cercare di forzare l'invio automatico** per i primi 1-2 mesi: rivedi tutte le bozze, controlla che il tono sia adatto al tuo brand, modifica dove serve. Dopo che il tuo benchmark di affidabilita' e' solido, puoi valutare di automatizzare via Routines, ma **mai per email a clienti chiave**.

### 5. Account team vs account personale

Se gestisci team con piu' membri:

- **Crea connettori a livello workspace**, non al tuo account personale. Cosi' se domani tu sei in ferie, il workflow funziona comunque.
- **Mai condividere le credenziali del tuo account Claude Pro/Max** con il team - ognuno deve avere il proprio. Anthropic permette di acquistare seat aggiuntivi a costo ridotto.
- **Audit periodico** (ogni 3 mesi): verifica chi ha quale scope su quale connector. Toglie quelli che non servono piu'.

### 6. Backup prima di workflow "potenti"

Per i workflow che possono modificare dati (`/close-month`, `/expense-categorizer` con scope write):

- **Backup attivo** del servizio coinvolto prima del primo run
- **Test su un periodo storico** (es. "categorizza le spese di marzo" - se le incasina, sai cosa rifare)
- **Mai prima volta su dati di chiusura mese in corso** - prova prima su dati gia' chiusi

---

## In caso di emergenza

Se sospetti che un connector abbia comportamenti strani o dati siano stati modificati in modo inatteso:

1. **Disconnetti subito** il connector da [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)
2. **Audita le ultime 24h** sul servizio collegato (HubSpot ha activity log, Google Workspace ha audit log, ecc.)
3. **Se trovi modifiche non volute**: rollback dai backup
4. **Segnala ad Anthropic** via [https://support.anthropic.com](https://support.anthropic.com) - sono molto reattivi su questi report

---

I 15 workflow Small Business sono progettati per essere sicuri di default. Le regole sopra sono per restare sicuri anche quando vai oltre il default.
