import sys

g = []
s = e = None
for i, line in enumerate(sys.stdin):
    line = line.rstrip('\n')
    if 'S' in line:
        s = (i, line.find('S'))
        line = line.replace('S', '.')
    if 'E' in line:
        e = (i, line.find('E'))
        line = line.replace('E', '.')
    g.append(list(line))
n,m = len(g), len(g[0])

def solve(start):
    Q = [(*start,0)]
    dist = [[None]*m for _ in range(n)]
    dist[start[0]][start[1]] = 0
    for i, j, d in Q:
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if g[i+di][j+dj] != '#' and dist[i+di][j+dj] is None:
                dist[i+di][j+dj] = d+1
                Q.append((i+di,j+dj,d+1))
    return dist

fromS = solve(s)
fromE = solve(e)
lb = fromS[e[0]][e[1]]-100
ans = 0
for i in range(n):
    for j in range(m):
        if fromS[i][j] is None: continue
        for ii in range(n):
            for jj in range(m):
                d = abs(i-ii)+abs(j-jj)
                if d > 20: continue
                if fromE[ii][jj] is None: continue
                if fromS[i][j] + fromE[ii][jj] + d <= lb:
                    ans += 1
print(ans)