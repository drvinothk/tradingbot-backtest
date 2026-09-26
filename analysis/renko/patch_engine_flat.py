p = "C:/Users/drvin/Trading Bot/backtest_engine/backend/scripts/run_backtest.py"
raw = open(p, 'rb').read()
assert b'\r\n' not in raw, "expected LF file"
s = raw.decode('utf-8')


def sub(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:70])
    s = s.replace(old, new)


sub('''    dyn_reverse_run = 0
    dyn_confirm_bricks = 1
    if renko_dynamic_exit is not None:
        dyn_confirm_bricks = int(renko_dynamic_exit["confirm_bricks"])
''', '''    dyn_reverse_run = 0
    dyn_confirm_bricks = 1
    dyn_flat_candles = 0
    dyn_flat_run = 0
    if renko_dynamic_exit is not None:
        dyn_confirm_bricks = int(renko_dynamic_exit["confirm_bricks"])
        dyn_flat_candles = int(renko_dynamic_exit.get("flat_exit_candles", 0))
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
            for brick_direction in dyn_events.get(bar.ts, ()):
                is_reverse = (
                    brick_direction == "down" if structure_favorable else brick_direction == "up"
                )
                dyn_reverse_run = dyn_reverse_run + 1 if is_reverse else 0
                if dyn_reverse_run >= dyn_confirm_bricks:
                    return _exit(bar.ts, close, "brick_reversal")
            # Flat exit (2026-09-23): a source candle close that printed NO
            # favourable brick (flat, or a reverse brick) counts as "flat";
            # `flat_exit_candles` consecutive ones exit. 0 = disabled.
            if dyn_flat_candles > 0 and bar.ts in dyn_events:
                favourable_direction = "up" if structure_favorable else "down"
                dyn_flat_run = (
                    0 if favourable_direction in dyn_events[bar.ts] else dyn_flat_run + 1
                )
                if dyn_flat_run >= dyn_flat_candles:
                    return _exit(bar.ts, close, "flat_exit")
''')
open(p, 'wb').write(s.encode('utf-8'))
print('engine flat exit patched')
