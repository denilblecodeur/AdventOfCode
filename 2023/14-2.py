grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

n = len(grid)

def roll(grid):
    for j in range(n):
        for i in range(n):
            if grid[i][j] == 'O':
                ii = i
                while ii - 1 >= 0 and grid[ii - 1][j] == '.':
                    ii -= 1
                grid[i][j] = '.'
                grid[ii][j] = 'O'

def cycle(grid):
    for _ in range(4):
        roll(grid)
        grid = [list(col)[::-1] for col in zip(*grid)]
    return grid

init = [list(grid[i]) for i in range(n)]
seen = {}
period = end = None

for i in range(1000000000):
    hsh = ''.join(''.join(grid[i]) for i in range(n))
    if hsh in seen:
        end = hsh
        period = i - seen[hsh]
        break
    seen[hsh] = i
    grid = cycle(grid)

grid = [list(init[i]) for i in range(n)]
start = None

for i in range(1000000000):
    hsh = ''.join(''.join(grid[i]) for i in range(n))
    if hsh == end:
        start = i
        break
    seen[hsh] = i
    grid = cycle(grid)

grid = [list(init[i]) for i in range(n)]

for _ in range(start + ((1000000000 - start) % period)):
    grid = cycle(grid)

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'O':
            ans += n - i
print(ans)