# Example newsletter produced by the system

What you see below is a real example of how a file in `newsletter/YYYY-MM-DD.md` looks after a successful run. It's exactly what arrives on your desk every morning (or in your email inbox, if you've enabled the email option).

---

# 🧠 Your AI Brief — Friday May 16, 2026

## 3 updates today

### 🚀 Claude Sonnet 4.7 available in beta
- 15% performance increase on reasoning tasks compared to 4.6
- New "thinking" model activatable on demand (parameter `enable_extended_thinking`)
- Available immediately on API and Claude.ai for Pro and Max plans
- 🔗 https://www.anthropic.com/news/claude-sonnet-4-7

### 📄 Paper: "Constitutional AI v2"
- Update to the system of principles behind model training
- Focus on transparency of safety trade-offs (safety vs helpfulness)
- Introduces new open-source evaluation metrics
- 🔗 https://www.anthropic.com/research/constitutional-ai-v2

### 🔧 Claude Code 2.4.0 — new "Plan Mode"
- Mode that separates planning and execution of the task
- Particularly useful for complex multi-step tasks (refactoring, migrations)
- Activatable with Shift+Tab during a session
- 🔗 https://docs.claude.com/en/release-notes/claude-code

---
Generated in 47 seconds · 3 sources consulted · 3 new articles · 2 articles skipped (already seen in previous runs)

---

## Notes about this example

- **"Average" day**: 3 relevant articles. On slow days you can have 0-1 article. On busy days (big launches, conferences) you can have 8-10.
- **Total time**: ~30-60 seconds per run, depends on the number of sources and network speed.
- **Skipped articles**: the system does NOT tell you which it skipped (to not clutter the newsletter), only how many. If you want to see them, check `state.json` — the URLs added in the last run are all those processed, both included and skipped.

## How a "dead day" looks

If none of the sources have news in the last 48 hours:

```markdown
# 🧠 Your AI Brief — Saturday May 17, 2026

No relevant updates today. All 3 sources consulted haven't published anything new in the last 48 hours.

---
Generated in 12 seconds · 3 sources consulted
```

Synthetic and honest. No invented news to "fill".
