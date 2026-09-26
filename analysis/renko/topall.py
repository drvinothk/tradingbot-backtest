import glob, os, sys
import replay as R
def pf(p):
    w=sum(x for x in p if x>0); l=-sum(x for x in p if x<0); return w/l if l else 9.99
rows=[]
for d in ['renko1','renko2a','renko2c','renko3b','renko3c','renko4','renko5','renko6']:
    for f in glob.glob(f'{d}/*_current.csv'):
        try: T=sorted(R.load_trades(f), key=lambda t:t['e'])
        except Exception as e: continue
        if len(T)<20: continue
        p=[t['pnl'] for t in T]; h=len(p)//2
        rows.append((d, os.path.basename(f)[:-12], len(p), sum(p), pf(p), sum(sorted(p)[:-2]), sum(t['pnl'] for t in T if t['ce']), sum(t['pnl'] for t in T if not t['ce']), sum(p[:h]), sum(p[h:])))
def show(title, ds):
    print('\n'+title)
    r=sorted([x for x in rows if x[0] in ds], key=lambda x:-x[3])[:5]
    for x in r: print(f" {x[0]:8} {x[1]:34} n={x[2]:2} net={x[3]:>7,.0f} PF={x[4]:4.2f} ex2={x[5]:>7,.0f} CE={x[6]:>7,.0f} PE={x[7]:>7,.0f} H1={x[8]:>6,.0f} H2={x[9]:>6,.0f}")
    print('  configs in set:', len([x for x in rows if x[0] in ds]))
show('SWEEP 1 (renko1 + renko2a)', ['renko1','renko2a'])
show('SWEEP 2 extended (renko2c,3b,3c,4,5,6)', ['renko2c','renko3b','renko3c','renko4','renko5','renko6'])
