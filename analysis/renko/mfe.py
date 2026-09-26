import csv,glob,os,statistics as st
from datetime import datetime
from collections import defaultdict
H="C:/Users/drvin/Trading Bot/backtest_engine/backend/data/historical/"
idx={}
for p in glob.glob(H+'options_1min_past/*/*/*.csv'): idx[os.path.basename(p)[:-4]]=p
files=sorted(glob.glob(H+'backtest_reports/*/*_current.csv'),key=os.path.getmtime,reverse=True)[:200]
seen={}
for f in files:
    for r in csv.DictReader(open(f)):
        if not r['symbol'].endswith('CE') or r['symbol'] not in idx: continue
        seen[(r['symbol'],r['entry_time'],r['entry_price'])]=r
cache={}
def bars(sym):
    if sym not in cache:
        cache[sym]=[(datetime.fromisoformat(x['timestamp']),float(x['high']),float(x['low']),float(x['close'])) for x in csv.DictReader(open(idx[sym]))]
    return cache[sym]
rows=[]
for (sym,et,ep),r in seen.items():
    e=datetime.fromisoformat(et).replace(tzinfo=None); x=datetime.fromisoformat(r['exit_time']).replace(tzinfo=None)
    entry=float(r['entry_price']); xp=float(r['exit_price'])
    b=bars(sym); hold=[z for z in b if e<=z[0]<=x]; after=[z for z in b if x<z[0].replace() and z[0].date()==x.date() and z[0].time()<=datetime(2000,1,1,15,15).time()]
    if not hold: continue
    mfe=max(z[1] for z in hold)/entry-1
    aft=(max(z[1] for z in after)/xp-1) if after else 0
    rows.append(dict(reason=r['exit_reason'],mfe=mfe,ret=xp/entry-1,aft=aft,pnl=float(r['pnl'])))
print('CE trades with option data:',len(rows))
by=defaultdict(list)
for r in rows: by[r['reason']].append(r)
for k,v in by.items():
    print(f"\n[{k}] n={len(v)}  median MFE={100*st.median([r['mfe'] for r in v]):.0f}%  median exit ret={100*st.median([r['ret'] for r in v]):.0f}%")
    if k in('stop','structure_break'):
        for th in (0.10,0.20,0.30):
            print(f"   reached +{int(th*100)}% before exit: {sum(r['mfe']>=th for r in v)}/{len(v)}")
    if k=='trail':
        cap=[ (r['ret'])/r['mfe'] for r in v if r['mfe']>0.01]
        print(f"   capture (exit ret / peak ret) median={st.median(cap):.2f}")
        print(f"   after exit, same-session further peak vs exit price: median +{100*st.median([r['aft'] for r in v]):.0f}%, >+20%: {sum(r['aft']>0.2 for r in v)}/{len(v)}, >+50%: {sum(r['aft']>0.5 for r in v)}/{len(v)}")
