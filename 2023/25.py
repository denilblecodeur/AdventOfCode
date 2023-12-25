import sys
sys.setrecursionlimit(10000)

graph = {}
while True:
    try:
        v, nei = input().split(': ')
        if v not in graph:
            graph[v] = []
        for u in nei.split():
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            graph[v].append(u)
    except EOFError:
        break

n = len(graph)
mapped = dict(zip(graph.keys(), range(n)))
G = [[] for _ in range(n)]
for v, nei in graph.items():
    for u in nei:
        G[mapped[v]].append(mapped[u])
graph = G

def augment(graph, flow, val, u, target, visit):
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        cuv = 1
        if not visit[v] and cuv > flow[u][v]:
            res = min(val, cuv - flow[u][v])
            delta = augment(graph, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta
    return 0

def ford_fulkerson(graph, s, t):
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    INF = 1<<59
    while augment(graph, flow, INF, s, t, [False] * n) > 0:
        pass
    return sum(flow[s])

p1, p2 = 1, 0
for t in range(1, n):
    if ford_fulkerson(graph, 0, t) == 3:
        p2 += 1
    else:
        p1 += 1

print(p1 * p2)