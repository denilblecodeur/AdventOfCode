import sys
from collections import defaultdict

adj = defaultdict(set)
edges = set()
for line in sys.stdin:
    a, b = line.strip('\n').split('-')
    adj[a].add(b)
    adj[b].add(a)
    edges.add((a,b))
    edges.add((b,a))

res = set()

def BronKerbosch(P, R, X):
    global res
    if len(P) == len(X) == 0:
        res = max(res, R, key=len)
    for v in list(P):
        BronKerbosch(P & adj[v], R | {v}, X & adj[v])
        P.discard(v)
        X.add(v)

BronKerbosch(set(adj.keys()), set(), set())
print(','.join(sorted(res)))