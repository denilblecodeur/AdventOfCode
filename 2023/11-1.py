grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

n, m = len(grid), len(grid[0])
gal = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            grid[i][j] = str(len(gal))
            gal[len(gal)] = (i, j)

big = [[0] * m for _ in range(n)]
for i in range(n):
    if all(grid[i][j] == '.' for j in range(m)):
        big[i] = [1] * m
for j in range(m):
    if all(grid[i][j] == '.' for i in range(n)):
        for i in range(n): big[i][j] = 1

from collections import deque
ans = 0
for x in range(len(gal)):
    mindist = [float('inf')] * len(gal)
    Q = deque([(*gal[x], 0)])
    seen = set()
    while Q:
        i, j, d = Q.popleft()
        d += big[i][j]
        if grid[i][j].isdigit():
            mindist[int(grid[i][j])] = d
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            if 0 <=i+di<n and 0<=j+dj<m and (i+di,j+dj) not in seen:
                seen.add((i+di,j+dj))
                Q.append((i+di,j+dj, d+1))
    ans += sum(mindist[y] for y in range(x))
print(ans)