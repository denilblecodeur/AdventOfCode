import sys
from functools import cache

tw = input().split(', '); input()

@cache
def solve(goal):
    if goal == '': return True
    for w in tw:
        if goal[:len(w)] == w and solve(goal[len(w):]):
            return True
    return False

ans = 0
for line in sys.stdin:
    if solve(line.rstrip('\n')):
        ans += 1
print(ans)