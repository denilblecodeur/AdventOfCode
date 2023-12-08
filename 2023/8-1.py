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
cur = 'AAA'
while True:
    for l in instr:
        cur = adj[cur][l == 'R']
        if cur == 'ZZZ':
            print(cnt)
            break
        cnt += 1
    else:
        continue
    break