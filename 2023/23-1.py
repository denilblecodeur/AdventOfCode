grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break
        
n, m = len(grid), len(grid[0])

Q = [((0, 1, 1, set()))]# way RDLU
ans = 0
while Q:
    i, j, way, path = Q.pop()
    if (i, j) == (n-1, m-2):
        ans = max(ans, len(path))
        continue
    if grid[i][j] in ">v<^":
        k = ">v<^".find(grid[i][j])
        if k == (way+2) % 4:
            continue
        di, dj = ((0,1),(1,0),(0,-1),(-1,0))[k]
        if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] != '#':
            if (i+di,j+dj) not in path:
                Q.append((i+di,j+dj,k,path|{(i+di,j+dj)}))
    else:
        for k, (di, dj) in enumerate(((0,1),(1,0),(0,-1),(-1,0))):
            if k == (way+2) % 4:
                continue
            if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] != '#':
                if (i+di,j+dj) not in path:
                    Q.append((i+di,j+dj,k,path|{(i+di,j+dj)}))
print(ans)