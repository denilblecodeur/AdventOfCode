grid = []
while True:
    try:
        grid.append(list(map(int,input())))
    except EOFError:
        break
n, m = len(grid), len(grid[0])

from heapq import *
Q = [(0, 0, 0, 1, 0)]
dist = [[[[1<<59] * 4 for _ in range(11)] for _ in range(m)] for _ in range(n)]
dist[0][0][1][0] = 0

D = ((0,1),(1,0),(0,-1),(-1,0)) #"RDLU"
while Q:
    cost, i, j, t, d = heappop(Q)
    if (i, j) == (n-1, m-1):
        print(cost)
        break
    if t < 10:
        di, dj = D[d]
        if 0<=i+di<n and 0<=j+dj<m:
            newcost = cost + grid[i+di][j+dj]
            if newcost < dist[i+di][j+dj][t+1][d]:
                dist[i+di][j+dj][t+1][d] = newcost
                heappush(Q, (newcost, i+di, j+dj, t+1, d))
    di, dj = D[(d-1)%4]
    if 0<=i+4*di<n and 0<=j+4*dj<m:
        newcost = cost + sum(grid[i+k*di][j+k*dj] for k in range(1, 5))
        if newcost < dist[i+4*di][j+4*dj][4][(d-1)%4]:
            dist[i+4*di][j+4*dj][4][(d-1)%4] = newcost
            heappush(Q, (newcost, i+4*di, j+4*dj, 4, (d-1)%4))
    di, dj = D[(d+1)%4]
    if 0<=i+4*di<n and 0<=j+4*dj<m:
        newcost = cost + sum(grid[i+k*di][j+k*dj] for k in range(1, 5))
        if newcost < dist[i+4*di][j+4*dj][4][(d+1)%4]:
            dist[i+4*di][j+4*dj][4][(d+1)%4] = newcost
            heappush(Q, (newcost, i+4*di, j+4*dj, 4, (d+1)%4))