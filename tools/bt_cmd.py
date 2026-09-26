#!/usr/bin/env python3
"""Send a btctl request to the backtest box through this repo and print the result (stdlib only).

  python tools/bt_cmd.py "status"                               # request string = a btctl command (see RUNBOOK_CLOUD.md)
  python tools/bt_cmd.py "logs w12 60"
  python tools/bt_cmd.py "apply sweep_configs/renko13a_x.txt" --payload sweep_configs/renko13a_x.txt   # payload -> btctl stdin
  python tools/bt_cmd.py --status                               # just show status/latest.md (pulled) and its age
Flow: writes inbox/<id>.cmd (+ .payload), commits + pushes; the box (btsync, every ~60 s) runs it and pushes outbox/<id>.out; this script
polls until it appears (default 300 s). Run from the repo root. Exit code = the btctl exit code (2 = refused), 3 = still pending, 4 = git problem.
"""
import argparse
import os
import re
import secrets
import subprocess
import sys
import time
from datetime import datetime, timezone

GIT = ["git", "-c", "user.name=cloud-claude", "-c", "user.email=cloud-claude@localhost"]


def run(*a, check=True):
    r = subprocess.run(list(a), capture_output=True, text=True)
    if check and r.returncode:
        sys.stderr.write(r.stdout + r.stderr)
        sys.exit(4)
    return r


def pull():
    run(*GIT, "pull", "--rebase", "-q", "origin", "main", check=False)


def push_with_retry():
    for _ in range(4):
        if run(*GIT, "push", "-q", "origin", "HEAD:main", check=False).returncode == 0:
            return
        pull()
        time.sleep(2)
    sys.exit("push failed")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("request", nargs="?")
    ap.add_argument("--payload")
    ap.add_argument("--wait", type=int, default=300)
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    pull()
    if a.status or not a.request:
        p = "status/latest.md"
        if not os.path.exists(p):
            sys.exit("no status/latest.md yet (btsync has not pushed)")
        age = (time.time() - os.path.getmtime(p)) / 60
        print(open(p, encoding="utf-8").read())
        first = open(p, encoding="utf-8").readline()
        m = re.search(r"(\d{4}-\d\d-\d\dT[\d:]+Z)", first)
        if m:
            t = datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            print(f"[status written {(datetime.now(timezone.utc) - t).total_seconds() / 60:.0f} min ago; >45 min = btsync/box problem]")
        return 0
    slug = re.sub(r"[^A-Za-z0-9]+", "_", a.request.split()[0])[:20]
    rid = f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}_{slug}_{secrets.token_hex(2)}"
    os.makedirs("inbox", exist_ok=True)
    open(f"inbox/{rid}.cmd", "w", encoding="utf-8", newline="\n").write(a.request.strip().splitlines()[0] + "\n")
    add = [f"inbox/{rid}.cmd"]
    if a.payload:
        data = open(a.payload, "rb").read()
        open(f"inbox/{rid}.payload", "wb").write(data)
        add.append(f"inbox/{rid}.payload")
    run(*GIT, "add", *add)
    run(*GIT, "commit", "-q", "-m", f"cmd {rid}: {a.request[:60]}")
    push_with_retry()
    out = f"outbox/{rid}.out"
    deadline = time.time() + a.wait
    while time.time() < deadline:
        time.sleep(15)
        pull()
        if os.path.exists(out):
            txt = open(out, encoding="utf-8", errors="replace").read()
            if "### exit=" in txt:
                print(txt)
                m = re.search(r"### exit=(\d+)", txt)
                return int(m.group(1)) if m else 0
    print(f"pending: {out} not there after {a.wait}s (btsync runs every ~60 s; check status/latest.md age)")
    return 3


if __name__ == "__main__":
    sys.exit(main())
