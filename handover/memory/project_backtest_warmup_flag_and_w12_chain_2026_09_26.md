---
name: project-backtest-warmup-flag-and-w12-chain-2026-09-26
description: run_backtest.py --extra-warmup-days (ATR/EMA 20-day history fix), why mt1 ATR/EMA results are approximate, and the unattended w12 chain (pilot + 24 configs)
metadata:
  type: project
---

Per-day harness only persisted the last 1000 underlying bars (~4 trading days) but renko_trend reads 20-calendar-day ATR14(30-min) brick size and EMA history from price_bars -> brick size/EMA differ from production (mean 1.9%, max 16%; band [10,60] flips 5 days; s1_top bricks are ~55-60pt, near max band). Explains the 13/33 s1_top weekly-vs-per-day mismatch. Fix: `--extra-warmup-days 21` (opt-in; default 0 byte-identical, verified vs mt1 rows; PriceBar-only bulk insert). Engine md5 587fefca (was 8de4eabc; the other session owns this file - tell them). Use `EXTRA_BT_ARGS="--extra-warmup-days 21"` for ALL renko_trend runs from now; label "multi-trade + warm-up"; never compare with mt1 numbers (mt1 base/mt3 ATR/EMA are approximate). Controls w12_base_ctrl / w12_s1top_ctrl in the batch measure the effect.

**Why:** user asked (2026-09-26) for precautions so the ATR warm-up issue is not missed on any test before a 28h unattended run.
**How to apply:** for any new renko/HTF-indicator sweep add the flag; guard chain = `launch_chain.sh` (TAG, END_BY_UTC, md5 freeze, chunk QC). w12 chain launched 2026-09-26 11:38 IST: pilot renko11 + renko12a..d, results s6_w12*, heartbeat logs/w12_chain.heartbeat. Details in backtest_engine/RENKO_HANDOFF_2026_09_24.md (last section). Related: [[feedback-backtest-default-harness-per-day-2026-09-25]], [[project_backtest_multi_trade_engine_2026_09_26]].
