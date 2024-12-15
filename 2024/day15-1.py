import sys
g = []
start = nl = None
moves = ""
for i, line in enumerate(sys.stdin):
    if line == '\n': nl = True; continue
    if nl: moves += line.rstrip('\n')
    else:
        if '@' in line: start = (i, line.find('@'))
        g.append(list(line.rstrip('\n')))
n, m = len(g), len(g[0])

i, j = start
for mv in moves:
    di, dj = {'^':(-1,0), 'v':(1,0), '>':(0,1), '<':(0,-1)}[mv]
    if g[i+di][j+dj] != '#':
        if g[i+di][j+dj] == 'O':
            k = 1
            while g[i+(k+1)*di][j+(k+1)*dj] == 'O': k += 1
            if g[i+(k+1)*di][j+(k+1)*dj] == '.':
                g[i][j] = '.'
                g[i+di][j+dj] = '@'
                for kk in range(2, k+2):
                    g[i+kk*di][j+kk*dj] = 'O'
                i, j = i+di, j+dj
            else: assert g[i+(k+1)*di][j+(k+1)*dj] == '#'
        else:
            g[i][j] = '.'
            g[i+di][j+dj] = '@'
            i, j = i+di, j+dj

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 'O':
            ans += 100*i+j
print(ans)
