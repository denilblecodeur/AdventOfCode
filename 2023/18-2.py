instr = []
while True:
    try:
        a, b, c = input().split()
        c = c.strip('()#')
        instr.append((int(c[:-1],16), "RDLU"[int(c[-1])]))
    except EOFError:
        break

pts = [(0, 0)]
D = ((0,1),(1,0),(0,-1),(-1,0)) # RDLU
i, j = 0, 0

boundary = 0
for n, d in instr:
    di, dj = D["RDLU".find(d)]
    i += n*di
    j += n*dj
    pts.append((i, j))
    boundary += n

def area(pts):
    A = 0
    for i in range(len(pts)):
        A += pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1]
    return int(abs(A / 2))

print(area(pts) + (boundary+2) // 2)