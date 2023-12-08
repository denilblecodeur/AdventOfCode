_, *time = input().split()
_, *dist = input().split()

ans = 1
for t, d in zip(time, dist):
    t, d = int(t), int(d)
    ans *= sum((t - start) * start > d for start in range(t))

print(ans)