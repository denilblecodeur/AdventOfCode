instr = input()
input()
adj = {}
while True:
    try:
        a, b = input().split(' = ')
        x, y = b.strip('()').split(', ')
        adj[a] = (x, y)
    except EOFError:
        break

cnt = 1
cur = [v for v in adj if v[-1] == 'A']
cycle = [float('inf')] * len(cur)
while True:
    for l in instr:
        cur = [adj[v][l == 'R'] for v in cur]
        for i in range(len(cur)):
            if cur[i][-1] == 'Z':
                cycle[i] = min(cycle[i], cnt)
        if not float('inf') in cycle:
            break
        cnt += 1
    else:
        continue
    break

from math import lcm
ans = 1
for v in cycle:
    ans = lcm(ans, v)
print(ans)