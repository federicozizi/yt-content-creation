#!/usr/bin/env bash
# Pre-commit hook: prima di ogni commit, fai fare a Claude un review veloce
# del diff e blocca il commit se trova problemi gravi.
#
# Setup:
#   cp .github/hooks/pre-commit-claude-review.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

set -e

DIFF=$(git diff --cached)

if [ -z "$DIFF" ]; then
  exit 0
fi

# Lancia Claude in modalità non-interattiva con il diff
echo "🔍 Claude review in corso..."

REVIEW=$(claude --print "Review questo diff. Rispondi solo:
- 'OK' se il diff è pulito (no segreti hardcoded, no print di debug, no TODO non gestiti)
- 'BLOCCO: <motivo in 1 riga>' se vedi un problema serio.

Diff:
$DIFF")

if [[ "$REVIEW" == OK* ]]; then
  echo "✅ Claude review: OK"
  exit 0
else
  echo "❌ $REVIEW"
  echo ""
  echo "Per bypassare (a tuo rischio): git commit --no-verify"
  exit 1
fi
