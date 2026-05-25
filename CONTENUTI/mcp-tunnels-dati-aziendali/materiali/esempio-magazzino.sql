-- Popolamento del magazzino "Vini delle Terre" - 30 prodotti + ~80 vendite degli ultimi 12 mesi.
-- Esegui questo script nel SQL Editor di Supabase DOPO schema-magazzino.sql.
--
-- ATTENZIONE: il dataset contiene 5 ANOMALIE NASCOSTE deliberate.
-- Servono per la demo del video - Claude le scopre rispondendo ai prompt di prompt-esempio.md.
-- NON correggerle. Le anomalie sono:
--   1. Sotto costo (id 1, 20): prezzo_vendita < costo_acquisto - errore tariffario
--   2. Esauriti ma visibili sul sito (id 4, 14, 24): giacenza=0 AND visibile_online=TRUE
--   3. Bestseller a rischio esaurimento (id 3, 7, 22): vendite recenti alte, giacenza sotto soglia
--   4. Magazzino morto (id 9, 19, 27, 29, 30): giacenza alta, nessuna vendita da 180+ giorni
--   5. Concentrazione Veneto (id 4, 5, 16, 22): 4 prodotti dalla stessa regione su 30
--
-- Le date sono RELATIVE: vendite distribuite negli ultimi 12 mesi a partire da 2026-05-22.

-- ===== PRODOTTI =====
INSERT INTO prodotti (nome, produttore, regione, annata, prezzo_vendita, costo_acquisto, giacenza, soglia_riordino, visibile_online, data_ultimo_riordino) VALUES
-- ANOMALIA 1: prezzo < costo (errore in cassa)
('Barolo DOCG',                'Cantina Rocca Antica',    'Piemonte',        2018, 25.00, 32.00, 14, 8,  TRUE,  '2026-03-10'),
-- Normali
('Brunello di Montalcino',     'Tenuta Santa Lucia',      'Toscana',         2017, 48.00, 28.00, 22, 10, TRUE,  '2026-04-05'),
-- ANOMALIA 3: bestseller a rischio (vendite alte, giacenza 4 < soglia 12)
('Chianti Classico DOCG',      'Vigna Pratoverde',        'Toscana',         2021, 18.00, 9.50,  4,  12, TRUE,  '2026-02-15'),
-- ANOMALIA 2: esaurito ma visibile sul sito
('Prosecco di Valdobbiadene',  'Cantine Bellavista',      'Veneto',          2023, 12.00, 5.50,  0,  24, TRUE,  '2026-04-22'),
('Amarone della Valpolicella', 'Cantina Borgo Antico',    'Veneto',          2018, 42.00, 24.00, 16, 8,  TRUE,  '2026-04-10'),
('Franciacorta Brut',          'Tenuta del Lago',         'Lombardia',       NULL, 22.00, 11.00, 28, 12, TRUE,  '2026-05-02'),
-- ANOMALIA 3: bestseller a rischio (estivo)
('Vermentino di Sardegna',     'Cantina del Mare',        'Sardegna',        2023, 14.00, 6.50,  6,  18, TRUE,  '2026-02-28'),
('Greco di Tufo DOCG',         'Cascina Vignaverde',      'Campania',        2022, 16.00, 8.00,  19, 10, TRUE,  '2026-04-18'),
-- ANOMALIA 4: magazzino morto (nessuna vendita da 230 giorni)
('Aglianico del Vulture',      'Tenuta Vulcano',          'Basilicata',      2019, 19.00, 10.50, 18, 8,  TRUE,  '2025-10-05'),
('Primitivo di Manduria',      'Masseria Trulli',         'Puglia',          2021, 17.00, 8.50,  24, 12, TRUE,  '2026-04-28'),
('Nero d''Avola',              'Cantine Etna Sud',        'Sicilia',         2021, 13.00, 6.00,  31, 14, TRUE,  '2026-05-08'),
('Lugana DOC',                 'Cantina del Lago',        'Lombardia',       2023, 15.00, 7.00,  22, 12, TRUE,  '2026-05-01'),
('Sangiovese di Romagna',      'Vigna del Borgo',         'Emilia-Romagna',  2022, 11.00, 5.50,  35, 16, TRUE,  '2026-04-15'),
-- ANOMALIA 2: esaurito ma visibile
('Pinot Grigio Friulano',      'Cantine del Collio',      'Friuli',          2023, 13.50, 6.50,  0,  20, TRUE,  '2026-04-30'),
('Verdicchio dei Castelli',    'Tenuta Marchigiana',      'Marche',          2022, 14.50, 7.00,  19, 10, TRUE,  '2026-04-20'),
('Soave Classico',             'Cantine Verona Est',      'Veneto',          2023, 11.00, 5.00,  26, 14, TRUE,  '2026-05-05'),
('Frascati Superiore',         'Tenuta del Tuscolo',      'Lazio',           2023, 10.50, 4.50,  21, 12, TRUE,  '2026-04-25'),
('Montepulciano d''Abruzzo',   'Cantina Adriatica',       'Abruzzo',         2020, 12.50, 6.00,  29, 14, TRUE,  '2026-04-12'),
-- ANOMALIA 4: magazzino morto
('Cannonau di Sardegna',       'Cantine del Gallura',     'Sardegna',        2020, 16.00, 8.00,  22, 10, TRUE,  '2025-11-08'),
-- ANOMALIA 1: prezzo < costo
('Champagne Brut',             'Maison Lacroix-Bertier',  'Champagne (FR)',  NULL, 58.00, 65.00, 11, 6,  TRUE,  '2026-03-22'),
('Barbaresco DOCG',            'Cantina delle Langhe',    'Piemonte',        2019, 32.00, 16.00, 18, 8,  TRUE,  '2026-04-08'),
-- ANOMALIA 3: bestseller a rischio (vendite alte, giacenza sotto soglia)
('Lambrusco di Sorbara',       'Cantina Emiliana',        'Veneto',          2023,  9.50, 4.00,  8,  20, TRUE,  '2026-03-01'),
('Etna Rosso',                 'Tenuta del Vulcano',      'Sicilia',         2020, 21.00, 10.50, 15, 8,  TRUE,  '2026-04-14'),
-- ANOMALIA 2: esaurito ma visibile (era bestseller a Pasqua)
('Moscato d''Asti DOCG',       'Cantine del Monferrato',  'Piemonte',        2023, 11.00, 5.00,  0,  18, TRUE,  '2026-03-20'),
('Trento DOC Riserva',         'Cantina Alpina',          'Trentino',        2018, 28.00, 14.00, 17, 8,  TRUE,  '2026-04-30'),
('Bolgheri Superiore',         'Tenuta del Tirreno',      'Toscana',         2019, 35.00, 18.00, 13, 6,  TRUE,  '2026-04-22'),
-- ANOMALIA 4: magazzino morto
('Ribolla Gialla',             'Cantine del Collio',      'Friuli',          2022, 16.50, 8.00,  14, 8,  TRUE,  '2025-11-02'),
('Pignoletto Spumante',        'Vigna dei Colli',         'Emilia-Romagna',  2023, 10.00, 4.50,  24, 14, TRUE,  '2026-05-03'),
-- ANOMALIA 4: magazzino morto (caso estremo - non vende DA SEMPRE)
('Marsala Vergine 10 anni',    'Cantine del Sud',         'Sicilia',         2015, 24.00, 12.00, 30, 6,  TRUE,  '2025-05-15'),
-- ANOMALIA 4: magazzino morto
('Refosco dal Peduncolo',      'Cantine del Friuli',      'Friuli',          2021, 17.00, 8.50,  19, 8,  TRUE,  '2025-11-12');

-- ===== VENDITE =====
-- ~80 vendite distribuite negli ultimi 12 mesi.
-- I bestseller a rischio (id 3, 7, 22) hanno vendite intensive negli ultimi 30 giorni.
-- I prodotti del magazzino morto (id 9, 19, 27, 29, 30) hanno vendite SOLO oltre i 180 giorni fa.
-- Prosecco/Pinot/Moscato (id 4, 14, 24) sono andati esauriti negli ultimi 30-45 giorni dopo grandi vendite.

INSERT INTO vendite (prodotto_id, quantita, data_vendita, canale) VALUES
-- Vendite ultimi 7 giorni
( 3, 2, '2026-05-21', 'sito'),
( 3, 1, '2026-05-20', 'sito'),
( 3, 3, '2026-05-19', 'enoteca'),
(22, 6, '2026-05-21', 'sito'),
(22, 2, '2026-05-20', 'sito'),
( 7, 2, '2026-05-22', 'sito'),
( 7, 1, '2026-05-19', 'sito'),
( 2, 1, '2026-05-21', 'sito'),
(20, 1, '2026-05-20', 'sito'),
(26, 1, '2026-05-19', 'sito'),

-- Vendite 8-30 giorni fa
( 3, 2, '2026-05-15', 'sito'),
( 3, 4, '2026-05-12', 'enoteca'),
( 3, 2, '2026-05-08', 'sito'),
(22, 4, '2026-05-14', 'sito'),
(22, 12, '2026-05-10', 'wholesale'),
( 7, 2, '2026-05-13', 'sito'),
( 7, 3, '2026-05-08', 'amazon'),
( 7, 2, '2026-05-04', 'sito'),
( 4, 6, '2026-05-02', 'sito'),   -- ultima vendita prima dell'esaurimento
( 4, 4, '2026-04-30', 'sito'),
( 4, 12, '2026-04-28', 'wholesale'),
(14, 3, '2026-05-01', 'sito'),   -- ultima vendita prima dell'esaurimento
(14, 8, '2026-04-29', 'wholesale'),
(14, 2, '2026-04-25', 'sito'),
(24, 4, '2026-04-12', 'sito'),   -- ultima vendita Moscato (Pasqua)
(24, 6, '2026-04-10', 'sito'),
(24, 12, '2026-04-08', 'wholesale'),
( 2, 2, '2026-05-10', 'sito'),
( 2, 1, '2026-05-03', 'sito'),
(20, 2, '2026-05-09', 'sito'),
(20, 1, '2026-05-02', 'sito'),
( 5, 1, '2026-05-11', 'sito'),
( 5, 2, '2026-05-05', 'sito'),
( 6, 2, '2026-05-14', 'sito'),
( 6, 1, '2026-05-07', 'sito'),
(10, 3, '2026-05-12', 'sito'),
(11, 4, '2026-05-08', 'sito'),
(15, 2, '2026-05-09', 'amazon'),
(17, 3, '2026-05-04', 'sito'),
(18, 2, '2026-05-11', 'sito'),
(21, 1, '2026-05-06', 'sito'),
(23, 2, '2026-05-13', 'sito'),
(25, 1, '2026-05-15', 'sito'),
(26, 1, '2026-05-07', 'sito'),
(28, 3, '2026-05-09', 'sito'),

-- Vendite 31-90 giorni fa
( 1, 1, '2026-04-15', 'sito'),
( 2, 2, '2026-04-20', 'enoteca'),
( 2, 1, '2026-04-02', 'sito'),
( 5, 1, '2026-04-22', 'sito'),
( 5, 2, '2026-04-10', 'sito'),
( 6, 3, '2026-04-15', 'enoteca'),
( 8, 2, '2026-04-25', 'sito'),
( 8, 1, '2026-04-12', 'sito'),
(10, 2, '2026-04-18', 'sito'),
(11, 3, '2026-04-08', 'amazon'),
(12, 2, '2026-04-20', 'sito'),
(12, 1, '2026-04-05', 'sito'),
(13, 4, '2026-04-15', 'sito'),
(15, 1, '2026-04-22', 'sito'),
(16, 2, '2026-04-10', 'sito'),
(17, 2, '2026-04-15', 'sito'),
(18, 1, '2026-04-08', 'sito'),
(21, 2, '2026-04-12', 'sito'),
(23, 1, '2026-04-20', 'sito'),
(25, 1, '2026-04-18', 'sito'),
(26, 2, '2026-04-22', 'enoteca'),
(28, 2, '2026-04-15', 'sito'),
( 1, 1, '2026-03-22', 'sito'),
( 2, 1, '2026-03-15', 'sito'),
( 6, 1, '2026-03-18', 'sito'),
(10, 1, '2026-03-10', 'sito'),
(13, 2, '2026-03-22', 'amazon'),

-- Vendite vecchie (oltre 90 giorni) - inclusi i prodotti del MAGAZZINO MORTO
( 9, 2, '2025-10-15', 'sito'),    -- Aglianico - ultima vendita 7 mesi fa
( 9, 3, '2025-09-22', 'enoteca'),
(19, 2, '2025-11-05', 'sito'),    -- Cannonau - ultima 6+ mesi fa
(19, 1, '2025-10-12', 'sito'),
(27, 1, '2025-11-02', 'sito'),    -- Ribolla Gialla
(27, 2, '2025-10-18', 'sito'),
(30, 2, '2025-11-08', 'sito'),    -- Refosco
(30, 1, '2025-10-22', 'sito');
-- NOTA: id 29 (Marsala) NON ha vendite - non e' mai stato venduto, peggior caso magazzino morto
