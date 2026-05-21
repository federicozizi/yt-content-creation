# Pattern: git worktree per parallelizzare task con Claude Code

## Il problema

Hai 3 task aperti per Claude Code (es. fix bug A, feature B, refactor C). Se li lanci uno dopo l'altro nella stessa cartella, vai serializzato. Se li lanci in parallelo nella stessa cartella, si pestano i piedi (modificano gli stessi file).

## La soluzione: git worktree

Un worktree è una **copia leggera del repo su un branch diverso**, che vive in una sottocartella. Ogni Claude Code lavora nel suo worktree, senza conflitti.

## Come funziona

### 1. Crea i worktree (una volta sola)

```bash
# Dal root del repo
git worktree add .worktrees/fix-bug-a -b fix/bug-a
git worktree add .worktrees/feature-b -b feat/feature-b
git worktree add .worktrees/refactor-c -b refactor/c
```

Risultato: 3 cartelle in `.worktrees/`, ognuna su un suo branch. Il branch `main` resta intoccato.

### 2. Lancia 3 Claude Code in parallelo

Apri 3 terminali (o 3 finestre Claude Desktop). In ognuno:

```bash
# Terminale 1
cd .worktrees/fix-bug-a
claude
> implementa il fix descritto nell'issue #12
```

```bash
# Terminale 2
cd .worktrees/feature-b
claude
> implementa la feature descritta nell'issue #15
```

```bash
# Terminale 3
cd .worktrees/refactor-c
claude
> refactora il modulo auth come descritto nell'issue #18
```

I 3 Claude lavorano **in parallelo, senza vedersi**. Ognuno ha il suo file system, il suo branch, il suo storico.

### 3. Quando un task finisce → PR

```bash
cd .worktrees/fix-bug-a
git push origin fix/bug-a
gh pr create --fill
```

(Oppure lascia che Claude lo faccia: "quando hai finito, apri una PR".)

### 4. Cleanup quando il task è mergiato

```bash
git worktree remove .worktrees/fix-bug-a
git branch -d fix/bug-a
```

## Quando ha senso usarlo

✅ Hai 2-5 task indipendenti da fare in parallelo (giornata di lavoro intensivo)
✅ Vuoi tenere `main` sempre pulito mentre Claude sperimenta
✅ Vuoi confrontare 2 implementazioni dello stesso task (lanci 2 Claude su 2 worktree diversi, poi confronti)

❌ Hai 1 solo task semplice — esagerato
❌ I task toccano gli stessi file in modo non-mergeable — meglio serializzare

## Trucchetto: lo "scarto" controllato

Lanci Claude su un task incerto in un worktree. Se il risultato non ti piace:

```bash
git worktree remove --force .worktrees/feature-b
git branch -D feat/feature-b
```

Hai buttato via tutto in 2 secondi senza toccare `main`. Riapri il worktree e rilanci con un prompt diverso.
