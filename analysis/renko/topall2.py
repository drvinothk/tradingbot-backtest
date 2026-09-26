import glob, os, math, statistics as st
import replay as R
rows=[]
for d in ['renko1','renko2a','renko2c','renko3b','renko3c','renko4','renko5','renko6','renko7']:
    for f in glob.glob(f'{d}/*_current.csv'):
        try: T=sorted(R.load_trades(f), key=lambda t:t['e'])
        except Exception: continue
        if len(T)<20: continue
        p=[t['pnl'] for t in T]; w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0)
        rows.append((sum(p),d,os.path.basename(f)[:-12],len(p),w/l,sum(sorted(p)[:-2])))
rows.sort(reverse=True)
print(len(rows),'configs (n>=20)')
print("by net:")
for r in rows[:10]: print(f" {r[1]:8} {r[2]:34} n={r[3]} net={r[0]:>7,.0f} PF={r[4]:.2f} ex2={r[5]:>7,.0f}")
print("by ex-top-2 (net>0):")
for r in sorted(rows,key=lambda x:-x[5])[:8]: print(f" {r[1]:8} {r[2]:34} n={r[3]} net={r[0]:>7,.0f} PF={r[4]:.2f} ex2={r[5]:>7,.0f}")
