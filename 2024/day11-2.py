from functools import cache

a = list(map(int,input().split()))

@cache
def solve(s, depth=0):
    if depth==75:
        return 1
    if s == 0:
        return solve(1, depth+1)
    if len(str(s))&1:
        return solve(s*2024, depth+1)
    x,y = str(s)[:len(str(s))>>1], str(s)[len(str(s))>>1:]
    return solve(int(y), depth+1) + solve(int(x), depth+1)

ans = 0
for s in a:
    ans += solve(s)
print(ans)