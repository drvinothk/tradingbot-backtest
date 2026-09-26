import statistics as st, collections
import replay as R
from datetime import date
import re
DN=['Mon','Tue','Wed','Thu','Fri']
def dte(t):
    m=re.search(r'NIFTY(\d{2})(\d{2})(\d{2})',t['sym']); return (date(2000+int(m[1]),int(m[2]),int(m[3]))-t['e'].date()).days
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
def line(lab,p,ndays=None):
    if not p: return f"{lab:10} n=0"
    return f"{lab:10} n={len(p):3} net={sum(p):>7,.0f} PF={pf(p):4.2f} WR={100*sum(x>0 for x in p)/len(p):3.0f}% avg={st.mean(p):>6,.0f} ex-best={sum(sorted(p)[:-1]):>7,.0f}"
ts=sorted(R.load_trades('mt1/renko10_mt3_s1_top_current.csv'),key=lambda t:t['e'])
first={}
for t in ts: first.setdefault(t['e'].date(),t)
F=list(first.values())
for name,S in (('ALL trades',ts),('FIRST trade/day',F),('RE-ENTRIES (#2+)',[t for t in ts if t not in F])):
    print('==',name)
    for wd in range(5): print(' ',line(DN[wd],[t['pnl'] for t in S if t['e'].weekday()==wd]))
    print(' by DTE')
    for d in sorted({dte(t) for t in S}): print(' ',line(f'DTE{d}',[t['pnl'] for t in S if dte(t)==d]))
# days count per weekday
c=collections.Counter(d.weekday() for d in first); print('days traded by weekday',{DN[k]:v for k,v in sorted(c.items())})
print('trades/day dist',collections.Counter(collections.Counter(t['e'].date() for t in ts).values()))
