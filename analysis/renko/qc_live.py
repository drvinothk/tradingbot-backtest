import csv, json, collections
from datetime import datetime, timedelta, time
B = 8.33
bars = []
for r in csv.reader(open('bars.csv')):
    ts = datetime.fromisoformat(r[0]); bars.append((ts, *map(float, r[1:5])))
bars = [b for b in bars if time(9,15) <= b[0].time() <= time(15,29,59)]
raw = open('sig.txt').read().strip()
gen, payload = raw.split('|', 1); gen = datetime.fromisoformat(gen.strip()); P = json.loads(payload)
today = gen.date(); is_ce = False  # the signal is a PE (see query)
by = collections.defaultdict(list)
for b in bars: by[b[0].date()].append(b)
hist_days = [d for d in sorted(by) if d < today and len(by[d]) >= 300][-6:]
def candles(day_bars, tf, now=None):
    g = collections.OrderedDict()
    for ts, o, h, l, c in day_bars:
        i = int(((ts - datetime.combine(ts.date(), time(9,15))).total_seconds()) // (tf*60))
        g.setdefault(i, []).append((ts,o,h,l,c))
    out = []
    for i, w in g.items():
        start = datetime.combine(w[0][0].date(), time(9,15)) + timedelta(minutes=tf*i)
        if now is not None and start + timedelta(minutes=tf) > now: continue
        out.append((start, w[-1][4]))
    return out
def renko(cs, seed_min):
    # lattice formulation: box index k (bottom = k*B); brick up when close >= (k+2)*B, down when close <= (k-1)*B
    k = None; dirs = []; last_end = None
    for start, c in cs:
        if k is None:
            if start.time() < seed_min: continue
            k = round(c / B)
        while c >= (k + 2) * B: k += 1; dirs.append('up'); last_end = start + timedelta(minutes=0)
        while c <= (k - 1) * B: k -= 1; dirs.append('down'); last_end = start
    return dirs, k
def ema(vals, n=30):
    if len(vals) < n: return None
    e = sum(vals[:n]) / n
    for v in vals[n:]: e = v * 2/(n+1) + e * (1 - 2/(n+1))
    return e
now = gen
tb = [b for b in by[today] if b[0] + timedelta(seconds=60) <= now]
spot = tb[-1][4]
print('spot', spot, '| payload spot', P['spot'], '| last bar', tb[-1][0].time())
ok = True
def chk(name, got, want, tol=0.011):
    global ok
    good = (abs(got - want) <= tol) if isinstance(want, (int, float)) and not isinstance(want, bool) else got == want
    ok &= good; print(('OK   ' if good else 'DIFF '), name, 'mine=', got, 'logged=', want)
for name, tf in (('a', 5), ('b', 15)):
    cs = candles(tb, tf, now)
    for label, seed, key in (('', time(9,30), name), ('early', time(0,0), name + '_early')):
        dirs, k = renko(cs, seed)
        run = 0
        for d in reversed(dirs):
            if d == dirs[-1]: run += 1
            else: break
        trend = dirs[-1].upper() if dirs and run >= 2 else None
        L = P[key]
        chk(f'{key}.bricks', len(dirs), L['bricks']); chk(f'{key}.trend', trend, L['trend']); chk(f'{key}.run_len', run, L['run_len'])
        chk(f'{key}.net', dirs.count('up') - dirs.count('down'), L['net_bricks'])
        if label == '':
            chk(f'{key}.bottom', k * B, L['bottom']); chk(f'{key}.top', (k + 1) * B, L['top'])
            chk(f'{key}.flips', sum(1 for x, y in zip(dirs, dirs[1:]) if x != y), L['flips']); chk(f'{key}.candles', len(cs), L['candles_finished'])
    hist = [c for d in hist_days for _, c in candles(by[d], tf)]
    e = ema(hist + [c for _, c in cs])
    L = P['ema30'][f'{tf}m']
    chk(f'ema30.{tf}m.value', e, L['value']); chk(f'ema30.{tf}m.spot_minus', spot - e, L['spot_minus']); chk(f'ema30.{tf}m.agrees(PE)', (spot - e) * -1 > 0, L['agrees'])
closes = [b[4] for b in tb[-31:]]
run = 0
for p, c in zip(reversed(closes[:-1]), reversed(closes[1:])):
    if c > p: run += 1
    else: break
chk('adverse_1m_run', run, P['adverse_1m_run']); chk('move_from_open(PE)', -(spot - tb[0][1]), P['move_from_open_pts'])
print('history days used:', [str(d) for d in hist_days]); print('ALL MATCH' if ok else 'MISMATCHES')
