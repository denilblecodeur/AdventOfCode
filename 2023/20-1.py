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

lo, hi = 0, 0
for _ in range(1000):
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
                
                sent[newsignal] += 1
                if nei not in adj: continue
                if typ[nei] == '%' and newsignal > 0:
                    continue
                if typ[nei] == '%': state[nei] ^= 1
                if typ[nei] == '&': par[nei][cur] = newsignal
                newQ.append((nei, newsignal))
        
        Q = newQ

    lo += sent[0]
    hi += sent[1]

print(lo * hi)