# I 15 workflow di Claude for Small Business

Riferimento veloce. Per ogni workflow: cosa fa, quali connettori servono, in quale scenario lo userai.

---

## A. Operativo settimanale

### 1. `/monday-brief`
**Cosa fa**: il tuo briefing del lunedi'. Sintetizza email non lette, meeting in calendario, lead nuovi su HubSpot, deal in scadenza. Output: 1 pagina con priorita' della settimana.
**Connettori**: Google Workspace o Microsoft 365 + HubSpot (consigliati)
**Quando usarlo**: ogni lunedi' alle 8:00. Risparmio: 30-60 minuti di "che faccio oggi?"

### 2. `/weekly-report`
**Cosa fa**: report dei numeri della settimana per te o per il tuo team. Vendite (HubSpot/QuickBooks), spese (PayPal/QuickBooks), produttivita' (calendar), eventuali alert.
**Connettori**: almeno 2 tra HubSpot, QuickBooks, PayPal, Google Workspace
**Quando usarlo**: ogni venerdi' pomeriggio per chiudere la settimana.

### 3. `/meeting-followup`
**Cosa fa**: dopo un meeting, prendi le tue note (testuali o trascrizione audio) e Claude genera: sommario, action items con responsabili, email di follow-up alle persone presenti.
**Connettori**: Google Workspace o Microsoft 365 (per email + drive)
**Quando usarlo**: subito dopo ogni meeting cliente importante.

---

## B. Vendite e clienti

### 4. `/lead-qualifier`
**Cosa fa**: dato un nuovo lead (form da sito, biglietto da visita scansionato, contatto LinkedIn), Claude lo arricchisce con info pubbliche (sito web aziendale, settore, dimensione team) e propone un punteggio MQL/SQL.
**Connettori**: HubSpot
**Quando usarlo**: ogni volta che arrivano lead da fonti diverse e devi prioritizzare.

### 5. `/run-campaign`
**Cosa fa**: prepara una mini-campagna marketing end-to-end. Definisci target + obiettivo, Claude produce: email sequence (3-5 email), versioni social per LinkedIn/Instagram, asset Canva (immagini placeholder).
**Connettori**: HubSpot + Canva + Google Workspace
**Quando usarlo**: per campagne stagionali, lanci prodotto, follow-up evento.

### 6. `/pitch-builder`
**Cosa fa**: dati pochi input (cliente target, settore, problema da risolvere), Claude costruisce una pitch deck base di 7-10 slide in Canva o un'email commerciale dettagliata.
**Connettori**: Canva + Google Workspace
**Quando usarlo**: prima di una prima call commerciale importante.

### 7. `/support-triage`
**Cosa fa**: prende le richieste customer support (da email, form, ticketing) e le classifica: urgente / da rispondere oggi / da rispondere in settimana / FAQ standard. Per le FAQ propone risposta pronta.
**Connettori**: Google Workspace o Microsoft 365 (per accesso a email/ticket)
**Quando usarlo**: ogni mattina prima di aprire la casella support.

---

## C. Amministrazione e finanze

### 8. `/close-month`
**Cosa fa**: prepara la chiusura contabile mensile. Riconcilia movimenti PayPal, fatture QuickBooks, spese categorizzate. Identifica anomalie (es. spese duplicate, fatture senza pagamento).
**Connettori**: QuickBooks + PayPal (entrambi consigliati)
**Quando usarlo**: ultimo giorno del mese o primo del mese successivo.

### 9. `/invoice-chaser`
**Cosa fa**: trova fatture scadute, classifica per anzianita', genera bozze di email di sollecito con tono crescente.
**Connettori**: HubSpot o QuickBooks + Google Workspace o Microsoft 365
**Quando usarlo**: settimanalmente. Recupero crediti diventa "click un workflow" invece di "perdita di 4 ore".

### 10. `/expense-categorizer`
**Cosa fa**: prende l'export delle transazioni (PayPal, banca, carta di credito) e le categorizza per voce di spesa (ufficio, marketing, viaggi, ecc.). Output: foglio pronto da inviare al commercialista.
**Connettori**: PayPal o QuickBooks
**Quando usarlo**: una volta al mese per il commercialista.

### 11. `/plan-payroll`
**Cosa fa**: prepara il riepilogo paghe mensile. Calcola ore extra (dai calendari), permessi (HR), variabili sui dipendenti. Output: prospetto sintetico per il commercialista del lavoro.
**Connettori**: Google Workspace o Microsoft 365 (calendari)
**Quando usarlo**: ogni 25 del mese (prima della chiusura paghe).

---

## D. Legale e fornitori

### 12. `/contract-review`
**Cosa fa**: analisi pre-firma di un contratto PDF. 12 punti di controllo standard (durata, rescissione, esclusivita', IP, ecc.) con flag verde/giallo/rosso.
**Connettori**: DocuSign (opzionale, per integrare il workflow pre-signing)
**Quando usarlo**: SEMPRE prima di firmare qualsiasi contratto > 5.000 EUR di valore.

### 13. `/vendor-vet`
**Cosa fa**: due diligence light su un fornitore. Cerca info pubbliche (sito, recensioni, bilanci se SpA), eventuali red flag legali o reputazionali. Output: scheda fornitore in 2 pagine.
**Connettori**: nessuno richiesto (usa WebSearch interno)
**Quando usarlo**: prima di firmare un primo contratto con un fornitore nuovo.

---

## E. Marketing e contenuti

### 14. `/social-pulse`
**Cosa fa**: analizza menzioni e feedback sui tuoi canali social (post tuoi + commenti). Classifica per sentiment, identifica temi caldi, segnala lamentele che richiedono risposta tempestiva.
**Connettori**: nessuno richiesto, ma puoi puntarlo a profili specifici
**Quando usarlo**: settimanalmente per restare con il polso sulla percezione del brand.

### 15. `/pricing-check`
**Cosa fa**: monitora i prezzi dei tuoi competitor principali. Sito web competitor in input -> tabella comparativa prezzi/feature -> alert su variazioni significative.
**Connettori**: nessuno richiesto (usa WebSearch + WebFetch)
**Quando usarlo**: una volta al mese o quando senti che il mercato si muove.

---

## Combinazioni potenti

- **`/monday-brief` + Routine ricorrente**: schedula via Claude Routines il lunedi' alle 8:00, ricevi il brief via email senza neanche aprire Claude.
- **`/lead-qualifier` + `/pitch-builder` in sequenza**: nuovo lead arriva, Claude lo qualifica e (se score alto) gia' ti prepara il pitch personalizzato.
- **`/contract-review` + DocuSign**: Claude analizza prima della firma, DocuSign gestisce la firma. Workflow end-to-end senza saltare lo step critico di review.

---

## Personalizzazione avanzata

Quasi tutti i workflow accettano modificatori in linguaggio naturale dopo il comando. Esempi:

```
/monday-brief solo focus su vendite
/contract-review settore consulenza IT, attenzione clausole IP
/invoice-chaser tono in italiano formale lei
/run-campaign target PMI nord Italia, budget basso
```

Sperimenta. Se il modificatore non e' chiaro, Claude ti chiede precisazioni prima di partire.

---

## Limiti onesti

- **Nessun workflow sostituisce il professionista**: `/contract-review` non e' un avvocato, `/close-month` non e' un commercialista, `/plan-payroll` non e' un consulente del lavoro. Sono **acceleratori** per ridurre il tempo del 70-80%, non sostituti del giudizio esperto sul restante 20-30%.
- **La qualita' dipende dai connector**: se HubSpot e' vuoto, `/monday-brief` produce poco. Piu' dati buoni hai, piu' i workflow ti danno valore.
- **Approvazione umana sempre obbligatoria** per azioni che toccano l'esterno (email inviate, contratti firmati, pagamenti). Claude prepara, tu confermi.
