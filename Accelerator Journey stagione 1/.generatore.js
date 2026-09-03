const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, LevelFormat, convertInchesToTwip
} = require('docx');
const fs = require('fs');

const ACCENT = '1F4E5B';
const GREY = '6B6B6B';

function H1(t){ return new Paragraph({ text: t, heading: HeadingLevel.HEADING_1, spacing:{before:240, after:160} }); }
function H2(t){ return new Paragraph({ text: t, heading: HeadingLevel.HEADING_2, spacing:{before:280, after:120} }); }
function H3(t){ return new Paragraph({ text: t, heading: HeadingLevel.HEADING_3, spacing:{before:200, after:100} }); }
function P(t, opts={}){ return new Paragraph({ children:[new TextRun({ text:t, ...opts })], spacing:{after: opts.after||120} }); }
function Bold(t){ return P(t, {bold:true}); }
function Italic(t){ return P(t, {italics:true, color:GREY}); }
function Bullet(t, lvl=0){ return new Paragraph({ text:t, bullet:{level:lvl}, spacing:{after:80} }); }
function Spacer(){ return new Paragraph({ text:'', spacing:{after:120} }); }
function Rule(){ return new Paragraph({ text:'', border:{ bottom:{ color:'CCCCCC', style:BorderStyle.SINGLE, size:6, space:1 } }, spacing:{before:120, after:200} }); }

// Marker line inside script (e.g. [A CAMERA], [CLIP])
function Marker(t){
  return new Paragraph({ children:[new TextRun({ text:t, bold:true, color:ACCENT, size:19 })], spacing:{before:200, after:80} });
}
// Spoken line
function Line(t){
  return new Paragraph({ children:[new TextRun({ text:t, size:24 })], spacing:{after:140}, indent:{left:convertInchesToTwip(0.15)} });
}
function Note(t){
  return new Paragraph({ children:[new TextRun({ text:t, italics:true, color:GREY, size:19 })], spacing:{after:140} });
}

function cell(text, {bold=false, width, shade=null, size=20}={}){
  return new TableCell({
    width:{ size:width, type:WidthType.DXA },
    shading: shade ? { type:ShadingType.CLEAR, fill:shade } : undefined,
    margins:{ top:80, bottom:80, left:120, right:120 },
    children:[ new Paragraph({ children:[new TextRun({ text, bold, size })] }) ]
  });
}

function table(header, rows, widths){
  const total = widths.reduce((a,b)=>a+b,0);
  return new Table({
    width:{ size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader:true, children: header.map((h,i)=>cell(h,{bold:true,width:widths[i],shade:'EFF3F4'})) }),
      ...rows.map(r => new TableRow({ children: r.map((c,i)=>cell(c,{width:widths[i]})) }))
    ]
  });
}

const numbering = {
  config: [{
    reference: 'steps',
    levels: [{ level:0, format: LevelFormat.DECIMAL, text:'%1.', alignment: AlignmentType.START,
      style:{ paragraph:{ indent:{ left: convertInchesToTwip(0.4), hanging: convertInchesToTwip(0.22) } } } }]
  }]
};
function Step(t){ return new Paragraph({ text:t, numbering:{ reference:'steps', level:0 }, spacing:{after:100} }); }

function doc(children){
  return new Document({
    numbering,
    styles:{ default:{ document:{ run:{ font:'Calibri', size:22 } } },
      paragraphStyles:[
        { id:'Heading1', name:'Heading 1', basedOn:'Normal', next:'Normal', quickFormat:true,
          run:{ size:34, bold:true, color:ACCENT, font:'Calibri' } },
        { id:'Heading2', name:'Heading 2', basedOn:'Normal', next:'Normal', quickFormat:true,
          run:{ size:26, bold:true, color:ACCENT, font:'Calibri' } },
        { id:'Heading3', name:'Heading 3', basedOn:'Normal', next:'Normal', quickFormat:true,
          run:{ size:23, bold:true, color:'333333', font:'Calibri' } }
      ]},
    sections:[{ properties:{ page:{ margin:{ top:1200, bottom:1200, left:1200, right:1200 } } }, children }]
  });
}

/* ======================= DOC 1 — FORMATI ======================= */

const W = [1500, 3450, 3450];

const formati = [
  new Paragraph({ children:[new TextRun({ text:'ACCELERATOR JOURNEY — STAGIONE 1', bold:true, size:20, color:GREY })], spacing:{after:60} }),
  H1('I due format della serie'),
  Italic('Documento di riferimento. Serve per costruire qualsiasi puntata senza ripartire da zero.'),
  Rule(),

  H2('A cosa serve'),
  P('La serie alterna due format. Hanno la stessa progressione in 8 blocchi, quindi si possono alternare liberamente senza che lo spettatore perda il filo. Cambia solo cosa riempie i blocchi.'),
  Spacer(),

  H2('I due format'),
  H3('FORMATO A — RACCONTO'),
  P('Parlato, tu a camera, con qualche clip di appoggio. Serve per le puntate di svolta: decisioni, trattative, risultati, errori, momenti con Christian.'),
  Bullet('Durata: 7-12 minuti'),
  Bullet('Produzione: camera fissa + clip di repertorio girate durante la settimana'),
  Bullet('Quando usarlo: quando la puntata ha dentro una decisione o un esito'),
  Spacer(),
  H3('FORMATO B — CANTIERE'),
  P('Tecnico-pratico. Stessa progressione, ma con gli strumenti sullo schermo. Serve per le puntate in cui si costruisce o si ripara qualcosa.'),
  Bullet('Durata: 8-14 minuti'),
  Bullet('Produzione: cattura schermo + tu in un angolo o in stacco'),
  Bullet('Quando usarlo: quando la puntata ha dentro una scelta tecnica o una rottura'),
  Bullet('Regola sovraordinata: si mostra, non si istruisce (vedi "Il test della pausa")'),
  Rule(),

  H2('Gli 8 blocchi'),
  P('Sempre in questo ordine. Nessun blocco si salta. Se un blocco non ha contenuto quella settimana, la puntata non è pronta.'),
  Spacer(),
  table(
    ['Blocco', 'FORMATO A — Racconto', 'FORMATO B — Cantiere'],
    [
      ['1. GANCIO', 'Un\'affermazione che apre un debito. Non un\'introduzione: una cosa che obbliga a restare.', 'Il problema concreto della settimana, detto in una riga.'],
      ['2. IL PATTO', 'Cosa promette questa puntata e cosa NON promette.', 'Cosa stiamo costruendo e perché proprio adesso.'],
      ['3. LO SPECCHIO', 'I problemi di chi guarda. Obiettivo: "sta parlando di me".', 'Dove eravamo rimasti e cosa si è rotto.'],
      ['4. IL BIVIO INVISIBILE', 'La scelta ovvia che era sbagliata. Mostrata come fatto, mai come lezione.', 'Le due strade tecniche possibili e quella presa. Il perché, non il come.'],
      ['5. LA PROVA', 'Numeri, scene reali, registrazioni, la faccia di chi sbaglia.', 'Lo schermo vero mentre si ragiona. Mai una procedura seguibile.'],
      ['6. IL COSTO', 'Cosa è costato: soldi, tempo, errori. Sempre dichiarato.', 'Quante ore, quanto è costato, cosa non ha funzionato.'],
      ['7. LA PORTA', 'Dove si apre lo spazio per chi sa fare questa cosa. Constatazione, mai invito.', 'Idem. Nessuna frase promozionale.'],
      ['8. IL DEBITO', 'Cosa si vedrà nel prossimo episodio. Deve restare qualcosa in sospeso.', 'Idem.']
    ],
    W
  ),
  Spacer(),
  Note('I blocchi 4 e 6 sono quelli che convertono. Il 4 fa pensare "io l\'avrei sbagliato". Il 6 è la prova che non stai vendendo fumo. Se una puntata è debole, quasi sempre è perché mancano quei due.'),
  Rule(),

  H2('Regole trasversali'),

  H3('Il test della pausa'),
  P('Se uno spettatore mette in pausa e riesce a copiare quello che vede, sei passato dal racconto all\'istruzione. Se mette in pausa e non ha niente da copiare — ma ha capito perfettamente cosa è successo — sei nel posto giusto.'),
  Bullet('Sempre il perché, mai la procedura'),
  Bullet('Nessun passaggio numerato, nessuno schermo seguibile'),
  Bullet('La compressione è onesta: "questa cosa ci ha preso tre giorni, ve la faccio vedere in due minuti"'),
  Spacer(),

  H3('Cosa non si mostra mai'),
  Bullet('Da dove escono i lead di Christian'),
  Bullet('I prompt e le istruzioni di sistema'),
  Bullet('L\'architettura interna riusabile dell\'azienda'),
  Bullet('Termini commerciali oltre quello che il cliente autorizza'),
  Note('Il non detto va sempre motivato a favore di Christian o del cliente, mai a favore tuo. "Questo non ve lo faccio vedere perché è il vantaggio suo" legge come integrità. "Questo è il mio segreto" legge come scatola nera.'),
  Spacer(),

  H3('La nota emotiva'),
  P('Ogni puntata attraversa tre battute, in quest\'ordine:'),
  Bullet('RICONOSCIMENTO — lo spettatore si vede descritto'),
  Bullet('TENSIONE — qualcosa può andare male, e a volte va male'),
  Bullet('DIGNITÀ — si può governare. Mai euforia, mai promesse'),
  Bold('Regola d\'oro: si chiude sotto, non sopra.'),
  P('Il finale non è "ce la puoi fare". Il finale è "è più difficile di come sembrava, ma adesso lo vedi". Chi chiude in alto vende un biglietto. Noi selezioniamo chi vuole correre.'),
  Spacer(),

  H3('Stile'),
  table(
    ['', 'Fare', 'Non fare'],
    [
      ['Posizione', 'Da pari che ci sta passando adesso', 'Da cattedra, da esperto che insegna'],
      ['Tono', 'Asciutto, concreto, nessun entusiasmo forzato', 'Enfasi da lancio, voce da pubblicità'],
      ['Nemico', 'Sempre un meccanismo o una pratica', 'Mai una persona o un\'azienda con nome'],
      ['Parole', 'Cifre vere, tempi veri, nomi di cose vere', '"Semplice", "basta fare", "in pochi click"'],
      ['Promesse', 'Solo cose verificabili', 'Qualunque cifra di guadagno promessa'],
      ['Chiusura', 'Una domanda aperta o un problema irrisolto', 'Un riassunto di quello che si è detto']
    ],
    W
  ),
  Rule(),

  H2('Come si costruisce una puntata — 6 passi'),
  Step('Scegli il format: c\'è una decisione o un esito? Formato A. C\'è una costruzione o una rottura? Formato B.'),
  Step('Trova il BIVIO INVISIBILE della settimana. Se non c\'è, cerca ancora: c\'è sempre. Senza quello la puntata non converte.'),
  Step('Trova IL COSTO: una cifra, un numero di ore, un errore. Deve essere vero e deve costare dirlo.'),
  Step('Scrivi il GANCIO e il DEBITO. Sono le uniche due parti che vanno scritte alla lettera.'),
  Step('Elenca i punti di appoggio degli altri sei blocchi: cosa devi AVER DETTO, non come dirlo.'),
  Step('Fai la lista delle clip che ti servono e verifica di averle girate. Se manca la clip del blocco 5, la puntata si sposta.'),
  Spacer(),
  Note('Il titolo si scrive per ultimo e deve funzionare da solo, senza che lo spettatore sappia che esiste una serie. Mai "Episodio 4". Sempre una promessa che si capisce a freddo.'),
  Rule(),

  H2('Checklist prima di girare'),
  Bullet('Ho il gancio scritto alla lettera?'),
  Bullet('C\'è un bivio invisibile?'),
  Bullet('C\'è un costo dichiarato, con un numero?'),
  Bullet('Il blocco 7 è una constatazione e non un invito?'),
  Bullet('Resta qualcosa in sospeso alla fine?'),
  Bullet('Ho passato il test della pausa?'),
  Bullet('Il titolo funziona per chi non ha visto niente della serie?')
];

/* ======================= DOC 2 — EPISODIO 01 ======================= */

const W2 = [1900, 6500];

const ep1 = [
  new Paragraph({ children:[new TextRun({ text:'ACCELERATOR JOURNEY — STAGIONE 1 — EPISODIO 01', bold:true, size:20, color:GREY })], spacing:{after:60} }),
  H1('Introduzione — Si può davvero vendere l\'AI alle aziende?'),
  Italic('Formato A — Racconto. Video di apertura della serie. Doppio uso: episodio 1 del canale + versione ridotta per le sponsorizzate.'),
  Rule(),

  H2('Scheda'),
  table(
    ['', ''],
    [
      ['Formato', 'A — Racconto (parlato, con clip di appoggio)'],
      ['Durata', '8-10 minuti'],
      ['Obiettivo', 'Fissare la promessa della serie e far dire allo spettatore "sta parlando di me"'],
      ['Nota emotiva', 'Riconoscimento (dominante) → tensione → dignità'],
      ['Chiusura', 'Sotto: la domanda resta aperta, l\'esito non è garantito'],
      ['Titoli possibili', 'Si può davvero guadagnare vendendo AI alle aziende? Ci provo davanti a voi / Ho 26 anni e sto lanciando un business AI. Vi faccio vedere tutto, anche se va male'],
      ['Da girare', 'Camera fissa + 4 clip di appoggio (vedi struttura)']
    ],
    W2
  ),
  Rule(),

  H2('Struttura in 8 blocchi'),
  table(
    ['Blocco', 'Contenuto di questa puntata'],
    [
      ['1. GANCIO', 'Tutti parlano di AI, quasi nessuno ci guadagna. Io provo a scoprire se si può, davanti a voi.'],
      ['2. IL PATTO', 'Questa è la testimonianza di un tentativo. Errori, budget buttati, call andate male e clienti chiusi. Se va bene lo vedete, se va male anche.'],
      ['3. LO SPECCHIO', 'Le tre situazioni in cui lo spettatore si riconosce: il prototipo che non regge, l\'idea ferma da mesi, sa vendere ma non sa valutare la parte tecnica.'],
      ['4. IL BIVIO INVISIBILE', 'L\'errore che facevo anch\'io: partire dallo strumento invece che dalla domanda. La convergenza su customer care e PMI.'],
      ['5. LA PROVA', 'Il progetto vero: l\'agente WhatsApp per gli appuntamenti. Christian, il programma, Alessandro. Chi siamo e da dove parliamo.'],
      ['6. IL COSTO', 'Christian non ha mollato tutto: lavora, non è un tecnico, ci sta mettendo mesi. Nessuna scorciatoia raccontata come tale.'],
      ['7. LA PORTA', 'Il problema non è l\'informazione: è che nessuno ti dice se la strada è giusta mentre la stai prendendo.'],
      ['8. IL DEBITO', 'Il chatbot è solo la porta d\'ingresso. Cosa si vende davvero dopo: prossimo episodio.']
    ],
    W2
  ),
  Spacer(),
  H3('Clip di appoggio da girare'),
  Bullet('CLIP 1 — spezzoni di video/post AI hype (schermo, 4-5 secondi ciascuno) per il gancio'),
  Bullet('CLIP 2 — Christian in call o al lavoro, anche solo di spalle, presa dal materiale già girato'),
  Bullet('CLIP 3 — l\'agente WhatsApp in funzione: messaggio che arriva, risposta, appuntamento a calendario (20-30 secondi)'),
  Bullet('CLIP 4 — tu e Alessandro che lavorate, girato di sfuggita'),
  Rule(),

  H2('Script'),
  Note('Scritto per essere letto ad alta voce. Ogni riga è un respiro. I punti a capo sono pause. Le parti tra parentesi quadre sono indicazioni, non si leggono.'),
  Spacer(),

  Marker('[A CAMERA — primo piano, nessuna introduzione, si parte secco]'),
  Line('Ogni giorno esce un tool nuovo che dovrebbe cambiare tutto.'),
  Line('Ogni giorno c\'è qualcuno che ti spiega come costruire il tuo secondo cervello, la tua automazione, il tuo agente.'),
  Line('E ogni giorno un sacco di gente ci prova, e non ci guadagna niente.'),
  Marker('[CLIP 1 — montaggio rapido di titoli e miniature AI, 5-6 secondi]'),
  Line('Io sono un developer. Ho ventisei anni.'),
  Line('E la domanda che mi sono fatto è una sola.'),
  Line('Si possono vendere davvero dei sistemi di intelligenza artificiale alle aziende, che funzionino, e guadagnarci sopra?'),
  Line('Non lo so.'),
  Line('Sto per scoprirlo, e lo faccio davanti a voi.'),

  Marker('[A CAMERA — cambio di ritmo, più lento]'),
  Line('Questa serie è la testimonianza di un tentativo.'),
  Line('Non è un corso. Non è una vetrina. Non ci sono risultati garantiti.'),
  Line('Ci saranno gli errori. I soldi buttati. Le call andate male. I clienti che dicono di no.'),
  Line('E anche quelli che dicono di sì.'),
  Line('Metterò a nudo il percorso per intero: se va bene lo vedete, se va male lo vedete lo stesso.'),
  Line('Questo è il patto.'),

  Marker('[A CAMERA]'),
  Line('Perché la domanda vera non è quale tool usare.'),
  Line('Le domande vere sono tre.'),
  Line('La prima: si può vendere un sistema AI a un\'azienda vera, che le serva davvero, e camparci?'),
  Line('La seconda: quali problemi ti trovi davanti mentre lo fai?'),
  Line('La terza, che secondo me è la più interessante: cosa pensano davvero le aziende dell\'intelligenza artificiale, quando chiudi la porta e ci parli da solo?'),
  Line('Sono tre domande su cui online trovi mille risposte.'),
  Line('Quasi tutte scritte da gente che non ha mai firmato un contratto.'),

  Marker('[A CAMERA — qui si abbassa la voce, è la parte dello specchio]'),
  Line('Se stai guardando questo video, probabilmente ti riconosci in una di queste tre situazioni.'),
  Line('La prima: hai visto decine di video, hai aperto n8n, o Make, o un GPT personalizzato. Hai messo insieme qualcosa che funzionava.'),
  Line('Finché non l\'hai mostrato a qualcuno.'),
  Line('La seconda: hai un\'idea in testa da mesi e non sai da che parte si comincia. E ogni volta che ci pensi ti sembra che sia troppo tardi.'),
  Line('La terza, e questa è quella che vedo più spesso: tu sai vendere.'),
  Line('Sei bravo a parlare con la gente, non hai paura di chiamare, non ti fai problemi ad esporti.'),
  Line('Ma quando si scende sulla parte tecnica ti fermi. Non perché non capisci: perché non hai modo di sapere se quello che ti stanno dicendo è giusto o è fumo.'),
  Line('Ecco.'),
  Line('Io parto esattamente dal punto in cui quella roba lì smette di essere teoria e diventa un problema concreto.'),
  Line('Cioè quando qualcuno ti deve pagare.'),

  Marker('[A CAMERA]'),
  Line('Nei mesi scorsi ho valutato un sacco di strade.'),
  Line('Modelli di business diversi, workflow, sistemi, prodotti.'),
  Line('E ogni volta finivo nello stesso errore. Che poi è l\'errore che facciamo quasi tutti: partire dallo strumento.'),
  Line('Partire da "io so fare questa cosa, adesso trovo a chi venderla".'),
  Line('Non funziona.'),
  Line('O meglio: funziona benissimo, finché non devi mandare la prima fattura.'),
  Line('La verità è una sola, ed è pure noiosa.'),
  Line('Devi partire dalla domanda. Da quello che le aziende hanno già deciso che è un problema loro.'),
  Line('Quindi la domanda è cambiata. Non più "cosa so fare", ma: di cosa hanno davvero bisogno le piccole e medie imprese italiane?'),
  Line('E la risposta converge quasi sempre nello stesso punto.'),
  Line('Il rapporto con il cliente.'),
  Line('Rispondere in tempo. Fissare un appuntamento. Non perdere una richiesta. Non far aspettare nessuno. Non dimenticarsi di richiamare.'),
  Line('Gestione del cliente, e tempo.'),
  Line('Non è sexy, infatti non ne parla nessuno.'),
  Line('Ma è lì che le aziende perdono soldi tutti i giorni, e lo sanno.'),

  Marker('[A CAMERA → CLIP 3, l\'agente in funzione, mentre parli]'),
  Line('Da qui nasce il progetto che lanciamo in questa serie.'),
  Line('Un agente AI su WhatsApp che gestisce gli appuntamenti.'),
  Line('Il cliente scrive, l\'agente risponde, propone gli orari liberi, fissa, mette tutto a calendario.'),
  Line('Detta così sembra una cosa semplice. È semplice. E deve esserlo.'),
  Line('Perché quello non è il prodotto.'),
  Line('Quella è la porta d\'ingresso: è l\'MVP che ti fa entrare in azienda.'),
  Line('Quello che viene dopo — i servizi collegati, quello che puoi vendere una volta che sei dentro — è l\'argomento del prossimo episodio.'),

  Marker('[A CAMERA → CLIP 2, Christian]'),
  Line('E non lo faccio da solo.'),
  Line('Questa serie fa parte di un percorso che offriamo come azienda a chi vuole lanciare un progetto digitale.'),
  Line('Uno dei ragazzi che abbiamo seguito si chiama Christian Figoni. Oggi collabora attivamente con noi.'),
  Line('Christian lo vedrete per tutta la serie, e vedrete cose vere: le sue call, i suoi dubbi, le volte che sbaglia.'),
  Line('E voglio essere chiaro su chi è, perché in giro si raccontano un sacco di storie che non stanno in piedi.'),
  Line('Christian non ha mollato tutto per inseguire un sogno.'),
  Line('Ha un altro lavoro, come quasi tutti. Non è un tecnico, e non lo diventerà domani.'),
  Line('È un ragazzo sveglio, che sa parlare con le persone, che ha voglia di imparare, e che in questi mesi ci ha messo un impegno serio.'),
  Line('La divisione dei ruoli è chiara: la parte tecnica la mettiamo noi.'),
  Line('Lui costruisce valore dove è forte davvero, cioè sulla vendita e sul mercato.'),
  Line('E sulla parte più strettamente informatica c\'è il mio socio, Alessandro Miri, che vedrete spesso.'),
  Line('L\'obiettivo di Christian è diventare imprenditore di sé stesso.'),
  Line('E ci prova partendo da qui: vendendo questo chatbot.'),

  Marker('[A CAMERA — CLIP 4 di sfondo]'),
  Line('Due parole su di me, giusto per capire da dove parlo.'),
  Line('Mi chiamo Federico Zizi, ho ventisei anni.'),
  Line('Un mese fa ho lanciato la mia azienda, Zizi Group.'),
  Line('Facciamo consulenza e sviluppiamo sistemi informatici per le aziende, con un\'attenzione precisa: usare l\'AI dove serve davvero, non dove fa scena.'),
  Line('Sono anche CTO di Biorigeneral, con cui facciamo consulenza digitale in ambito sanitario.'),
  Line('Quindi sul piano tecnico non parto da zero.'),
  Line('Sul piano imprenditoriale sì. Questa è la mia avventura, e comincia adesso.'),

  Marker('[A CAMERA — più lento, è il punto in cui si apre la porta]'),
  Line('Una cosa la dico subito, così è chiara.'),
  Line('Io non credo che il problema di chi non riesce a lanciare un progetto sia l\'informazione.'),
  Line('I tutorial ci sono. I video ci sono. Le guide ci sono, e sono anche fatte bene.'),
  Line('Il problema è un altro.'),
  Line('È che nessuno ti dice se la strada che stai prendendo è quella giusta, mentre la stai prendendo.'),
  Line('Christian quella cosa lì ce l\'ha avuta.'),
  Line('Io ve la faccio vedere.'),

  Marker('[A CAMERA — chiusura]'),
  Line('Nel prossimo episodio entriamo nel merito.'),
  Line('Perché un chatbot per gli appuntamenti è solo l\'inizio, e cosa si vende davvero a un\'azienda una volta che ci sei entrato.'),
  Line('Se vuoi vedere come va a finire — bene o male — iscriviti, perché questa storia va avanti a episodi.'),
  Line('Ci vediamo lì.'),
  Rule(),

  H2('Le due frasi da sapere a memoria'),
  P('Sono gli unici due punti dove la formulazione esatta conta. Tutto il resto viene meglio se lo dici a modo tuo.'),
  Bold('Apertura: "Ogni giorno esce un tool nuovo che dovrebbe cambiare tutto. E ogni giorno un sacco di gente ci prova, e non ci guadagna niente."'),
  Bold('Chiusura del patto: "Se va bene lo vedete, se va male lo vedete lo stesso."'),
  Rule(),

  H2('Versione sponsorizzata — 60/90 secondi'),
  Note('Stessa voce, stesso montaggio. Serve solo a portare al video lungo e alla serie. Non vende niente.'),
  Spacer(),
  Marker('[A CAMERA]'),
  Line('Tutti parlano di intelligenza artificiale. Quasi nessuno ci sta guadagnando.'),
  Line('Io sono un developer, ho ventisei anni, e ho deciso di scoprire se si può davvero vendere l\'AI alle aziende e camparci.'),
  Line('Non ve lo racconto: ve lo faccio vedere.'),
  Marker('[CLIP 3 — l\'agente in funzione]'),
  Line('Stiamo lanciando un agente su WhatsApp che gestisce gli appuntamenti per le aziende.'),
  Line('Insieme a Christian, un ragazzo che abbiamo seguito e che oggi lavora con noi. Ha un altro lavoro, non è un tecnico, e ci sta provando sul serio.'),
  Marker('[A CAMERA]'),
  Line('Vedrete tutto: le call andate male, i soldi buttati, i clienti chiusi e quelli persi.'),
  Line('Se va bene lo vedete. Se va male lo vedete lo stesso.'),
  Line('È una serie, comincia dal primo episodio. Il link è qui sotto.'),
  Rule(),

  H2('Note di regia'),
  Bullet('Nessuna sigla, nessuna intro animata. Si parte dal parlato: i primi 15 secondi decidono tutto.'),
  Bullet('Luce ferma, camera fissa, nessun movimento. La produzione bassa funziona se il contenuto è denso.'),
  Bullet('Non nominare mai il prezzo del percorso, non dire mai "iscriviti al programma".'),
  Bullet('Il blocco su Christian va detto con calma: è il punto in cui lo spettatore decide se fidarsi.'),
  Bullet('Se una frase suona finta mentre la leggi, riscrivila a modo tuo. Lo script è un binario, non una gabbia.')
];

/* ======================= WRITE ======================= */

const base = 'C:/Users/zizif/Desktop/Youtube Fede Machine/Accelerator Journey stagione 1';
(async () => {
  fs.writeFileSync(base + '/Formati - Come si costruisce una puntata.docx', await Packer.toBuffer(doc(formati)));
  fs.writeFileSync(base + '/Episodio 01 - Introduzione/Episodio 01 - Introduzione.docx', await Packer.toBuffer(doc(ep1)));
  console.log('OK');
})();
