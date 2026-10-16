# Cloud session settings — ATR/PDT grid watch session

Written 2026-10-16 so anyone looking for this cloud session (or resuming the work) knows how it is set up.
**No secrets in this file.** The SSH private key the operator uploaded is NOT stored here (or anywhere in this repo).

## Session
| Item | Value |
|---|---|
| Title | SSK info cloud session |
| Session ID | `session_01AcQbvAjZr3EjCTDrJ7foPD` |
| URL | https://claude.ai/code/session_01AcQbvAjZr3EjCTDrJ7foPD |
| Environment | `env_013XjaAn1KGbETBxsk5VsgEy` (Anthropic cloud) |
| Origin | desktop app |
| Created | 2026-10-01 18:43 UTC |
| Model | claude-sonnet-5-5 (configured), effort high |
| Permission mode | auto |
| Repo / branch | `drvinothk/tradingbot-backtest` / `claude/inspiring-cori-m2x8dj` |
| PR policy | draft PR auto-created on push (`config:auto-create-pr:draft`) |

## Network (important)
- Outbound is **HTTPS via proxy only**. Raw TCP **SSH to the box (`144.24.137.112:22`) times out** from this session.
- So the "SSH in" route in `atr_pdt_grid_handoff_2026_10_01.md` does not work here. Use the **repo channel** instead (below).
- To allow SSH, the operator would have to widen the environment's Network access (environment menu in the session title bar -> Edit) — port 22 may still not pass an HTTPS-only proxy.

## How this session talks to the box
Per `RUNBOOK_CLOUD.md`: box polls this repo every minute (`btsync`), runs requests through `btctl`.
- Read status: `git pull origin main`, then `status/latest.md` (first line = UTC time; > ~45 min old => btsync/box down, tell the operator).
- Send commands: `python tools/bt_cmd.py "<request>"` (or `--status`).
- Never touch the live bot (`~/trading-bot`, `trading-bot.service`) — see RUNBOOK_CLOUD.md Boundaries.

## State at write time (2026-10-16 13:12 IST, from `status/latest.md`)
- No backtest units running, 0 `run_backtest` procs, reaper timer active, 5 leaked backtest DBs (housekeeping: `reap`).
- Last chains finished cleanly (rc=0): `par_a1`, `vc_old`, `vc_new` (14 Oct).
- The ATR grid (r31-r37) hand-off is from 2026-10-01; its result CSVs are under `backend/data/historical/backtest_reports/s6_r3{1..7}/` on the box. Not verified from this session.

## Resuming
1. New session on this repo: read `RUNBOOK_CLOUD.md`, then this file, then `status/latest.md`.
2. Run `python tools/bt_cmd.py "results r3"` style checks via the repo channel to confirm grid completion.
3. Report plainly: finished?, any intervention?, live bot healthy? (`attention` flags).
