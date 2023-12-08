ans = 0
d = "zero one two three four five six seven eight nine".split()
while True:
    try:
        s = input()
        A = B = None
        for i in range(len(s)):
            if s[i].isdigit():
                if not A:
                    A = int(s[i])
                B = int(s[i])
            else:
                for w in d:
                    if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                        if not A:
                            A = w
                        B = w
        if type(A) != int:
            A = d.index(A)
        if type(B) != int:
            B = d.index(B)
        ans += int(str(A) + str(B))
    except: break
print(ans)