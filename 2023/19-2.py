import re

work = {}
while True:
    s = input()
    if s == '': break
    name, dic = s[:s.find('{')], s[s.find('{'):]
    dic = dic[:dic.rfind(',')+1] + 'default:' + dic[dic.rfind(',')+1:]
    dic = dic.strip('}{').split(',')
    work[name] = dic

Q = [([[1, 4000] for _ in range(4)], 'in')]
accepted = set()
while Q:
    xmas, cur = Q.pop()
    for regle in work[cur]:
        p1, p2 = regle.split(':')
        new = [list(X) for X in xmas]
        if p1 == 'default':
            if p2 in 'AR':
                if p2 == 'A': accepted.add(tuple(tuple(X) for X in new))
            else:
                Q.append((new, p2))
        else:
            sign = re.search(r'[<>]+', p1)[0]
            term, val = p1.split(sign)
            term = "xmas".find(term)
            if sign == '>':
                new[term][0] = int(val) + 1
                xmas[term][1] = int(val)
            elif sign == '<':
                new[term][1] = int(val) - 1
                xmas[term][0] = int(val)
            if p2 in 'AR':
                if p2 == 'A': accepted.add(tuple(tuple(X) for X in new))
            else:
                Q.append((new, p2))

ans = 0
for tup in accepted:
    cur = 1
    for lo, hi in tup:
        cur *= (hi - lo + 1)
    ans += cur
print(ans)