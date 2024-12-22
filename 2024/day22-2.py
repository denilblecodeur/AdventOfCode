import sys
from collections import defaultdict

def f(x):
    x = ((x*64)^x)%16777216
    x = ((x//32)^x)%16777216
    x = ((x*2048)^x)%16777216
    return x

sequences = defaultdict(int)
for line in sys.stdin:
    seed = int(line.strip('\n'))
    ban = [seed%10]
    change = []
    for _ in range(2000):
        seed = f(seed)
        ban.append(seed%10)
        change.append(ban[-2]-ban[-1])
    sc = set()
    for i in range(len(change)-4):
        seq = tuple(change[i:i+4])
        if seq in sc: continue
        sc.add(seq)
        sequences[seq] += ban[i+4]

print(max(sequences.values()))