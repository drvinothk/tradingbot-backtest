# NIFTY historical data — known limitations + market-regime archetypes

Read this before starting any backtest work or judging a strategy's history. Built 2026-09-28 from a
full vendor data purchase (Jan 2020 - Sep 2025) merged into `backend/data/historical/`.

Files in the vendor drop (`Google Drive: Nifty Historical Data/`): `archetype_map.png` (plot),
`archetype_signature.csv` (indicator values per archetype), `nifty_daily_with_regime_indicators.csv`
(full daily series with the indicators below, Nov 2019 - Aug 2026 — regenerate from the merged spot
data if it's ever meaningfully out of date).

## 1. Data coverage and known defects

- **Options (1-min, per-expiry)**: `options_1min_past/NIFTY/<expiry-date>/` now covers every
  weekly/monthly expiry **2020-01-02 → present** (previously only ~1yr, from 2025-08-26). 297 expiry
  folders added from the vendor purchase; 0 conflicts with existing (TrueData/Shoonya-sourced) data.
- **Spot (1-min)**: `underlyings/NIFTY_alice_index_1min.csv` (2023-06-13+, our own primary source —
  always prefer this where it exists) + `underlyings/NIFTY_vendor_index_1min.csv` (2019-11-01 →
  2025-08-21, fills everything before our own coverage starts).
  **2026-09-28 update**: these two are now also available pre-stitched as
  `underlyings/NIFTY_combined_2020_1min.csv` (vendor before 2023-06-13 09:15 IST, alice_index from
  there on) — use via `run_backtest.py --underlying-source combined_2020`. Verified byte-identical
  to `alice_index` alone on every date both cover before this was trusted (parity test, 2026-09-28).
- **NIFTY only** — no BANKNIFTY in this vendor purchase.
- **OI is unreliable before ~Sep 2020.** ATM-strike OI populated only 6-55% of bars, erratically,
  Jan-Aug 2020; from Sep 2020 onward it's consistently ~99%+. Any OI/PCR-dependent gate (OI/Volume
  Confirmed, PCR filters, MDIS when eventually backtestable) should only be trusted from Sep 2020
  forward. Price/volume-only strategies (ORB, VWAP, EMA, renko) have no such limit across the full
  2020-2025 range.
- **Deep ITM/OTM strikes are sparse** (spot-checked 2026-09-28: a deep-ITM contract on the
  2020-03-26 expiry had only 27 one-minute bars across its whole life) — real illiquidity, not a
  data defect. Doesn't affect ATM±N strategies (everything this codebase runs today).

**Two real vendor defects found and fixed before merge** (vendor confirmed both, 2026-09-27):
1. `20220122` expiry folder was junk (misplaced data, not a real NIFTY expiry — 2022-01-22 is a
   Saturday) — deleted. The real Jan-2022 Thursdays (06/13/20/27) were already present and correct.
2. `20250925` + `20250930` were the same monthly contract split across two folders (NSE moved that
   contract's expiry date after listing) — merged into one continuous `20250930` series, deduped,
   verified continuous (e.g. `17000CE`: folder A ends 2025-07-31, folder B picks up 2025-08-01, zero
   timestamp overlap).

Both fixes independently re-verified 2026-09-28 (not just trusted): `2022-01-22` dir confirmed
absent, `2025-09-25` dir confirmed absent, `2025-09-30` confirmed at a normal 22-contract count.

**Vendor data is genuine, not fabricated** — cross-checked against our own TrueData for the
2025-09-23 expiry: close matched 100% bar-for-bar across 22 contracts, OI 97.6% exact, volume 94.5%
exact. Spot quality is clean throughout: yearly price ranges match real NIFTY history exactly (incl.
the COVID crash to ~7,500 and back — independently re-verified 2026-09-28: the file's exact low on
2020-03-24 is 7511.10, matching the real public-record NIFTY low that day), the only large 1-min
jumps (17 of them, all >3%) are real March-2020 circuit-halt events, not data errors.

## 2. The 8 market archetypes

Every trading day from Nov 2019 to Aug 2026 falls into one of 8 archetypes, defined by direction
(bullish/bearish/none) × volatility level × chop (does drawdown track the net move, or is it much
deeper — i.e. whipsaw). Several disjoint calendar windows share the same archetype.

| Archetype | Calendar windows | Days | % of data | Character |
|---|---|---|---|---|
| **A**. Range-bound / sideways, low vol | Nov'19-Feb'20, Dec'22-Mar'23, Jan-May'24, Jul-Sep'25, Oct'25-Feb'26, May-Aug'26 | 516 | 31% | No sustained direction, vol <13%, small net drift |
| **B**. Sustained bull, moderate vol | Jul'20-Oct'21, Jul-Nov'22 | 435 | 26% | Strong clean uptrend, vol 14-15% |
| **C**. Sustained bull, low vol | Apr-Dec'23, Jul-Sep'24 | 247 | 15% | Cleanest possible bull tape, vol 8-11% |
| **D**. Bull + high/extreme vol (V-recovery) | Apr-Jun'20, Mar-Jun'25, Apr'26 | 160 | 9% | Sharp violent up-moves, vol 15-42% |
| **E**. Choppy + bearish bias + volatile | Nov'21-Feb'22, Mar-Jun'22 | 166 | 10% | Topping/whipsaw, no clean trend, vol 17-22% |
| **F**. Sustained bear, moderate/high vol | Oct'24-Feb'25, Mar'26 | 123 | 7% | Clean downtrend, drawdown ≈ net move, vol 12-18% |
| **G**. Bear + extreme vol (crash) | Mar'20 | 21 | 1% | COVID crash — unique severity, nothing else matches it |
| **H**. Single-event vol shock | Jun'24 | 19 | 1% | One-off news-day spike (election result) inside a flat month |

### Measured signature per archetype (this dataset)

| Archetype | ADX14 | DI+ minus DI- | 20d vol% | Efficiency Ratio(20) | % days > MA60 |
|---|---|---|---|---|---|
| A. Range-bound, low vol | 18.7 | -2.3 | 10.8 | 0.16 | 53.7% |
| B. Bull, moderate vol | 26.7 | +8.9 | 15.0 | 0.29 | 87.8% |
| C. Bull, low vol | 27.2 | +9.9 | 9.3 | 0.34 | 89.1% |
| D. Bull + high vol | 21.2 | +3.7 | 26.2 | 0.23 | 55.0% |
| E. Choppy + bearish + volatile | 21.0 | -7.6 | 19.5 | 0.20 | 31.3% |
| F. Sustained bear | 30.4 | -15.3 | 13.3 | 0.25 | 7.3% |
| G. Crash | 60.6 | -40.4 | 46.3 | 0.5 | 0.0% |
| H. Event shock | 14.0 | -4.0 | 26.7 | 0.21 | 94.7% |

See `archetype_map.png` for the direction-vs-volatility plot; dot size ~ number of days in the archetype.

## 3. Detecting the current archetype live — indicator recipe

Computed from daily NIFTY spot OHLC (no options data needed). All are standard, cheap to compute on
top of what the app already tracks:

- **ADX(14) with +DI / -DI** (Wilder's method) — trend strength + direction. `di_diff = +DI - -DI`
  is the single best directional signal.
- **20-day annualized realized vol** (`std(daily log/pct returns, 20d) * sqrt(252) * 100`) — volatility level.
- **Kaufman Efficiency Ratio(20)** = `|close_t - close_t-20| / sum(|daily close changes|, 20d)` — how
  "clean" the trend is (1 = straight line, near 0 = pure noise/chop).
- **% of last 60 days closed above the 60-day MA** — a simpler, ADX-free proxy for direction, easy to
  sanity-check ADX against.

The live app already computes most of this — `shadow_context.py`'s `daily_regime` block (deployed
2026-09-21) logs ADX14-daily and ATR14 %-rank on every signal already. Add DI+/DI- and
`vol20ann`/`pct_above_ma60` alongside it rather than building a second pipeline.

### Practical decision rule (rough, use as a starting point)

- `vol20ann > 35%` → **G** (crash), regardless of direction.
- `di_diff <= -12` → **F** (sustained bear) if `vol20ann` 10-20%, else consider **G**.
- `di_diff <= -5` and `vol20ann >= 17%` → **E** (choppy bearish/volatile).
- `di_diff >= +7` → bull: **C** if `vol20ann < 12%`, **B** if 12-18%, **D** if >= 18%.
- `|di_diff| < 5` and `vol20ann < 13%` → **A** (range-bound).
- A sudden 1-3 day vol spike (`vol20ann` jumps sharply) inside an otherwise A/B/C tape, with no
  sustained `di_diff` change → **H** (event shock) — treat as transient, don't reclassify the
  underlying regime.

### How to use this for config selection

Once a strategy's backtest results are tagged by which archetype each trade fell in (join on
`entry_date` against the daily table), you can see whether a config is broadly robust or is really
"only good in bull markets." On a live/paper morning, compute today's `di_diff`/`vol20ann` from the
last ~20-60 days, map to the nearest archetype above, and prefer whichever configs' backtest showed
strength in that archetype (or in the same direction/vol quadrant if the exact archetype has too few
historical days to trust).

**Caveat — this is for config selection/allocation, not an entry gate.** A separate investigation
(2026-09-21, `project_chop_day_filter`) tested 7 day-level regime classifiers as hard entry filters
and found 5 of 7 would have hurt net P&L — don't rebuild that mistake. This regime read is about
*which strategy/config to run more of*, not about blocking individual trades.
