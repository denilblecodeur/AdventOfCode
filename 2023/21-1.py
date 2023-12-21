grid = []
start = None
while True:
    try:
        s = input()
        if 'S' in s:
            start = len(grid), s.find('S')
            s = s.replace('S', '.')
        grid.append(s)
    except EOFError:
        break
n, m = len(grid), len(grid[0])

Q = [start]
for _ in range(64):
    newQ = []
    for i, j in Q:
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<n and 0<=j+dj<m and grid[i+di][j+dj] == '.':
                newQ.append((i+di,j+dj))
    Q=list(set(newQ))
print(len(set(Q)))