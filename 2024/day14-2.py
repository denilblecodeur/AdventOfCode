import sys

w, h = 101, 103
rbs = []
for line in sys.stdin:
    p, v = line.split()
    p = tuple(map(int,p.strip('p=').split(',')))
    v = tuple(map(int,v.strip('v=').split(',')))
    rbs.append((p,v))

seen = set()
sec = 1
while True:
    g = [[0]*w for _ in range(h)]
    for p, v in rbs:
        x, y = (p[0]+v[0]*sec)%w,(p[1]+v[1]*sec)%h
        g[y][x] += 1
    if max(max(g[i]) for i in range(h)) == 1:
        print(sec)
        for i in range(h):print(''.join(" 0"[x] for x in g[i]))
        print('-'*w)
    hash = ''.join(''.join(map(str,g[i])) for i in range(h))
    if hash in seen: print(sec) & exit()
    seen.add(hash)
    sec += 1