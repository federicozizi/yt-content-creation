# Example newsletter produced by `newsletter.py` (Variant 2)

Output identical to the 2 previous methods — that's the point: only the how changes.

---

# 🧠 Your AI Brief — Friday May 16, 2026

## 3 updates today

### 🚀 Claude Sonnet 4.7 available in beta
- 15% performance increase on reasoning tasks
- New "thinking" model activatable on demand
- Available immediately on API and Claude.ai for Pro and Max plans
- 🔗 https://www.anthropic.com/news/claude-sonnet-4-7

### 📄 Paper: "Constitutional AI v2"
- Update to the system of principles behind training
- Focus on transparency of safety trade-offs
- 🔗 https://www.anthropic.com/research/constitutional-ai-v2

### 🆕 [HN] Show HN: lightweight RSS aggregator in Rust
- Open-source alternative to Feedly, ~5MB binary
- Self-hosted, supports sync via WebDAV
- 🔗 https://news.ycombinator.com/item?id=12345678

---

## `python newsletter.py` console output

```
🚀 Starting newsletter for 2026-05-16
📖 Anthropic News...
📖 Anthropic Research...
📖 Hacker News front page...

✅ Newsletter generated: newsletter/2026-05-16.md
   - 3 sources consulted
   - 8 articles read
   - 3 articles included
   - 5 articles skipped
   - 38.2 seconds total
```

Note: 38 seconds total — faster than Variant 1 because there's no agent loop. The script controls every step explicitly.
