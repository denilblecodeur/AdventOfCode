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
ans = 0
for a in adj:
    for b in adj[a]:
        for c in adj[a]:
            if b == c: continue
            if (b,c) in edges:
                ans += int(a.startswith('t') or b.startswith('t') or c.startswith('t'))
print((ans//3)>>1)