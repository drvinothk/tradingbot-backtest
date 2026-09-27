# Renko w13 + w14 results (12-day warm-up), 2026-09-27

Harness: multi-trade per day, `--extra-warmup-days 12` (corrected ATR/EMA warm-up window;
supersedes the earlier w12 pilot which used 21 days and took ~2x longer per config for no
measurable benefit). Full year 2025-08-28..2026-09-18 (236 tradable days). Gross P&L per lot
(65 qty). `est-net` = gross net minus a flat per-trade cost estimate.

**Cost model note (2026-09-27 correction):** the `est-net(-130/trade)` figure printed by
`analysis/csv_analyze.py` (`COST = 130.0`) uses the old `flat ₹40/lot` brokerage assumption.
The real broker (Shoonya) charges a flat ₹5/order = ₹10/round-trip (entry+exit) regardless of
quantity, not ₹40/lot (see `BACKTEST_LEARNINGS.md`, 2026-08-30 cost-model correction, which
was applied to other strategies' scripts but never carried into the renko `csv_analyze.py`
constant). Swapping ₹40→₹10 flat drops the per-trade cost from ~130 to ~100 (turnover/STT/
slippage terms unchanged). Both figures are given below where the corrected number matters;
`csv_analyze.py`'s `COST` constant itself has not been edited (still prints -130).

## w13 chain — 24 configs across 4 chunks (w13a-d)

### ATR-brick "s1_top" family (14 configs) — brick sizing, confirm rules, filters, exits

| config | n/days | net | est-net(-130) | PF | note |
|---|---|---|---|---|---|
| s1top_ctrl (baseline, htf30 x1.0) | 92/64 | -13,710 | -25,670 | 0.76 | baseline; reverses the old mt3 (+10,658) result once warm-up is corrected |
| s1_pe (PE-only) | 64/44 | +4,207 | -4,113 | 1.15 | best PE cut in w13 |
| s1_msd1 (max 1/dir) | 66/64 | -7,629 | -16,209 | 0.81 | |
| s1_m075 (x0.75 brick) | 237/131 | -38,713 | -69,523 | 0.77 | smaller brick = worse |
| s1_m05 (x0.5 brick) | 466/203 | -63,143 | -123,723 | 0.81 | smaller brick = worse |
| s1_htf15_m1 (15m, x1.0) | 310/159 | -44,062 | -84,362 | 0.80 | |
| s1_htf15_m15 (15m, x1.5) | 96/68 | -8,582 | -21,062 | 0.85 | least-bad sizing variant |
| s1_conf1 (confirm=1) | 216/118 | -44,609 | -72,689 | 0.69 | loosening confirm hurts a lot |
| s1_conf3 (confirm=3) | 32/24 | -9,048 | -13,208 | 0.60 | tiny n |
| s1_ema30x15 (EMA filter) | 89/61 | -7,589 | -19,159 | 0.85 | |
| s1_exit_wide (wide stop/target/trail) | 85/64 | +8,874 | -2,176 | 1.15 | best gross result in w13 |
| s1_nofilter (ctrl, no dir filter) | 94/64 | -12,353 | -24,573 | 0.78 | ~= baseline |
| s1_pe_m075 (PE + x0.75) | 147/88 | -19,956 | -39,066 | 0.80 | |

### Fixed-brick family (10 configs) — msd1 cuts, filter variants, legacy sizing (pd3-5)

| config | n/days | net | est-net(-130) | PF | note |
|---|---|---|---|---|---|
| base_ctrl (full multi-trade) | 785/236 | -172,906 | -274,956 | 0.66 | matches mt1 base exactly (warm-up-insensitive) |
| base_msd1 (max 1/dir) | 359/236 | -43,063 | -89,733 | 0.81 | msd1 cuts the loss ~4x |
| base_pe_msd1 (PE + msd1) | 182/182 | +2,571 | -21,089 | 1.02 | near-breakeven gross |
| h1_15m_fib_mv50 | 201/152 | -43,511 | -69,641 | 0.67 | |
| h2_15m_fib_ema15 | 156/135 | -14,970 | -35,250 | 0.85 | |
| h4_15m_fib_nocap | 299/233 | -63,349 | -102,219 | 0.71 | worst of the batch |
| h6_5m_fib_cc5 | 253/219 | -47,671 | -80,561 | 0.73 | |
| mv50_msd1 (max 1/dir) | 161/155 | -2,073 | -23,003 | 0.98 | near-breakeven gross |
| pd3_e4 | 356/237 | -44,460 | -90,740 | 0.80 | |
| pd4_tf5x5 | 435/237 | -43,787 | -100,337 | 0.84 | |
| pd5_b833mv50 | 208/178 | -35,906 | -62,946 | 0.76 | |

### w13 bottom line
- Only 2 of 24 configs are gross-positive: `s1_pe` (+4,207) and `s1_exit_wide` (+8,874).
  **Every one of the 24 is negative after the (old, -130) cost estimate.**
- **msd1 (max 1 signal per direction) is the single biggest lever**, not brick sizing or
  exits: `base_msd1` cuts the full-multi-trade loss from -172,906 to -43,063; `base_pe_msd1`
  and `mv50_msd1` both land near gross breakeven. Re-entries are the core loss driver.
- **PE consistently beats CE** in nearly every config.
- **Wednesday / DTE6 (day-after-weekly-expiry)** is the only reliably positive weekday/DTE
  bucket in almost every config; every other day is negative almost everywhere.
- Loosening brick confirm rules (`conf1`) or shrinking brick size (`m075`, `m05`) makes
  things meaningfully worse.
- The corrected 12-day warm-up **reverses the earlier mt3 headline finding**: the previously
  "only positive" ATR s1_top config (mt3, +10,658, using a 1000-bar warm-up) is negative here
  (`s1top_ctrl`, -13,710) once properly warmed up.

## w14a chain — 4 follow-up configs combining the levers that worked

Built from the w13 findings: msd1 and PE-only both helped individually; wide exit produced
the single best gross result. None of these three had been combined before w14.

| config | n/days | net (gross) | PF | est-net (old -130) | **est-net (corrected -100)** |
|---|---|---|---|---|---|
| s1_pe_msd1 (PE + msd1, ATR family) | 44/44 | +3,527 | 1.19 | -2,193 | -873 |
| **s1_pe_exit_wide** (PE + wide exit, ATR family) | 60/44 | **+15,361** | **1.43** | +7,561 | **+9,361** |
| base_pe_msd1_wide (PE + msd1 + wide exit, fixed-brick) | 182/182 | -1,407 | 0.99 | -25,067 | -19,607 |
| mv50_pe_msd1 (PE + msd1, fixed-brick mv50) | 81/81 | +1,674 | 1.03 | -8,856 | -6,426 |

### w14a bottom line
- **`s1_pe_exit_wide` is the only config across all 28 tested (w13 + w14) that clears costs**
  under either cost estimate: +7,561 (old) / +9,361 (corrected). t-stat is still weak (1.09).
- The edge comes entirely from **re-entries riding the wide trailing exit** (+17,691 net from
  16 re-entry trades, avg +1,106/trade) — first-trade-of-day alone is still slightly negative
  (-2,330). This is the opposite of every other config, where re-entries were the loss driver.
- Widening the exit does **not** help the fixed-brick family the same way
  (`base_pe_msd1_wide` -1,407 vs the narrower `base_pe_msd1` +2,571) — the benefit looks
  specific to the ATR/s1_top brick structure, not general.
- `mv50_pe_msd1` (isolating PE on the already-near-breakeven `mv50_msd1`) made things worse
  (-6,426 corrected vs the all-direction `mv50_msd1`'s -23,003 at the same n... actually worse
  in gross terms too: +1,674 vs mv50_msd1's -2,073 gross is a small improvement, but nowhere
  near what PE-only did for the ATR family).

## Caveats (apply throughout)
- Small samples on most ATR-family configs (24-92 trades; `s1_pe_exit_wide` itself is only 60
  trades / 44 days).
- Weak t-stats everywhere (best is 1.09); none reach conventional significance.
- Selection bias: 28 configs tested on ~1 year of data, with each round of "next 4" chosen
  after seeing which levers looked best in the prior round (multi-stage in-sample search).
- Harness label: multi-trade + 12-day warm-up. Not directly comparable to mt1 (1000-bar
  warm-up) or the original weekly-only harness numbers.
- `s1_pe_exit_wide` is the one config worth a closer look (larger n / different date range /
  walk-forward split) before treating it as more than a promising lead.
