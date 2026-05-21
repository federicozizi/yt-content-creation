"""
Competitor Intel Team — Claude Agent SDK

Orchestra 4 sub-agent (3 watcher + 1 synthesizer) usando il Claude Agent SDK.
I sub-agent sono caricati automaticamente da `.claude/agents/*.md` (stessi file del Metodo A).

Cosa cambia rispetto al Metodo B:
- NIENTE asyncio.gather() scritto a mano: il parallelismo lo gestisce l'SDK
- NIENTE loop tool-use: l'SDK lo ha dentro
- NIENTE implementazione di WebFetch / Read / Write: tool built-in dell'SDK
- I 4 ruoli sono gli stessi .md del Metodo A, riusati senza riscriverli

Run:
    python team_agenti.py
"""

import asyncio
import json
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from pathlib import Path

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ResultMessage,
    query,
)
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).parent
BRIEFS_DIR = ROOT / "briefs"
BRIEFS_DIR.mkdir(exist_ok=True)


def load_competitors() -> str:
    return (ROOT / "competitors.json").read_text(encoding="utf-8")


def send_email(brief: str, today: str) -> None:
    user = os.getenv("GMAIL_USER")
    pwd = os.getenv("GMAIL_APP_PASSWORD")
    to = os.getenv("BRIEF_RECIPIENT")
    if not (user and pwd and to):
        print(f"[email] credenziali Gmail mancanti, salto invio")
        return

    msg = MIMEText(brief, "plain", "utf-8")
    msg["Subject"] = f"Brief competitor {today}"
    msg["From"] = user
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(user, pwd)
        s.send_message(msg)
    print(f"[email] inviata a {to} ✓")


async def run_team() -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    competitors = load_competitors()

    # Il prompt orchestratore: dichiarativo, non procedurale.
    # Diciamo COSA serve, non COME farlo. L'SDK + i sub-agent fanno il resto.
    orchestrator_prompt = f"""Sei l'orchestrator del team competitor-intel. Data di oggi: {today}.

Competitor da analizzare (JSON):
{competitors}

Procedura:
1. Lancia in PARALLELO i 3 watcher usando il tool Agent (un'unica risposta con 3 tool call insieme):
   - pricing-watcher
   - feature-watcher
   - social-watcher
   A ognuno passa la lista completa dei competitor.

2. Quando hai i 3 risultati, lancia il synthesizer (sempre via tool Agent) passandogli i 3 findings.

3. Il synthesizer scrive il brief in `briefs/{today}.md`. Verificalo con Read.

4. Quando il file esiste, restituisci come messaggio finale SOLO il contenuto del brief (markdown grezzo, senza commenti).

Niente narrazione superflua, niente riassunti tuoi: tu sei solo il coordinatore."""

    # I 4 sub-agent vengono caricati automaticamente da .claude/agents/*.md
    # grazie a setting_sources=["project"]. Stesso meccanismo del Claude Code CLI.
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "WebFetch", "WebSearch", "Bash", "Agent"],
        setting_sources=["project"],
        permission_mode="acceptEdits",
        cwd=str(ROOT),
    )

    print(f"[{datetime.now():%H:%M:%S}] orchestrator → start")

    final_brief = ""
    async for message in query(prompt=orchestrator_prompt, options=options):
        ts = datetime.now().strftime("%H:%M:%S")
        cls = type(message).__name__
        in_sub = bool(getattr(message, "parent_tool_use_id", None))
        prefix = "  subagent" if in_sub else "orchestrator"

        # Estrai un summary breve dal contenuto
        summary = ""
        content = getattr(message, "content", None)
        if isinstance(content, list):
            parts = []
            for block in content:
                btype = type(block).__name__
                if btype == "TextBlock":
                    txt = (getattr(block, "text", "") or "").strip().replace("\n", " ")
                    if txt:
                        parts.append(f"text: {txt[:120]}")
                elif btype == "ToolUseBlock":
                    name = getattr(block, "name", "?")
                    inp = getattr(block, "input", {}) or {}
                    hint = inp.get("subagent_type") or inp.get("url") or inp.get("file_path") or inp.get("command") or inp.get("description") or ""
                    parts.append(f"tool: {name}({str(hint)[:80]})")
                elif btype == "ToolResultBlock":
                    parts.append("tool_result")
            summary = " | ".join(parts)[:200]

        print(f"[{ts}] {prefix} → {cls} {summary}", flush=True)

        if isinstance(message, ResultMessage):
            final_brief = message.result or ""

    # Brief già scritto su file dal synthesizer; lo rileggiamo per essere sicuri
    brief_path = BRIEFS_DIR / f"{today}.md"
    if brief_path.exists():
        final_brief = brief_path.read_text(encoding="utf-8")
        print(f"[{datetime.now():%H:%M:%S}] briefs/{today}.md ✓")
    else:
        # fallback: salva il messaggio finale dell'orchestrator
        brief_path.write_text(final_brief, encoding="utf-8")
        print(f"[{datetime.now():%H:%M:%S}] briefs/{today}.md (fallback) ✓")

    send_email(final_brief, today)
    print(f"[{datetime.now():%H:%M:%S}] done.")


if __name__ == "__main__":
    asyncio.run(run_team())
