import csv,glob,os,sys,statistics as st
from datetime import datetime,timedelta
from collections import defaultdict
ROOT="D:/TradingBot/backtest_engine/backend/data/historical/underlyings_alice_1min_past/NIFTY"
bars=defaultdict(list)
for f in sorted(glob.glob(ROOT+'/*.csv')):
    for r in csv.DictReader(open(f)):
        ts=datetime.fromisoformat(r['timestamp'])
        bars[ts.date()].append((ts,float(r['open']),float(r['high']),float(r['low']),float(r['close'])))
for d in bars: bars[d].sort()
def atr14(day,ts):
    b=[x for x in bars[day] if x[0]<=ts][-15:]
    trs=[max(b[i][2]-b[i][3],abs(b[i][2]-b[i-1][4]),abs(b[i][3]-b[i-1][4])) for i in range(1,len(b))]
    return sum(trs)/len(trs) if trs else 0
def at(day,ts):
    c=[x for x in bars[day] if x[0]<=ts]
    return c[-1] if c else None
def load(path):
    out=[]
    for r in csv.DictReader(open(path)):
        e=datetime.fromisoformat(r['entry_time']).replace(tzinfo=None); x=datetime.fromisoformat(r['exit_time']).replace(tzinfo=None)
        out.append(dict(sym=r['symbol'],ce=r['symbol'].endswith('CE'),e=e,x=x,reason=r['exit_reason'],pnl=float(r['pnl']),ep=float(r['entry_price']),xp=float(r['exit_price'])))
    return out
def fib(day):
    fb=[b for b in bars[day] if b[0].time()<datetime(2000,1,1,9,20).time()]
    if len(fb)<5: return None
    hi=max(b[2] for b in fb); lo=min(b[3] for b in fb); return lo,hi
def summ(name,vals,unit=''):
    if not vals: print('  ',name,'n/a'); return
    v=sorted(vals); print(f"   {name}: n={len(v)} min={v[0]:.1f} p25={v[len(v)//4]:.1f} med={st.median(v):.1f} p75={v[3*len(v)//4]:.1f} max={v[-1]:.1f}{unit}")
if __name__=='__main__':
    d=sys.argv[1]
    for n in sys.argv[2:]:
        T=load(f'{d}/{n}_current.csv'); rows=[]
        for t in T:
            day=t['e'].date()
            if day not in bars or day>datetime(2026,8,20).date(): continue
            f=fib(day)
            if not f: continue
            lo,hi=f; rg=hi-lo
            lvl=lo+(0.382 if t['ce'] else 0.618)*rg; pob=lo+0.5*rg
            u=at(day,t['e']); ux=at(day,t['x'])
            if not u or not ux: continue
            dist=(u[4]-lvl) if t['ce'] else (lvl-u[4])
            rows.append(dict(t=t,rg=rg,dist=dist,a=atr14(day,t['e']),u=u[4],ux=ux[4],hold=(t['x']-t['e']).total_seconds()/60,lvl=lvl))
        print('\n==',n,'trades w/ data',len(rows))
        for grp in ('structure_break','trail','eod_square_off','stop'):
            g=[r for r in rows if r['t']['reason']==grp]
            if not g: continue
            print(f' [{grp}] n={len(g)} net={sum(r["t"]["pnl"] for r in g):,.0f}')
            summ('first-5min range pts',[r['rg'] for r in g])
            summ('entry->fib level dist pts',[r['dist'] for r in g])
            summ('dist / 1min-ATR14',[r['dist']/r['a'] for r in g if r['a']])
            summ('hold min',[r['hold'] for r in g])
            if grp=='structure_break':
                summ('underlying move entry->exit pts (against)',[(r['u']-r['ux']) if r['t']['ce'] else (r['ux']-r['u']) for r in g])
                print('   entry already beyond level (dist<=0):',sum(r['dist']<=0 for r in g),' dist<5pts:',sum(r['dist']<5 for r in g),' hold<=2min:',sum(r['hold']<=2 for r in g))
