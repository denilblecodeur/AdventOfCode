grid = []
while True:
    try:
        grid.append(list(map(int,input())))
    except EOFError:
        break
n, m = len(grid), len(grid[0])

from heapq import *
Q = [(0, 0, 0, 1, 0)]
dist = [[[[1<<59] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
dist[0][0][1][0] = 0

D = ((0,1),(1,0),(0,-1),(-1,0)) #"RDLU"
while Q:
    cost, i, j, t, d = heappop(Q)
    if (i, j) == (n-1, m-1):
        print(cost)
        break
    if t < 3:
        di, dj = D[d]
        if 0<=i+di<n and 0<=j+dj<m:
            newcost = cost + grid[i+di][j+dj]
            if newcost < dist[i+di][j+dj][t+1][d]:
                dist[i+di][j+dj][t+1][d] = newcost
                heappush(Q, (newcost, i+di, j+dj, t+1, d))
    di, dj = D[(d-1)%4]
    if 0<=i+di<n and 0<=j+dj<m:
        newcost = cost + grid[i+di][j+dj]
        if newcost < dist[i+di][j+dj][1][(d-1)%4]:
            dist[i+di][j+dj][1][(d-1)%4] = newcost
            heappush(Q, (newcost, i+di, j+dj, 1, (d-1)%4))
    di, dj = D[(d+1)%4]
    if 0<=i+di<n and 0<=j+dj<m:
        newcost = cost + grid[i+di][j+dj]
        if newcost < dist[i+di][j+dj][1][(d+1)%4]:
            dist[i+di][j+dj][1][(d+1)%4] = newcost
            heappush(Q, (newcost, i+di, j+dj, 1, (d+1)%4))