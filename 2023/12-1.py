from itertools import groupby

ans = 0
while True:
    try:
        s, cnt = input().split()
        cnt = list(map(int,cnt.split(',')))
        n = s.count('?')
        for mask in range(1<<n):
            a = []
            i = 0
            for j in range(len(s)):
                if s[j] != '?':
                    a.append(s[j])
                else:
                    a.append('#' if mask >> i & 1 else '.')
                    i += 1
            i = 0
            for k, v in groupby(a):
                if k == '#':
                    if i >= len(cnt) or len(list(v)) != cnt[i]:
                        break
                    i+=1
            else:
                ans += i == len(cnt)
    except EOFError:
        break
print(ans)