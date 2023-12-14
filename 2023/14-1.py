grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

n = len(grid)

for j in range(n):
    for i in range(n):
        if grid[i][j] == 'O':
            ii = i
            while ii - 1 >= 0 and grid[ii - 1][j] == '.':
                ii -= 1
            grid[i][j] = '.'
            grid[ii][j] = 'O'

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'O':
            ans += n - i
print(ans)