import sys

g = []
for line in sys.stdin:
    g.append(line.rstrip('\n'))

n,m=len(g),len(g[0])
ans = 0

def solve(i,j):
    letter = g[i][j]
    Q = [(i,j)]
    pts = b = 0
    while Q:
        i,j=Q.pop()
        if vis[i][j]:continue
        vis[i][j] = 1
        pts += 1
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<n and 0<=j+dj<m and g[i+di][j+dj] == letter:
                Q.append((i+di,j+dj))
            else:
                b += 1
    return pts * b

vis = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            ans += solve(i,j)
print(ans)