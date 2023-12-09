ans = 0
while True:
    try:
        a = [list(map(int,input().split()))]
        while any(x != 0 for x in a[-1]):
            a.append([a[-1][i] - a[-1][i-1] for i in range(1, len(a[-1]))])
        ans += sum(b[-1] for b in a)
    except EOFError:
        break
print(ans)