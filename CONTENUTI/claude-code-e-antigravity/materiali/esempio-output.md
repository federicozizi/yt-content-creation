<!-- ⚠️ Gemello inglese: CONTENUTI/claude-code-and-antigravity/materiali/esempio-output.md -->

# Come si presenta il risultato dopo il workflow

Esempio reale di come la cartella del tuo sito appare prima e dopo aver eseguito il workflow combinato Antigravity → Claude Code.

## Prima

```
mio-sito/
├── index.html                  ← home "vecchia", stanca
├── about.html
├── contatti.html
├── css/
│   └── style.css
├── img/
│   ├── hero.jpg
│   └── logo.svg
└── .git/
```

## Durante (dopo aver scaricato gli artefatti da Antigravity)

```
mio-sito/
├── index.html                  ← ancora la vecchia, non toccata
├── _da_antigravity/            ← cartella temporanea
│   ├── landing-vincitrice.html ← la versione che hai scelto
│   ├── landing-corporate.html  ← (opzionale) le scartate
│   └── landing-aggressive.html
├── about.html
├── contatti.html
├── css/
├── img/
└── .git/
```

## Dopo (Claude Code ha integrato e committato)

```
mio-sito/
├── index.html                  ← AGGIORNATA: design nuovo + link/meta del vecchio
├── _da_antigravity/
│   └── _archivio/              ← le 3 varianti spostate qui per storico
│       ├── landing-vincitrice-2026-05-18.html
│       ├── landing-corporate.html
│       └── landing-aggressive.html
├── about.html                  ← invariato
├── contatti.html               ← invariato
├── css/                        ← invariato (Claude non ha toccato lo style esistente, l'artefatto era self-contained)
├── img/                        ← invariato
└── .git/
```

## Esempio di diff che Claude Code ti mostra prima del commit

```diff
diff --git a/index.html b/index.html
index a1b2c3d..e4f5g6h 100644
--- a/index.html
+++ b/index.html
@@ -1,15 +1,30 @@
 <!DOCTYPE html>
 <html lang="it">
 <head>
-  <title>Studio Rossi — consulenza aziendale</title>
+  <title>Studio Rossi — consulenza aziendale</title>   ← preservato
   <meta name="description" content="...">             ← preservato
+  <style>
+    /* nuovo CSS inline dell'artefatto */
+    body { background: #fef9f3; font-family: 'Inter', system-ui; }
+    .hero { ... }
+    ...
+  </style>
 </head>
 <body>
-  <nav>
-    <a href="/chi-siamo">Chi siamo</a>
-    <a href="/servizi">Servizi</a>
-    <a href="/contatti">Contatti</a>
-  </nav>
+  <nav class="navbar-soft">
+    <a href="/chi-siamo">Chi siamo</a>      ← href preservato dal vecchio
+    <a href="/servizi">Servizi</a>          ← href preservato
+    <a href="/contatti">Contatti</a>        ← href preservato
+  </nav>
-  <section class="hero">
-    <h1>Studio Rossi — esperti in consulenza</h1>
-    <p>Da 30 anni al fianco delle imprese.</p>
-    <a class="cta" href="/contatti">Contattaci</a>
-  </section>
+  <section class="hero-warm">
+    <h1>Ti aiutiamo a far crescere la tua impresa, senza giri di parole.</h1>
+    <p>30 anni di esperienza, condivisa una persona alla volta.</p>
+    <a class="cta-amichevole" href="/contatti">Iniziamo insieme →</a>
+  </section>
+
+  <section class="testimonial">                       ← nuovo blocco aggiunto
+    <blockquote>...</blockquote>
+  </section>
 </body>
 </html>
```

## Decisioni che Claude Code ti segnala prima di committare

> 📝 **Casi border decisi automaticamente:**
> - L'artefatto Antigravity importava `https://fonts.googleapis.com/css2?family=Inter` via CDN → ho rimosso l'import e sostituito con `font-family: 'Inter', system-ui` (fallback di sistema). Vedi riga 12.
> - L'artefatto referenziava `img/hero-friendly.jpg` che non esiste nel repo → ho lasciato il riferimento e lo segnalo: **devi aggiungere quel file in `img/` prima di pubblicare**, oppure dimmi di sostituirlo con `hero.jpg` esistente.
> - L'artefatto aveva un menu con 5 voci, il vecchio aveva 3 → ho preservato le 3 del vecchio con i loro href reali, e ho aggiunto le 2 nuove ("Blog", "Casi studio") con `href="#"`. Decidi tu se aggiungere queste pagine o rimuoverle.
>
> **OK al commit?**

A questo punto rispondi:
- `OK` → committa.
- `OK ma sostituisci hero-friendly.jpg con hero.jpg` → applica la correzione, poi committa.
- `Aspetta, rimuovi Blog e Casi studio dal menu` → applica, poi mostra di nuovo il diff per OK finale.

## Commit message finale

```
feat: refresh home (variante amichevole da Antigravity)

- nuovo design e copy in stile amichevole, generato come artefatto Antigravity
- preservati: meta tag, href interni, struttura semantica del menu
- aggiunti blocchi: section.testimonial
- pending: img/hero-friendly.jpg da aggiungere, voci menu "Blog"/"Casi studio" con href="#"
```
