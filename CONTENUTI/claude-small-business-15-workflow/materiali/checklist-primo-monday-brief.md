# Checklist - Preparare il tuo primo `/monday-brief`

Cosa avere pronto nei 5 minuti prima di lanciare il workflow per la prima volta. Una volta che gira bene, le volte successive sono zero setup.

---

## A. Account e connessioni

- [ ] Sei loggato su [claude.ai/cowork](https://claude.ai/cowork) (NON su claude.ai normale)
- [ ] Pacchetto **Small Business** in stato **Active** (sidebar Cowork -> Packages)
- [ ] **Google Workspace** o **Microsoft 365** connesso (sidebar -> Connectors, badge verde)
- [ ] **HubSpot** connesso (opzionale ma consigliato)

---

## B. Dati minimi nei tuoi tool

Perche' `/monday-brief` ti dia un output utile, deve **avere qualcosa da leggere**. Verifica:

### Google Calendar / Outlook

- [ ] Almeno 2-3 meeting in calendario per la settimana corrente
- [ ] I meeting hanno **titoli descrittivi** (non "Riunione" - meglio "Call cliente Bianchi - revisione contratto")
- [ ] Inviti hanno persone reali nei partecipanti (non solo te)

### Gmail / Outlook

- [ ] Almeno 5-10 email non lette degli ultimi 7 giorni (la situazione normale per chi non e' inbox-zero)
- [ ] Almeno un thread di lavoro in corso che andrebbe ripreso

### HubSpot (se connesso)

- [ ] Almeno 3-5 deal attivi nel CRM
- [ ] Almeno 1 deal con campo "scadenza" entro 2 settimane
- [ ] Contatti popolati con nome + email (no record fantasma)

---

## C. Cosa scrivere in chat

Prompt minimo:

```
/monday-brief
```

Prompt completo (consigliato la prima volta):

```
/monday-brief

Contesto:
- Sono un consulente freelance (oppure: titolare PMI / responsabile sales / ecc.)
- Le priorita' che mi interessano questa settimana sono: chiudere il deal X, preparare la proposta per Y, recuperare clienti dormienti
- Tono: professionale ma sintetico, NIENTE preamboli tipo "ecco il tuo briefing"
- Lingua: italiano
- Formato: markdown con 4 sezioni (Priorita', Meeting, Conversazioni pendenti, Numeri settimana scorsa)
```

Piu' contesto dai la prima volta, meglio Claude calibra il formato per le settimane successive.

---

## D. Cosa verificare nell'output

Quando Claude ti consegna il brief, controlla:

- [ ] **Priorita' della settimana** - sono effettivamente prioritarie? O ha listato cose minori? Se troppe banalita': rispondi "concentrati sulle 3 priorita' a piu' alto impatto" e rigenera.
- [ ] **Meeting** - tutti presenti? Note di preparazione sensate per quelli importanti?
- [ ] **Conversazioni pendenti** - sta chiedendo follow-up su persone giuste o sta pescando email automatiche/promozionali?
- [ ] **Numeri** - se hai HubSpot, dovrebbe avere conteggi di deal/contatti aggiornati

Se uno o piu' di questi sono scarsi: il problema NON e' Claude, e' che il tuo CRM/email **non hanno abbastanza segnale**. Le settimane successive migliorano automaticamente quando popoli meglio.

---

## E. Salva il brief

Dopo il primo brief riuscito:

1. Copia il markdown
2. Salvalo in **Google Drive** o **Notion** o **OneDrive** in una cartella `briefing-settimanali/YYYY-MM-DD.md`
3. La settimana dopo, dai il file della scorsa settimana come contesto a Claude: "Ecco il brief della scorsa settimana, riprendi i punti aperti."

In 4 settimane hai un sistema operativo settimanale solido.

---

## F. Schedulalo (opzionale ma raccomandato)

Una volta che il workflow gira bene **manualmente**, schedulalo automatico ogni lunedi' alle 7:30 cosi' lo trovi gia' pronto in casella email alle 8:00:

1. Vai su [https://claude.ai/code/routines](https://claude.ai/code/routines)
2. Crea una nuova Routine:
   - Schedule: ogni lunedi' alle 07:30 (cron `30 6 * * 1` in UTC = 07:30 ora italiana CEST)
   - Prompt: "Esegui /monday-brief con il mio contesto consueto e invia il risultato via email a [TUA-EMAIL]"
3. Salva.

**Risultato finale**: ogni lunedi' alle 7:30 il brief arriva in casella senza che tu apra Claude. Tempo guadagnato a settimana: 30-60 minuti.
