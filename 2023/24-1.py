import math

pos, vel = [], []
while True:
    try:
        a, b = input().split(' @ ')
        px, py, pz = map(int,a.split(', '))
        vx, vy, vz = map(int,b.split(', '))
        pos.append((px, py, pz))
        vel.append((vx, vy, vz))
    except EOFError:
        break

lo, hi = 200000000000000, 400000000000000
n = len(pos)
ans = 0
for i in range(n):
    ai = round(vel[i][1] / vel[i][0], 7)
    bi = round(pos[i][1] - ai * pos[i][0], 7)
    for j in range(i):
        aj = round(vel[j][1] / vel[j][0], 7)
        bj = round(pos[j][1] - aj * pos[j][0], 7)
        if ai == aj:
            if bi == bj:
                ans += 1
        else:
            x = round((bj - bi)/(ai - aj), 7)
            y = round(ai*x+bi, 7)
            if lo<=x<=hi and lo<=y<=hi:
                if math.dist((x, y), pos[i][:-1])>math.dist((x, y), (pos[i][0]+vel[i][0], pos[i][1]+vel[i][1])) and\
                math.dist((x, y), pos[j][:-1])>math.dist((x, y), (pos[j][0]+vel[j][0], pos[j][1]+vel[j][1])):
                    ans += 1
print(ans)