---
name: project-backtest-multi-trade-engine-2026-09-26
description: "FULLY DEPLOYED 2026-09-26 ~11:15 IST + validated by the mt1 sweep. 2026-09-26: `--multi-trade` (backtest closes Positions in-replay so a strategy can trade >1/day) built, QC'd and DEPLOYED to the A1 backtest bundle (~01:00 IST 09-26, md5 8de4eabc…); default OFF; docs on main (5fca325). STOP_PERDAY flag on the box left in place."
metadata:
  type: project
---

Root cause of 1-trade/run: `ConfirmationFilterStrategy.evaluate` returns None while `get_open_position_for_run` is non-None, and the engine reconstructs exits offline so no Position ever closes (risk is NOT the blocker, risk-rejected = 0).

Fix: reconstruct each approved trade once at signal time (shared nested `_reconstruct_current`), close the Position at the exit bar with production `close_position_from_external_fill`, simulated `risk_engine.service._utcnow` so the universal 5-min same-contract re-entry cooldown works (`--no-reentry-cooldown`, `--reentry-lag-bars N`). Requires `--exit-mode current` + single-day runs. Full plan/QC/results: docs/ops/plan_backtest_multi_trade_2026_09_25.md (branch docs/backtest-multi-trade-2026-09-26, worktree ../tb-mt-docs). Ledger entry 2026-09-26 in bundle BACKTEST_LEARNINGS.md; README rule 18.

Proof (6 days): flag off = byte-identical CSV; first trade/day identical ORB+EMA; 0 overlaps; mutation (clock patch removed) killed. Deliverable md5 `8de4eabc631dc4c85f7603e0e4e9dbd1`; pinned original `c115d5309a57a659f45b9ad729e53a9c` (backup `run_backtest.py.pre-mt-20260925`). Staged `run_sweep_perday.sh.staged` (scratchpad) adds `MULTI_TRADE=1`.

**Deployed 09-26 ~01:00 IST** (box idle: night2 chain had been stopped by a `STOP_PERDAY` flag file someone else created; left in place — delete `~/backtest_engine/STOP_PERDAY` to resume per-day sweeps). Backups `~/deploy-bak/*.bak-20260926-multitrade`; README/VERSION/ledger synced; box ORB 2-day smoke == local. Still to do: one VWAP/OI/Sweep/Renko smoke with `MULTI_TRADE=1`. Rule kept: never edit run_backtest.py / run_sweep_perday.sh in place while a backtest-* unit runs (later configs load the new file).

Open decisions for the user: default `--multi-trade` in `run_sweep_default.sh`? per-day trade cap for uncapped strategies (EMA fired up to 16x/day; `max_trades_per_day` is live-scoped)? re-run pre-09-23 PE-side conclusions. Links: [[project_backtest_engine_pe_structure_break_bug_2026_09_23]].

**2026-09-26 ~02:00 IST — made the DEFAULT (user):** multi-trade per-day is the default harness, `ONE_TRADE_PER_DAY=1` opt-out, weekly OFF. Scripts (`run_sweep_default.sh`, `run_sweep_perday.sh`, `run_sweep.sh`, `backend/scripts/run_sweep_canonical.sh`) edited + tested LOCALLY only; box deploy PENDING (another session's `launch_mt1.sh` renko10 multi-trade sweep, tag mt1, was running; STOP_PERDAY was removed by them). Docs on main (e3974d7). Pending items 1-6 in the plan doc's last section; launchers calling run_sweep_canonical.sh (launch_renko7/8/9, launch_night2 B) now refuse.

**2026-09-26 ~11:30 IST — FULLY DEPLOYED + validated.** After the mt1 renko10 sweep finished (06:27 IST, 6/6 OK; STOP_PERDAY removed by its owner) the four default-change scripts + README/VERSION/ledger were scp'd to the box, md5 box == local, refusals + DRY_RUN default path re-tested, backups ~/deploy-bak/md-20260926/. mt1 validated the engine: first trade/day == one-trade/day result (parity 236/236 base); re-entries lose -62k..-160k in every 5/15-min-brick candle-exit config; only ATR-sized s1_top positive (+10.7k gross, cost-adj ~0). Docs on main (af99e51). Remaining = pending list items 1-6 in the plan doc (per-day cap, PE re-runs, family smokes VWAP/OI/Sweep, defaults confirm, re-baseline old numbers, stale handoff mentions); launchers calling run_sweep_canonical.sh (launch_renko7/8/9, launch_night2 B) refuse until repointed.
