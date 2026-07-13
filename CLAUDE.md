# YouTube Content Creation — v6 (struttura snella + ricerca automatica)

Sistema per produrre contenuti YouTube sul canale **AI applicata al business**. Struttura radicalmente semplificata rispetto alle versioni precedenti: ogni contenuto e' **3 cose**, niente di piu'.

## Cos'e' cambiato rispetto a v5

- **Niente piu' pipeline a 5 stadi**, niente piu' cartelle gemelle IT+EN, niente piu' SCRIPT.md, niente piu' _revisione.md, niente piu' 2 varianti tecniche per contenuto.
- **Una sola lingua di produzione** (italiano), con traduzione inglese del solo file PRINCIPALE per valutare se rifare il video in inglese.
- **Ricerca automatica delle idee**: due volte al giorno (mattina + sera) viene eseguita una ricerca remota (`/schedule`) che propone nuovi contenuti virali rivisitati sul mio settore.

## Le 3 cose che compongono ogni contenuto

Per ogni idea selezionata si produce **una sola cartella** in `CONTENUTI/<slug>/` che contiene **esattamente** queste 3 cose:

### 1. `materiali/` — cartella zippabile per il pubblico

Cosa lo spettatore scarica alla fine del video.

Contenuto MINIMO obbligatorio:
- `README.md` → guida **step-by-step a prova di idiota** per replicare quello che faccio nel video (installare plugin, usare strumenti, capire i concetti). C'e' SEMPRE, anche se non ci sono file pratici.
- `DISCLAIMER.md` → **solo se il contenuto usa `.env` o credenziali**. Ricorda all'utente di togliere le proprie credenziali prima di condividere o committare i materiali.

Contenuto opzionale (solo se il video lo richiede):
- File concreti che servono al video (script, prompt, config, esempi). Tutti al root della cartella, niente sottocartelle numerate.

### 2. `PRINCIPALE.html` — spiegazione del sistema (materiale di supporto)

Documento **per me**: spiega il **sistema** che si costruisce nel video — com'e' fatto, a livello tecnico ma comprensibile — e **con diagrammi/grafici** rende evidente il punto centrale del video (es. per l'Ep2: *perche' costa poco*). NON e' un copione da leggere parola per parola ("banale script"): e' lo schema mentale + i visual che tengo davanti mentre registro, e che posso anche mostrare a schermo. Le frasi da pronunciare le dico a braccio, da esperto del dominio.

Struttura tipica (adattala al contenuto):

1. **Cos'e' questo documento** — una riga che ricorda: materiale di supporto, spiegazione del sistema, non copione.
2. **Cosa costruiamo** — il sistema in 2-3 frasi.
3. **Architettura del sistema** — un **diagramma** (SVG o HTML/CSS inline) dei componenti e di come si parlano.
4. **Come funziona, pezzo per pezzo** — ogni componente: cos'e', cosa fa, com'e' fatto. Tecnico ma chiaro: qui i termini tecnici si possono usare, **spiegandoli**.
5. **Perche' funziona / perche' conviene** (LO SCOPO del video) — con **grafici** che dimostrano la tesi: per un video sui costi, barre "sistema vs modo ingenuo" e "dove va la spesa"; per altri video, il grafico che prova il punto (es. file prima/dopo, tempo prima/dopo).
6. **I numeri** — tabella con dati reali (prezzi, quantita') se rilevante.
7. **Limiti / onesta'** — cosa il sistema NON e' / NON fa.
8. **Cosa c'è nei materiali** — mappa della cartella che lo spettatore scarica: ogni file cos'e' / a cosa serve, e come i pezzi si parlano (input → programma → output). Tabella + una riga di sintesi. Va **prima** della sezione "Come testare".
9. **Come testare il tutto** — ultima sezione, **chiaramente separata** dal resto (sezione operativa, stile visivo distinto): la sequenza esatta per provare il sistema **coi materiali del corso** — comandi passo-passo, output atteso (anche un blocco "terminale"), e come verificare che ogni pezzo faccia la sua parte. E' l'unica sezione "fai questo", il resto del documento spiega.

Niente blocchi "Cosa dire" verbatim, niente scaletta parola-per-parola. Il valore del file e' la **comprensione visiva del sistema** + la prova pratica finale. Riferimento canonico: `CONTENUTI/serie-agenti-ai-aziende/ep2-agenti-ai-sostenibili/PRINCIPALE.html`.

### 3. `PRINCIPALE_ENG.html` — traduzione inglese del PRINCIPALE

Stessa struttura, **tutto tradotto in inglese** (tutte le sezioni: spiegazione del sistema, diagrammi, grafici), per valutare se rifare il video anche in lingua inglese.

Vive nella stessa cartella del PRINCIPALE.html italiano. Non e' bilingue per audience — e' un'opzione per me.

## Struttura della cartella progetto

```
yt-content-creation/
|-- CLAUDE.md                          <- questo file (regole globali)
|-- IDEE/                              <- input: idee da cui partire
|   |-- CLAUDE.md
|   |-- manuali.md                     <- idee scritte da me a mano
|   |-- topics.md                      <- appunti su macro-temi
|   `-- ricerche-auto/                 <- idee generate dallo /schedule (2x al giorno)
|       |-- YYYY-MM-DD-mattina.md
|       `-- YYYY-MM-DD-sera.md
|-- RICERCA_AUTOMATICA/                <- config dello scheduling
|   |-- CLAUDE.md
|   `-- prompt-ricerca.md              <- prompt usato dallo /schedule
|-- CONTENUTI/                         <- output: contenuti prodotti
|   |-- CLAUDE.md
|   `-- <slug>/                        <- una cartella per contenuto
|       |-- PRINCIPALE.html
|       |-- PRINCIPALE_ENG.html
|       `-- materiali/
|           |-- README.md              <- guida step-by-step pubblico
|           |-- DISCLAIMER.md          <- solo se .env/credenziali
|           `-- ... (eventuali file)
|-- _TEMPLATE_CONTENUTO/               <- template di partenza
`-- _archivio_v5_pipeline/             <- roba della vecchia pipeline (riferimento)
```

## Flusso operativo

### Generazione automatica idee (2x al giorno via /schedule)

Lo schedule remoto esegue il prompt definito in `RICERCA_AUTOMATICA/prompt-ricerca.md`. L'output:
- Cerca su web/YouTube/Twitter/Reddit cosa sta diventando virale su: **AI automazioni, software, Claude Code, intelligenza artificiale per il business**
- Calcola la **media dei contenuti virali** sull'argomento
- Propone **5-8 idee nuove** che NON sono copie banali — sono varianti, combinazioni, angoli inediti
- Scrive il file in `IDEE/ricerche-auto/YYYY-MM-DD-{mattina|sera}.md`

Ogni esecuzione produce un file nuovo (non sovrascrive). Lo storico resta consultabile.

### Selezione idea da produrre

L'utente sceglie un'idea da una delle fonti (`IDEE/manuali.md` o un file in `IDEE/ricerche-auto/`) e dice:

> "lavora sull'idea [titolo o keyword]"

Claude trova l'idea, genera la cartella `CONTENUTI/<slug>/` con le 3 cose (materiali/, PRINCIPALE.html, PRINCIPALE_ENG.html).

### Comandi tipici

- `aggiorna le idee manuali` -> apre `IDEE/manuali.md`
- `che idee abbiamo` -> elenca titoli da `IDEE/manuali.md` + ultimo file di `IDEE/ricerche-auto/`
- `lavora sull'idea X` -> produce `CONTENUTI/<slug>/` completa (materiali + PRINCIPALE + PRINCIPALE_ENG)
- `rifai il PRINCIPALE per X` -> rigenera solo i due HTML
- `rifai i materiali per X` -> rigenera solo `materiali/`
- `traduci il PRINCIPALE di X` -> rigenera solo PRINCIPALE_ENG.html

## Identita' del canale (REGOLE GLOBALI)

- **Tema**: AI applicata al business, casi d'uso pratici
- **Audience**: utenti **non tecnici** (imprenditori, manager, marketer, freelance, curiosi). NON developer.
- **Stile**: pratico, divulgativo, accessibile. Mai gergo tecnico senza spiegarlo.
- **Durata video target**: 8-18 minuti
- **Format prevalente**: build di mini-tool/sistema concreto, dimostrato live, replicabile dallo spettatore
- **Persona narrativa**: seconda persona ("tu fai X"), MAI prima persona finta ("ho creato X").

## Editor di riferimento

**VS Code** e' l'editor canonico. Quando il README delle materiali dice "modifica il file X", deve dire "apri X con VS Code", mai Blocco Note / Notepad / "editor di testo a scelta". Per i comandi: `code <path>`, non `notepad <path>`.

## Sicurezza credenziali (REGOLA GLOBALE)

1. **Mai credenziali vere nei materiali.** Solo placeholder fittizi (`.env.example`).
2. **Mai `.env` a video.** A voce dico "compila .env coi tuoi valori, non lo faccio a schermo per ovvi motivi di sicurezza".
3. **`.gitignore` esiste prima di `git init`** in ogni progetto pratico.
4. **Quando ci sono credenziali -> `DISCLAIMER.md` obbligatorio** dentro `materiali/`, che ricorda:
   - di non committare il `.env`
   - di **revocare e rigenerare** le credenziali se per sbaglio sono finite su GitHub (cancellarle dalla storia git da sole non basta — i bot scansionano).

## API e modelli (REGOLA GLOBALE)

Per i progetti pratici che chiamano i modelli **via codice**, si usa **OpenRouter** (non l'API diretta di un singolo provider):

- **Una sola chiave** (`OPENROUTER_API_KEY`, da [openrouter.ai/keys](https://openrouter.ai/keys)) dà accesso a tutti i modelli. Più facile, e si cambia modello/produttore cambiando una riga.
- Endpoint **compatibile OpenAI**: si usa la libreria `openai` con `base_url="https://openrouter.ai/api/v1"`. NON l'SDK Anthropic (OpenRouter non parla il protocollo nativo Anthropic).
- **Modelli da usare: Anthropic o Google** (restiamo su questi due produttori salvo motivo specifico), col prefisso del produttore: `anthropic/claude-opus-4-8`, `anthropic/claude-haiku-4-5`, `google/gemini-...`, ecc.
- **Structured output**: `response_format` con json_schema (il `.parse()` del client OpenAI con un modello Pydantic funziona). **Reasoning/thinking**: parametro `reasoning` di OpenRouter (`{"effort": "..."}` o `{"max_tokens": ...}`) via `extra_body`, non il `thinking` nativo Anthropic.
- **Unica eccezione**: un contenuto il cui *argomento è proprio l'SDK ufficiale Anthropic* (es. Ep1 "Cos'è il Claude SDK" con `tool_runner`) può restare sull'SDK Anthropic con `ANTHROPIC_API_KEY` — lì l'SDK è il punto del video, non un dettaglio.
- Riferimento canonico: `CONTENUTI/serie-agenti-ai-aziende/ep2-agenti-ai-sostenibili/materiali/analizza_recensioni.py`.

## Stile del PRINCIPALE.html (regole non negoziabili)

1. **E' materiale di supporto, non un copione** — spiega il sistema (com'e' fatto, perche' funziona/conviene), non le frasi da pronunciare. Niente blocchi "Cosa dire" verbatim.
2. **Spiegazione tecnica ma comprensibile** — qui i termini tecnici si possono usare, sempre spiegandoli; il livello e' "capisco com'e' fatto", non "lo so gia'".
3. **Almeno un diagramma dell'architettura** e — quando il video ha una tesi dimostrabile coi numeri (costi, tempo, file...) — **almeno un grafico** che la prova. Diagrammi/grafici in SVG o HTML/CSS inline.
4. **HTML self-contained** (CSS inline, nessuna dipendenza esterna, nessuna libreria JS di grafici).
5. **Leggibile e scansionabile** — sezioni evidenti, un'idea per blocco, il visual prima del testo lungo.
6. **Puo' essere mostrato a schermo** nel video (diagrammi e grafici sono pensati anche per quello).

## Stile del README.md dentro materiali/ (regole non negoziabili)

1. **A prova di idiota** — assume zero conoscenze tecniche pregresse.
2. **Step numerati** — un click/comando per step, non agglomerare.
3. **Spiega anche i concetti** — non solo "fai X", anche "X serve perche' Y".
4. **Quick start in cima**: 3-5 comandi/click per partire (se il contenuto e' eseguibile) o riassunto in 5 punti (se e' concettuale).
5. **Linguaggio divulgativo** — stessa audience del video, niente gergo dev.

## Voice Guide (REGOLE NON NEGOZIABILI PER OGNI CONTENUTO)

Tono di riferimento: **divulgativo accessibile con sano effetto nerd**. Tipo Piero Angela / Vsauce / Veritasium in salsa business. L'audience non e' tecnica ma deve sentirsi **rispettata** (non addomesticata) e **affascinata** (non istruita da manuale).

### Le 5 regole d'oro

1. **Niente termini-da-blog-tecnico mai.** Vietati nella prima persona di Claude (quando scrivo per il regista) e ancora di piu' nelle frasi che il regista dovra' pronunciare a voce:
   - "Standard de facto" -> di' "tutti i grandi ormai lo usano"
   - "Attacco superficie" -> di' "porte aperte agli hacker"
   - "Sandbox / sandboxed" -> di' "ambiente isolato"
   - "Scope read-only / read-write" -> di' "solo lettura / anche scrittura"
   - "Token autorizzato / OAuth" -> di' "una chiave che il servizio rilascia a Claude, limitata a quello"
   - "Self-hosted / on-prem" -> di' "il server che hai nel tuo ufficio / a casa tua"
   - "Endpoint, API, payload, middleware" -> di' la cosa concreta che fanno
   - "Setup un filo piu' tecnico" (e simili diminutivi) -> sono finti pragmatici, BANDITI

2. **Analogie ricorrenti sempre.** Ogni concetto astratto deve avere un'analogia fisica/quotidiana. Esempi-modello:
   - MCP = "lingua franca dei porti" / "Bluetooth dell'AI"
   - Connector = "interruttore della luce - clicchi e si accende, non devi sapere come funziona il cavo"
   - Scope read-only = "il nuovo stagista: primo mese guarda e impara, poi gli dai i tasti grossi"
   - Sub-agent = "stagisti specializzati che lavorano in parallelo mentre tu segui il cliente"
   - Routine schedulata = "lo svuotabuste del PC mentre dormi"

3. **Hook personalizzati, non frasi-funnel.** Niente "in questo video ti mostro come X" piatto. Preferisci:
   - "C'e' una conversazione che ho almeno una volta al mese con un cliente..."
   - "Tre giorni fa mi e' successa una cosa che secondo me da sola vale il prezzo del biglietto..."
   - "Se gestisci un'azienda o sei freelance, c'e' una scena che hai vissuto cento volte..."
   - Lo storyhook batte la promessa-funzionale al primo colpo.

4. **Il "wow" arriva dal pratico-utile, NON dal drammatico-clickbait.**
   - SI': dati realistici densi, sintesi chiara, valore in euro/ore visibile, sequenza naturale di lavoro
   - NO: comparison shot col cronometro che pesta i 60 minuti vs 1 minuto, "il cadavere nascosto nel contratto", "diciotto clienti persi nel cassetto, 170mila euro" se non e' DAVVERO la cosa centrale del video
   - Test: la frase, detta da te a un cliente reale a cena, suonerebbe credibile o "venditore al telefono"?

5. **Sano effetto nerd = ammirazione per la magia del processo, NON per la tecnica.**
   - SI': "sotto il cofano sta succedendo qualcosa di pazzesco: praticamente tutti i grandi si sono messi d'accordo per parlare lo stesso linguaggio, e questo cambia il gioco"
   - NO: "MCP supporta SSE bidirezionale con stato persistente e annotation server-side"
   - Lo spettatore deve pensare "ah figata, e' affascinante" non "non ho capito, non clicco like"

### Esempi prima/dopo da memorizzare

| Concetto | Prima (sbagliato) | Dopo (giusto) |
|---|---|---|
| Cos'e' MCP | "Model Context Protocol, standard di Anthropic rilasciato a fine 2024" | "C'e' una cosa che e' successa negli ultimi due anni di cui pochi parlano: tutti i grandi - Anthropic, OpenAI, Microsoft, Google - si sono messi d'accordo su un linguaggio comune con cui le AI parlano alle tue app. E' il Bluetooth dell'AI - una volta che esiste, qualsiasi cuffia parla con qualsiasi telefono" |
| Sicurezza OAuth | "Scope read-only sempre la prima volta. Token gestito da claude.ai" | "Regola d'oro scritta col sangue: prima volta che colleghi qualcosa, gli dai solo le chiavi di lettura. Puo' guardare, non puo' toccare. Stesso ragionamento del nuovo stagista" |
| Tunnel per DB on-prem | "MCP Tunnel rilasciato il 19 maggio per database self-hosted, evita di esporre porte sul firewall" | "Il diciannove maggio Anthropic ha rilasciato una cosa che chiameranno MCP Tunnels. Se il tuo gestionale gira su un server fisico nel tuo ufficio - non in cloud, su una macchina che vedi - questa feature crea un canale temporaneo tra Claude e quel server. Niente porte aperte, niente VPN, niente IT da disturbare" |
| Conclusione di un workflow | "Risparmio: 30-60 minuti a settimana" | "Stamattina, mentre prendevo il caffe', il brief era gia' nella mia casella. Questo lavoro - che il lunedi' mi prende quaranta minuti tra calendario aperto, mail aperte, post-it - oggi non l'ho fatto. Sta succedendo da solo. E sta succedendo anche per te se segui questi step" |

### Strutture-modello per i casi-frequenti

**Aprire un concetto astratto:**
> "Adesso una cosa che sembra noiosa ma resta con me trenta secondi perche' cambia tutto. [CONCETTO]. Tradotto: [ANALOGIA FISICA]. E il motivo per cui ti riguarda e': [PAYOFF CONCRETO]."

**Mostrare un comando/workflow per la prima volta:**
> "Digito [COMANDO]. Premo invio. Guarda cosa fa. [PAUSA - mostra il processo]. Tradotto in italiano normale: [TRADUZIONE]. Risultato pratico: [VALORE]."

**Spiegare un limite/disclaimer:**
> "Una cosa che voglio dirti in chiaro perche' qua ci si gioca la credibilita': [LIMITE]. Quello che fa Claude e': [CAPACITA' REALI]. Quello che NON fa: [CAPACITA' ESCLUSE]. Per il resto, ti serve sempre [PROFESSIONISTA / GIUDIZIO UMANO]."

### Check finale prima di consegnare un PRINCIPALE.html

Guarda il documento e immagina di spiegare il sistema a un amico imprenditore non tecnico usando **solo** i diagrammi e i grafici. Domanda di controllo: "Con questi visual davanti, riesco a fargli capire com'e' fatto il sistema e perche' funziona/conviene, e li trova chiari e interessanti?"

Se per spiegarlo devo scusarmi del gergo, o manca il grafico che prova la tesi del video, riscrivi.

> Nota: la Voice Guide qui sopra governa il **parlato** (le frasi a braccio davanti alla camera) e il README per il pubblico. Il PRINCIPALE.html invece e' materiale tecnico di supporto: i termini tecnici si usano, spiegandoli.

---

## Format YouTube ad alta performance (REGOLA GLOBALE per ogni contenuto)

Il canale ha verificato empiricamente che quattro format performano significativamente meglio degli altri (alto CTR + alta retention). Ogni nuovo contenuto deve appartenere a UNO di questi quattro format. Format generici tipo "Tutorial su X" o "Guida a Y" sono BANDITI.

### Format 1 — Listicle "Le N cose..."

**Template titolo**: `Le [N] [cose / errori / tecniche / regole / motivi / segnali] [verbo] [tema] ([sotto-promessa concreta])`

Esempi:
- "Le 5 cose da sapere sui Cloud Agents di Claude (prima di delegare il primo task)"
- "Le 7 regole che seguo quando metto Claude in produzione (dopo 6 mesi sul campo)"
- "Le 5 tecniche per evitare il 90% dei file che Claude Code genera"
- "I 3 errori che fai col CLAUDE.md (e che ti costano tempo ogni giorno)"

**Perche' funziona**: N preciso fa percepire un'aspettativa contenuta e chiara. Sotto-promessa in parentesi alza il valore. Retention sopra media perche' lo spettatore conta in mente quanti item mancano.

**Vincoli di struttura per il video**:
- N tra 3 e 7 (mai oltre 9, mai sotto 3)
- Ogni item ha una **mini-storia o esempio concreto**, non solo descrizione
- Item 1 = quello piu' immediato/facile (familiarita')
- Item N = quello piu' forte/sorprendente (payoff finale)
- L'ordine NON e' alfabetico — e' drammatico

### Format 2 — Storia personale "Hai mai... Io l'ho fatto"

**Template titolo**: `Hai mai [azione poco comune ma realistica]? Io l'ho fatto [in questo video / per N mesi / e ti dico cosa ho imparato]`

Esempi:
- "Hai mai messo Claude Code in un vero server di produzione? Io l'ho fatto."
- "Hai mai schedulato un agente Claude per girare 30 giorni di fila senza supervisione? Io l'ho fatto."
- "Hai mai lasciato Claude scrivere TUTTO il codice di un mini-progetto reale? Io l'ho fatto."

**Perche' funziona**: domanda diretta apre curiosity loop. Affermazione "Io l'ho fatto" promette esperienza vera, non teoria. Triggera "voglio vedere cosa e' successo".

**Vincoli di struttura per il video**:
- Aprire con la SCENA della storia (non con "ciao a tutti")
- Almeno UN momento di "cose che NON sono andate come previsto" — credibilita'
- Estrarre **lezioni concrete** alla fine, non solo "che esperienza"
- La storia e' lo scheletro, ma l'utente deve poter replicare quello che hai imparato

### Format 3 — Problem-solver "Come evitare / risolvere / sistemare X"

**Template titolo**: `Come [evitare / risolvere / sistemare] [problema specifico molto comune] [in N minuti / senza X / quando Y]`

Esempi:
- "Come evitare il 90% dei file che Claude Code genera (e non ti servono)"
- "Come sistemare un CLAUDE.md che e' diventato un mostro da mille righe"
- "Come fare in modo che Claude smetta di chiederti conferma per ogni cosa"

**Perche' funziona**: query intent fortissimo. Chi cerca questa frase ha gia' il problema, vuole la soluzione subito. Alto matching con cerca su YouTube.

**Vincoli di struttura per il video**:
- Apri descrivendo il problema in modo che lo spettatore dica "si', proprio questo!"
- Soluzione presentata in 3-5 step, non in un blocco
- Mostra il **prima e dopo** concreto (es. cartella sporca con 40 file -> cartella pulita con 8 file)
- Disclaimer onesto: in quale caso la tua soluzione NON va bene

### Format 4 — Build dimostrativa "Costruisco X in N minuti / con Y"

**Template titolo**: `[Costruisco / Realizzo / Faccio] [cosa concreta utile] [in N minuti / con un solo prompt / senza scrivere codice]`

Esempi:
- "Costruisco il mio analista di contratti AI in 15 minuti (e te lo regalo)"
- "Realizzo una newsletter AI personalizzata col solo Claude Code (senza scrivere una riga di Python)"
- "Faccio parlare il mio magazzino di vini con Claude in 12 minuti"

**Perche' funziona**: promessa di un artefatto consegnabile. Spettatore vede crescere qualcosa di tangibile. Buona shareability ("guarda cosa si puo' fare").

**Vincoli di struttura per il video**:
- Vedi la cosa finita NEI PRIMI 60 secondi (anche solo per 5 secondi) — promessa visibile
- Build progressivo: ogni step deve aggiungere qualcosa di visibile
- Finale: "lo metti in mano allo spettatore", file gia' pronto da scaricare

### Format **BANDITI** (mai usarli)

- "Tutorial completo su X" (troppo generico, niente promessa)
- "Tutto quello che devi sapere su X" (overpromise, retention bassa)
- "Guida definitiva a X" (overpromise + commodity)
- "X in 60 secondi" (clickbait + sottostimato il valore reale)
- "X spiegato semplice" (sa di YouTube 2018)
- Domande con risposta "ovvia": "Vale la pena Claude Pro?" (gia' polarizzante)

### Regola di portfolio del canale

Per non saturare un solo format, mantieni una rotazione approssimativa:
- 40% Listicle
- 30% Build dimostrativa
- 20% Problem-solver
- 10% Storia personale

Lo "Storia personale" e' il piu' potente ma il piu' difficile da fare credibile: usalo quando hai DAVVERO una storia, non per format.

---

## Memoria persistente

I feedback dell'utente accumulati nelle conversazioni passate sono in `~/.claude/projects/C--Users-zizif-Desktop-Lavoro-Progetti-lavorativi-GitHub-yt-content-creation/memory/`. Leggerli sempre come contesto aggiuntivo.
