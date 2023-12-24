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

n = len(pos)
ans = 0

rays = set(range(n))

for i in range(n):
    for j in range(i):
        if round(vel[i][0] / vel[j][0], 7) == round(vel[i][1] / vel[j][1], 7) == round(vel[i][2] / vel[j][2], 7):
            rays.remove(i)
            break

a, b, c, *_ = rays

pos = [pos[i] for i in (a, b, c)]
vel = [vel[i] for i in (a, b, c)]

"""
SAGE MATH part

var('x y z dx dy dz t s u v')
xyz = x,y,z
dxyz = dx,dy,dz
dtsu = t,s,u

eq = [xyz[j] + dtsu[i] * (dxyz[j] - vel[i][j]) - pos[i][j] for i in range(3) for j in range(3)]

ans = solve(eq, (x,y,z,dx,dy,dz,t,s,u,v))[0][:3]

sum(ans[i].rhs() for i in range(3))
"""