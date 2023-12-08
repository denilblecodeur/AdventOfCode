time = int(''.join(input().split()[1:]))
dist = int(''.join(input().split()[1:]))

lo, hi = 0, (time + 1) // 2
while lo < hi:
    start = (lo + hi) // 2
    if (time - start) * start > dist:
        hi = start
    else:
        lo = start + 1

lower = lo

lo, hi = time // 2, time
while lo < hi:
    start = (lo + hi + 1) // 2
    if (time - start) * start > dist:
        lo = start
    else:
        hi = start - 1

upper = lo

print(upper - lower + 1)