ans = 0
while True:
    try:
        a, c = input().split(' | ')
        a, b = a.split(': ')
        b = list(map(int,b.split()))
        cnt = sum(x in b for x in map(int,c.split()))
        if cnt:
            ans += 1 << (cnt-1)
    except EOFError:
        break
print(ans)