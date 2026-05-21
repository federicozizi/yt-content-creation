#!/usr/bin/env bash
# Pre-commit hook: before every commit, have Claude do a quick review
# of the diff and block the commit if it finds serious issues.
#
# Setup:
#   cp .github/hooks/pre-commit-claude-review.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

set -e

DIFF=$(git diff --cached)

if [ -z "$DIFF" ]; then
  exit 0
fi

# Launch Claude in non-interactive mode with the diff
echo "🔍 Claude review in progress..."

REVIEW=$(claude --print "Review this diff. Reply only:
- 'OK' if the diff is clean (no hardcoded secrets, no debug prints, no unhandled TODOs)
- 'BLOCK: <reason in 1 line>' if you see a serious problem.

Diff:
$DIFF")

if [[ "$REVIEW" == OK* ]]; then
  echo "✅ Claude review: OK"
  exit 0
else
  echo "❌ $REVIEW"
  echo ""
  echo "To bypass (at your risk): git commit --no-verify"
  exit 1
fi
