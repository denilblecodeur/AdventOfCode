state = set(map(int,input().split()[1:]))
print(state)
newstate = set()
input()
for _ in range(7):
    print(input())
    mapped = set()
    while True:
        try: s = input()
        except EOFError: s = ''
        if s == '': break
        a, b, r = map(int,s.split())
        for s in state:
            if b <= s < b + r:
                newstate.add(a + s - b)
                mapped.add(s)
    for s in state:
        if s not in mapped:
            newstate.add(s)
    state, newstate = newstate, set()
    print(state)

print(min(state))