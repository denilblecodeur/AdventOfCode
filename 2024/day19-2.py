import sys
from functools import cache

tw = input().split(', '); input()

@cache
def solve(goal):
    if goal == '': return 1
    res = 0
    for w in tw:
        if goal[:len(w)] == w:
            res += solve(goal[len(w):])
    return res

ans = 0
for line in sys.stdin:
    ans += solve(line.rstrip('\n'))
print(ans)