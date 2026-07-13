"""
Analizza le recensioni dei clienti con un sistema di agenti AI sostenibile.
Serie "Agenti AI per aziende veri, zero fuffa" - Episodio 2.

I modelli si richiamano via OPENROUTER: una sola chiave dà accesso a tutti i
modelli (per l'Ep2 restiamo su Anthropic; in generale Anthropic o Google). L'endpoint di OpenRouter è compatibile
con la libreria ufficiale OpenAI, quindi usiamo quella - e per cambiare modello
(anche produttore) basta cambiare una riga.

L'idea (zero fuffa): NON usare il modello più potente per tutto. Usa il modello
giusto al posto giusto, su tre strati:

  STRATO 1 - un MODELLO ECONOMICO (Haiku) per il lavoro di volume: legge ogni
             recensione e la inquadra in una "scheda" (voto, tema, sentiment).

  STRATO 2 - uno SCRIPT normale (gratis, deterministico) per le cose meccaniche:
             aggrega, conta, calcola le medie, e decide quali pochi casi
             meritano il modello potente. Niente AI: qui basta del codice.

  STRATO 3 - un MODELLO SMART (Opus) solo sui pochi casi delicati: li valida
             con calma (ragionamento acceso) e propone come rispondere.

Alla fine stampa il conto reale dei costi e lo confronta con quanto avresti
speso usando il modello potente per OGNI recensione.

Prima di lanciarlo:
  - copia .env.example in .env e compila OPENROUTER_API_KEY
  - pip install -r requirements.txt
  - python analizza_recensioni.py
"""

import csv
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from openai import OpenAI

# Carica la chiave dal file .env (OPENROUTER_API_KEY).
load_dotenv()

# --- OpenRouter: una chiave, tutti i modelli (endpoint compatibile OpenAI) ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# Su OpenRouter i modelli hanno il prefisso del produttore. Per usarne un altro
# (anche di un altro produttore) basta cambiare queste due righe.
MODELLO_ECONOMICO = "anthropic/claude-haiku-4-5"   # costa poco, veloce: fa il grosso
MODELLO_SMART = "anthropic/claude-opus-4-8"         # costa di più: solo sui casi delicati

# Prezzi per 1 milione di token (USD), come indicati su OpenRouter: input = quello
# che il modello legge, output = quello che scrive (ragionamento incluso).
PREZZI = {
    MODELLO_ECONOMICO: {"input": 1.00, "output": 5.00},
    MODELLO_SMART:     {"input": 5.00, "output": 25.00},
}

# Tetto di sicurezza sui costi: al massimo quante recensioni mandare al modello
# smart. È una decisione dello SCRIPT, non dell'AI, così il conto non sfugge di
# mano nemmeno se il modello economico segnala troppi casi come dubbi.
MAX_CASI_SMART = 5


# --- La "scheda" che il modello economico compila per ogni recensione --------
# Invece di lasciarlo scrivere a ruota libera, gli imponiamo questo schema
# (structured output): risponde corto e ordinato, subito utilizzabile dallo
# script. Output corto = più economico.
class SchedaRecensione(BaseModel):
    voto_stimato: int = Field(description="Voto da 1 a 5 che la recensione esprime")
    tema_principale: Literal[
        "pulizia", "colazione", "posizione", "personale", "prezzo", "rumore", "altro"
    ] = Field(description="Il tema principale della recensione")
    sentiment: Literal["positivo", "neutro", "negativo"] = Field(
        description="Il tono generale della recensione"
    )
    serve_revisione: bool = Field(
        description="True solo se la recensione è grave, ambigua o delicata e "
        "merita l'occhio di un esperto (minacce, rimborsi, accuse serie)"
    )
    motivo: str = Field(description="In poche parole, perché serve (o non serve) la revisione")


def carica_recensioni(percorso: str) -> list[dict]:
    """Legge le recensioni dal file CSV (colonne: autore, testo)."""
    with open(percorso, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def classifica_con_modello_economico(testo: str):
    """STRATO 1 - il modello economico inquadra una recensione.

    Compila la "scheda" imponendo lo schema (response_format). Niente
    ragionamento esteso: deve essere veloce ed economico. Restituisce la scheda
    compilata e il conteggio dei token usati.
    """
    completamento = client.chat.completions.parse(
        model=MODELLO_ECONOMICO,
        max_tokens=400,
        response_format=SchedaRecensione,
        messages=[{
            "role": "user",
            "content": (
                "Inquadra questa recensione di un B&B compilando la scheda. "
                "Metti serve_revisione=true SOLO se è un caso grave o delicato "
                "(minacce, richieste di rimborso o disdetta, accuse serie) "
                "oppure se il giudizio è davvero ambiguo.\n\n"
                f"Recensione: {testo}"
            ),
        }],
    )
    return completamento.choices[0].message.parsed, completamento.usage


def valida_con_modello_smart(testo: str):
    """STRATO 3 - il modello smart si occupa solo dei casi delicati.

    Qui accendiamo il ragionamento (parametro `reasoning` di OpenRouter): lo
    paghiamo di più, ma lo usiamo su pochissimi casi, quindi va bene.
    Restituisce il giudizio scritto e il conteggio dei token usati.
    """
    completamento = client.chat.completions.create(
        model=MODELLO_SMART,
        max_tokens=1500,
        extra_body={"reasoning": {"effort": "medium"}},
        messages=[{
            "role": "user",
            "content": (
                "Sei il responsabile dell'assistenza di un B&B. Questa "
                "recensione è stata segnalata come delicata. Rispondi in modo "
                "conciso con:\n"
                "1) quanto è grave (priorità bassa / media / alta)\n"
                "2) cosa fare concretamente\n"
                "3) una bozza di risposta pubblica, cortese e professionale.\n\n"
                f"Recensione: {testo}"
            ),
        }],
    )
    return completamento.choices[0].message.content, completamento.usage


class ContaCosti:
    """Tiene il conto dei token usati, modello per modello, e li traduce in dollari."""

    def __init__(self):
        self.token = {m: {"input": 0, "output": 0} for m in PREZZI}

    def aggiungi(self, modello: str, usage) -> None:
        # OpenRouter restituisce i token nel formato OpenAI: prompt_tokens (input)
        # e completion_tokens (output, con il ragionamento già incluso).
        self.token[modello]["input"] += usage.prompt_tokens
        self.token[modello]["output"] += usage.completion_tokens

    def costo(self, modello: str) -> float:
        t, p = self.token[modello], PREZZI[modello]
        return t["input"] / 1_000_000 * p["input"] + t["output"] / 1_000_000 * p["output"]

    def costo_totale(self) -> float:
        return sum(self.costo(m) for m in PREZZI)


def scrivi_report(schede, da_validare, media, conteggio_temi) -> None:
    """STRATO 2 (parte finale) - mette tutto in un report leggibile."""
    righe = ["# Report recensioni\n",
             f"Recensioni analizzate: **{len(schede)}**  ",
             f"Voto medio: **{media:.1f} / 5**\n",
             "## Temi più citati\n"]
    for tema, n in sorted(conteggio_temi.items(), key=lambda x: x[1], reverse=True):
        righe.append(f"- {tema}: {n}")
    righe.append("\n## Casi delicati (validati dal modello smart)\n")
    if da_validare:
        for s in da_validare:
            autore = s["recensione"].get("autore", "Anonimo")
            righe.append(f"### {autore}")
            righe.append(f"> {s['recensione']['testo']}\n")
            righe.append(s.get("giudizio", ""))
            righe.append("")
    else:
        righe.append("Nessun caso delicato in questo lotto.")
    Path("report.md").write_text("\n".join(righe), encoding="utf-8")
    print("Report salvato in report.md\n")


def stampa_conto(costi: ContaCosti, schede, da_validare) -> None:
    """Il momento della verità: quanto è costato, e quanto avresti speso senza testa."""
    n = len(schede)
    eco = costi.costo(MODELLO_ECONOMICO)
    smart = costi.costo(MODELLO_SMART)
    totale = costi.costo_totale()

    # Stima onesta: e se OGNI recensione l'avesse trattata il modello smart
    # (con il suo ragionamento), come facciamo coi pochi casi delicati?
    if da_validare:
        costo_medio_smart = smart / len(da_validare)
        stima_tutto_smart = costo_medio_smart * n
    else:
        # Nessun caso delicato: stima prudente, stessi token dell'economico ma
        # alla tariffa (più alta) del modello smart.
        t, p = costi.token[MODELLO_ECONOMICO], PREZZI[MODELLO_SMART]
        stima_tutto_smart = t["input"] / 1_000_000 * p["input"] + t["output"] / 1_000_000 * p["output"]

    print("=" * 56)
    print("                IL CONTO (quello che conta)")
    print("=" * 56)
    print(f"Recensioni analizzate: {n}")
    print(f"  Strato 1 - {MODELLO_ECONOMICO}: ${eco:.4f}")
    print(f"  Strato 2 - script (sul tuo PC):      $0.0000")
    print(f"  Strato 3 - {MODELLO_SMART}:  ${smart:.4f}")
    print(f"  --> TOTALE del sistema:              ${totale:.4f}")
    print("-" * 56)
    print(f"  Se usassi il modello smart per OGNI recensione: ~${stima_tutto_smart:.4f}")
    if totale > 0:
        print(f"  --> Così costa circa {stima_tutto_smart / totale:.0f} volte di meno.")
    print("=" * 56)


def main():
    recensioni = carica_recensioni("recensioni.csv")
    print(f"Caricate {len(recensioni)} recensioni.\n")

    costi = ContaCosti()
    schede = []

    # --- STRATO 1: il modello economico inquadra TUTTE le recensioni ---------
    print(f"Strato 1 - {MODELLO_ECONOMICO} sta inquadrando tutte le recensioni...")
    for rec in recensioni:
        scheda, usage = classifica_con_modello_economico(rec["testo"])
        costi.aggiungi(MODELLO_ECONOMICO, usage)
        schede.append({"recensione": rec, "scheda": scheda})

    # --- STRATO 2: lo SCRIPT fa il lavoro meccanico (gratis) -----------------
    voti = [s["scheda"].voto_stimato for s in schede]
    media = sum(voti) / len(voti)

    conteggio_temi = {}
    for s in schede:
        tema = s["scheda"].tema_principale
        conteggio_temi[tema] = conteggio_temi.get(tema, 0) + 1

    # Selezione: i casi marcati "serve_revisione", con il tetto massimo.
    da_validare = [s for s in schede if s["scheda"].serve_revisione][:MAX_CASI_SMART]
    print(f"Strato 2 - lo script ha aggregato tutto. Voto medio: {media:.1f}/5.")
    print(f"           Casi delicati da passare al modello smart: {len(da_validare)}\n")

    # --- STRATO 3: il modello smart valida solo i pochi casi delicati --------
    print(f"Strato 3 - {MODELLO_SMART} sta validando i casi delicati...")
    for s in da_validare:
        giudizio, usage = valida_con_modello_smart(s["recensione"]["testo"])
        costi.aggiungi(MODELLO_SMART, usage)
        s["giudizio"] = giudizio
    print()

    scrivi_report(schede, da_validare, media, conteggio_temi)
    stampa_conto(costi, schede, da_validare)


if __name__ == "__main__":
    main()
