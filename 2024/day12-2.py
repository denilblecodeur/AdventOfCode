import sys

g = []
for line in sys.stdin:
    g.append(line.rstrip('\n'))

n,m=len(g),len(g[0])
ans = 0

def solve(i,j):
    letter = g[i][j]
    Q = [(i,j)]
    pts = 0
    col = [[] for _ in range((m+1)<<1)]
    row = [[] for _ in range((n+1)<<1)]
    while Q:
        i,j=Q.pop()
        if vis[i][j]:continue
        vis[i][j] = 1
        pts += 1
        for e, (di,dj) in enumerate(((0,1),(0,-1), (1,0),(-1,0))):
            if 0<=i+di<n and 0<=j+dj<m and g[i+di][j+dj] == letter:
                Q.append((i+di,j+dj))
            else:
                if e<2:
                    col[2*j+max(dj,0)].append(i)
                else:
                    row[2*i+max(di,0)].append(j)
    faces = 0
    for L in col, row:
        for comp in L:
            l = -2
            for r in sorted(comp):
                if l+1 < r:
                    faces += 1
                l = r
    return pts * faces

vis = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            ans += solve(i,j)
print(ans)