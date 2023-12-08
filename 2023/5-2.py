state = set()
inputs = list(map(int,input().split()[1:]))
for i in range(0, len(inputs), 2):
    state.add((tuple(inputs[i: i+2])))
print(state)
newstate = set()
input()
for _ in range(7):
    print(input())
    _map = []
    while True:
        try: s = input()
        except EOFError: s = ''
        if s == '': break
        _map.append(tuple(map(int,s.split())))
    for s, rng in state:
        for a, b, r in sorted(_map, key=lambda t:t[1]):
            lo, hi = b, b + r
            if s < lo:
                newstate.add((s, min(rng, lo - s)))
                rng -= min(rng, lo - s)
                s = lo
                if rng <= 0: break
            if s < hi:
                if s + rng <= hi:
                    newstate.add((a + (s - lo), rng))
                    rng = 0
                else:
                    newstate.add((a + (s - lo), hi - s))
                    rng -= hi - s
                    s = hi
                if rng <= 0: break
        else:
            newstate.add((s, rng))
    state, newstate = newstate, set()
    print(state)

print(min(state))