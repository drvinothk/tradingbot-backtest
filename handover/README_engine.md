# backtest_engine — self-contained backtest bundle

Everything needed to run the conviction-strategy backtests, in one folder.
Assembled 2026-09-01 by recovering the e4 backtest VM (`129.159.226.106`)
before its trial-credit cutoff and merging it with the local archive.

**To move to A1: copy this whole folder, run `setup/provision_a1.sh`. Nothing
else is needed.** See `VERSION.txt` for exact provenance.

## Read this first

Before running, changing, or reasoning about any backtest work, read the
**Restrictive rules** and **Efficiency rules** tables below in full. They
supersede any older/looser assumption about how this engine behaves on A1 —
this box also runs live trading, and the rules exist specifically to keep the
two from touching each other.

## Layout

| path | what |
|---|---|
| `backend/scripts/` | the engine (`run_backtest.py`) + every `analyze_*.py` |
| `backend/app/` | strategy/domain code the engine imports (pinned snapshot) |
| `backend/data/historical/` | the whole archive: 1-min options, underlyings, VIX, **and all 749 backtest report dirs** |
| `backend/.env.example` | env template — **`DB_NAME=btengine`, deliberately not `trading_bot`** |
| `run_sweep.sh` | the entry point. Use this. |
| `runners/` | the 33 historical e4 sweep runners, unmodified, as provenance |
| `sweep_configs/` | every phase's config list, Phase 2 → Phase 8 |
| `logs/` | e4 status/master logs for every phase |
| `setup/` | provisioning + the disk-hygiene tooling |

> `runners/*.sh` are kept for reference only. Their relative paths and
> `SHARD_COUNT=28` assume the old 32-vCPU VM — **run `./run_sweep.sh` instead.**

## Install on A1

```bash
scp -r backtest_engine ubuntu@144.24.137.112:~/
ssh ubuntu@144.24.137.112
cd ~/backtest_engine
DB_PASSWORD='pick-one' ./setup/provision_a1.sh
```

## Run a sweep

**DEFAULT HARNESS = PER-DAY, MULTI-TRADE (standing rule; multi-trade made the default 2026-09-26 by user decision). **STATUS: fully DEPLOYED to the box 2026-09-26 ~11:15 IST** (scripts md5-verified; the box had been running the renko10 `mt1` multi-trade sweep until 06:27 IST). Every backtest/sweep runs each trading
day as an isolated fresh-DB replay (`--pairs`, ~224-236 days) with `--multi-trade`: a dispatched position is closed inside the replay at its reconstructed exit,
so a strategy can enter again the same day exactly as it does live/paper (its own per-day/per-direction caps, production's 5-min same-contract re-entry cooldown).
This is the normal, unbiased way to backtest. **Only when the user explicitly asks for "one trade per day"** (a quick, biased, first-signal-only look) run
`ONE_TRADE_PER_DAY=1`. **The one-trade-per-expiry-WEEK harness is permanently OFF** (94% Wednesday-only; it inverted strategy signs, e.g. Renko base +29.4k weekly vs
-14.1k per-day): `run_sweep.sh` / `run_sweep_canonical.sh` now refuse to run and `HARNESS=` is rejected. Always state which harness a number came from; results from
multi-trade, one-trade-per-day and (historical) weekly runs are **never comparable** -- re-run before comparing.

```bash
# per-day MULTI-TRADE (DEFAULT) -- config format name|strategy_type|params_json ; ~35-50 min/config at SHARD_COUNT=4 for a Renko-sized strategy
sudo /opt/backtest/run_bt.sh /bin/bash -c "cd /home/ubuntu/backtest_engine && RUN_TAG=<tag> SHARD_COUNT=4 ./run_sweep_default.sh sweep_configs/<file>.txt"
# one trade per day (first signal only) -- ONLY when the user explicitly asks
sudo /opt/backtest/run_bt.sh /bin/bash -c "cd /home/ubuntu/backtest_engine && ONE_TRADE_PER_DAY=1 RUN_TAG=<tag> SHARD_COUNT=4 ./run_sweep_default.sh sweep_configs/<file>.txt"
```

`run_sweep_default.sh` rebuilds the pair list from the data on disk (`setup/build_perday_pairs.py`: expiry dir E contributes weekdays D with
E-6 <= D <= E that have option rows AND underlying data; ~237 pairs, 25 trading days have no near-week option data and are untradable in
either harness), runs the canonical source-resolution + real `_build_strategy` QC gate, then `run_sweep_perday.sh` (a copy of `run_sweep.sh`
with `--pairs` instead of `--all-expiries`). Results land in `backend/data/historical/backtest_reports/s6_<tag>/`. Parity: a per-day trade
equals the weekly-harness trade on every day both cover (checked 2026-09-25, 50/50 for the Renko base config).
Sizing: per-day takes ~1.5-2x the wall time of a weekly run (~236 replays vs ~52 expiry runs, each a fresh DB; Renko ~47 min/config vs ~28 min).
The raw legacy entry points (`run_sweep.sh`, `run_sweep_canonical.sh`) are the WEEKLY harness and are now disabled (they exit 2 with a message).

(The old weekly `run_sweep.sh` form has been removed from this README on purpose: that harness is OFF. `EXTRA_BT_ARGS='--structure-stop-mode pivot_s1r1'` etc. still pass through `run_sweep_default.sh`/`run_sweep_perday.sh`.)

Analyse:

```bash
./backend/.venv/bin/python backend/scripts/analyze_walkforward.py \
  --dir backend/data/historical/backtest_reports/s6_g9a \
  --configs cfg1,cfg2,cfg3
```

## Restrictive rules — safety & isolation (never violate)

| # | Rule |
|---|---|
| 1 | Launch only via `sudo /opt/backtest/run_bt.sh /bin/bash -c "cd /home/ubuntu/backtest_engine && RUN_TAG=<tag> ./run_sweep.sh sweep_configs/<file>.txt"` — detached (`systemd-run`, no `--wait`) and `backtest.slice`-capped. Never run `run_sweep.sh` bare, never in a foreground SSH session, never add `--wait` back to the launcher. Safe to close the laptop/SSH client right after launching — the run survives it. |
| 2 | Session separation is absolute: never edit trading-app files from a backtest session, never edit `backtest_engine/` from a trading-app session — separate dirs (`/home/ubuntu/trading-bot` vs `/home/ubuntu/backtest_engine`), separate purposes. Never run migrations, `alembic`, or app-restart commands from a backtest session. |
| 3 | `.env`/`DB_NAME` always `btengine`, never `trading_bot`. `btengine` has no `CONNECT` grant on `trading_bot` (revoked from `PUBLIC` 2026-09-01) — re-apply the same revoke if a new DB/role ever appears on the box. |
| 4 | `app/` in this bundle is a **pinned snapshot** (see `VERSION.txt` for the current commit) — never auto-sync it from the live `trading-bot` deploy, and keep it pinned across an entire sweep series so results stay comparable, not just reproducible. A deliberate re-pin (e.g. a sweep needs code that didn't exist at the old pin) is fine — when doing one, **exclude `app/config/credentials/*.env` and `.alice_blue_session_cache.json`** from whatever copies `app/` over. Both are gitignored, so `git`-based tooling naturally skips them, but a plain filesystem `tar`/`scp`/`rsync` of `app/` does not — it will copy live broker credentials into the bundle. |
| 5 | Never touch shared Postgres **server** config (`wal_sync_method`, `checkpoint_timeout`, `max_wal_size`, `shared_buffers`) — same cluster as live trading; any of these needs a `postgresql.conf`/`ALTER SYSTEM` change + reload-or-restart of the **whole instance**, which is exactly the coupling the "no second cluster" decision avoided ([[project_backtest_a1_deployment_2026_09_01]]). `fsync = off` is rejected outright, always — server-wide, would strip crash-safety from live trading's own data too. |
| 6 | `SHARD_COUNT`: **4 off-hours (tested ceiling — do not exceed), 2 during market hours (09:00–15:30 IST)** — halved because Postgres itself runs unconstrained in `system.slice`, so a heavy shard commit-storm can still pressure live-trading IO/checkpoints even though the Python workers are cgroup-capped. |
| 7 | **2026-09-19: the 100% cap (and this rule's window) applies only on NSE trading days (Mon–Fri, not an NSE holiday)** — `backtest-market-open.timer` is `Mon..Fri` and its service now runs `/opt/backtest/set_quota_for_now.sh`, which also skips NSE holidays via a read-only lookup of the live app's `market_holidays` table (lookup failure ⇒ treated as a trading day ⇒ 100%). Weekends, holidays and off-hours stay at 200%, so rule 6's "2 shards during market hours" only binds on trading days (backups `*.bak-20260919*`). Prefer running sweeps outside **09:00–15:30 IST** (the same window `backtest.slice`'s `CPUQuota` timers flip on) — don't override the quota manually during that window. |
| 8 | Keep `MIN_FREE_GB` at 15 or higher (`disk_guard.sh` default) — never lower it. A full disk on A1 takes the live trading service down with it. |
| 9 | **Warn at 12 GB total backtest footprint (A1 + local `backtest_engine\`), then again every +5 GB after** (17, 22, 27 GB...) — check with `du -sh`; reap orphan DBs (`setup/reap_backtest_dbs.sh --apply`) and prune old `backtest_reports/` dirs if over. |
| 10 | Never run two `run_sweep.sh` invocations concurrently — both hit the same shared Postgres instance and multiply commit contention instead of parallelizing cleanly. |
| 11 | Save and leave results on the VM (`data/historical/backtest_reports/`) — don't routinely `scp` full result sets back to Windows; pull only the specific merged CSVs you need for local analysis. |
| 12 | Confirm `trading-bot.service` / live positions are unaffected after any long sweep: `systemctl status trading-bot`, check `/strategies/running` still polls normally. |
| 13 | **Stop `backtest-reaper.timer` (`sudo systemctl stop backtest-reaper.timer`) before launching any sweep; re-enable it (`sudo systemctl start backtest-reaper.timer`) only once the whole sweep series fully completes and results are pulled — never on an interim download mid-sweep.** The reaper force-drops (`DROP DATABASE ... WITH (FORCE)`) any database matching the backtest naming pattern with **no check for active connections** — including a currently-running sweep's own in-progress shard databases. `run_sweep.sh`'s own per-config reaping (between configs, plus its exit trap) is unaffected by stopping the timer and is what actually keeps disk usage in check during a run. **Cadence changed 2026-09-02: daily at 16:00 IST (was hourly)** — disk headroom (~300 MB/shard, tens of GB free) makes hourly unnecessary; `Persistent=true` means a resume after a paused sweep that missed that day's 16:00 slot fires an immediate catch-up run instead of waiting until the next day — safe by construction, since resume only ever happens once nothing is active. |
| 14 | Before spending compute on a sweep that tests a `strategy_configs.params` key that didn't exist at the last `app/` pin, verify `_build_strategy` actually constructs every config line in the file — `run_backtest.py` imports the real production `_build_strategy`, whose PARAM_KEYS filtering **silently ignores** unrecognized keys rather than erroring. A typo'd or stale param produces a normal-looking result with the intended gate/param simply never applied, not a visible failure. |
| 15 | After `scp`-ing an updated file to the bundle (a sweep config, a re-synced `app/` tree), verify with a checksum (e.g. `md5sum`) that what landed matches the local source before launching anything against it — a stale copy on the box from an earlier sync is a silent failure mode, not something `run_sweep.sh` can detect on its own. |
| 16 | **A chain-watcher script (one sweep phase auto-launching the next on completion) must never call `sudo /opt/backtest/run_bt.sh` a second time from inside its own already-running unit.** Confirmed live 2026-09-15: a process spawned by systemd (the chain-watcher's own unit) has no logind session, so a nested `systemd-run` call to create a NEW transient unit fails with `Failed to start transient service unit: Interactive authentication required` — NOPASSWD sudo (`(ALL) NOPASSWD: ALL`, confirmed present) does not help, since this is polkit rejecting the D-Bus call, not sudo asking for a password. It fails the same way regardless of whether the watcher itself is already correctly placed in `backtest.slice`. Fix: launch the chain-watcher itself via `run_bt.sh` (so it inherits `backtest.slice` from the start), and have its own final step be a plain `exec ./run_sweep_canonical.sh ...` — no second unit, nothing for polkit to reject. See `chain_p21.sh`/`chain_p22.sh` for the corrected pattern. First hit 2026-09-15: a chain from p20→p21→p22 sat idle for ~1h45min because p21's launch attempt failed silently (logged, but nothing alerted) while its own unit exited with `status=1/FAILURE`. |
| 17 | **Default harness = PER-DAY MULTI-TRADE (`run_sweep_default.sh`).** `ONE_TRADE_PER_DAY=1` (first signal per day, biased) only when the user explicitly asks; the weekly one-trade-per-expiry-week harness (`run_sweep.sh` / `run_sweep_canonical.sh` / `HARNESS=`) is permanently OFF (refuses to run; 94% Wednesday-only, inverted strategy signs). Always state which harness a number came from; never compare numbers across harnesses. Sweeps still follow rules 1, 6, 10, 13 (launcher, shard limits, one sweep at a time, reaper timer). |
| 18 | **`--multi-trade` (2026-09-26, DEPLOYED to the box, md5 `8de4eabc…`; made the sweep default the same day).** Closes each dispatched position inside the replay at its reconstructed exit (`run_backtest.py --multi-trade`; `run_sweep_perday.sh` adds it unless `ONE_TRADE_PER_DAY=1`; a bare direct `run_backtest.py` call without the flag is still first-signal-only). Needs `--exit-mode current` and single-day runs (`--pairs`/`--dates`). Production's 5-min same-contract re-entry cooldown is ON via a simulated clock (`--no-reentry-cooldown` to disable, `--reentry-lag-bars N` for a conservative release lag). Strategies with no own per-day cap (EMA micro-pullback fired up to 16x/day in the smoke) are effectively uncapped -- open item, see `docs/ops/plan_backtest_multi_trade_2026_09_25.md`. **Never edit `run_backtest.py` / any `run_sweep*.sh` in place while a `backtest-*` unit is running**: later configs of a running chain start fresh processes and would load the new file. |
| 19 | **`--extra-warmup-days 12` (launch_chain default; 21 = 2.4x slower, same ATR/EMA to <0.4%) for every `renko_trend` (and any multi-day-history strategy) run (2026-09-26).** The per-day DB only holds the last 1000 bars (~4 trading days) while the strategy reads 20 calendar days of ATR14/EMA history, so brick sizes/EMAs differ from production (ATR configs most). The flag persists N older days as PriceBar rows only (default 0 = byte-identical to before). Set `EXTRA_BT_ARGS="--extra-warmup-days 12"` (the `launch_chain.sh` chain does it). Results with and without it are not comparable; label the harness "multi-trade + warm-up". Unattended runs: use `launch_chain.sh` (md5 freeze, chunk QC, END_BY guard) -- launch it from a script file, not an inline `ssh ... pgrep`-containing command (its single-instance check would match the ssh command line). |

## Efficiency rules — performance (apply when it helps)

| # | Point |
|---|---|
| 1 | **RAM does not speed this up.** Real usage is ~100–200 MB/shard (<300 MB total, confirmed live); the 4 GB cgroup cap is already ~13x headroom. Don't chase more RAM — the box's 12 GB total is fixed by Oracle's free tier anyway. |
| 2 | **The real bottleneck is Postgres commit I/O (one commit per bar), not CPU or RAM.** This is *why* shard count can usefully exceed OCPU count — a shard waiting on a commit round-trip isn't burning CPU quota, so other shards can use that gap. |
| 3 | `CPUQuota` on `backtest.slice` is a shared budget for the *whole slice* (100% ≈ 1 core market hours, 200% ≈ 2 cores off-hours), not per-shard — it doesn't map cleanly to "N shards per OCPU." |
| 4 | **Per-config time at `SHARD_COUNT=4` on A1 is confirmed and strongly strategy-family-dependent, not a single number.** `vwap_pullback`/`vwap_pullback_conviction` (fewer trades/evaluations per year): ~6.3–6.7 min/config. `ema_micro_pullback_conviction`, `orb`/`orb_conviction`, `oi_volume_confirmed`/`oi_volume_confirmed_conviction`, `liquidity_sweep_reversal_conviction`: ~22–25 min/config. Budget a sweep's total time from these per-family rates × config count, not a flat per-config estimate — a mixed-strategy sweep list should be summed family-by-family. |
| 5 | Off-hours sweeps get the full 200% CPU quota *and* zero live-trading Postgres IO contention — the single biggest speed lever available today, and the same window restrictive rule 7 already requires. |
| 6 | **The fix worth actually building, if speed becomes a real priority**: batch commits per-day or every 5,000–20,000 bars instead of per-bar in `run_backtest.py` — directly targets the confirmed bottleneck, 100% code-scoped, zero shared-server risk. (A secondary idea in the same spirit: `UNLOGGED` tables for the per-shard DB, since it's dropped after every run anyway — smaller win, same "code change, not config" caveat.) Needs its own before/after timing proof either way. |
| 7 | Also safe, connection-scoped, no shared-server risk: `SET synchronous_commit = off` and a larger `work_mem`/`maintenance_work_mem` on the backtest's own DB connection only (smaller during market hours, larger off-hours) — the per-shard DB is dropped after every run anyway, so there's nothing durable to lose. |

## Disk hygiene — the mechanism behind restrictive rules 8–10

`run_backtest.py` creates **one Postgres database per shard** and never drops
it. A 28-shard sweep of 5 configs leaves 140 behind. On the e4 this reached
**202 orphan databases / 4.0 GB** before anyone noticed. The sweep runners reap
between configs, but anything that dies mid-run (SSH drop, OOM, Ctrl-C) leaks
its databases permanently.

Three layers, all included:

1. **`run_sweep.sh` reaps between every config and on exit** (`trap`), same as
   the e4 runners did.
2. **`setup/disk_guard.sh N`** — refuses to start a sweep below `N` GB free
   (default 15), reaping first and aborting if that isn't enough. `run_sweep.sh`
   calls it automatically.
3. **`setup/backtest-reaper.{service,timer}`** — daily (16:00 IST) systemd
   safety net that catches anything the first two miss. `provision_a1.sh`
   enables it (originally hourly; changed to daily 2026-09-02, see
   restrictive rule 13).

Manual use:

```bash
./setup/reap_backtest_dbs.sh           # dry run — lists what would be dropped
./setup/reap_backtest_dbs.sh --apply   # actually drop
```

### Why the reaper is safe to run on the live box

A1 also hosts the **live trading Postgres**. The reaper:

* matches with POSIX regex `^<DB_NAME>_backtest_`, **not SQL `LIKE`** — in
  `LIKE`, `_` is a single-char wildcard, so `'trading_bot_backtest_%'` would
  also match `trading_botXbacktestY`;
* hard-refuses `postgres`, `template0`, `template1`, `<DB_NAME>`,
  `<DB_NAME>_test`, filtered again in shell after the query returns;
* is scoped to `DB_NAME=btengine`, so it cannot even see `trading_bot*`.

That last point is the real protection: **the bundle uses its own `DB_NAME`, so
no backtest database ever shares a namespace with production.**

## Access — SSH, DB, full engine access

| What | Value |
|---|---|
| Box | `A1_2CPU_12GBRAM_Trading`, `144.24.137.112` (`https://144-24-137-112.sslip.io`) — same box as live trading |
| SSH | `ssh -i "D:\Documents\Trading Bot_Oracle\ssh-key-2026-08-03_Pvt Key.key" ubuntu@144.24.137.112` |
| SSH user | `ubuntu` (not `opc`/`root`) |
| Engine path | `/home/ubuntu/backtest_engine` |
| Venv | `/home/ubuntu/backtest_engine/backend/.venv` (own venv, aarch64 wheels, rebuilt by `provision_a1.sh` — never reuse the e4 x86_64 one) |
| DB | Postgres, same cluster as live (`:5432`), role/DB **`btengine`/`btengine`** — no `CONNECT` grant on `trading_bot` |
| Launcher | `/opt/backtest/run_bt.sh` (requires `sudo`; wraps `systemd-run --slice=backtest.slice`) |
| Logs | `journalctl -fu backtest-<timestamp>` for a live run; `logs/` in the bundle for historical e4 logs |
| From a sandboxed Claude session | copy the key into the session scratchpad and `chmod 600` it first — Windows file perms aren't usable as-is for SSH's strict check |

## Not included, on purpose

* `.venv` / `an_venv` from the e4 — **x86_64, useless on ARM**. `provision_a1.sh`
  rebuilds from `pyproject.toml`.
* Broker credentials. The backtest replays a CSV archive and needs none.
