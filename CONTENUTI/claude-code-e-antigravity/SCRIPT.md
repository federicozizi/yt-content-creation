# SCRIPT.md — Claude Code + Antigravity: come usarli insieme

> ⚠️ Gemello inglese: `CONTENUTI/claude-code-and-antigravity/SCRIPT.md` (solo le righe `🎙️ DIRE` sono tradotte là, il resto è in italiano come qui).

Durata target: **7 minuti**.
Stile: pratico, conversazionale. Un workflow chiaro, un caso d'esempio, un pattern che generalizza.

---

## 0. SETUP UNA TANTUM

Cose della vita, da fare una sola volta e basta:

- Account Google con accesso ad Antigravity attivo (verifica login a `antigravity.google.com`).
- Profilo Chrome dedicato "youtube-demo" — niente cronologia personale, niente estensioni inutili.
- Claude Code installato globalmente (`claude --version` deve funzionare).
- OBS configurato con due scene: `BROWSER` (1920x1080, finestra Chrome) e `TERMINALE` (1920x1080, terminale a tutto schermo, font 18pt, prompt minimale).
- Microfono testato, livello -12dB di picco.
- Webcam con sfondo neutro per le clip CAMERA.

---

## 1. PRE-REC GIORNATA (30-40 min prima di registrare)

Tutto quello che NON deve essere fatto live, da preparare prima di accendere la camera:

### Account e ambiente
- [ ] Login a `antigravity.google.com` con il profilo Chrome "youtube-demo". Verifica che il workspace creato per la demo (`homepage-refresh-demo`) sia vuoto e pronto.
- [ ] Login a `claude.ai` se ti serve, ma per il video non lo useremo.
- [ ] Terminale aperto nella cartella `~/demo/mio-sito-fake/` (sito demo già preparato — vedi sotto).

### Repo demo
- [ ] Cartella `~/demo/mio-sito-fake/` esiste e contiene un `index.html` brutto-ma-funzionante (header, hero, 3 sezioni, footer). Stile generico, copy bidimensionale: deve essere chiaramente "una home che ha bisogno di un refresh".
- [ ] Dentro c'è anche una sottocartella `materiali/` con i 2 prompt pronti da copiare (gli stessi che daremo al pubblico).
- [ ] `git status` deve essere pulito. Se hai già fatto prove, `git checkout -- .` e ricomincia.

### Artefatti pre-cotti (BACKUP, da usare solo se la demo live fallisce)
- [ ] Tre file HTML pre-generati in `~/demo/backup/`: `landing-corporate.html`, `landing-amichevole.html`, `landing-aggressive.html`. Servono solo se Antigravity è lento o down nel momento della registrazione.
- [ ] Screenshot delle 3 preview salvati in `~/demo/backup/screenshots/` (per inserto in editing).

### Tab del browser in ordine fisso
Apri prima di registrare, lascia in questo ordine:
1. Antigravity workspace (la dashboard pronta, vuota)
2. PRINCIPALE.html locale (per le clip slide)
3. Il sito demo "vecchio" aperto in localhost (`http://localhost:8080`) — Python `http.server` già avviato

### Terminale
- [ ] Aperto in `~/demo/mio-sito-fake/`
- [ ] Prompt impostato per essere leggibile (es. `PS1='\W $ '`)
- [ ] History pulita (`history -c`)

### Materiali clip
- [ ] PRINCIPALE.html aperto in VS Code in parallelo (per consultarlo durante il taglio, non a video)
- [ ] Copione clip-per-clip stampato o aperto su un secondo monitor

---

## 2. CLIP — elenco completo

| # | Schermata | Durata | Modalità |
|---|---|---|---|
| 01 | CAMERA | ~25s | LIVE |
| 02 | PRINCIPALE.html `#cosa-e` | ~50s | LIVE |
| 03 | PRINCIPALE.html `#cosa-costruiremo` | ~40s | LIVE |
| 04 | PRINCIPALE.html `#come-funziona` | ~30s | LIVE |
| 05 | PRINCIPALE.html `#setup` | ~25s | LIVE |
| 06 | PRINCIPALE.html `#step-1` | ~25s | LIVE |
| 07 | BROWSER Antigravity | ~70s | MISTO (live spawn, preview accelerata in editing) |
| 08 | PRINCIPALE.html `#step-2` | ~20s | LIVE |
| 09 | BROWSER Antigravity | ~40s | LIVE (scelta + download) |
| 10 | PRINCIPALE.html `#step-3` | ~25s | LIVE |
| 11 | TERMINALE (Claude Code) | ~60s | LIVE |
| 12 | PRINCIPALE.html `#oltre` | ~35s | LIVE |
| 13 | CAMERA | ~20s | LIVE |
| 14 | CAMERA | ~25s | LIVE (CTA verbatim) |

**Totale stimato**: ~7 min. Bilancio CAMERA: 3 clip (hook + riepilogo + CTA). Tutto il resto è slide-HTML + demo concrete.

---

## CLIP 01 — Hook

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`.
- Postura aperta, sguardo dritto in camera.

**🎙️ DIRE (verbatim):**
> "Hai Claude Code e va benissimo. Ora c'è anche Antigravity, il nuovo agent IDE di Google, e ti sei chiesto: mi conviene usarli insieme? In 7 minuti ti mostro come. Senza forzature: ognuno fa il pezzo che sa fare meglio, e tu li metti in fila."

**🖥️ MOSTRARE:** Solo CAMERA. Niente lavagnetta in questo hook — il tempo è poco, la prima slide HTML arriva subito dopo.

**🎬 LIVE**

---

## CLIP 02 — Cos'è questa integrazione

**🧰 Cosa preparare prima della camera:**
- Switcha a tab PRINCIPALE.html, scorri fino alla sezione `#cosa-e`. Verifica che i due box `.concetto-chiave` siano entrambi visibili senza scrollare.

**🎙️ DIRE (verbatim per il concetto, libero per i punti):**
> "Claude Code e Antigravity sono entrambi agenti AI che lavorano per te, ma stanno in posti opposti e fanno cose opposte. Antigravity vive in cloud: apri il browser, gli dai un'istruzione, lui spawna agenti in parallelo che lavorano ognuno per conto suo, e ti restituisce dei file che puoi vedere e approvare prima. Claude Code vive sul tuo PC: vede i tuoi file veri, modifica il tuo repo, fa i commit. Metterli insieme non vuol dire farli litigare. Vuol dire dare a ognuno il pezzo di lavoro che sa fare meglio."

**🖥️ MOSTRARE:** PRINCIPALE.html scrollato a `#cosa-e`. Punta col cursore i 2 box gialli `.concetto-chiave` mentre li commenti.

**🎬 LIVE**

---

## CLIP 03 — Cosa faremo oggi (case study)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#cosa-costruiremo`. Verifica che il diagramma `.diagram` sia ben visibile a schermo intero.

**🎙️ DIRE (verbatim):**
> "Caso concreto per dimostrare il pattern: rifare la home page di un sito che hai già. Hai un index.html un po' stanco. Vuoi vedere 3 versioni grafiche diverse prima di decidere. E vuoi che la vincente venga cucita nel tuo repo, non lasciata a fluttuare in cloud. Tre mosse: Antigravity sforna 3 varianti in parallelo, tu scegli con l'occhio, Claude Code fa il finale a casa tua."

**🖥️ MOSTRARE:** PRINCIPALE.html `#cosa-costruiremo`. Soffermati sul diagramma ASCII per ~10s — è il punto in cui tutto il video si vede in una schermata.

**🎬 LIVE**

---

## CLIP 04 — Come funziona

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#come-funziona`. La lista numerata dei 3 pezzi deve essere visibile.

**🎙️ DIRE:**
> "Tre pezzi in sequenza. Antigravity Manager: l'interfaccia browser, dove tu dai un prompt e lui lo distribuisce a N agenti. Artefatti: i file e le preview che ogni agente produce — non leggi codice, guardi il render. Claude Code: il finale, sul tuo PC, che prende la versione scelta e la integra nel tuo progetto reale. Regola di divisione, leggi il box giallo: esplora in cloud, taglia e cuci in locale."

**🖥️ MOSTRARE:** PRINCIPALE.html `#come-funziona`. Punta il box `.concetto-chiave` finale quando lo leggi.

**🎬 LIVE**

---

## CLIP 05 — Setup

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#setup`. Lista checks visibile.

**🎙️ DIRE:**
> "Setup minimo: account Google con accesso Antigravity, Claude Code che già usi, una cartella di progetto col tuo index.html. Se ti manca il sito, nei materiali c'è un mini-sito demo già pronto. Per il setup operativo: dentro la cartella materiali lanci claude e gli dici esegui il setup leggendo CLAUDE.md. Un minuto."

**🖥️ MOSTRARE:** PRINCIPALE.html `#setup`. Punta la lista `ul.checks`.

**🎬 LIVE**

---

## CLIP 06 — Step 1 (concetto)

**🧰 Cosa preparare prima della camera:**
- Scrolla a `#step-1`. Concetto-chiave visibile sopra il fold.

**🎙️ DIRE:**
> "Primo step, il pezzo che da soli non si fa veloce: generare 3 alternative contemporaneamente, in 3 ambienti separati. Claude Code è seriale — un'istanza, una macchina, una cosa alla volta. Antigravity spawna 3 agenti in cloud con un click. Tre teste in parallelo, tu aspetti una volta sola. Nel nostro caso: stile corporate, amichevole, aggressive. Tre prompt quasi identici, cambia solo la parola STILE."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-1`. Punta il box giallo con la frase "Antigravity ti spawna 3 agenti in cloud con un click".

**🎬 LIVE**

---

## CLIP 07 — Demo Antigravity (spawn + lavoro parallelo)

**🧰 Cosa preparare prima della camera:**
- Switcha a tab Antigravity (workspace `homepage-refresh-demo`, vuoto).
- Apri in un secondo monitor il file `materiali/prompts/antigravity-parallel-draft.md` da cui copierai il prompt.
- Tieni a portata il vecchio `index.html` pronto da caricare.

**🎙️ DIRE (libero, da commento mentre fai):**
> "Carico il file di partenza, spawno 3 sessioni, incollo il prompt in ognuna cambiando solo lo stile. Premo invio in tutte e tre. Adesso lavorano insieme, non in fila. Mentre lavorano, dashboard ti dice chi è arrivato dove."

**🖥️ MOSTRARE:** BROWSER su Antigravity. Mostra: workspace → upload `index.html` → spawn 3 sessioni → paste prompt × 3 → run. Quando le sessioni sono "running", la dashboard mostra le 3 barre di progresso.

**🎬 MISTO**
> Lo spawn delle 3 sessioni va LIVE (3-4 minuti effettivi accelerati a ~30s in editing). Il rendering dei progressi va in time-lapse 4-8x.

---

## CLIP 08 — Step 2 (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-2`. Concetto-chiave visibile.

**🎙️ DIRE:**
> "Quando i 3 agenti finiscono, Antigravity non ti scarica un blob di codice da leggere. Ti mostra il rendering. Tre preview affiancate. Giudichi con l'occhio in 30 secondi a versione: questa è troppo fredda, questa è urlata, questa ha il tono giusto."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-2`. Punta il box giallo "non devi leggere 300 righe di codice".

**🎬 LIVE**

---

## CLIP 09 — Demo Antigravity (scelta + download artefatto)

**🧰 Cosa preparare prima della camera:**
- Le 3 sessioni in Antigravity hanno terminato (se la registrazione live non è arrivata in tempo, usa i 3 file pre-cotti in `~/demo/backup/`).
- Apri le 3 preview affiancate (split view se Antigravity lo supporta, altrimenti 3 tab adiacenti).

**🎙️ DIRE (libero, da commento):**
> "Le 3 home, una accanto all'altra. La corporate è fredda. La aggressive urla. L'amichevole ha il claim debole ma il tono giusto. Prendo l'amichevole. Click destro, download artifact, lo salvo come landing-vincitrice.html nella cartella materiali del mio sito."

**🖥️ MOSTRARE:** BROWSER Antigravity con le 3 preview, poi il flusso di download dell'artefatto vincente.

**🎬 LIVE** (questa parte è breve e funziona bene live)

---

## CLIP 10 — Step 3 (concetto)

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#step-3`. Concetto-chiave visibile.

**🎙️ DIRE:**
> "L'HTML che ho scaricato è bello ma scollegato dal mio progetto. Usa link inventati, non ha i miei meta tag, magari ha rinominato file che esistono già. Antigravity lavorava in sandbox — non sapeva nulla del mio repo. Claude Code sì. Lui legge tutto, capisce cosa mantenere, e fa un commit pulito. È il finale a casa."

**🖥️ MOSTRARE:** PRINCIPALE.html `#step-3`. Punta il box giallo "Antigravity lavora in sandbox. Il tuo file vero, il tuo repo, il tuo commit — lo fa Claude Code".

**🎬 LIVE**

---

## CLIP 11 — Demo Claude Code (integrazione locale)

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `TERMINALE`. Cwd in `~/demo/mio-sito-fake/`.
- Il file `landing-vincitrice.html` è già salvato in `./materiali/` (l'hai messo lì alla fine di CLIP 09, oppure è pre-cotto se la demo backup).
- Apri in un secondo monitor `materiali/prompts/claude-code-handoff.md` da cui copierai il prompt.

**🎙️ DIRE (libero, da commento):**
> "Apro Claude Code nella cartella del sito. Incollo il prompt di handoff: leggi landing-vincitrice.html, fondila con index.html mantenendo link, meta e asset, e mostrami il diff prima di toccare il file. Lui legge i due file, propone il merge. Diff a schermo: tolgo il claim debole, accetto le sezioni nuove, mantengo i miei link interni che lui ha riconosciuto. Approvo. Commit con un messaggio sensato. Fatto."

**🖥️ MOSTRARE:** TERMINALE: `cd ~/demo/mio-sito-fake && claude` → paste prompt → Claude legge i file, propone diff → tu accetti → commit.

**🎬 LIVE** (se Claude Code è lento sulla generazione del diff, può essere accelerato 2x in editing, ma il taglio finale del commit deve essere realtime per autenticità).

---

## CLIP 12 — Oltre il caso: dove vale lo stesso pattern

**🧰 Cosa preparare prima della camera:**
- Switcha a PRINCIPALE.html `#oltre`. I 5 box `.use-case` visibili scrollando lentamente.

**🎙️ DIRE:**
> "Lo schema vale ogni volta che hai più strade plausibili e l'occhio umano deve scegliere. Email di vendita in tre toni. Proposta cliente in tre angoli. Audit competitor in parallelo, uno per concorrente. Documentazione di prodotto in tre voci. Test di un'idea con tre mini-landing. Antigravity esplora, tu scegli, Claude Code chiude."

**🖥️ MOSTRARE:** PRINCIPALE.html `#oltre`. Scrolla lentamente attraverso i 5 box `.use-case`. Non leggere ogni box parola per parola — il pubblico li ha sotto gli occhi.

**🎬 LIVE**

---

## CLIP 13 — Riepilogo

**🧰 Cosa preparare prima della camera:**
- Switcha a scena `CAMERA`.

**🎙️ DIRE (verbatim):**
> "Riepilogo veloce. Antigravity quando devi esplorare in parallelo: tre versioni invece di una, senza scaldare il PC. Claude Code quando devi chiudere il cerchio nel progetto reale: file veri, struttura tua, commit tuoi. Il ponte è l'artefatto: scarichi da Antigravity, passi a Claude Code. Nessuna API magica, nessuna integrazione difficile. Solo un workflow con te in mezzo che fa il giudice."

**🖥️ MOSTRARE:** CAMERA. Sguardo dritto.

**🎬 LIVE**

---

## CLIP 14 — CTA Skool + consulenza

**🧰 Cosa preparare prima della camera:**
- Resta su CAMERA.
- Tieni gli URL community/consulenza pronti per il lower-third in editing.

**🎙️ DIRE (verbatim — non improvvisare):**
> "Se ti interessano altri pattern di integrazione tra AI — Claude Code con n8n, con GitHub Actions, con Antigravity in workflow più articolati — sono nella community Skool, link in descrizione. È il posto dove condivido i workflow che uso davvero, con prompt e configurazioni. Se hai un caso specifico in azienda e vuoi capire se il pattern parallelo-più-locale ti risolve un problema concreto, c'è anche la consulenza diretta: parti dal tuo flusso reale e ti dico quale pezzo conviene mettere in cloud e quale in locale. Link in descrizione anche per quello. Ci vediamo nel prossimo video."

**🖥️ MOSTRARE:** CAMERA. Sorriso a fine frase, poi taglio.

**🎬 LIVE**

---

## 3. POST-REC (sicurezza)

Subito dopo aver fermato la registrazione:

- [ ] Logout dal workspace Antigravity demo (così non resta loggato sul profilo Chrome).
- [ ] Cancella la cartella `~/demo/mio-sito-fake/.git` se la pushavi su un repo remoto reale durante le prove.
- [ ] Verifica che il file `landing-vincitrice.html` non contenga dati personali o chiavi (era un artefatto Antigravity, dovrebbe essere pulito, ma controlla).
- [ ] Chiudi Claude Code (`exit` dal terminale).
- [ ] Salva i raw OBS in `~/registrazioni/<data>-claude-antigravity/` prima di toccare l'editing.

---

## 4. CHECKLIST MONTAGGIO

- [ ] Ordine clip: 01 → 14, come da tabella.
- [ ] Time-lapse della CLIP 07 (spawn parallelo Antigravity): comprimere a ~30 secondi mostrando la dashboard con le 3 barre di progresso.
- [ ] Lower-third sui link Skool/consulenza nella CLIP 14, sincronizzato con la frase pronunciata.
- [ ] Audio: noise gate, EQ, compressione leggera. Livello di uscita -14 LUFS.
- [ ] Sottotitoli IT autogenerati + correzione manuale dei nomi propri ("Antigravity", "Claude Code").
- [ ] Censure: nessuna in questo video (nessuna chiave API mostrata, nessun dato reale di clienti).
- [ ] Thumbnail: split del frame con preview Antigravity a sinistra e terminale Claude Code a destra, freccia che si incontra al centro. Testo: "1 + 1 = 5 in 7 minuti".
- [ ] Descrizione video: link al repo template materiali, link Skool, link consulenza.
- [ ] End screen: card al video precedente sul workflow parallelo + iscriviti.
