ans = 0
while True:
    try:
        a = [list(map(int,input().split()))]
        while any(x != 0 for x in a[-1]):
            a.append([a[-1][i] - a[-1][i-1] for i in range(1, len(a[-1]))])
        for i in range(len(a)):
            a[i].reverse()
        a[-1].append(0)
        for i in reversed(range(len(a) - 1)):
            a[i].append(a[i][-1] - a[i + 1][-1])
        ans += a[0][-1]
    except EOFError:
        break
print(ans)