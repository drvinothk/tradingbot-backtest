---
name: project-2020plus-data-deployed-verified-2026-09-28
description: "NIFTY 2020+ vendor options data deployed to box + verified end-to-end (combined_2020 underlying source, md5 356260ad). Prior session did the local merge only; this session deployed+verified+wired the engine."
metadata:
  type: project
---

Prior LOCAL-only session merged vendor NIFTY options data (297 expiry folders, 2020-01-02..2025-08-21, `NIFTY_vendor_index_1min.csv`) into local `backend/data/historical/` and reported "ready for backtesting" -- true for local, but the box (separate machine, nothing auto-syncs) still only had the old ~1yr data. This session: independently re-verified the merge (both documented defects confirmed fixed, COVID-low cross-checked against public record 7511.10 exact, file format confirmed compatible), built `underlyings/NIFTY_combined_2020_1min.csv` (vendor+alice_index stitched, alice preferred in the 2023-06-13..2025-08-21 overlap per the vendor read-me's own rule) + a new `--underlying-source combined_2020` engine flag (byte-identical-verified vs alice_index alone on shared dates), deployed the 7.8GB options data + combined CSV + engine (md5 `356260ad…`) to the box, ran a real end-to-end 2020 smoke test (incl. COVID crash week) -- clean, 20 sensible trades.

**Coverage now on box: NIFTY options 2020-01-02..2026-09 (355 expiry dirs), spot 2019-11-01..2026-09-18. NIFTY only (no BANKNIFTY).** OI unreliable before Sep 2020 (vendor's own caveat) -- don't trust OI/PCR-gated strategies pre-Sep-2020.

**Data limitations + 8 market-regime archetypes doc**: `backtest_engine/NIFTY_DATA_README_2026_09_28.md` (also on box, also in cloud-channel repo `handover/`) -- ADX/vol/efficiency-ratio recipe for classifying trading regime, useful for tagging backtest trades by archetype (config-selection tool, NOT an entry gate -- a 2026-09-21 study already found 5/7 day-regime hard-filters hurt net P&L).

**Not yet run**: any real strategy sweep on the 2020+ range -- this was pipeline verification only. Next: 2023-2025 first (higher-confidence years), ~3h/config at current (post-lookup-cache-fix) speed.

Related: [[project_backtest_lookup_cache_speedup_2026_09_28]], [[project_w13_w14_renko_results_2026_09_27]], [[project_backtest_warmup_flag_and_w12_chain_2026_09_26]].
