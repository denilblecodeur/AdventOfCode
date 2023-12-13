def solve(rows):
    n, m = len(rows), len(rows[0])
    cols = [list(c) for c in zip(*rows)]
    for i in range(n - 1):
        d = min(i + 1, n - i - 1)
        if [rows[k] for k in range(i - d + 1, i + 1)] == [rows[k] for k in range(i + 1, i + d + 1)][::-1]:
            return 100 * (i + 1)
    for j in range(m - 1):
        d = min(j + 1, m - j - 1)
        if [cols[k] for k in range(j - d + 1, j + 1)] == [cols[k] for k in range(j + 1, j + d + 1)][::-1]:
            return j + 1

ans = 0
rows = []
while True:
    try:
        s = input()
        if s == '':
            ans += solve(rows)
            rows = []
        else:
            rows.append(s)
    except EOFError:
        break
print(ans)