from functools import cache

@cache
def rec(i, j, cur, z, s, cnt):
    if i == len(s) and j == len(cnt): return 1
    if i == len(s): return 0
    if j == len(cnt): return int('#' not in s[i:])
    if s[i] == '.':
        if cur == 0:
            return rec(i+1, j, 0, '.', s, cnt)
        if cur == cnt[j]:
            return rec(i+1, j+1, 0, '.', s, cnt)
        return 0
    elif s[i] == '#':
        if cur == 0 and z=='#':
            return 0
        if cur + 1 < cnt[j]:
            return rec(i+1, j, cur+1, '#', s, cnt)
        if cur + 1 == cnt[j]:
            return rec(i+1, j+1, 0, '#', s, cnt)
        return 0
    else:
        res = 0
        # '.'
        if cur == 0:
            res += rec(i+1, j, 0, '.', s, cnt)
        elif cur == cnt[j]:
            res += rec(i+1, j+1, 0, '.', s, cnt)
        # '#'
        if cur > 0 or z!='#':
            if cur + 1 < cnt[j]:
                res += rec(i+1, j, cur + 1, '#', s, cnt)
            elif cur + 1 == cnt[j]:
                res += rec(i+1, j+1, 0, '#', s, cnt)
        return res

ans = 0
while True:
    try:
        s, cnt = input().split()
        s = '?'.join([s] * 5)
        cnt = list(map(int,','.join([cnt] * 5).split(',')))
        ans += rec(0, 0, 0, "", s, tuple(cnt))
    except EOFError:
        break
print(ans)