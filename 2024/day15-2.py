import sys
import time
g = []
start = nl = None
moves = ""
for i, line in enumerate(sys.stdin):
    if line == '\n': nl = True; continue
    if nl: moves += line.rstrip('\n')
    else:
        line = line.replace('#', '##')
        line = line.replace('O', '[]')
        line = line.replace('.', '..')
        line = line.replace('@', '@.')
        if '@' in line: start = (i, line.find('@'))
        g.append(list(line.rstrip('\n')))
n, m = len(g), len(g[0])

def see():
    for i in range(n): print(*g[i], sep='')
    print(' '*m)
    time.sleep(0.5)
see()

i, j = start
for mv in moves:
    di, dj = {'^':(-1,0), 'v':(1,0), '>':(0,1), '<':(0,-1)}[mv]
    if g[i+di][j+dj] in '[]':
        if mv in '<>':
            k = 1
            while g[i][j+(k+1)*dj] in '[]': k += 1
            if g[i][j+(k+1)*dj] == '.':
                for kk in reversed(range(2, k+2)):
                    g[i][j+kk*dj] = g[i][j+(kk-1)*dj]
                g[i][j] = '.'
                g[i][j+dj] = '@'
                j += dj
            else: assert g[i][j+(k+1)*dj] == '#'
        else:
            Q = [(i,j)]
            for ii, jj in Q:
                if g[ii+di][jj] == '[':
                    Q.extend([(ii+di,jj), (ii+di,jj+1)])
                elif g[ii+di][jj] == ']':
                    Q.extend([(ii+di,jj), (ii+di,jj-1)])
            Q.pop(0)
            touch = False
            for ii, jj in Q:
                touch |= g[ii+di][jj] == '#'
            if not touch:
                Q = sorted(set(Q), reverse=bool(mv=='v'))
                for ii, jj in Q:
                    g[ii+di][jj] = g[ii][jj]
                    g[ii][jj] = '.'
                g[i][j] = '.'
                g[i+di][j] = '@'
                i += di
    elif g[i+di][j+dj] == '.':
        g[i][j] = '.'
        g[i+di][j+dj] = '@'
        i, j = i+di, j+dj

    see()

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == '[':
            ans += 100*i+j
print(ans)
