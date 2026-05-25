# MCP Tunnels - I tuoi dati aziendali in Claude senza toccare il firewall

> Materiali del video YouTube **"Il magazzino della mia cantina parla con Claude — e mi ha trovato 4.000 euro fermi al deposito"**.
> Trovi qui tutto quello che ho usato nella build dimostrata nel video + una guida passo-passo per replicarla sul tuo magazzino, sul tuo CRM, sul tuo gestionale.

---

## In 30 secondi — di che si tratta

Colleghi un database aziendale (Supabase, PostgreSQL, MySQL, MongoDB) a Claude tramite un **connettore MCP**. Da quel momento Claude risponde a domande sui tuoi dati come se fosse un analista che ha l'archivio sotto mano: *"Chi sta per finire le scorte? Su quali prodotti sto perdendo soldi? Che capitale ho fermo in magazzino da piu' di sei mesi?"*

E qua sta il punto che cambia tutto: **succede senza che tu esponga il database su Internet**. Il MCP funziona come un citofono — Claude bussa, chiede una cosa specifica, riceve la risposta. Non entra in casa. Non vede gli archivi. Non puo' rovistare.

Il pattern e' utile per:
- **Cantine, e-commerce, distribuzione**: salute del magazzino, bestseller a rischio, capitale immobilizzato
- **Studi commercialisti, consulenti**: scadenze, clienti dormienti, pratiche aperte
- **PMI con gestionale custom**: domande sui tuoi dati senza dover imparare SQL o aspettare il consulente IT

---

## Cosa ti serve prima di iniziare

- [ ] **Account Claude (Pro o Max)** — [https://claude.ai](https://claude.ai) — la versione con i connector e' inclusa qui
- [ ] **Account Supabase** — [https://supabase.com](https://supabase.com) — gratuito (basta il piano free per provare)
- [ ] **VS Code** — [https://code.visualstudio.com](https://code.visualstudio.com) — per aprire i file di questa cartella
- [ ] 15 minuti

Nessun software da installare in locale. Tutto via browser.

---

## Quick start (3 passi per chi gia' sa il giro)

1. Crea un progetto Supabase, esegui `schema-magazzino.sql` e poi `esempio-magazzino.sql` (sono i 30 vini con qualche anomalia nascosta).
2. Su Claude (claude.ai), vai in **Settings -> Connectors** e collega **Supabase**. Da' solo le chiavi di lettura.
3. In una nuova chat scrivi: *"Generami un'analisi salute magazzino. Quali sono le 5 cose da sistemare questa settimana, in ordine di impatto economico?"*. Claude legge il database, trova le anomalie, ti consegna il piano.

Se sei alle prime armi, segui la **guida completa** qui sotto.

---

## Guida completa passo-passo

### Step 1 — Capire cosa stiamo facendo (l'analogia del citofono)

Prima di mettere mano al setup, vale la pena capire perche' questa cosa funziona — bastano 90 secondi.

**MCP** sta per **Model Context Protocol**. Tradotto in italiano normale: e' il linguaggio comune con cui le intelligenze artificiali parlano alle app aziendali. E' come quando il Bluetooth e' diventato standard — di colpo ogni cuffia parlava con ogni telefono, senza che tu installassi software. Oggi sta succedendo la stessa cosa nel mondo AI: tutti i grandi (Anthropic, OpenAI, Microsoft, Google) si sono messi d'accordo sull'MCP, e qualsiasi nuova app aziendale (Supabase, HubSpot, Notion, Google Drive) parla gia' questo linguaggio.

Per te significa una cosa sola: colleghi il **connector** (in pratica un interruttore) e Claude vede il database. Non scrivi codice. Non apri porte sul firewall. Non scrivi configurazioni.

E qui arriva la novita' del **19 maggio 2026**, che si chiama **MCP Tunnel**. Pensata per chi ha database **dentro casa propria** — il server fisico nel tuo ufficio, dietro al firewall. Tunnel apre un canale temporaneo dal tuo server a Claude, dura solo il tempo della conversazione, e poi si chiude. Sicuro per default, niente porte aperte 24/7.

**L'analogia del citofono**: Claude e' il fattorino, l'MCP e' il citofono del palazzo. Il fattorino dal pianerottolo dice cosa serve, tu rispondi dal citofono. Lui non entra in casa. Lui non vede gli armadi. Vede solo cio' che il citofono — l'MCP — decide di mostrare.

---

### Step 2 — Crea il progetto Supabase

Supabase e' un servizio che ti regala un database PostgreSQL gia' configurato in cloud. Lo useremo per simulare il magazzino di una cantina online — nel video lo chiamo "Vini delle Terre", e' un negozio inventato con 30 referenze.

1. Vai su [https://supabase.com](https://supabase.com) e clicca **Start your project**.
2. Login con Google o GitHub. Niente carta di credito.
3. Una volta dentro, click **New project**:
   - **Name**: `cantina-vini-demo` (o quello che vuoi)
   - **Database Password**: clicca **Generate a password** e **annotala** subito in un gestore di password (1Password, Bitwarden, KeePass). Supabase non te la mostra una seconda volta.
   - **Region**: Frankfurt o Ireland — le piu' vicine all'Italia
4. Click **Create new project**. Aspetta 1-2 minuti che Supabase prepari il database.

**Cosa hai ottenuto**: un database PostgreSQL gratuito, protetto da password, nella regione europea piu' vicina a te.

---

### Step 3 — Crea le tabelle e popola il magazzino

Sempre nel pannello Supabase:

1. Sidebar sinistra, clicca **SQL Editor** (icona terminale).
2. Click **+ New query** in alto.
3. Apri `schema-magazzino.sql` di questa cartella con **VS Code** (`code schema-magazzino.sql` dal terminale, oppure aprilo da Esplora risorse).
4. **Copia tutto il contenuto** del file.
5. **Incollalo** nell'editor SQL di Supabase.
6. Click **Run** in basso a destra (oppure `Ctrl+Enter`).
7. Vedi "Success. No rows returned" — le tabelle `prodotti` e `vendite` sono create.

Adesso popola:

8. **+ New query** di nuovo.
9. Apri `esempio-magazzino.sql` con VS Code.
10. Copia tutto, incolla, **Run**.
11. Vedi "Success" — sono stati inseriti 30 prodotti e ~80 record di vendite.

**Verifica**: sidebar Supabase, click **Table Editor** -> seleziona `prodotti`. Devi vedere 30 righe (Barolo, Brunello, Chianti...). Poi `vendite` — circa 80 righe.

> **Importante**: il dataset contiene **5 anomalie nascoste** che simulano problemi reali di una cantina (prodotti sotto costo, esauriti ma ancora ordinabili, capitale fermo in magazzino, ecc.). Claude le scopre nello Step 5. Non correggerle.

---

### Step 4 — Collega Supabase a Claude

1. Vai su [https://claude.ai](https://claude.ai). Loggati col tuo account.
2. In alto a destra, click sull'avatar -> **Settings**.
3. Sidebar -> **Connectors** (oppure direttamente [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)).
4. Cerca **Supabase**. Click **Connect**.
5. Si apre la finestra Supabase: ti chiede di autorizzare Claude a leggere/scrivere sui tuoi progetti.
   - **Regola d'oro**: la prima volta scegli **solo lettura**. Claude potra' vedere i dati ma non modificarli. Stessa logica del nuovo stagista — primo mese guarda e impara, poi gli dai anche i tasti grossi.
6. Seleziona il progetto `cantina-vini-demo`. Conferma.

Da questo momento, in qualsiasi chat di Claude, hai accesso ai dati del magazzino. Senza aver aperto una porta sul firewall, senza aver salvato password sul tuo PC, senza aver fatto nulla di tecnico.

---

### Step 5 — Mettilo alla prova

Apri una **nuova chat** su [https://claude.ai](https://claude.ai). Lancia questi prompt nell'ordine. Il file `prompt-esempio.md` di questa cartella ne contiene molti altri.

**Prompt 1 — esplorazione base**:
> "Che tabelle ho nel database collegato? Spiegami a cosa servono."

Claude risponde descrivendoti `prodotti` e `vendite`. Sa gia' che e' un magazzino.

**Prompt 2 — bestseller dell'ultimo mese**:
> "Quali sono i 5 vini che hanno venduto di piu' negli ultimi 30 giorni? Mostrami quantita', numero di ordini, ricavo."

Claude torna con la classifica. Pronta da mettere in una slide.

**Prompt 3 — il momento che ti fa drizzare le orecchie**:
> "Ho prodotti che stanno per esaurirsi senza che me ne accorga? Considera 'a rischio' quelli dove la giacenza coprira' meno di 21 giorni di vendita."

Claude trova **Chianti, Vermentino, Lambrusco**. Sotto soglia, vendite intense. Se non riordini questa settimana, perdi fatturato.

**Prompt 4 — errori in cassa**:
> "Verifica se ci sono prodotti dove sto vendendo sotto costo. Quanto sto perdendo per bottiglia?"

Claude trova **Barolo** e **Champagne**: prezzo di vendita sotto il costo di acquisto. Errori di tariffazione che non avresti mai visto sfogliando il listino.

**Prompt 5 — capitale fermo**:
> "Quali prodotti sono fermi senza vendite da piu' di 6 mesi? Voglio sapere il capitale immobilizzato totale."

Claude trova 5 vini bloccati da 7+ mesi (Marsala addirittura mai venduto). Capitale fermo: circa 1.200 EUR su 3.500 totali del magazzino.

**Prompt 6 — il piano della settimana**:
> "Generami una dashboard 'salute magazzino'. Le 5 cose piu' importanti da sistemare questa settimana, in ordine di impatto economico, con il valore in euro per ognuna."

Claude mette insieme tutto in un report. Da quel report fai il tuo lunedi' mattina in 5 minuti.

---

### Step 6 — Combinazioni potenti (use case avanzato)

Una volta che la base funziona, puoi usare i dati del magazzino **insieme** ad altri connettori. Esempi:

**Supabase + Gmail (Google Workspace)**:
> "Per ogni prodotto in esaurimento del prompt 3, scrivi una bozza di email al produttore — tono professionale ma cordiale — per ordinare le scorte. Salva ogni email come bozza Gmail. Non inviare."

Risultato: 3 bozze pronte in Gmail. Tu rivedi, eventualmente correggi, clicchi Invia. Recupero scorte in 5 minuti invece di un pomeriggio.

**Supabase + Google Drive**:
> "Esporta l'analisi salute magazzino del prompt 6 come documento Google Doc nella cartella 'Report mensili'. Aggiungi un riassunto da inviare al commercialista."

---

## Concetti spiegati semplici

- **MCP (Model Context Protocol)**: il linguaggio comune con cui le AI parlano alle app aziendali. Come il Bluetooth — una volta che esiste, tutto si parla.
- **Connector**: l'interruttore che colleghi una volta sola per dare a Claude accesso a un servizio. Click, autorizzazione, fine.
- **MCP Tunnel**: variante per database che vivono dentro la tua azienda (non in cloud). Crea un canale temporaneo, niente porte aperte sul firewall.
- **OAuth**: il protocollo standard con cui i servizi web rilasciano "chiavi limitate" senza che tu condivida password.
- **Solo lettura / anche scrittura**: scegli cosa puo' fare Claude. Sempre solo lettura per cominciare.

---

## Cosa fare adesso

- **Strada A — replica uguale**: usa il magazzino-demo, gioca con i prompt del video, abituati al pattern.
- **Strada B — applica al tuo caso**: hai gia' un database aziendale in cloud (Supabase, MongoDB Atlas, PlanetScale)? Collega quello al posto della demo. Stessa procedura, dati veri. **Solo lettura le prime due settimane**.
- **Strada C — database in azienda**: se il tuo gestionale gira su un server fisico in ufficio (non in cloud), guarda **MCP Tunnels**. Stessa logica, configurazione iniziale un po' piu' tecnica (ma 1-2 ore di IT, non un progetto).

---

## Riferimenti

- **Documentazione ufficiale MCP**: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Supabase MCP connector**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp)
- **Annuncio MCP Tunnels (19 maggio 2026)**: cerca "Anthropic MCP Tunnels" su Google
- **Lista connettori ufficiali Claude**: [https://claude.ai/customize/connectors](https://claude.ai/customize/connectors)

---

## Dubbi o problemi?

- Commenta sotto il video YouTube — rispondo a tutti.
- Se Claude non vede Supabase dopo il setup: ricarica la pagina, oppure rifai il **Connect** dallo step 4 (a volte la chiave scade dopo qualche giorno di inattivita').

Buon lavoro.
