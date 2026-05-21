"""
Newsletter AI personale — Variante 1 (Claude Agent SDK)

Visita le fonti in fonti.json, identifica articoli nuovi (rispetto a state.json),
li riassume in newsletter/YYYY-MM-DD.md seguendo le regole di CLAUDE.md,
aggiorna state.json.

Uso:
    python newsletter.py

Schedulazione: vedi scheduling/crontab-example.txt
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

try:
    from claude_agent_sdk import Agent
except ImportError:
    print("❌ Manca claude-agent-sdk. Installa con: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).parent
NEWSLETTER_DIR = ROOT / "newsletter"


def main() -> int:
    load_dotenv(ROOT / ".env")

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key or "XXXX" in api_key:
        print("❌ ANTHROPIC_API_KEY non configurata in .env", file=sys.stderr)
        return 1

    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-7")

    fonti = json.loads((ROOT / "fonti.json").read_text(encoding="utf-8"))
    state = json.loads((ROOT / "state.json").read_text(encoding="utf-8"))
    tono = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")

    NEWSLETTER_DIR.mkdir(exist_ok=True)
    oggi = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_path = NEWSLETTER_DIR / f"{oggi}.md"

    system = (
        "Sei un assistente che genera newsletter giornaliere personali su un argomento di interesse.\n"
        "Hai accesso al tool web_fetch per leggere pagine web.\n"
        "Segui SEMPRE le regole di tono e formato qui sotto.\n\n"
        f"{tono}"
    )

    prompt = f"""Genera la newsletter di oggi ({oggi}).

FONTI DA VISITARE (in parallelo):
{json.dumps(fonti, ensure_ascii=False, indent=2)}

ARTICOLI GIA' VISTI (non riproporli):
{json.dumps(state.get("articoli_visti", []), ensure_ascii=False, indent=2)}

ISTRUZIONI:
1. Per ogni fonte, leggi la pagina con web_fetch e estrai gli articoli pubblicati nelle ultime 48 ore.
2. Filtra: tieni solo articoli NON gia' visti.
3. Per ogni articolo nuovo, leggi il contenuto completo (web_fetch della URL piena) e riassumi seguendo CLAUDE.md.
4. Componi il file newsletter seguendo la struttura in CLAUDE.md (header, sezione per articolo con emoji, link finale).
5. Salva il risultato esattamente in: {output_path.as_posix()}
6. Rispondi con un riassunto strutturato (JSON) di cosa hai fatto:
   {{
     "articoli_processati": ["url1", "url2"],
     "articoli_inclusi": N,
     "articoli_scartati": M,
     "tempo_secondi": T
   }}
"""

    print(f"🚀 Avvio newsletter per {oggi} (modello: {model})")
    inizio = time.time()

    agent = Agent(
        model=model,
        system=system,
        tools=["web_fetch", "file_write"],
        api_key=api_key,
    )

    result = agent.run(prompt)
    durata = time.time() - inizio

    # Aggiorna state con gli URL processati
    try:
        riassunto = json.loads(result.text) if hasattr(result, "text") else {}
    except json.JSONDecodeError:
        riassunto = {}

    nuovi_url = riassunto.get("articoli_processati", [])
    state["articoli_visti"] = list({*state.get("articoli_visti", []), *nuovi_url})
    state["ultimo_run"] = datetime.now(timezone.utc).isoformat()
    (ROOT / "state.json").write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"✅ Newsletter generata: {output_path}")
    print(f"   - {riassunto.get('articoli_inclusi', '?')} articoli inclusi")
    print(f"   - {riassunto.get('articoli_scartati', '?')} articoli scartati")
    print(f"   - {durata:.1f} secondi totali")

    return 0


if __name__ == "__main__":
    sys.exit(main())
