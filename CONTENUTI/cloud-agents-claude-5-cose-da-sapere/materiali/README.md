# Le 5 cose da sapere sui Cloud Agents di Claude (prima di delegare il primo task)

> Materiali del video YouTube **"Le 5 cose da sapere sui Cloud Agents di Claude (prima di delegare il primo task)"**.
> Trovi qui un riassunto delle 5 cose, un template di Routine pronta da usare, e una guida per replicare quello che ho mostrato nel video.

---

## In 30 secondi — di che si tratta

I **Cloud Agents** (che Anthropic chiama anche **Claude Code Routines**) sono agenti Claude che girano nel **cloud Anthropic**, su una macchina che non e' la tua, ad orari che decidi tu — anche quando il tuo PC e' spento.

Servono a delegare task ricorrenti: scouting di news quotidiano, generazione di contenuti, monitoraggio competitor, sintesi report. Il pattern e' "stagista che lavora la notte mentre dormi": gli lasci un foglio di istruzioni, lui esegue, al mattino trovi il risultato.

Questo documento ti aiuta a evitare i 5 errori piu' comuni dei principianti.

---

## Cosa ti serve prima di iniziare

- [ ] **Claude Pro o Max** — [https://claude.ai/upgrade](https://claude.ai/upgrade) — il Cloud Agent consuma quota del tuo piano
- [ ] **Account GitHub** — [https://github.com](https://github.com) — gratuito. Serve come "filesystem persistente" (vedi Cosa #4)
- [ ] **VS Code** — [https://code.visualstudio.com](https://code.visualstudio.com) — per leggere i template di questa cartella
- [ ] 15 minuti

---

## Quick start (5 passi)

1. Crea un repository GitHub vuoto (es. `claude-routines-personali`).
2. Crea un Personal Access Token GitHub con scope `repo` ([https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)).
3. Vai su [https://claude.ai/code/routines](https://claude.ai/code/routines) -> **New Routine**.
4. Compila: nome routine, prompt (usa `esempio-routine.md` di questa cartella come template), schedule cron, repository GitHub di destinazione.
5. Salva. La routine partira' al primo orario schedulato. Per testare subito: **Run now**.

Se sei alle prime armi, leggi la guida completa qui sotto.

---

## Le 5 cose da sapere — riassunto operativo

### Cosa 1 — Cloud Agent NON e' Claude Code locale

I Cloud Agents girano su una macchina di Anthropic, non sul tuo PC.

Implicazioni:
- **Niente filesystem locale persistente**: non possono salvare file sul tuo Mac/Windows
- **Ogni esecuzione parte da zero**: il sandbox e' "pulito" ogni volta
- **Nessuna persistenza tra run**: se vuoi conservare un risultato, devi committarlo su Git (vedi Cosa #4)

Quando NON usarli: per sviluppo software vero (quello fai con Claude Code locale, con i tuoi file aperti in VS Code).

### Cosa 2 — Servono per task RICORRENTI, non one-shot

I Cloud Agents danno valore quando un task si ripete con frequenza prevedibile. Casi reali dove funzionano:

- **Scouting quotidiano**: cerca news/post virali nel tuo settore ogni mattina alle 8
- **Monitoraggio competitor**: una volta a settimana scansiona siti competitor e ti manda report
- **Generazione contenuti**: una volta al mese genera un report PDF basato sui dati di un Google Sheet
- **Customer support digest**: ogni venerdi' sintetizza i ticket della settimana

Casi dove NON funzionano:
- "Aiutami a scrivere un'email a Mario adesso" -> usa la chat normale
- "Modifica questo file di Excel" -> il file e' sul tuo PC, sandbox non lo vede

### Cosa 3 — Costano quota del tuo piano (occhio al budget)

Ogni esecuzione consuma usage del tuo piano Pro o Max. Esempio reale: una routine che fa WebSearch (3-5 chiamate) + WebFetch (5-10 chiamate) + analisi + scrittura di un file markdown puo' consumare l'equivalente di **40-60 messaggi di chat**.

Stima per cadenze tipiche:
- 1 routine, 1 volta al giorno -> ~5 GB di context al mese
- 1 routine, 2 volte al giorno (come nostro sistema di scouting) -> ~10 GB
- 5 routine, ognuna 1 volta al giorno -> ~25 GB

Se sei su Pro (~7 GB/mese di context), oltre 1-2 routine giornaliere significa upgrade a Max. Non spaventarti, ma calcola.

**Regola pratica**: parti con UNA routine. Per le prime 2 settimane misura quanto consuma. Aggiungi le altre dopo.

### Cosa 4 — GitHub e' il filesystem persistente

Visto che il sandbox e' effimero, l'unico modo per conservare i risultati e' committare su un repository Git. Quindi:

1. Ogni Cloud Agent **e' associato a un repository GitHub**
2. Il sandbox **clona** il repo ad ogni esecuzione
3. Alla fine, il sandbox deve **committare + pushare** i nuovi file

**Importante**: il push richiede credenziali. Hai due opzioni:
- **OAuth GitHub** dall'integrazione Anthropic (semplice ma a volte non disponibile)
- **Personal Access Token (PAT)** passato nel prompt della routine (vedi `DISCLAIMER.md` di questa cartella per le precauzioni)

Nel video uso il PAT perche' a oggi e' il metodo che funziona in modo affidabile per tutti gli account.

### Cosa 5 — L'approvazione umana resta obbligatoria

I Cloud Agents girano da soli. Tentazione: farli mandare email/fare pagamenti/eseguire azioni distruttive in autonomia. **NON FARLO**.

Regola d'oro: ogni routine produce un **artefatto da revisione** (file markdown, bozza email salvata come Draft, report PDF), MAI un'azione esterna definitiva.

- ✅ "Genera 5 bozze email e salvale nei Draft di Gmail"
- ❌ "Manda 5 email a questi clienti"
- ✅ "Crea un report PDF e committalo nel repo"
- ❌ "Fai un pagamento di 200 EUR a questo fornitore"
- ✅ "Identifica i 5 prodotti a rischio esaurimento e scrivili in un file"
- ❌ "Ordina automaticamente le scorte mancanti"

Anche se il modello fosse capace tecnicamente, NON gli dai mai l'autonomia su azioni che toccano clienti, soldi, dati persi.

---

## Guida completa passo-passo (replica quello che ho fatto nel video)

### Step 1 — Crea il repository GitHub

1. Vai su [https://github.com/new](https://github.com/new).
2. **Repository name**: `claude-routines-personali` (o quello che vuoi).
3. **Private** consigliato (i risultati delle routine possono contenere info sensibili).
4. Click **Create repository**.
5. Click **Code** -> **HTTPS** -> copia l'URL del repo (lo userai dopo).

### Step 2 — Crea un Personal Access Token GitHub

1. Vai su [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new) (classic token, e' il piu' semplice).
2. **Note**: `claude-routines-pat`
3. **Expiration**: 1 anno (o quello che preferisci)
4. **Select scopes**: spunta solo **`repo`** (parent checkbox che include tutto il sotto-albero).
5. Click **Generate token** in fondo.
6. **Copia il token** subito (inizia con `ghp_...`) — lo vedi una sola volta.
7. Salvalo nel tuo gestore di password.

### Step 3 — Apri Claude Code Routines

Vai su [https://claude.ai/code/routines](https://claude.ai/code/routines). Loggati col tuo account Pro/Max.

Vedi (se sei al primo accesso) una pagina con "No routines yet". Click **Create new routine**.

### Step 4 — Compila la routine

Campi da riempire:

- **Name**: nome significativo, es. `scouting-news-ai-mattina`
- **Schedule (cron)**: quando deve girare. Esempi:
  - Ogni giorno alle 08:00 ora italiana (CEST = UTC+2 d'estate): `0 6 * * *`
  - Ogni lunedi' mattina: `0 6 * * 1`
  - Tre volte al giorno (8, 14, 20): `0 6,12,18 * * *`
  - Ricorda: **il cron e' in UTC**. Calcola con offset della tua timezone.
- **Repository**: l'URL del repo che hai creato allo Step 1
- **Prompt**: il testo che la routine eseguira'. Vedi `esempio-routine.md` di questa cartella per un template completo pronto da copiare.
- **Allowed tools**: spunta `Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch` (i tool che il sandbox puo' usare)
- **Model**: `claude-sonnet-4-6` (default — non cambiarlo a meno che tu sappia perche')

Click **Save**.

### Step 5 — Testa subito con Run Now

Non aspettare il prossimo cron. Click **Run now** sulla routine appena creata.

In 3-8 minuti dovresti vedere:
- Stato della routine: `succeeded`
- Un nuovo commit nel tuo repository GitHub con il file generato

Se NON vedi il commit:
- Apri la timeline della routine su claude.ai
- Cerca l'errore (tipicamente: errore `git push` -> PAT sbagliato o scope insufficiente)
- Vedi la sezione troubleshooting di `DISCLAIMER.md`

### Step 6 — Schedula altre routine

Quando la prima gira bene da 5-7 giorni, aggiungi le altre. Suggerimenti di routine da costruire:

1. **Newsletter personale settimanale** — ogni venerdi' alle 18:00, scansiona i tuoi feed preferiti e ti manda un report mail
2. **Monitor competitor** — ogni lunedi' alle 9:00, controlla prezzi/news di 3 competitor scelti
3. **Daily digest customer support** — ogni mattina, sintetizza ticket della giornata precedente

Per ogni nuova routine: nuovo prompt, stesso repository di destinazione (o diversi se vuoi tenere separati i risultati).

---

## Concetti spiegati semplici

- **Cloud Agent / Routine**: agente Claude che gira nel cloud Anthropic ad orari prestabiliti, anche col tuo PC spento. Non e' la chat normale di Claude.
- **Sandbox**: ambiente isolato dove il Cloud Agent gira. Effimero: ad ogni esecuzione parte da zero, niente memoria tra run.
- **Cron**: formato standard per definire "quando" (es. `0 6 * * *` = "ogni giorno alle 6:00 UTC"). I siti come [crontab.guru](https://crontab.guru/) ti aiutano a tradurlo.
- **PAT (Personal Access Token)**: una chiave personale che dai al Cloud Agent per poter pushare sul tuo repo GitHub. Sostituisce la password.
- **Scope `repo`**: il permesso che il PAT include — significa "puo' leggere e scrivere sui tuoi repository".

---

## Riferimenti

- **Pagina ufficiale Routines** (claude.ai): [https://claude.ai/code/routines](https://claude.ai/code/routines)
- **Documentazione cron**: [https://crontab.guru](https://crontab.guru) — traduce cron in italiano leggibile
- **Documentazione GitHub PAT**: [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

---

## Dubbi o problemi?

- Commenta sotto il video YouTube — rispondo a tutti.
- Errore tipico: "git push failed: authentication failed" -> il PAT e' scaduto o ha scope insufficiente. Rigeneralo dallo Step 2.
- Errore tipico: routine "succeeded" ma niente commit nel repo -> verifica nel prompt di aver scritto correttamente il path del file e il comando `git push`. Vedi `esempio-routine.md`.

Buon lavoro.
