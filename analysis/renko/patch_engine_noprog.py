p = "C:/Users/drvin/Trading Bot/backtest_engine/backend/scripts/run_backtest.py"
raw = open(p, 'rb').read()
assert b'\r\n' not in raw, "expected LF file"
s = raw.decode('utf-8')


def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)


sub('''    dyn_flat_candles = 0
    dyn_flat_run = 0
    if renko_dynamic_exit is not None:
        dyn_confirm_bricks = int(renko_dynamic_exit["confirm_bricks"])
        dyn_flat_candles = int(renko_dynamic_exit.get("flat_exit_candles", 0))
''', '''    dyn_flat_candles = 0
    dyn_flat_run = 0
    dyn_noprog_candles = 0
    dyn_candles_held = 0
    dyn_net_favourable = 0
    dyn_peak_favourable = 0
    if renko_dynamic_exit is not None:
        dyn_confirm_bricks = int(renko_dynamic_exit["confirm_bricks"])
        dyn_flat_candles = int(renko_dynamic_exit.get("flat_exit_candles", 0))
        dyn_noprog_candles = int(renko_dynamic_exit.get("no_progress_exit_candles", 0))
''')
sub('''        if renko_dynamic_exit is not None:
            for brick_direction in dyn_events.get(bar.ts, ()):
                is_reverse = (
                    brick_direction == "down" if structure_favorable else brick_direction == "up"
                )
                dyn_reverse_run = dyn_reverse_run + 1 if is_reverse else 0
                if dyn_reverse_run >= dyn_confirm_bricks:
                    return _exit(bar.ts, close, "brick_reversal")
''', '''        if renko_dynamic_exit is not None:
            if bar.ts in dyn_events:
                dyn_candles_held += 1
            for brick_direction in dyn_events.get(bar.ts, ()):
                is_reverse = (
                    brick_direction == "down" if structure_favorable else brick_direction == "up"
                )
                dyn_reverse_run = dyn_reverse_run + 1 if is_reverse else 0
                dyn_net_favourable += -1 if is_reverse else 1
                dyn_peak_favourable = max(dyn_peak_favourable, dyn_net_favourable)
                if dyn_reverse_run >= dyn_confirm_bricks:
                    return _exit(bar.ts, close, "brick_reversal")
''')
sub('''                if dyn_flat_run >= dyn_flat_candles:
                    return _exit(bar.ts, close, "flat_exit")
''', '''                if dyn_flat_run >= dyn_flat_candles:
                    return _exit(bar.ts, close, "flat_exit")
            # No-progress exit (2026-09-24): after `no_progress_exit_candles`
            # source candles the trade has still never printed a net
            # favourable brick (peak <= 0) -> cut it. Only ever touches trades
            # that never got going; a winner pausing is never affected.
            if (
                dyn_noprog_candles > 0
                and bar.ts in dyn_events
                and dyn_candles_held >= dyn_noprog_candles
                and dyn_peak_favourable <= 0
            ):
                return _exit(bar.ts, close, "no_progress")
''')
open(p, 'wb').write(s.encode('utf-8'))
print('engine no-progress patched')
