#!/usr/bin/env bash
# Verifica prerequisiti per il Metodo A (Claude Code Agent Teams)

set -e

echo "=== Verifica prerequisiti — Metodo A ==="
echo ""

# Node
if command -v node >/dev/null 2>&1; then
  NODE_V=$(node --version)
  echo "✅ Node $NODE_V"
else
  echo "❌ Node non trovato. Installalo da https://nodejs.org (versione LTS)."
  exit 1
fi

# Claude Code
if command -v claude >/dev/null 2>&1; then
  CLAUDE_V=$(claude --version 2>&1 | head -1)
  echo "✅ Claude Code: $CLAUDE_V"
else
  echo "❌ Claude Code CLI non trovato."
  echo "   Installalo con: npm install -g @anthropic-ai/claude-code"
  exit 1
fi

# .claude/settings.json
if [ -f ".claude/settings.json" ]; then
  echo "✅ .claude/settings.json presente"
else
  echo "❌ .claude/settings.json mancante (serve per attivare Agent Teams)"
  exit 1
fi

# competitors.json
if [ -f "competitors.json" ]; then
  echo "✅ competitors.json presente"
else
  echo "❌ competitors.json mancante"
  exit 1
fi

echo ""
echo "Tutto pronto. Lancia 'claude' e digita: \"esegui il prompt in daily-brief.md\""
