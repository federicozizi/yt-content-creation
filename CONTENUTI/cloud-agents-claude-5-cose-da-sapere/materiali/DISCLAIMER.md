# Disclaimer - Sicurezza Cloud Agents e PAT GitHub

Le Routines/Cloud Agents girano nel cloud Anthropic in un sandbox isolato. Anche se il loro design e' relativamente sicuro per default, ci sono **due punti critici** da gestire bene per non avere brutte sorprese.

## Punto critico 1 — Il Personal Access Token GitHub (PAT)

Per pushare i risultati delle routine sul tuo repository GitHub, il sandbox usa un PAT che metti **in chiaro nel prompt della routine**.

### Cosa significa "in chiaro"
- Il PAT e' visibile a chiunque abbia accesso al tuo account claude.ai
- Se invii il prompt della routine a qualcuno (chat, screenshot, supporto Anthropic), il PAT e' li' dentro
- I log delle esecuzioni della routine NON includono il PAT, ma il prompt s'

### Mitigazioni obbligatorie
1. **Crea un PAT dedicato per le routine** — separato da quello che usi per altri scopi. Cosi' se devi revocarlo, non rompi nient'altro.
2. **Scope minimo** — solo `repo` (lettura+scrittura repository). NON dare scope su organizzazioni, billing, admin.
3. **Repository dedicato** — il PAT puo' accedere SOLO ai repo che gli permetti. Crea un repository specifico per i risultati delle routine, e da' al PAT accesso solo a quello.
4. **Scadenza breve la prima volta** — 30-90 giorni. Se la routine va bene per quel periodo, rinnova con scadenza piu' lunga.
5. **Revoca immediata se sospetti compromissione** — vai su [https://github.com/settings/tokens](https://github.com/settings/tokens) e click **Delete** accanto al token.

### Se il PAT trapela per errore
1. Vai su GitHub -> Settings -> Developer settings -> Personal access tokens
2. **Delete** del token compromesso (immediato, 5 secondi)
3. Genera un nuovo PAT
4. Aggiorna tutte le routine che lo usavano (entra in claude.ai/code/routines -> Edit -> sostituisci la stringa nel prompt)
5. Audita il repo GitHub per modifiche non autorizzate nelle ultime ore

## Punto critico 2 — Cosa puo' fare il sandbox in autonomia

Il sandbox esegue il prompt che gli dai. Se nel prompt scrivi "manda email a Mario", lui prova a farlo (se ha gli strumenti per).

### Regole d'oro per scrivere prompt sicuri

1. **Mai azioni distruttive in autonomia**: non dire al sandbox "cancella file X" o "elimina record Y dal database". Se serve una cancellazione, fagliela SCRIVERE in un file da revisionare; tu la confermi a mano.

2. **Mai invii definitivi**: email, pagamenti, post sui social — sempre come **bozze** o **draft**. Mai con "send" effettivo.

3. **Limita gli allowed_tools al minimo necessario**: se la routine fa solo WebSearch + Write, non darle accesso a Edit o Bash che potrebbero fare azioni inaspettate.

4. **Restrict access ai repository sensibili**: il PAT con scope `repo` ha accesso a TUTTI i tuoi repo. Se vuoi limitare, considera i **fine-grained PAT** ([https://github.com/settings/personal-access-tokens/new](https://github.com/settings/personal-access-tokens/new)) che permettono di scegliere repo specifici.

5. **Test prima in run-now**: prima di lasciare una routine schedulata in libera uscita, fai **Run now** dalla UI e leggi cosa fa. Se ti convince, lascia il cron attivo. Se vedi comportamenti strani, disabilita prima di rilanciare.

## Punto critico 3 — Il consumo di quota

I Cloud Agents consumano usage del tuo piano Claude. Una routine che gira due volte al giorno per un mese puo' consumare **20-40% del tuo piano Pro mensile**.

### Mitigazioni
- **Inizia con UNA routine sola** per le prime 2 settimane
- **Misura il consumo** nella pagina di billing claude.ai dopo i primi 7 giorni
- **Ottimizza il prompt** se vedi troppe chiamate: meno WebFetch, prompt piu' concisi, evita scansioni multiple delle stesse fonti
- **Cambia cadenza se necessario**: una routine quotidiana che potrebbe essere settimanale sta sprecando quota

## In caso di emergenza

Se sospetti che una routine si stia comportando male:

1. **Disabilita immediatamente** la routine da [https://claude.ai/code/routines](https://claude.ai/code/routines) (toggle Active -> Off)
2. **Audita il repo GitHub** per i commit delle ultime 24h
3. **Se ci sono modifiche non volute**: rollback dei commit dal repo
4. **Revoca il PAT** se sospetti compromissione del token

I Cloud Agents sono progettati per essere sicuri di default. Queste regole sono per restare sicuri anche quando vai oltre il default.
