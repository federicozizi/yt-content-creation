-- Schema del magazzino e-commerce per la demo MCP Tunnels.
-- Caso d'uso: cantina online "Vini delle Terre" con 30 prodotti.
-- Esegui questo script nel SQL Editor di Supabase PRIMA di esempio-magazzino.sql.

-- Pulizia (se esegui lo script piu' di una volta).
DROP TABLE IF EXISTS vendite CASCADE;
DROP TABLE IF EXISTS prodotti CASCADE;

-- Tabella prodotti: il catalogo della cantina online.
CREATE TABLE prodotti (
  id                  SERIAL PRIMARY KEY,
  nome                TEXT NOT NULL,
  produttore          TEXT NOT NULL,
  regione             TEXT NOT NULL,
  annata              INTEGER,
  formato_ml          INTEGER DEFAULT 750,
  prezzo_vendita      NUMERIC(8, 2) NOT NULL,    -- in EUR
  costo_acquisto      NUMERIC(8, 2) NOT NULL,    -- in EUR
  giacenza            INTEGER NOT NULL DEFAULT 0, -- bottiglie disponibili
  soglia_riordino     INTEGER NOT NULL DEFAULT 6,
  visibile_online     BOOLEAN NOT NULL DEFAULT TRUE,
  data_ultimo_riordino DATE,
  creato_il           TIMESTAMPTZ DEFAULT now()
);

-- Tabella vendite: ogni riga e' un singolo ordine cliente per quel prodotto.
CREATE TABLE vendite (
  id           SERIAL PRIMARY KEY,
  prodotto_id  INTEGER NOT NULL REFERENCES prodotti(id),
  quantita     INTEGER NOT NULL,
  data_vendita DATE NOT NULL,
  canale       TEXT NOT NULL    -- 'sito', 'amazon', 'enoteca', 'wholesale'
);

-- Indici utili.
CREATE INDEX idx_prodotti_giacenza ON prodotti(giacenza);
CREATE INDEX idx_prodotti_visibile ON prodotti(visibile_online);
CREATE INDEX idx_vendite_data ON vendite(data_vendita DESC);
CREATE INDEX idx_vendite_prodotto ON vendite(prodotto_id);

-- Commenti (utili a Claude per generare query sensate).
COMMENT ON TABLE  prodotti IS 'Catalogo prodotti della cantina online. Ogni riga = una referenza in vendita.';
COMMENT ON COLUMN prodotti.prezzo_vendita IS 'Prezzo a cui vendi la bottiglia al cliente (EUR, IVA inclusa).';
COMMENT ON COLUMN prodotti.costo_acquisto IS 'Quanto ti costa la bottiglia dal produttore (EUR, IVA esclusa).';
COMMENT ON COLUMN prodotti.giacenza IS 'Numero di bottiglie attualmente in magazzino.';
COMMENT ON COLUMN prodotti.soglia_riordino IS 'Quando la giacenza scende sotto questa soglia, devi riordinare.';
COMMENT ON COLUMN prodotti.visibile_online IS 'TRUE = il prodotto e'' ordinabile dal sito. FALSE = nascosto.';
COMMENT ON TABLE  vendite IS 'Storico vendite di tutti i canali. Una riga = un ordine cliente per un singolo prodotto.';
