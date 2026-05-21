<!-- ⚠️ Italian twin: CONTENUTI/claude-code-e-antigravity/materiali/esempio-output.md -->

# What the result looks like after the workflow

Real example of how your site's folder looks before and after running the combined Antigravity → Claude Code workflow.

## Before

```
my-site/
├── index.html                  ← "old" home, tired-looking
├── about.html
├── contact.html
├── css/
│   └── style.css
├── img/
│   ├── hero.jpg
│   └── logo.svg
└── .git/
```

## During (after downloading artifacts from Antigravity)

```
my-site/
├── index.html                  ← still the old one, untouched
├── _from_antigravity/          ← temporary folder
│   ├── landing-winner.html     ← the version you chose
│   ├── landing-corporate.html  ← (optional) the discarded ones
│   └── landing-aggressive.html
├── about.html
├── contact.html
├── css/
├── img/
└── .git/
```

## After (Claude Code integrated and committed)

```
my-site/
├── index.html                  ← UPDATED: new design + old links/meta
├── _from_antigravity/
│   └── _archive/               ← the 3 variants moved here for history
│       ├── landing-winner-2026-05-18.html
│       ├── landing-corporate.html
│       └── landing-aggressive.html
├── about.html                  ← unchanged
├── contact.html                ← unchanged
├── css/                        ← unchanged (Claude didn't touch existing styles, the artifact was self-contained)
├── img/                        ← unchanged
└── .git/
```

## Sample diff Claude Code shows you before committing

```diff
diff --git a/index.html b/index.html
index a1b2c3d..e4f5g6h 100644
--- a/index.html
+++ b/index.html
@@ -1,15 +1,30 @@
 <!DOCTYPE html>
 <html lang="en">
 <head>
-  <title>Rossi Studio — business consulting</title>
+  <title>Rossi Studio — business consulting</title>   ← preserved
   <meta name="description" content="...">             ← preserved
+  <style>
+    /* new inline CSS from the artifact */
+    body { background: #fef9f3; font-family: 'Inter', system-ui; }
+    .hero { ... }
+    ...
+  </style>
 </head>
 <body>
-  <nav>
-    <a href="/about">About</a>
-    <a href="/services">Services</a>
-    <a href="/contact">Contact</a>
-  </nav>
+  <nav class="navbar-soft">
+    <a href="/about">About</a>          ← href preserved from old
+    <a href="/services">Services</a>    ← href preserved
+    <a href="/contact">Contact</a>      ← href preserved
+  </nav>
-  <section class="hero">
-    <h1>Rossi Studio — consulting experts</h1>
-    <p>30 years alongside companies.</p>
-    <a class="cta" href="/contact">Contact us</a>
-  </section>
+  <section class="hero-warm">
+    <h1>We help your business grow, no fluff.</h1>
+    <p>30 years of experience, shared one person at a time.</p>
+    <a class="cta-friendly" href="/contact">Let's start together →</a>
+  </section>
+
+  <section class="testimonial">                       ← new block added
+    <blockquote>...</blockquote>
+  </section>
 </body>
 </html>
```

## Decisions Claude Code flags before committing

> 📝 **Edge cases decided automatically:**
> - The Antigravity artifact imported `https://fonts.googleapis.com/css2?family=Inter` via CDN → I removed the import and replaced with `font-family: 'Inter', system-ui` (system fallback). See line 12.
> - The artifact referenced `img/hero-friendly.jpg` which doesn't exist in the repo → I kept the reference and I'm flagging it: **you need to add that file under `img/` before publishing**, or tell me to swap with the existing `hero.jpg`.
> - The artifact had a 5-item menu, the old had 3 → I preserved the 3 old ones with their real hrefs, and I added the 2 new ones ("Blog", "Case studies") with `href="#"`. You decide whether to add those pages or remove the items.
>
> **OK to commit?**

At this point you respond:
- `OK` → commit.
- `OK but swap hero-friendly.jpg with hero.jpg` → apply the fix, then commit.
- `Wait, drop Blog and Case studies from the menu` → apply, then show the diff again for final OK.

## Final commit message

```
feat: refresh home (friendly variant from Antigravity)

- new design and copy in friendly style, generated as Antigravity artifact
- preserved: meta tags, internal hrefs, semantic menu structure
- added blocks: section.testimonial
- pending: img/hero-friendly.jpg to add, menu items "Blog"/"Case studies" with href="#"
```
