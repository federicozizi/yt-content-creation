<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-and-antigravity/materiali/prompts/claude-code-handoff.md -->

# Prompt per Claude Code — handoff dall'artefatto Antigravity

Questo prompt si usa **in locale**, lanciando `claude` dentro la cartella del tuo sito reale (non dentro la cartella materiali del video).

## Quando usarlo

Dopo che hai:
1. Generato 3 varianti in Antigravity (con il prompt `antigravity-parallel-draft.md`).
2. Scelto la migliore.
3. Scaricato l'artefatto come `_da_antigravity/landing-vincitrice.html` nella cartella del tuo sito.

## Setup

```
# 1. Vai nella cartella del tuo sito
cd ~/percorso/al/tuo-sito

# 2. Verifica che ci siano:
#    - index.html (la home attuale)
#    - _da_antigravity/landing-vincitrice.html (l'artefatto scelto)

# 3. Lancia Claude Code
claude
```

## PROMPT da incollare

```
Devo integrare un artefatto di Antigravity nel mio sito reale. Procedi così:

CONTESTO:
- Il file index.html in questa cartella è la home attuale del mio sito (con i miei link interni, meta tag, asset, eventuali script di tracking).
- Il file _da_antigravity/landing-vincitrice.html è la nuova home generata da un agente Antigravity in cloud. È bella graficamente ma è scollegata dal mio progetto: usa link inventati, magari ha rinominato file, non conosce i miei meta tag.

OBIETTIVO:
Produrre un NUOVO index.html che prende il design e il copy dell'artefatto, ma rispetta TUTTO il contesto del sito reale.

REGOLE DI FUSIONE:

1. Dal nuovo (landing-vincitrice.html) prendi:
   - Struttura visiva, palette, tipografia
   - Copy delle sezioni (headline, sottotitoli, paragrafi, claim)
   - Eventuali nuovi blocchi semantici (es. una sezione "testimonial" se prima non c'era)

2. Dal vecchio (index.html) preservi SEMPRE:
   - Tutti i link interni con href reale (es. "/about", "/servizi/consulenza", "/contatti")
     → se l'artefatto ha href="#" o href inventati per le stesse label, sostituiscili con quelli del vecchio
   - I meta tag in <head>: title, description, OpenGraph, Twitter card, canonical
   - I percorsi degli asset esistenti (immagini, css esterni, favicon) — se l'artefatto referenzia asset che non esistono nel mio repo, segnalalo e proponi una di queste opzioni:
     (a) sostituire con un asset esistente equivalente
     (b) tenere il riferimento e dirmi quale file devo aggiungere
   - Script di tracking, analytics, pixel, tag manager
   - L'attributo lang dell'elemento <html>

3. Casi border:
   - Se nel nuovo c'è un menu che ha 5 voci e nel vecchio ne aveva 3, conserva le 3 del vecchio (con i loro href) e aggiungi le 2 nuove con href="#" segnalandomele.
   - Se il nuovo importa Google Fonts via CDN, RIMUOVI quell'import (regola del progetto: niente CDN esterni) e sostituisci con font di sistema simili.

PROCESSO:
1. Leggi entrambi i file.
2. Costruisci il merge in un blocco markdown — NON sovrascrivere ancora index.html.
3. Mostrami:
   (a) il diff sintetico (cosa cambia rispetto a index.html attuale)
   (b) la lista delle decisioni che hai preso sui casi border (link sostituiti, asset segnalati, ecc.)
4. Aspetta il mio OK esplicito.
5. Dopo l'OK:
   - Sovrascrivi index.html con la versione mergiata
   - Se questa cartella è un repo git, fai un commit con messaggio: `feat: refresh home (variante <stile> da Antigravity)`
   - Sposta _da_antigravity/landing-vincitrice.html in _da_antigravity/_archivio/ rinominandolo con la data (es. landing-vincitrice-2026-05-18.html)
   - Se nella cartella _da_antigravity/ ci sono altre varianti scartate (es. landing-corporate.html, landing-aggressive.html), spostale anche loro in _archivio/

Procedi.
```

## Cosa aspettarsi

- Claude Code legge i due file, produce il diff: tipicamente 2-5 minuti se il sito è semplice (una home da ~300 righe).
- Il diff include sia le modifiche al codice sia le decisioni di "casi border" (link sostituiti, asset segnalati).
- Tu approvi (o chiedi correzioni mirate prima di approvare).
- Il commit finale è pulito, un solo cambiamento atomico.

## Se qualcosa va storto

- "L'artefatto importa Google Fonts e Claude lo ha rimosso, ora i font sono brutti" → digli: "rimettilo come fallback, ma usa font-family system-ui in primo, Inter in secondo".
- "Ha sostituito un link interno che non doveva sostituire" → segnalagli il link specifico e digli: "ripristina /about-noi originale, lascia /chi-siamo solo se compare nel nuovo come label diversa".
- "Vorrei vedere il diff in modo più visuale" → digli: "mostralo come `git diff --color`".
