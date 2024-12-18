import sys

cor = []
for line in sys.stdin:
    x, y = map(int,line.split(','))
    cor.append((y,x))

n = 71
g = [[0] * n for _ in range(n)]

for (x, y) in cor:
    g[x][y] = 1
    Q = [(0,0,0)]
    vis = [[0] * n for _ in range(n)]
    for i,j,d in Q:
        if (i,j) == (70,70): break
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<n and 0<=j+dj<n and not vis[i+di][j+dj] and not g[i+di][j+dj]:
                vis[i+di][j+dj] = 1
                Q.append((i+di,j+dj,d+1))
    if not vis[n-1][n-1]:
        print(f"{y},{x}") & exit()