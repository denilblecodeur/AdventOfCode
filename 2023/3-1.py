grid = []
good = []
done = False
while not done:
    try:
        s = input() + '.'
        grid.append(s)
        good.append([False] * len(s))
    except EOFError:
        done = True

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.' and not grid[i][j].isdigit():
            good[i][j] = True

ans = 0
for i in range(len(grid)):
    cur = None
    G = False
    for j in range(len(grid[i])):
        if grid[i][j].isdigit():
            if cur is None:
                cur = grid[i][j]
            else:
                cur += grid[i][j]
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                try:
                    G |= good[i+di][j+dj]
                except: continue
        else:
            if cur is not None:
                ans += int(cur) * G
            G = False
            cur = None
print(ans)