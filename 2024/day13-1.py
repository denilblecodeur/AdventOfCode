def solve(ax, ay, bx, by, X, Y):
    num = X - (ax * Y) / ay
    den = bx - (ax * by) / ay
    B = num / den
    A = X / ax - (B * bx) / ax
    if min(A,B) < 0: return 0, 0
    return A, B

ans = 0
while True:
    _, x, y = input().replace(':', ',').split(', ')
    ax, ay = (int(x.strip('X')), int(y.strip('Y')))
    _, x, y = input().replace(':', ',').split(', ')
    bx, by = (int(x.strip('X')), int(y.strip('Y')))
    _, x, y = input().replace(':', ',').split(', ')
    X, Y = int(x.strip('X=')), int(y.strip('Y='))
    A, B = map(round,solve(ax, ay, bx, by, X, Y))
    if A*ax+B*bx == X and A*ay+B*by == Y:
        ans += 3*A+B
    try:input()
    except EOFError:break
print(ans)