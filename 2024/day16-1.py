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

D = ((0,1),(1,0),(0,-1),(-1,0)) #RDLU
Q = [(0, *S, 0)]
dist = [[[1<<59] * 4 for _ in range(m)] for _ in range(n)]
dist[S[0]][S[1]][0] = 0

while Q:
    c, i, j, d = heappop(Q)
    if (i,j) == E:
        print(c) & exit()
    # forward
    di, dj = D[d]
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
assert False, "not found"