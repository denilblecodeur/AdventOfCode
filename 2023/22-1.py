bricks = []
while True:
    try:
        a,b = input().split('~')
        xa,ya,za = map(int,a.split(','))
        xb,yb,zb = map(int,b.split(','))
        bricks.append([(xa,ya,za), (xb,yb,zb)])
    except EOFError:
        break

n = len(bricks)
bricks.sort(key=lambda t:min(t[0][2], t[1][2]))

hauteur = [[0] * 10 for _ in range(10)]
idx = [[None] * 10 for _ in range(10)]
hold = [set() for _ in range(n)]
ishold = []

for i, [(xa,ya,za), (xb,yb,zb)] in enumerate(bricks):
    min_z = 0
    holder = set()
    for x in range(xa, xb + 1):
        for y in range(ya, yb + 1):
            if hauteur[x][y] > min_z:
                min_z = hauteur[x][y]
                holder = {idx[x][y]}
            elif hauteur[x][y] == min_z:
                if idx[x][y] is not None:
                    holder.add(idx[x][y])
    for x in range(xa, xb + 1):
        for y in range(ya, yb + 1):
            hauteur[x][y] = min_z + (zb - za + 1)
            idx[x][y] = i
    ishold.append(holder)
    for j in holder:
        hold[j].add(i)

ans = 0
for i in range(n):
    free = True
    for j in hold[i]:
        free &= len(ishold[j]) > 1
    ans += free
print(ans)