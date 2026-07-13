"""
app.py
======
Mini server web. Serve la pagina (index.html) e, quando premi il pulsante,
esegue il confronto "con vs senza Headroom" e ti restituisce i numeri.

I log dettagliati escono SUL TERMINALE dove hai lanciato questo file: e' li'
che vedi, riga per riga, cosa fa Headroom e la differenza di token.

Avvio:
    python app.py
poi apri http://localhost:8000 nel browser.
"""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from flask import Flask, jsonify, send_from_directory

# Su Windows il terminale puo' essere in cp1252: forziamo UTF-8 cosi' i log
# (che possono contenere accenti dalle risposte di Opus) non crashano.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

load_dotenv()  # legge la chiave dal file .env, se c'e'

from headroom_demo import esegui_confronto

app = Flask(__name__)
QUI = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def home():
    return send_from_directory(QUI, "index.html")


@app.post("/api/confronto")
def confronto():
    # Raccogliamo i log riga per riga: vanno SIA sul terminale SIA nella pagina.
    righe: list[str] = []

    def log(msg: str = "") -> None:
        print(msg)            # terminale
        righe.append(msg)     # pagina/console del browser

    try:
        risultato = esegui_confronto(log=log)
    except Exception as e:  # noqa: BLE001 — vogliamo mostrare l'errore a schermo
        import traceback

        traceback.print_exc()
        return jsonify({"ok": False, "errore": str(e), "log": righe}), 500

    risultato["log"] = righe
    return jsonify(risultato)


if __name__ == "__main__":
    print("\n  Apri  http://localhost:8000  nel browser.")
    print("  I log del confronto appariranno qui sotto.\n")
    app.run(host="127.0.0.1", port=8000, debug=False)
