# Pattern: git worktree to parallelize tasks with Claude Code

> ⚠️ Italian twin: `CONTENUTI/github-per-claude-code/materiali/docs/worktree-pattern.md` — keep both in sync.

## The problem

You have 3 open tasks for Claude Code (e.g. fix bug A, feature B, refactor C). If you launch them one after the other in the same folder, you go serial. If you launch them in parallel in the same folder, they step on each other (they modify the same files).

## The solution: git worktree

A worktree is a **lightweight copy of the repo on a different branch**, living in a subfolder. Each Claude Code works in its own worktree, without conflicts.

## How it works

### 1. Create the worktrees (one time only)

```bash
# From the repo root
git worktree add .worktrees/fix-bug-a -b fix/bug-a
git worktree add .worktrees/feature-b -b feat/feature-b
git worktree add .worktrees/refactor-c -b refactor/c
```

Result: 3 folders in `.worktrees/`, each on its own branch. The `main` branch stays untouched.

### 2. Launch 3 Claude Codes in parallel

Open 3 terminals (or 3 Claude Desktop windows). In each:

```bash
# Terminal 1
cd .worktrees/fix-bug-a
claude
> implement the fix described in issue #12
```

```bash
# Terminal 2
cd .worktrees/feature-b
claude
> implement the feature described in issue #15
```

```bash
# Terminal 3
cd .worktrees/refactor-c
claude
> refactor the auth module as described in issue #18
```

The 3 Claudes work **in parallel, without seeing each other**. Each has its own file system, its own branch, its own history.

### 3. When a task finishes → PR

```bash
cd .worktrees/fix-bug-a
git push origin fix/bug-a
gh pr create --fill
```

(Or let Claude do it: "when you're done, open a PR".)

### 4. Cleanup when the task is merged

```bash
git worktree remove .worktrees/fix-bug-a
git branch -d fix/bug-a
```

## When it makes sense to use it

✅ You have 2-5 independent tasks to do in parallel (intense workday)
✅ You want to keep `main` always clean while Claude experiments
✅ You want to compare 2 implementations of the same task (you launch 2 Claudes on 2 different worktrees, then compare)

❌ You have 1 simple task only — overkill
❌ The tasks touch the same files in a non-mergeable way — better to serialize

## Trick: controlled "discard"

You launch Claude on an uncertain task in a worktree. If the result doesn't convince you:

```bash
git worktree remove --force .worktrees/feature-b
git branch -D feat/feature-b
```

You threw everything away in 2 seconds without touching `main`. Reopen the worktree and relaunch with a different prompt.
