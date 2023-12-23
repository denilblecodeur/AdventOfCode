import re

grid = []
while True:
    try:
        grid.append(list(re.sub(r'[<|>|v|^]+', '.', input())))
    except EOFError:
        break

n, m = len(grid), len(grid[0])

def nb_nei(i, j):
    return sum(
        0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] != '#'
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0))
        )

src, end = (0,1), (n-1,m-2)
node = {src:0}
Q = [((0, 1, src, 0))]
seen = set()
while Q:
    i, j, last, d = Q.pop()
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
        if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] != '#':
            if (i+di,j+dj) == last:
                continue
            if nb_nei(i+di,j+dj) == 2:
                if (i+di,j+dj) not in seen:
                    seen.add((i+di,j+dj))
                    Q.append((i+di,j+dj,last,d+1))
            else:
                if (i+di,j+dj) not in node:
                    node[(i+di,j+dj)] = len(node)
                Q.append((i+di,j+dj,(i+di,j+dj),0))

adj = [{} for _ in range(len(node))]
for (_i, _j), v in node.items():
    Q = [(_i, _j, 0)]
    seen = set()
    while Q:
        i, j, d = Q.pop()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] != '#' and (i+di,j+dj) not in seen:
                if nb_nei(i+di,j+dj) == 2:
                    Q.append((i+di,j+dj,d+1))
                else:
                    adj[v][node[(i+di,j+dj)]] = max(adj[v].get(node[(i+di,j+dj)], 0), d+1)

used = [False] * 36
used[0] = True
Q = [(0,0,used)]
ans = 0
while Q:
    v, d, used = Q.pop()
    if v == node[end]:
        ans = max(ans, d)
        continue
    for u, w in adj[v].items():
        if not used[u]:
            used[u] = True
            Q.append((u,d+w,list(used)))
            used[u] = False

print(ans)