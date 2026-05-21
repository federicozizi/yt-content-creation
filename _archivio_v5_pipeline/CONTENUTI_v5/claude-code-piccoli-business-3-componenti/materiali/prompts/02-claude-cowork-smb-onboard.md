<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/prompts/02-claude-cowork-smb-onboard.md -->

# Prompt 02 — Attivazione del pacchetto Claude for Small Business

Questo step si svolge **nel browser, dentro Claude Cowork**. Non è una cosa che Claude Code può fare per te: il pacchetto Small Business è un plugin di Cowork, non di Code.

Però Claude Code può **prepararti la strada** e poi **leggere/scrivere lo stesso Supabase** che il pacchetto userà — vedi `prompts/04-integrazione-end-to-end.md` per come i due si parlano.

## Cosa fare nel browser (senza Claude Code)

### 1. Verifica il piano

- Login a `claude.com/cowork`.
- Se non vedi la voce "Cowork" nella navigazione laterale, hai il piano Pro singolo. Devi passare al piano **Team** (~25€/utente/mese). Vai in Settings → Plan → Upgrade.
- Se vedi Cowork: ok, prosegui.

### 2. Lancia l'onboarding del pacchetto

Apri una nuova chat di Cowork e digita:

```
/smb-onboard
```

Parte una procedura guidata (Anthropic la chiama "Small Business setup"). Risponde a queste domande:

- **Settore del business**: scegli quello più vicino (commercialisti / studio legale / e-commerce / agenzia / artigiano / altro).
- **Strumenti che già usi**: ti propone una lista. Spunta solo quelli che usi davvero (es. QuickBooks per la contabilità, Google Workspace per email e Drive). Non spuntare tutto.
- **Permessi**: per ogni tool spuntato, parte un OAuth flow standard nel browser. Dai il consenso. Anthropic ha pre-registrato l'app, quindi NON serve console Google Cloud, NON serve credentials.json a mano.

### 3. Verifica i workflow disponibili

Al termine dell'onboarding vedrai in sidebar una nuova sezione "Small Business" con i 15 workflow attivati. Prova:

```
/monday-brief
```

Output atteso: un riassunto che cita la cassa attuale (da QuickBooks se collegato) e i lead nuovi (da HubSpot se collegato). Se cita "data non disponibile" per qualche fonte, significa che quel tool non è collegato — tornaci sopra solo se ti serve.

## Cosa fare dopo (di nuovo in Claude Code)

Quando hai completato l'onboarding nel browser:

```bash
cd materiali
claude
```

E incolla:

```
Il pacchetto Claude for Small Business è stato attivato in Cowork.
Aggiorna ./README.md indicando questo stato (aggiungi una sezione "Stato setup"
con tre voci: Supabase MCP ✓ | Claude for Small Business ✓ | Agent View ⏳).
Poi vai al prompt 03 per i sub-agent custom.
```

## Cose da NON fare

- Non collegare TUTTI i tool della lista. Parti da 2-3 davvero usati. Aggiungi gli altri solo quando ne hai bisogno.
- Non testare i workflow che fanno azioni esterne (es. `/invoice-chaser` o `/run-campaign`) in produzione la prima volta. Usa una sandbox QuickBooks / HubSpot se possibile per le prime prove, oppure fermati prima dell'approvazione finale così niente viene inviato davvero.
- Non condividere lo schermo di Cowork loggato in pubblico: la sidebar mostra dati aziendali reali una volta collegati i tool.

## Riferimenti

- Annuncio ufficiale: https://www.anthropic.com/news/claude-for-small-business
- Pagina plugin: https://claude.com/plugins/small-business
- How-to dettagliato: `docs/claude-for-small-business-howto.md` in questa cartella
