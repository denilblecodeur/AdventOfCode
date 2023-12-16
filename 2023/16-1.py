grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

n, m = len(grid), len(grid[0])
nrj = [[[0] * 4 for _ in range(m)] for _ in range(n)]
DIR = lambda d : ((-1,0),(1,0),(0,-1),(0,1))["UDLR".find(d)]
Q = [(0, 0, 'R')]
while Q:
    i, j, d = Q.pop()
    if not(0<=i<n and 0<=j<m) or nrj[i][j]["UDLR".find(d)]:
        continue
    nrj[i][j]["UDLR".find(d)] = 1
    if grid[i][j] == '.':
        di, dj = DIR(d)
        Q.append((i+di,j+dj,d))
    elif grid[i][j] == '/':
        d = {'R':'U','U':'R','L':'D','D':'L'}[d]
        di, dj = DIR(d)
        Q.append((i+di,j+dj,d))
    elif grid[i][j] == '\\':
        d = {'R':'D','D':'R','L':'U','U':'L'}[d]
        di, dj = DIR(d)
        Q.append((i+di,j+dj,d))
    elif grid[i][j] == '|':
        if d in 'RL':
            di, dj = DIR('U')
            Q.append((i+di,j+dj,'U'))
            di, dj = DIR('D')
            Q.append((i+di,j+dj,'D'))
        else:
            di, dj = DIR(d)
            Q.append((i+di,j+dj,d))
    elif grid[i][j] == '-':
        if d in 'UD':
            di, dj = DIR('R')
            Q.append((i+di,j+dj,'R'))
            di, dj = DIR('L')
            Q.append((i+di,j+dj,'L'))
        else:
            di, dj = DIR(d)
            Q.append((i+di,j+dj,d))

ans = 0
for i in range(n):
    for j in range(m):
        ans += max(nrj[i][j])
print(ans)