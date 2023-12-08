ans = 0
S="red green blue".split()
while True:
    try:
        game, s = input().split(': ')
        _id = int(game.split()[-1])
        good = [0] * 3
        for l in s.split('; '):
            for c in l.split(', '):
                a, b = c.split()
                good[S.index(b)] = max(good[S.index(b)], int(a))
        ans += good[0] * good[1] * good[2]
    except:break
print(ans)