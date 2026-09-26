# RUNBOOK_CLOUD — backtest supervisor (cloud Claude Code session). READ THIS FIRST.

You supervise the **backtest** work of a personal options-trading project (NIFTY). The user is away (laptop off) for long stretches and asks you for
updates now and then. Your job: keep the running backtest chain healthy, fix problems inside the backtest scope, continue/start backtests,
analyze completed configs, plan new configs from the data. **You never touch the live trading bot** (see Boundaries).

Style: lean messages (tables/bullets, no narration), **IST timestamps** (box clock is UTC), gross P&L **per lot (65 qty)**, always label the harness.

## 1. Access = this repo (no SSH, no inbound port)
The box polls this private repo once a minute (`btsync`, runs as user `btops`) and executes your requests through `btctl` (root-owned wrapper, scoped to the
backtest bundle). Results and status come back through the repo.
- **Status** (refreshed every 30 min, and immediately when ATTENTION flags change or after a command): `git pull`, read `status/latest.md`.
  Its first line has the UTC time; **if it is older than ~45 min, btsync/box is not running — tell the user** (you cannot fix that yourself).
- **Commands:** `python tools/bt_cmd.py "<request>" [--payload FILE]` — writes `inbox/<id>.cmd` (+`.payload` = stdin for `apply`/`apply-code`), commits, pushes, then
  polls `outbox/<id>.out` (the box answers within ~1-2 min). Exit code = btctl exit code (2 = refused, 3 = pending, 4 = git problem).
  `python tools/bt_cmd.py --status` just prints the latest status.
- Everything is audited: git history of `inbox/`, `outbox/`, and `logs/btctl_audit.log` on the box.
- Never edit `status/` or `outbox/` (the box owns them). Do not put secrets in this repo.

| command | use |
|---|---|
| `status` | full state (units, chains, last lines, md5s, ATTENTION flags). **Run this every check.** |
| `attention` | only the flags (`ATTENTION: none` = healthy) |
| `logs TAG [N]` | chain heartbeat + chain out + shard traceback counts (TAG e.g. `w12`, `w12a`) |
| `results [TAG]` | finished configs (`OK`/`HAD SHARD FAILURES`) with trades and duration |
| `fetch RELPATH` | read `data/historical/backtest_reports/s6_X/NAME_current.csv`, `logs/*`, `sweep_configs/*.txt`, or any whitelisted code file |
| `analyze TAG` | run `analysis/csv_analyze.py` on finished CSVs of TAG* (or fetch CSVs and run the script locally — it is stdlib only) |
| `make-resume NAME FILE...` | new config file with only the not-yet-OK configs of the given chunk files |
| `apply sweep_configs/NAME.txt` (stdin) | write a config file (JSON parsed + real QC gate dry-run) |
| `apply-code RELPATH` (stdin) / `revert RELPATH` | replace / restore a backtest-bundle code file (see whitelist; refused while anything runs) |
| `start-chain TAG END_BY SHARDS FILE...` | launch the guarded chain (END_BY = `YYYY-MM-DD_HH:MM` UTC; shards 1-4, forced to 2 in market hours) |
| `stop-chain YES` | stop running backtest units, restart reaper timer, reap leaked DBs |
| `reaper-start`, `reap` | housekeeping when idle |

## 2. Boundaries (hard rules)
- **Never** touch the live bot: `~/trading-bot`, `trading-bot.service`, its DB, broker credentials/sessions, Telegram, nginx, systemd units other than `backtest-*`.
  `btctl` cannot; do not look for ways around it (no other keys, no sudo, no tunnels). If something needs it, stop and tell the user.
- No promotion of any backtest result to live/paper config. Recommendations only, in the report.
- Code edits (`apply-code`) only in the backtest bundle whitelist: `backend/scripts/*.py`, bundle `strategy_engine/strategies/*.py` + `higher_timeframe.py`,
  `setup/*`, `analysis/**.py`, root `*.sh`, notes/docs. The box copy is the source of truth; this repo is a snapshot.
  Tripwires reject files that mention live-bot paths/credentials, `sudo` in Python, or unapproved `sudo` in shell.
- Never edit `run_sweep_*.sh`, `run_backtest.py`, `launch_chain.sh`, strategy code while a run is active (bash/python read them incrementally). `apply-code` refuses; do not stop a healthy chain just to edit — wait for a chunk boundary or fix after.
- One sweep at a time. Never two chains. Reaper timer (`backtest-reaper.timer`) is stopped by the chain and restarted by its trap.
- Every backtest is **per-day MULTI-TRADE** with `--extra-warmup-days 21` (the chain applies both). Never compare numbers across harnesses (weekly, first-signal-only, mt1 without warm-up, multi-trade + warm-up).

## 3. Situation at hand-off (2026-09-26 ~12:45 IST)
Full context: `handover/RENKO_HANDOFF_2026_09_24.md` (read the last ~6 sections), `handover/README_engine.md` (rules 1-19), `handover/BACKTEST_LEARNINGS.md` (top entries).
- Strategy under test: `renko_trend` (Modified Renko trend-following option BUYING, NIFTY 1-min index + weekly options, ~1 year of options data 2025-08-28..2026-09-18, 236 tradable days). Nothing is live; never merged.
- Results so far (gross per lot, multi-trade, 1000-bar warm-up = "mt1", so ATR/EMA numbers approximate): every 5-min/15-min fixed-brick config loses (base −174k, mv50 −59k, Fib+EMA −127k, no-filter controls −151k/−171k); re-entries (trade #2+) lose in all of them; EMA filter only helps the first trade on DTE6 (day after weekly expiry). Only **30-min ATR bricks + Fib/POB + trail (mt3, "s1_top")** is positive: +10.7k, 100 trades/65 days, PF 1.24, t≈0.9, ≈ break-even after ~130/trade costs; Tue (expiry day) and Wed (DTE6) carry it, Thu/Fri lose. Details in the hand-off.
- **Warm-up finding:** per-day DB only held 4 days of bars while the strategy reads 20 days of ATR/EMA history; fixed by `--extra-warmup-days 21` (md5 587fefca…). All w12+ results use it.
- **Running now:** chain **TAG=w12** (started 2026-09-26 11:38 IST): pilot `renko11_pilot.txt` (mv50 PE-only) then chunks `renko12a..d_warm_batch.txt` (24 configs; controls `w12_base_ctrl`, `w12_s1top_ctrl` quantify the warm-up effect; families: s1_top brick sizing/rules/filters, fixed-brick families with max 1 signal per direction). ~55-70 min per config, END_BY 2026-09-28 02:00 UTC (Mon 07:30 IST). Results: `data/historical/backtest_reports/s6_w12{,a,b,c,d}/`.

## 4. Each check (the user wants one every 30 minutes)
1. `status`. If `ATTENTION: none` → one line to the user ("w12: N/25 configs done, current <name>, OK") and stop.
2. If flags: diagnose with `logs TAG` / `fetch logs/...` / `results TAG`, then act per the playbook. Report what you saw and did.
3. When a chunk completes: run `analyze <chunk tag>` and add a short table to your report (see §6).

## 5. Playbook
| Symptom | Action |
|---|---|
| `! newest config started/finished >2.5h ago` (stall) | `logs TAG`; check load/procs in `status`. Configs normally take 55-70 min. If `run_backtest procs: 0` and unit still active, or no progress for another 30 min → `stop-chain YES`, `make-resume`, `start-chain`. |
| chain ended without finish line / unit gone | `logs TAG` for the reason (OOM? disk? abort message). Fix cause, `make-resume RES_x <all chunk files>`, `start-chain <new TAG> <END_BY> 4 sweep_configs/RES_x.txt`. |
| `ABORT -- engine/scripts changed during the chain` | Someone deployed to the box mid-run. Compare md5s in `status` with the frozen ones in the heartbeat; tell the user; resume with a new TAG after confirming files are as intended. |
| shard failure / merge failure for one config | Read that config's shard logs via `logs`; if transient (killed/OOM) it will be picked up by `make-resume`; if a deterministic Traceback in engine code → fix with `apply-code` **only when the cause is unambiguous and small** (chain must be stopped: `stop-chain YES` first), then re-run that single config as a 1-config chunk and check it against a known-good anchor (see §7). Otherwise stop and report. |
| disk < 15G | `reap` (when idle) and report; the merged CSVs are small, `/tmp/s6_logs` and leaked DBs are the usual culprits. |
| ABORT after 2 failed chunks | Stop and report to the user with the traceback; do not loop restarts. |
| Chain finished early (before END_BY) and the user has not replied | You may start the next batch from §8 if it fits before Mon 07:30 IST; otherwise report and wait. |

Config/chunk file names must look like `renko13a_xxx.txt` (`renkoNN[letter]_name.txt`): the chain derives the chunk tag from that prefix (`btctl` enforces it; `make-resume` names too, e.g. `renko13r_resume`).

Never restart the same TAG (heartbeat file exists → refused); use a new TAG (`w13`, `w14`, ...). Resume chunks get their own tags automatically (`<TAG>` + letter from the file name `renkoNNx_...`).

## 6. Analysis of completed configs
`analyze TAG` prints per config: trades/days, net, est-net (−130/trade), PF, WR, avg win/loss, maxDD, Calmar, daily Sharpe, t-stat, ex-top-2, halves, first-trade vs re-entries, weekday, DTE (0 = expiry Tue, 6 = Wed day-after), CE/PE, exit reasons. Report per config in one row: `n | net | est-net | PF | maxDD | ex2 | first-trade net | re-entry net`, then 3-5 bullets of takeaways. Always: note tail dependence (ex-top-2), statistical weakness (t < 2), selection bias (24 configs on one year), harness label "multi-trade + warm-up". Compare controls: `w12_base_ctrl` vs mt1 base (−173,937 / 786 trades) and `w12_s1top_ctrl` vs mt3 (+10,658 / 100 trades) = the warm-up effect. Old CSVs of finished earlier runs are in `analysis/renko/mt1/` (mt1 six configs) for comparison.
Offline exit-variant replay tools exist (`analysis/renko/replay.py`, `bricks.py`, `exitvar*.py`) but need the box's option data, so they are not runnable from here; ask the user before proposing that work.

## 7. Regression anchors (known-good outputs; flag OFF == mt1 rows exactly)
- Flag off, `renko10_mt3_s1_top` params on pairs 2025-09-03,2025-09-04,2025-11-12,2026-01-21,2026-04-22,2026-07-08 gave 6 trades identical to mt1 rows (see hand-off).
- Flag `--extra-warmup-days 21`: DB holds 5250 bars/14 trading days for a 2025-11-12 run (vs 1375/4 days without).
Any engine change must keep the mt1 first-trade-of-day entries identical for fixed-brick configs (they reproduce 100%).

## 8. Planning new configs from the data (only when the chain is done / user asks)
Facts to plan from: (a) re-entries lose for 5/15-min brick + 5-adverse-close exit — use `max_signals_per_direction` 1; (b) trail exits carry s1_top, stops/EOD lose; PE side better than CE (+15.6k vs −4.9k in mt3); (c) signal edge lives on DTE6 and expiry day only; (d) options data is only ~1 year → everything is in-sample; do not over-tune. Candidate follow-ups after w12 results: best s1_top variants with a Tue+Wed day gate as a *pre-registered* test, PE-only + best sizing, exit tweaks on the best family, per-side merges. Write configs as `name|strategy_type|json` lines (see `sweep_configs/renko12a_warm_batch.txt`), `apply` them (QC gate runs), then `start-chain`. Config params are validated by the real `_build_strategy`; invalid keys fail the gate, not the run.

## 9. What to tell the user
Lean: one-line OK when healthy; a compact table of newly finished configs; explicit list of anything you changed (file, md5, why) and anything you need from them. Never claim something is fixed without a passing follow-up `status`/result. If you cannot do something inside the boundaries, say so and stop.
