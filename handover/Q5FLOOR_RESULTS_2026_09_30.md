# q5floor chain results (r21-r23), 2026-09-30

Strategy: `ema_micro_pullback_conviction` (EMA_*_Q5Floor configs), source `combined_2020`.
Not the renko_trend work tracked elsewhere in `handover/` — a separate chain that ran
overnight 2026-09-29/30 (unit `backtest-20260929-184442.service`, `chain_q5floor.sh`,
engine md5 `53208abd`). Not being actively monitored going forward; this is a one-off
results snapshot.

Gross P&L per lot (65 qty), as printed by `analysis/csv_analyze.py`. Cost model used
below: **flat ₹40/lot**, applied per trade (each trade = 1 lot in this harness), i.e.
`cost_total = 40 x trades`. QC check applied: `net/lot == gross/lot - 40` and
`net_total == gross_total - cost_total` verified to match exactly for every row.

| config | trades (lots) | Gross Total PnL | Gross PnL/lot | PF | Cost Total (@Rs40/lot) | Net Total | Net PnL/lot |
|---|---|---|---|---|---|---|---|
| r21 EMA_Base_Q5Floor | 3,923 | Rs213,377 | Rs54.39 | 1.29 | Rs156,920 | **Rs56,457** | Rs14.39 |
| r22 EMA_Convic_Paper_Q5Floor | 1,158 | Rs154,969 | Rs133.82 | 2.15 | Rs46,320 | **Rs108,649** | Rs93.82 |
| r23 EMA_PCR_Live_Convic_Q5Floor | 690 | Rs86,529 | Rs125.40 | 1.98 | Rs27,600 | **Rs58,929** | Rs85.40 |

## Additional stats (from `analyze <tag>`, gross basis)

| config | days traded | WR | maxDD | Calmar | t-stat |
|---|---|---|---|---|---|
| r21 EMA_Base_Q5Floor | 1,414 | 56% | 10,984 | 19.43 | 6.37 |
| r22 EMA_Convic_Paper_Q5Floor | 737 | 71% | 4,843 | 32.00 | 9.90 |
| r23 EMA_PCR_Live_Convic_Q5Floor | 451 | 70% | 5,084 | 17.02 | 6.86 |

## Read

- All three are net-positive at Rs40/lot flat cost.
- **r22 (paper conviction filter) is the standout**: highest PF (2.15), strongest
  t-stat (9.90), smallest drawdown, highest net/lot (Rs93.82).
- **r21 (no conviction filter, "base")** has the largest trade count (3,923) but the
  thinnest per-lot edge (Rs14.39 net/lot after cost) — the conviction filter cuts trade
  count ~3.4x (r21 to r22) while raising PF from 1.29 to 2.15, i.e. the filter is doing
  real work, not just reducing sample size.
- **r23 (live conviction filter)** is a scaled-down version of r22 (690 vs 1,158 trades),
  still solidly profitable per lot (Rs85.40) though smaller in total.
- t-stats (6.4-9.9) and Calmar ratios (17-32) are far stronger here than in the renko
  search (best there was t = 1.09) - on a longer dataset too (1,414 vs 236 tradable days).

## Caveat

This is a single overnight run read off the finished CSVs, not independently re-verified
(no QC pass on the trade-level data itself, only the PnL/cost arithmetic above). Not being
tracked further per user instruction ("don't have to keep an eye").
