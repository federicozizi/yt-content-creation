"""
headroom_demo.py
================
Il cuore della demo. Fa UNA cosa, due volte:

  A) manda il pacchetto incidente a Claude Opus COSI' COM'E'  (senza Headroom)
  B) lo manda dopo averlo passato in Headroom                 (con Headroom)

e stampa la differenza di token (e di costo) tra le due chiamate.

Headroom comprime in locale, senza chiamare nessun modello: e' il
ContentRouter che riconosce il tipo di ogni pezzo (JSON, codice, testo) e lo
manda al compressore giusto. Qui sotto lo accendiamo con la compressione del
codice attiva, cosi' si vedono tutti e tre i tipi al lavoro.
"""

from __future__ import annotations

import os
import sys
import time

# Su Windows il terminale puo' essere cp1252: forziamo UTF-8 cosi' i log con
# accenti (le risposte di Opus) non crashano e non escono come "?".
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from dati_esempio import (
    CODICE_PYTHON,
    DOMANDA,
    EVENTI_JSON,
    RUNBOOK_TESTO,
    assembla,
    costruisci_pacchetto,
)

# --- Prezzi indicativi di Claude Opus (USD per 1 milione di token) -----------
# AGGIORNALI coi valori reali da https://openrouter.ai/models (cerca opus).
# Sono solo per mostrare il costo a schermo: i TOKEN invece sono quelli veri,
# restituiti dall'API.
PREZZO_INPUT_PER_MILIONE = 15.0
PREZZO_OUTPUT_PER_MILIONE = 75.0

MODELLO = "anthropic/claude-opus-4-8"
MODELLO_PER_CONTEGGIO = "claude-opus-4-8"


# ---------------------------------------------------------------------------
# 1) Compressione Headroom (locale, niente API)
# ---------------------------------------------------------------------------
def comprimi_con_headroom(domanda: str):
    """Comprime i tre pezzi dell'incidente, ognuno nella sua forma NATIVA.

    Questo e' il punto chiave: dando a Headroom il JSON come JSON (non incollato
    dentro un blocco di testo), il router lo riconosce e lo manda a SmartCrusher,
    che lo schiaccia del ~98%. Stessa cosa per testo (Kompress) e codice.

    Ritorna (pacchetto_compresso, dettagli) dove dettagli elenca, per ogni pezzo,
    quale compressore e' stato scelto e quanti token sono stati tagliati.
    """
    from headroom.transforms.content_router import ContentRouter, ContentRouterConfig

    # Config di default di Headroom (la stessa che usa in produzione):
    #  - JSON  -> SmartCrusher  (taglio fortissimo e SENZA perdere dati)
    #  - testo -> Kompress      (taglio forte; serve l'extra [ml] per il modello)
    #  - codice -> lasciato INTATTO di proposito: Headroom non rischia di
    #    rompere la logica del tuo codice. Per questo enable_code_aware resta off.
    config = ContentRouterConfig(
        enable_smart_crusher=True,
        enable_kompress=True,
        protect_analysis_context=False,  # non saltare nulla per via di "analizza"
    )
    router = ContentRouter(config=config)

    pezzi = [
        ("testo", RUNBOOK_TESTO),
        ("JSON", EVENTI_JSON),
        ("codice", CODICE_PYTHON),
    ]

    compressi: dict[str, str] = {}
    dettagli = []
    for nome, contenuto in pezzi:
        res = router.compress(contenuto, question=domanda)
        compressi[nome] = res.compressed
        dettagli.append(
            {
                "tipo": nome,
                "compressore": getattr(res.strategy_used, "value", str(res.strategy_used)),
                "token_prima": res.total_original_tokens,
                "token_dopo": res.total_compressed_tokens,
            }
        )

    pacchetto_compresso = assembla(
        compressi["testo"], compressi["JSON"], compressi["codice"]
    )
    return pacchetto_compresso, dettagli


# ---------------------------------------------------------------------------
# 2) Chiamata a Claude Opus via OpenRouter
# ---------------------------------------------------------------------------
def chiama_opus(client, contenuto_utente: str):
    """Manda system + un messaggio utente a Opus. Ritorna (risposta, usage)."""
    resp = client.chat.completions.create(
        model=MODELLO,
        max_tokens=400,
        messages=[
            {
                "role": "system",
                "content": "Sei un ingegnere SRE conciso. Rispondi in italiano, max 3 righe.",
            },
            {"role": "user", "content": contenuto_utente},
        ],
    )
    usage = resp.usage
    return resp.choices[0].message.content, usage


def _costo(input_tok: int, output_tok: int) -> float:
    return (
        input_tok / 1_000_000 * PREZZO_INPUT_PER_MILIONE
        + output_tok / 1_000_000 * PREZZO_OUTPUT_PER_MILIONE
    )


# ---------------------------------------------------------------------------
# 3) Il confronto completo (quello che chiama il pulsante)
# ---------------------------------------------------------------------------
def esegui_confronto(log=print) -> dict:
    """Esegue A (senza) e B (con) Headroom e ritorna un dizionario di risultati.

    `log` e' una funzione di stampa (default: print sul terminale). Cosi' gli
    stessi messaggi finiscono sia nel terminale sia, volendo, altrove.
    """
    pacchetto = costruisci_pacchetto()
    contenuto_grezzo = f"{DOMANDA}\n\n{pacchetto}"

    log("=" * 64)
    log("  HEADROOM - confronto: stessa domanda, stesso modello (Opus)")
    log("=" * 64)
    log(f"  Pacchetto incidente: {len(pacchetto):,} caratteri (testo + JSON + codice)")

    # --- Compressione locale con Headroom ---
    log("\n[1/3] Comprimo il pacchetto con Headroom (in locale, niente API)...")
    t0 = time.perf_counter()
    pacchetto_compresso, dettagli = comprimi_con_headroom(DOMANDA)
    ms = (time.perf_counter() - t0) * 1000
    contenuto_compresso = f"{DOMANDA}\n\n{pacchetto_compresso}"

    log(f"      fatto in {ms:.0f} ms. Cosa ha fatto, pezzo per pezzo:")
    for d in dettagli:
        risp = (
            0
            if d["token_prima"] == 0
            else (1 - d["token_dopo"] / d["token_prima"]) * 100
        )
        nota = "" if risp >= 1 else "   (lasciato intatto, per sicurezza)"
        log(
            f"        - {d['tipo']:<7} -> {d['compressore']:<14} "
            f"{d['token_prima']:>5} -> {d['token_dopo']:>5} token (-{risp:.0f}%){nota}"
        )
    log(
        f"      pacchetto: {len(pacchetto):,} -> {len(pacchetto_compresso):,} caratteri"
    )

    # --- Serve la chiave? Se manca, mostriamo solo la compressione locale. ---
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        log(
            "\n[!] Nessuna OPENROUTER_API_KEY: salto le chiamate a Opus e mostro "
            "solo la compressione locale.\n    (Crea il file .env dall'esempio per "
            "vedere anche i token reali fatturati.)"
        )
        log("=" * 64)
        return {
            "ok": True,
            "con_api": False,
            "dettagli_compressione": dettagli,
            "caratteri_prima": len(pacchetto),
            "caratteri_dopo": len(pacchetto_compresso),
        }

    from openai import OpenAI

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    # --- A) SENZA Headroom ---
    log("\n[2/3] Mando a Claude Opus il pacchetto INTERO (senza Headroom)...")
    risposta_senza, u_senza = chiama_opus(client, contenuto_grezzo)
    in_senza, out_senza = u_senza.prompt_tokens, u_senza.completion_tokens
    log(f"      input: {in_senza:>6} token | output: {out_senza:>5} token")
    log(f"      risposta di Opus: {risposta_senza.strip()[:200]}")

    # --- B) CON Headroom ---
    log("\n[3/3] Mando a Claude Opus il pacchetto COMPRESSO (con Headroom)...")
    risposta_con, u_con = chiama_opus(client, contenuto_compresso)
    in_con, out_con = u_con.prompt_tokens, u_con.completion_tokens
    log(f"      input: {in_con:>6} token | output: {out_con:>5} token")
    log(f"      risposta di Opus: {risposta_con.strip()[:200]}")

    # --- Conti ---
    risp_in = 0 if in_senza == 0 else (1 - in_con / in_senza) * 100
    costo_senza = _costo(in_senza, out_senza)
    costo_con = _costo(in_con, out_con)
    risparmio_pct = 0 if costo_senza == 0 else (1 - costo_con / costo_senza) * 100

    log("\n" + "-" * 64)
    log("  RISULTATO — la differenza di token (e di costo)")
    log("-" * 64)
    log(f"  {'':<22}{'SENZA':>12}{'CON':>12}{'risparmio':>14}")
    log(
        f"  {'token in input':<22}{in_senza:>12,}{in_con:>12,}"
        f"{('-' + format(risp_in, '.0f') + '%'):>14}"
    )
    log(f"  {'token in output':<22}{out_senza:>12,}{out_con:>12,}{'':>14}")
    log(
        f"  {'costo stimato (USD)':<22}{('$' + format(costo_senza, '.4f')):>12}"
        f"{('$' + format(costo_con, '.4f')):>12}"
        f"{('-' + format(risparmio_pct, '.0f') + '%'):>14}"
    )
    log("-" * 64)
    log(
        f"  Stesso modello, stessa domanda, stessa risposta: "
        f"{risp_in:.0f}% di token in input in meno."
    )
    log("=" * 64)

    return {
        "ok": True,
        "con_api": True,
        "dettagli_compressione": dettagli,
        "caratteri_prima": len(pacchetto),
        "caratteri_dopo": len(pacchetto_compresso),
        "input_senza": in_senza,
        "input_con": in_con,
        "output_senza": out_senza,
        "output_con": out_con,
        "risparmio_input_pct": round(risp_in, 1),
        "costo_senza": round(costo_senza, 4),
        "costo_con": round(costo_con, 4),
        "risparmio_costo_pct": round(risparmio_pct, 1),
        "risposta_senza": risposta_senza.strip(),
        "risposta_con": risposta_con.strip(),
    }


if __name__ == "__main__":
    esegui_confronto()
