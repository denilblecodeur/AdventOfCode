ans = 0
for s in input().split(','):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    ans += cur
print(ans)