import csv,glob,os,sys
from collections import defaultdict
d=sys.argv[1]
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0)
    return w/l if l>0 else float('inf')
def mdd(p):
    c=m=dd=0
    for x in p:
        c+=x; m=max(m,c); dd=max(dd,m-c)
    return dd
rows=[]
for f in sorted(glob.glob(d+'/*_current.csv')):
    n=os.path.basename(f).replace('_current.csv','')
    t=list(csv.DictReader(open(f)))
    t.sort(key=lambda r:r['entry_time'])
    p=[float(r['pnl']) for r in t]
    if not p: print(n,'no trades'); continue
    dates=sorted({r['entry_time'][:10] for r in t})
    mid=t[len(t)//2]['entry_time']
    a=[float(r['pnl']) for r in t if r['entry_time']<mid]; b=[float(r['pnl']) for r in t if r['entry_time']>=mid]
    s=sorted(p,reverse=True); d2=p[:]; 
    for x in s[:2]: d2.remove(x)
    ex=defaultdict(lambda:[0,0.0])
    for r in t: e=ex[r['exit_reason']]; e[0]+=1; e[1]+=float(r['pnl'])
    ce=[float(r['pnl']) for r in t if r['symbol'].endswith('CE')]; pe=[float(r['pnl']) for r in t if r['symbol'].endswith('PE')]
    print(f"\n== {n}\n trades={len(p)} win%={100*sum(x>0 for x in p)/len(p):.1f} net={sum(p):,.0f} PF={pf(p):.2f} avgW={sum(x for x in p if x>0)/max(1,sum(x>0 for x in p)):,.0f} avgL={sum(x for x in p if x<=0)/max(1,sum(x<=0 for x in p)):,.0f} maxDD={mdd(p):,.0f}")
    print(f" top2={[round(x) for x in s[:2]]} | net ex-top2={sum(d2):,.0f} PF ex-top2={pf(d2):.2f} | worst2={[round(x) for x in s[-2:]]}")
    print(f" 1st half n={len(a)} net={sum(a):,.0f} PF={pf(a):.2f} | 2nd half n={len(b)} net={sum(b):,.0f} PF={pf(b):.2f}  (split {mid[:10]}; span {dates[0]}..{dates[-1]}, {len(dates)} trade-days)")
    print(f" CE n={len(ce)} net={sum(ce):,.0f} PF={pf(ce):.2f} | PE n={len(pe)} net={sum(pe):,.0f} PF={pf(pe):.2f}")
    print(" exits:", {k:(v[0],round(v[1])) for k,v in sorted(ex.items())})
