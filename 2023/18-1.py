instr = []
while True:
    try:
        s = input().split()
        instr.append(s)
    except EOFError:
        break

grid = [[0] * 1000 for _ in range(1000)]
D = ((0,1),(1,0),(0,-1),(-1,0)) # RDLU
i, j = 500, 500
grid[i][j] = 1
for s in instr:
    d, n, c = s
    di, dj = D["RDLU".find(d)]
    for k in range(int(n)):
        grid[i+di][j+dj] = 1
        i+=di
        j+=dj

Q = [(0, 0)]
while Q:
    i, j = Q.pop()
    if grid[i][j] == 2:
        continue
    grid[i][j] = 2
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
        if 0<=i+di<1000 and 0<=j+dj<1000 and grid[i+di][j+dj] == 0:
            Q.append((i+di, j+dj))

print(sum(row.count(1) + row.count(0) for row in grid))