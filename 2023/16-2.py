grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

n, m = len(grid), len(grid[0])
DIR = lambda d : ((-1,0),(1,0),(0,-1),(0,1))["UDLR".find(d)]

best = 0
for k in range(2 * n + 2 * m):
    nrj = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    if k < n:
        Q = [(k, 0, 'R')]
    elif k < n+m:
        Q = [(n-1, k-n, 'U')]
    elif k < 2*n+m:
        Q = [(k-(n+m), m-1, 'L')]
    else:
        Q = [(0, k-(2*n+m), 'D')]
        
    while Q:
        i, j, d = Q.pop()
        if not(0<=i<n and 0<=j<m) or nrj[i][j]["UDLR".find(d)]:
            continue
        nrj[i][j]["UDLR".find(d)] = 1
        if grid[i][j] == '/':
            d = {'R':'U','U':'R','L':'D','D':'L'}[d]
        elif grid[i][j] == '\\':
            d = {'R':'D','D':'R','L':'U','U':'L'}[d]
        elif grid[i][j] == '|':
            if d in 'RL':
                di, dj = DIR('U')
                Q.append((i+di,j+dj,'U'))
                di, dj = DIR('D')
                Q.append((i+di,j+dj,'D'))
                continue
        elif grid[i][j] == '-':
            if d in 'UD':
                di, dj = DIR('R')
                Q.append((i+di,j+dj,'R'))
                di, dj = DIR('L')
                Q.append((i+di,j+dj,'L'))
                continue
        di, dj = DIR(d)
        Q.append((i+di,j+dj,d))

    cur = 0
    for i in range(n):
        for j in range(m):
            cur += max(nrj[i][j])
    best = max(best, cur)


print(best)