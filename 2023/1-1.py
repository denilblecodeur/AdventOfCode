ans = 0
while True:
    try:
        s = [x for x in input() if x.isdigit()]
        ans += int(s[0] + s[-1])
    except: break
print(ans)