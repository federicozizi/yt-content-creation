"""
Agente AI per le comunicazioni interne su Telegram.
Serie "Agenti AI per aziende veri, zero fuffa" - Episodio 1.

Cosa fa questo agente:
  1. Risponde alle domande dei dipendenti usando SOLO il "manuale aziendale"
     contenuto in azienda_knowledge.md.
  2. Quando un dipendente chiede ferie, segnala un'assenza o un problema IT,
     usa lo strumento `registra_richiesta` per protocollare la richiesta in un
     file (richieste.log). E' questo strumento - "le mani dell'agente" - che lo
     rende un AGENTE vero e non un semplice chatbot.

Prima di lanciarlo:
  - copia .env.example in .env e compila ANTHROPIC_API_KEY e TELEGRAM_BOT_TOKEN
  - pip install -r requirements.txt
  - python agente_telegram.py
"""

import os
import json
from pathlib import Path

from dotenv import load_dotenv

import anthropic
from anthropic import beta_tool

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

# Carica le credenziali dal file .env (ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN)
load_dotenv()

# Il client legge automaticamente ANTHROPIC_API_KEY dall'ambiente.
client = anthropic.Anthropic()

# Il "manuale aziendale": la conoscenza da cui l'agente attinge per rispondere.
CONOSCENZA = Path("azienda_knowledge.md").read_text(encoding="utf-8")

# Il registro dove finiscono le richieste protocollate.
REGISTRO = Path("richieste.log")


# --- LO STRUMENTO: le "mani" dell'agente ---------------------------------
# Il decoratore @beta_tool trasforma questa normale funzione Python in uno
# strumento che Claude puo' decidere di usare da solo. La docstring qui sotto
# NON e' un commento qualsiasi: e' la spiegazione che Claude legge per capire
# quando e come usare lo strumento. Scrivila chiara.
@beta_tool
def registra_richiesta(tipo: str, dipendente: str, dettaglio: str) -> str:
    """Protocolla una richiesta interna di un dipendente.

    Usa questo strumento quando un dipendente chiede ferie/permessi, segnala
    un'assenza, o segnala un problema informatico.

    Args:
        tipo: categoria della richiesta. Uno tra: "ferie", "assenza", "IT", "altro".
        dipendente: nome del dipendente che fa la richiesta.
        dettaglio: descrizione libera (date, motivo, dispositivo, ecc.).
    """
    riga = {"tipo": tipo, "dipendente": dipendente, "dettaglio": dettaglio}
    with REGISTRO.open("a", encoding="utf-8") as f:
        f.write(json.dumps(riga, ensure_ascii=False) + "\n")
    return f"Richiesta '{tipo}' registrata correttamente per {dipendente}."


# --- LE ISTRUZIONI: chi e' l'agente e come si comporta -------------------
SYSTEM = f"""Sei l'assistente interno dell'azienda. Parli in italiano, in modo
breve, chiaro e cordiale. Rispondi alle domande dei dipendenti usando SOLO le
informazioni del manuale aziendale qui sotto.

Regole:
- Se la richiesta riguarda ferie, permessi, assenze o problemi informatici,
  usa lo strumento registra_richiesta per protocollarla, poi conferma al dipendente.
- Se non trovi la risposta nel manuale, dillo onestamente e indica a chi rivolgersi.
- Non inventare politiche o numeri che non sono nel manuale.

== MANUALE AZIENDALE ==
{CONOSCENZA}
"""


# --- IL PONTE CON TELEGRAM -----------------------------------------------
async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    testo = update.message.text
    nome = update.effective_user.first_name or "collega"

    # Il tool runner e' il vero "ciclo dell'agente": Claude legge il messaggio,
    # se serve chiama da solo lo strumento, riceve il risultato e continua,
    # finche' non ha una risposta finale. Tutto questo senza che noi scriviamo
    # il loop a mano.
    runner = client.beta.messages.tool_runner(
        model="claude-opus-4-8",  # per costi piu' bassi: "claude-haiku-4-5"
        max_tokens=1024,
        system=SYSTEM,
        tools=[registra_richiesta],
        messages=[{"role": "user", "content": f"[{nome}] {testo}"}],
    )

    risposta = ""
    for message in runner:
        for block in message.content:
            if block.type == "text":
                risposta = block.text  # l'ultima risposta testuale e' quella finale

    await update.message.reply_text(risposta or "Scusa, non ho capito la richiesta.")


def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    print("Agente in ascolto su Telegram. Premi CTRL+C per fermarlo.")
    app.run_polling()


if __name__ == "__main__":
    main()
