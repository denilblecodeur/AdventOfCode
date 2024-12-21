import sys

door = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [None,'0','A']
    ]
rob = [
    [None,'U','A'],
    ['L','D','R']
    ]
pos2door = dict()
for i in range(4):
    for j in range(3):
        pos2door[door[i][j]] = (i,j)

class State:
    def __init__(self, r1i, r2i, r3i, r1j, r2j, r3j):
        self.ri = [r1i,r2i,r3i]
        self.rj = [r1j,r2j,r3j]
    def __hash__(self):
        return hash(tuple(self.ri) + tuple(self.rj))
    def __eq__(self, other):
        return hash(self) == hash(other)
    def copy(self):
        return State(*self.ri, *self.rj)
    def get_adj(self):
        for mi in range(2):
            for mj in range(3):
                if rob[mi][mj] is None: continue
                nri = list(self.ri); nrj = list(self.rj)
                if rob[mi][mj] == 'A':
                    k = 0
                    while k<2 and rob[self.ri[k]][self.rj[k]] == 'A': k+=1
                    if k == 2: continue
                    di, dj = {'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}[rob[self.ri[k]][self.rj[k]]]
                else:
                    k = -1
                    di, dj = {'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}[rob[mi][mj]]
                nri[k+1] += di; nrj[k+1] += dj
                if k+1 < 2:
                    if 0<=nri[k+1]<2 and 0<=nrj[k+1]<3 and rob[nri[k+1]][nrj[k+1]] != None:
                        yield State(*nri, *nrj)
                else:
                    if 0<=nri[k+1]<4 and 0<=nrj[k+1]<3 and door[nri[k+1]][nrj[k+1]] != None:
                        yield State(*nri, *nrj)

ans = 0
for line in sys.stdin:
    code = line.rstrip('\n')
    Q = [(State(*[0,0,3], *[2,2,2]), 0, 0)]
    hsh = lambda t:hash((hash(t[0]), t[1], t[2]))
    seen = {hsh(Q[0])}
    res = None
    for (state, ptr, d) in Q:
        if ptr == len(code):
            res = d; break
        gi, gj = pos2door[code[ptr]]
        goal = State(*[0,0,gi], *[2,2,gj])
        if state == goal:
            h = hsh((state, ptr+1, d+1))
            if h not in seen:
                seen.add(h)
                Q.append((state, ptr+1, d+1))
            continue
        for st in state.get_adj():
            h = hsh((st, ptr, d+1))
            if h not in seen:
                seen.add(h)
                Q.append((st, ptr, d+1))
    assert res is not None
    print(code, res)
    ans += int(code.strip('A')) * res

print(ans)