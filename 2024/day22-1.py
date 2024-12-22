import sys

def f(x):
    x = ((x*64)^x)%16777216
    x = ((x//32)^x)%16777216
    x = ((x*2048)^x)%16777216
    return x

ans = 0
for line in sys.stdin:
    seed = int(line.strip('\n'))
    for _ in range(2000):
        seed = f(seed)
    ans += seed
print(ans)