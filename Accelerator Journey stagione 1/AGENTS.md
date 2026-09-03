# Accelerator Journey — Stagione 1

Serie in cui si lancia un business AI e se ne racconta il viaggio senza filtri, insegnando agli utenti tramite le nostre esperienze. Accelerator è il nostro programma di consulenza per startup, e questa serie è il racconto di cosa succede dentro.

Prima di scrivere qualsiasi puntata leggi questi file e rispettali.

- `../voce-e-stile.md` — la voce del canale
- `voce-accelerator.md` — le regole di voce di questa serie
- `formato-puntate.md`
- `serie.md`

La scaletta delle puntate è in `Puntate.docx`, in questa cartella, e viene aggiornata spesso nel tempo. Va riletta ogni volta che si comincia una puntata nuova.

## Regole di lavoro

- Il file di una puntata contiene due sole sezioni: l'elenco dei blocchi con una riga ciascuno, e il testo da leggere davanti alla camera con i marker `CLIP:` al punto giusto.
- Niente tabelle, niente scheda tecnica, niente sezioni su titoli, miniature, ritenzione, packaging o motivazioni delle scelte fatte. Se quel ragionamento serve, si fa in chat.
- Concreto sempre. Le spiegazioni di cosa si sta facendo e perché non vanno nel file.
- Il blocco HYPE non si scrive come testo da leggere: si danno poche righe di consiglio sullo stile di editing e su cosa anticipare.
- Le indicazioni di editing dentro un blocco si scrivono come citazione, con `>` davanti. Non sono testo da leggere e nel `.docx` escono in corsivo grigio, staccate dal parlato.
- Le clip non stanno per forza dopo il testo: se aprono il blocco vanno messe prima del parlato, come nell'apertura della puntata 1 dove partono su musica prima che Federico dica la prima parola.
- Non si inventano mai numeri, cifre, date o fatti. Dove serve un dato vero e non c'è, si lascia un segnaposto `[DA RIEMPIRE: ...]`.

## Dove stanno le puntate

Ogni episodio ha la sua cartella qui dentro, `Episodio NN - Titolo`, e contiene il `.md` e il `.docx` con lo stesso nome. Si scrive nel `.md` e poi si genera il `.docx` con `.genera-docx.py`, che sta nella cartella principale del progetto.

I `.docx` vecchi rimasti in giro sono la prima stesura, superata dai `.md`. L'unico `.docx` ancora vivo è `Puntate.docx`, che è la scaletta.

## Attenzione al nome "video standard"

Dentro `formato-puntate.md` il format A si chiama "VIDEO STANDARD", ma è una cosa diversa dalla cartella `Video standard/` che sta nella cartella principale. Qui è un tipo di puntata della serie, là sono i video singoli sui tool AI. Non confonderli.
