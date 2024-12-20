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

def solve():
    Q = [(*s,0)]
    vis = [[0]*m for _ in range(n)]
    vis[s[0]][s[1]] = 1
    for i, j, d in Q:
        if (i,j) == e:
            return d
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if g[i+di][j+dj] != '#' and not vis[i+di][j+dj]:
                vis[i+di][j+dj] = 1
                Q.append((i+di,j+dj,d+1))
    return float('inf')

res = solve()
ans = 0
for i in range(n):
    for j in range(m):
        if 0<i<n-1 and 0<j<m-1 and g[i][j] == '#':
            g[i][j] = '.'
            r = solve()
            if res-100 >= r:
                ans += 1
            g[i][j] = '#'
print(ans)
