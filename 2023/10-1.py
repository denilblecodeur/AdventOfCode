grid = []
start = None
while True:
    try:
        s = input()
        if 'S' in s:
            start = len(grid), s.find('S')
        grid.append(s)
    except EOFError:
        break

n, m = len(grid), len(grid[0])
i, j = start
dist = [[0] * m for _ in range(n)]
Q = []
for e, (di, dj) in enumerate(((-1,0),(1,0),(0,-1),(0,1))):
    if 0<=i+di<n and 0<=j+dj<m:
        if e > 1:
            if grid[i+di][j+dj] in "FL-":
                Q.append((i+di,j+dj))
        else:
            if grid[i+di][j+dj] in "J7|":
                Q.append((i+di,j+dj))

ni, nj = Q[0]
d = 1
while dist[ni][nj] == 0:
    dist[ni][nj] = d
    d += 1
    if grid[ni][nj] == '-':
        if j == nj - 1:
            di, dj = 0, 1
        else:
            di, dj = 0, -1
    elif grid[ni][nj] == '|':
        if i == ni - 1:
            di, dj = 1, 0
        else:
            di, dj = -1, 0
    elif grid[ni][nj] == 'F':
        if j == nj + 1:
            di, dj = 1, 0
        elif i == ni + 1:
            di, dj = 0, 1
    elif grid[ni][nj] == 'J':
        if j == nj - 1:
            di, dj = -1, 0
        elif i == ni - 1:
            di, dj = 0, -1
    elif grid[ni][nj] == '7':
        if j == nj - 1:
            di, dj = 1, 0
        elif i == ni + 1:
            di, dj = 0, -1
    elif grid[ni][nj] == 'L':
        if j == nj + 1:
            di, dj = -1, 0
        elif i == ni - 1:
            di, dj = 0, 1
    i, j, ni, nj = ni, nj, ni + di, nj + dj

print(d//2)