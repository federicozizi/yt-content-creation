"""
dati_esempio.py
================
Costruisce un "pacchetto incidente" realistico, del tipo che daresti a Claude
quando gli chiedi: "guarda cosa e' successo in produzione e dimmi la causa".

Il pacchetto contiene di proposito i TRE tipi di contenuto che Headroom sa
comprimere in modo diverso:

  1. TESTO    -> il runbook / postmortem scritto a parole (prosa verbosa)
  2. JSON     -> gli eventi di monitoraggio (un array lungo e ripetitivo)
  3. CODICE   -> il sorgente del servizio che ha fallito (Python)

La risposta giusta ("la causa") e' ricavabile sia dal pacchetto intero sia da
quello compresso: e' questo il punto del video. La pistola fumante e' l'unico
evento FATAL dentro il JSON + la funzione che lo provoca nel codice.
"""

from __future__ import annotations

import json


# ---------------------------------------------------------------------------
# 1) TESTO — il runbook / postmortem (prosa, volutamente prolissa)
# ---------------------------------------------------------------------------
RUNBOOK_TESTO = """\
Runbook del servizio "checkout-api" — note operative per chi e' di turno.

Il servizio checkout-api e' il cuore del processo di pagamento del nostro
e-commerce. Riceve le richieste dal frontend, valida il carrello, parla con il
gateway di pagamento esterno e infine scrive l'ordine sul database Postgres.
E' un servizio considerato critico: se va giu', i clienti non riescono a
concludere gli acquisti e perdiamo fatturato in modo diretto e immediato.

Architettura, raccontata a parole. Ogni istanza del servizio mantiene un
"pool" di connessioni verso il database, cioe' un piccolo gruppo di linee
telefoniche gia' aperte verso Postgres che vengono prese in prestito quando
serve e restituite quando l'operazione e' finita. Il pool e' dimensionato a
venti connessioni per istanza. Quando tutte e venti le linee sono occupate,
le nuove richieste si mettono in coda e aspettano che una linea si liberi.
Se nessuna linea si libera entro il timeout configurato, la richiesta viene
abbandonata e l'utente vede un errore.

Comportamento atteso in condizioni normali. In una giornata tipica il pool non
arriva mai a saturazione: le query sono veloci, le connessioni vengono
restituite in fretta e la coda resta vuota. I tempi di risposta stanno sotto i
duecento millisecondi nel novantanovesimo percentile. Quando vedi i tempi di
risposta salire lentamente ma in modo costante, senza un picco di traffico che
lo giustifichi, la prima cosa da sospettare e' una perdita di connessioni: cioe'
connessioni prese in prestito dal pool e mai restituite, che restano occupate
per sempre e riducono via via le linee disponibili.

Cosa fare quando scatta l'allarme. Per prima cosa guarda la metrica del numero
di connessioni attive sul pool: se cresce in modo monotono e non scende mai,
e' quasi sicuramente una perdita. Per seconda cosa cerca nei log gli eventi di
tipo "pool_exhausted", che indicano che una richiesta non ha trovato linee
libere entro il timeout. Per terza cosa, come mitigazione temporanea, puoi
riavviare l'istanza: il riavvio ricrea il pool da zero e libera tutte le linee,
ma e' una pezza, non una soluzione, perche' la perdita ricomincia subito dopo.

Storia. Abbiamo gia' avuto un incidente simile sei mesi fa, causato da un percorso
di codice che, in caso di eccezione del gateway di pagamento, usciva dalla
funzione senza restituire la connessione al pool. Era stato risolto mettendo la
restituzione in un blocco che viene eseguito sempre, anche quando c'e' un errore.
Se rivedi un comportamento del genere, controlla per prima cosa i percorsi di
errore: e' li' che le connessioni si perdono, non nel percorso felice.
"""


# ---------------------------------------------------------------------------
# 2) JSON — gli eventi di monitoraggio (array lungo, ripetitivo, una pistola fumante)
# ---------------------------------------------------------------------------
def _costruisci_eventi() -> list[dict]:
    """Genera ~40 eventi di telemetria: tanti routine, uno FATAL."""
    eventi: list[dict] = []

    # 120 eventi "di routine": stessa forma, valori che si ripetono.
    # E' esattamente il tipo di array che SmartCrusher comprime tantissimo,
    # perche' le chiavi e i valori si ripetono quasi identici. In un incidente
    # vero i log sono CENTINAIA di righe cosi': e' qui che va a finire il conto.
    for i in range(120):
        eventi.append(
            {
                "timestamp": f"2026-06-22T09:{i % 60:02d}:0{i % 10}Z",
                "service": "checkout-api",
                "host": f"checkout-api-pod-{(i % 4) + 1}",
                "level": "INFO",
                "event": "request_completed",
                "route": "/api/v1/checkout",
                "method": "POST",
                "status_code": 200,
                "latency_ms": 140 + (i % 7) * 10,
                "db_pool_active": 6 + (i % 4),
                "db_pool_size": 20,
                "trace_id": f"trace-{1000 + i}",
                "region": "eu-west-1",
            }
        )

    # 8 eventi che mostrano la SALITA lenta del pool (il sintomo).
    for i in range(8):
        eventi.append(
            {
                "timestamp": f"2026-06-22T10:{10 + i:02d}:00Z",
                "service": "checkout-api",
                "host": "checkout-api-pod-2",
                "level": "WARN",
                "event": "db_pool_pressure",
                "route": "/api/v1/checkout",
                "method": "POST",
                "status_code": 200,
                "latency_ms": 380 + i * 120,
                "db_pool_active": 13 + i,  # cresce e non scende: perdita
                "db_pool_size": 20,
                "trace_id": f"trace-{2000 + i}",
                "region": "eu-west-1",
            }
        )

    # 1 evento ERROR: la coda non trova linee libere.
    eventi.append(
        {
            "timestamp": "2026-06-22T10:18:30Z",
            "service": "checkout-api",
            "host": "checkout-api-pod-2",
            "level": "ERROR",
            "event": "pool_exhausted",
            "route": "/api/v1/checkout",
            "method": "POST",
            "status_code": 503,
            "latency_ms": 5000,
            "db_pool_active": 20,
            "db_pool_size": 20,
            "trace_id": "trace-2999",
            "region": "eu-west-1",
            "message": "timeout acquiring DB connection from pool after 5000ms",
        }
    )

    # 1 evento FATAL: la pistola fumante. Indica funzione e causa.
    eventi.append(
        {
            "timestamp": "2026-06-22T10:18:31Z",
            "service": "checkout-api",
            "host": "checkout-api-pod-2",
            "level": "FATAL",
            "event": "connection_leak_detected",
            "route": "/api/v1/checkout",
            "method": "POST",
            "status_code": 503,
            "latency_ms": 5001,
            "db_pool_active": 20,
            "db_pool_size": 20,
            "leaked_connections": 20,
            "offending_function": "process_payment",
            "offending_file": "checkout_service.py",
            "trace_id": "trace-3000",
            "region": "eu-west-1",
            "message": (
                "Connection leak: 20/20 connections checked out and never "
                "released. All leaks traced to process_payment() error path: "
                "gateway exception returns before conn.release()."
            ),
        }
    )

    return eventi


EVENTI_JSON = json.dumps(_costruisci_eventi(), indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# 3) CODICE — il sorgente del servizio (con il bug, su un percorso di errore)
# ---------------------------------------------------------------------------
CODICE_PYTHON = '''\
"""checkout_service.py — gestione del checkout e del pagamento."""

import logging

logger = logging.getLogger("checkout-api")


class PaymentGatewayError(Exception):
    """Sollevata quando il gateway di pagamento esterno risponde male."""


class CheckoutService:
    def __init__(self, db_pool, payment_gateway):
        self.db_pool = db_pool
        self.gateway = payment_gateway

    def validate_cart(self, cart):
        if not cart.get("items"):
            raise ValueError("Carrello vuoto")
        total = sum(i["price"] * i["qty"] for i in cart["items"])
        if total <= 0:
            raise ValueError("Totale non valido")
        return total

    def process_payment(self, cart, customer_id):
        """Esegue il pagamento e scrive l'ordine.

        BUG: la connessione viene presa dal pool ma, se il gateway solleva
        un'eccezione, la funzione esce PRIMA di chiamare conn.release().
        La connessione resta occupata per sempre -> perdita di connessioni.
        """
        total = self.validate_cart(cart)
        conn = self.db_pool.acquire()  # prende una linea dal pool

        # Percorso che puo' fallire: se il gateway alza un'eccezione,
        # saltiamo direttamente al chiamante e NON liberiamo "conn".
        charge = self.gateway.charge(customer_id, total)  # puo' lanciare PaymentGatewayError

        order_id = conn.execute(
            "INSERT INTO orders (customer_id, total, charge_id) "
            "VALUES (%s, %s, %s) RETURNING id",
            (customer_id, total, charge["id"]),
        )
        conn.commit()
        self.db_pool.release(conn)  # restituisce la linea SOLO nel percorso felice
        logger.info("ordine %s creato per cliente %s", order_id, customer_id)
        return {"order_id": order_id, "charge_id": charge["id"]}

    def refund(self, order_id):
        conn = self.db_pool.acquire()
        try:
            self.gateway.refund(order_id)
            conn.execute("UPDATE orders SET refunded = true WHERE id = %s", (order_id,))
            conn.commit()
        finally:
            self.db_pool.release(conn)  # qui invece e' fatto bene: release SEMPRE
        return {"refunded": order_id}
'''


# ---------------------------------------------------------------------------
# Assemblaggio del pacchetto unico (mixed content) che diamo a Claude
# ---------------------------------------------------------------------------
def assembla(testo: str, eventi_json: str, codice: str) -> str:
    """Mette insieme i tre pezzi (gia' compressi o grezzi) in un unico pacchetto
    leggibile, con etichette chiare. La stessa struttura per la versione grezza
    e per quella compressa: cosi' il confronto e' mela-contro-mela."""
    return f"""\
== RUNBOOK (testo) ==
{testo}

== EVENTI DI MONITORAGGIO (JSON) ==
{eventi_json}

== SORGENTE DEL SERVIZIO (codice) ==
{codice}
"""


def costruisci_pacchetto() -> str:
    """Il pacchetto incidente GREZZO: i tre pezzi originali, senza compressione."""
    return assembla(RUNBOOK_TESTO, EVENTI_JSON, CODICE_PYTHON)


DOMANDA = (
    "Sei un ingegnere SRE. Dal pacchetto incidente qui sotto, dimmi in 2-3 righe: "
    "(1) qual e' la causa radice, (2) in quale funzione e file si trova, "
    "(3) la fix in una frase. Cita l'evento FATAL che lo prova."
)


if __name__ == "__main__":
    pacchetto = costruisci_pacchetto()
    print(f"Pacchetto incidente: {len(pacchetto):,} caratteri")
    print(f"  - testo runbook:  {len(RUNBOOK_TESTO):,} caratteri")
    print(f"  - eventi JSON:    {len(EVENTI_JSON):,} caratteri")
    print(f"  - codice Python:  {len(CODICE_PYTHON):,} caratteri")
