-- ⚠️ Gemello inglese: CONTENUTI/claude-code-small-business-3-components/materiali/schema-aziendale.sql
--
-- Schema starter per uno studio commercialisti.
-- 4 tabelle che tengono i DATI CUSTOM dello studio — quelli che né QuickBooks
-- né altri software fiscali standard conoscono.
--
-- Come usare:
-- 1. Vai sul tuo progetto Supabase → SQL Editor → New query.
-- 2. Incolla tutto questo file.
-- 3. Run.
-- 4. Verifica in Table Editor che le 4 tabelle siano create con le 5 righe di
--    seed in regimi_fiscali.

-- =====================================================================
-- TABELLA: regimi_fiscali (lookup table dei regimi italiani)
-- =====================================================================
create table if not exists regimi_fiscali (
  codice text primary key,
  descrizione text not null,
  limite_fatturato_annuo numeric,  -- null = nessun limite (ordinario)
  aliquota_sostitutiva numeric,    -- null se non applicabile
  note text
);

insert into regimi_fiscali (codice, descrizione, limite_fatturato_annuo, aliquota_sostitutiva, note) values
  ('forfettario', 'Regime forfettario', 85000, 15, 'Aliquota 5% primi 5 anni nuove attività'),
  ('forfettario_startup', 'Forfettario startup (5% primi 5 anni)', 85000, 5, 'Solo nuove attività, primi 5 anni'),
  ('minimi_residuo', 'Regime dei minimi (residuale)', 30000, 5, 'Chiuso ai nuovi ingressi dal 2016, alcuni soggetti ancora ammessi'),
  ('ordinario', 'Regime ordinario', null, null, 'Senza limiti di fatturato, contabilità ordinaria'),
  ('semplificato', 'Regime semplificato (contabilità semplificata)', 500000, null, 'Servizi 500k, altre attività 800k')
on conflict (codice) do nothing;

-- =====================================================================
-- TABELLA: clienti (anagrafica + regime fiscale + fatturato)
-- =====================================================================
create table if not exists clienti (
  id uuid primary key default gen_random_uuid(),
  ragione_sociale text not null,
  partita_iva text unique,
  codice_fiscale text,
  regime_fiscale_codice text references regimi_fiscali(codice),
  fatturato_anno_corrente numeric default 0,
  fatturato_anno_precedente numeric default 0,
  data_acquisizione date default current_date,
  email_referente text,
  settore text,
  attivo boolean default true,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create index if not exists idx_clienti_regime on clienti(regime_fiscale_codice);
create index if not exists idx_clienti_attivo on clienti(attivo);

-- =====================================================================
-- TABELLA: scadenze_custom (scadenze SPECIFICHE dello studio
-- che non sono nello scadenziario fiscale standard nazionale)
-- =====================================================================
create table if not exists scadenze_custom (
  id uuid primary key default gen_random_uuid(),
  cliente_id uuid references clienti(id) on delete cascade,
  tipo text not null,                  -- es. 'rinnovo_iscrizione_albo', 'scadenza_contratto_consulenza'
  descrizione text,
  data_scadenza date not null,
  ricorrenza text,                     -- 'annuale', 'mensile', 'unica'
  promemoria_giorni_prima int default 7,
  completata boolean default false,
  note text,
  created_at timestamptz default now()
);

create index if not exists idx_scadenze_data on scadenze_custom(data_scadenza);
create index if not exists idx_scadenze_cliente on scadenze_custom(cliente_id);
create index if not exists idx_scadenze_attive on scadenze_custom(completata) where completata = false;

-- =====================================================================
-- TABELLA: note_interne (commenti del team su ciascun cliente,
-- incluso alert generati dagli agenti custom)
-- =====================================================================
create table if not exists note_interne (
  id uuid primary key default gen_random_uuid(),
  cliente_id uuid references clienti(id) on delete cascade,
  tipo text not null,                  -- 'commento', 'alert_soglia', 'alert_scadenza', 'flag_attenzione'
  testo text not null,
  autore text,                          -- nome socio dello studio o 'agente:regime-checker'
  flag_per_invoice_chaser text,        -- es. 'non_sollecitare', 'sollecitare_modo_morbido', null
  letto boolean default false,
  created_at timestamptz default now()
);

create index if not exists idx_note_cliente on note_interne(cliente_id);
create index if not exists idx_note_tipo on note_interne(tipo);
create index if not exists idx_note_non_letti on note_interne(letto) where letto = false;
create index if not exists idx_note_flag_chaser on note_interne(flag_per_invoice_chaser) where flag_per_invoice_chaser is not null;

-- =====================================================================
-- VISTE COMODE (opzionali, per query frequenti)
-- =====================================================================

-- Clienti vicini al limite del proprio regime (per regime-checker)
create or replace view v_clienti_vicini_limite as
select
  c.id,
  c.ragione_sociale,
  c.regime_fiscale_codice,
  c.fatturato_anno_corrente,
  r.limite_fatturato_annuo,
  round((c.fatturato_anno_corrente / nullif(r.limite_fatturato_annuo, 0) * 100)::numeric, 1) as percentuale_limite
from clienti c
join regimi_fiscali r on r.codice = c.regime_fiscale_codice
where c.attivo = true
  and r.limite_fatturato_annuo is not null
  and c.fatturato_anno_corrente >= r.limite_fatturato_annuo * 0.8;

-- Scadenze custom in arrivo nei prossimi 30 giorni
create or replace view v_scadenze_imminenti as
select
  s.id,
  s.cliente_id,
  c.ragione_sociale,
  s.tipo,
  s.descrizione,
  s.data_scadenza,
  s.data_scadenza - current_date as giorni_rimanenti
from scadenze_custom s
join clienti c on c.id = s.cliente_id
where s.completata = false
  and s.data_scadenza <= current_date + interval '30 days'
order by s.data_scadenza;

-- =====================================================================
-- FINE SCHEMA
-- 4 tabelle + 5 righe seed in regimi_fiscali + 2 viste comode.
-- Personalizza i tipi (es. aggiungi colonna sul tuo CRM, aggiungi un settore
-- specifico) modificando questo file e rieseguendolo.
-- =====================================================================
