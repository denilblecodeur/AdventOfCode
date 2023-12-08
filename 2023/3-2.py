grid = []
good = []
done = False
while not done:
    try:
        s = input() + '.'
        grid.append(s)
        good.append([None] * len(s))
    except EOFError:
        done = True

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.' and not grid[i][j].isdigit():
            num = []
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                try:
                    if grid[i+di][j+dj].isdigit():
                        num.append((i+di, j+dj))
                except: continue
            num.sort()
            rem = []
            for k in range(1, len(num)):
                if num[k-1][0] == num[k][0] and num[k-1][1] + 1 == num[k][1]:
                    rem.append(num[k-1])
            for el in rem:
                num.remove(el)
            if len(num) == 2:
                good[i][j] = (i, j)

ans = [[0] * len(grid[i]) for i in range(len(grid))]
for i in range(len(grid)):
    cur = None
    G = []
    for j in range(len(grid[i])):
        if grid[i][j].isdigit():
            if cur is None:
                cur = grid[i][j]
            else:
                cur += grid[i][j]
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                try:
                    if good[i+di][j+dj] is not None:
                        G.append(good[i+di][j+dj])
                except: continue
        else:
            if cur is not None and G:
                G = set(G)
                for ii, jj in G:
                    if ans[ii][jj] == 0:
                        ans[ii][jj] = 1
                    ans[ii][jj] *= int(cur)
            G = []
            cur = None
            
print(sum(sum(row) for row in ans))