ans = 0
S="red green blue".split()
while True:
    try:
        game, s = input().split(': ')
        _id = int(game.split()[-1])
        good = True
        for l in s.split('; '):
            for c in l.split(', '):
                a, b = c.split()
                good &= (int(a) <= 12+S.index(b))
        if good:
            ans += _id
    except:break
print(ans)