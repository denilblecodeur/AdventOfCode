import sys

def f(x):
    x = ((x*64)^x)%16777216
    x = ((x//32)^x)%16777216
    x = ((x*2048)^x)%16777216
    return x

sequences = []
possibilities = set()
for line in sys.stdin:
    seed = int(line.strip('\n'))
    ban = [seed%10]
    change = []
    for _ in range(2000):
        seed = f(seed)
        ban.append(seed%10)
        change.append(ban[-2]-ban[-1])
    sc = dict()
    for i in range(len(change)-4):
        seq = tuple(change[i:i+4])
        if seq not in sc:
            sc[seq] = ban[i+4]
            possibilities.add(seq)
    sequences.append(sc)

ans = 0
for p in possibilities:
    res = 0
    for sc in sequences:
        res += sc.get(p, 0)
    ans = max(ans, res)
print(ans)