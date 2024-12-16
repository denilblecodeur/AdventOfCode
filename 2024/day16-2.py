import sys
from heapq import *

g = []
S=E=None
for i, line in enumerate(sys.stdin):
    if 'E' in line:
        E = (i, line.find('E'))
        line = line.replace('E', '.')
    if 'S' in line:
        S = (i, line.find('S'))
        line = line.replace('S', '.')
    g.append(line.rstrip('\n'))
n,m = len(g), len(g[0])

def get_dist(start, start_d=None):
    Q = []
    dist = [[[1<<59] * 4 for _ in range(m)] for _ in range(n)]
    if start_d is None:
        for d in range(4):
            Q.append((0, *start, d))
            dist[start[0]][start[1]][d] = 0
    else:
        Q.append((0, *start, start_d))
        dist[start[0]][start[1]][start_d] = 0
    while Q:
        c, i, j, d = heappop(Q)
        # forward
        di, dj = ((0,1),(1,0),(0,-1),(-1,0))[d] #RDLU
        if 0<=i+di<n and 0<=j+dj<m and g[i+di][j+dj] == '.':
            if dist[i+di][j+dj][d] > c+1:
                dist[i+di][j+dj][d] = c+1
                heappush(Q, (c+1, i+di, j+dj, d))
        # clockwise
        d = (d+1)%4
        if dist[i][j][d] > c+1000:
            dist[i][j][d] = c+1000
            heappush(Q, (c+1000, i, j, d))
        # anticlockwise
        d = (d-2)%4
        if dist[i][j][d] > c+1000:
            dist[i][j][d] = c+1000
            heappush(Q, (c+1000, i, j, d))
    return dist

fromS = get_dist(S, 0)
fromE = get_dist(E)
best = min(fromS[E[0]][E[1]])
ans = 0
for i in range(n):
    for j in range(m):
        good = 0
        for d in range(4):
            if fromS[i][j][d] + fromE[i][j][(d+2)%4] == best:
                good = 1
        ans += good
print(ans)