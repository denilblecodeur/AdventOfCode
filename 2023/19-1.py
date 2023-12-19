import re

work = {}
while True:
    s = input()
    if s == '': break
    name, dic = s[:s.find('{')], s[s.find('{'):]
    dic = dic[:dic.rfind(',')+1] + 'default:' + dic[dic.rfind(',')+1:]
    dic = dic.strip('}{').split(',')
    work[name] = dic

ans = 0
while True:
    try:
        i = 0
        val = [0] * 4
        for n in re.split(r'\D+', input()):
            if len(n) == 0: continue
            val[i] = int(n)
            i += 1
        x, m, a, s = val
        cur = 'in'
        while cur not in 'AR':
            for regle in work[cur]:
                p1, p2 = regle.split(':')
                if p1 == 'default' or eval(p1):
                    cur = p2
                    break
        if cur == 'A':
            ans += sum(val)
    except EOFError:
        break
print(ans)