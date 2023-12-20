adj, typ, state = {}, {}, {}
while True:
    try:
        a, b = input().split(' -> ')
        if all(c.isalpha() for c in a):
            adj[a] = b.split(', ')
            typ[a] = None
        else:
            typ[a[1:]] = a[0]
            if a[0] == '%':
                state[a[1:]] = 0
            adj[a[1:]] = b.split(', ')
    except EOFError:
        break

par = {v:{} for v in adj}
for v, nei in adj.items():
    for u in nei:
        if u not in adj: continue
        par[u][v] = 0

# unique parent de rx est lv
prev_prev_rx = dict.fromkeys(par['lv'].keys(), float('inf'))

for step in range(5000):
    Q = [('broadcaster', 0)]
    sent = [1, 0]
    while Q:
        newQ = []
        for cur, signal in Q:
            for nei in adj[cur]:
                if typ[cur] is None:
                    newsignal = 0

                if typ[cur] == '%':
                    newsignal = state[cur]

                if typ[cur] == '&':
                    newsignal = 1
                    for pre, s in par[cur].items():
                        newsignal &= s
                    newsignal ^= 1

                    if cur in prev_prev_rx and newsignal == 1:
                        prev_prev_rx[cur] = min(prev_prev_rx[cur], step+1)
                
                sent[newsignal] += 1
                if nei not in adj: continue
                if typ[nei] == '%' and newsignal > 0:
                    continue
                if typ[nei] == '%': state[nei] ^= 1
                if typ[nei] == '&': par[nei][cur] = newsignal
                newQ.append((nei, newsignal))
        
        Q = newQ

from math import lcm
ans = 1
for cycle in prev_prev_rx.values():
    ans = lcm(ans, cycle)
print(ans)