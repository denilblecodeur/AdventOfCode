a = list(map(int,input().split()))

def stone(s):
    if s == 0:
        return [1]
    if len(str(s))&1:
        return [s*2024]
    x,y = str(s)[:len(str(s))>>1],str(s)[len(str(s))>>1:]
    return [int(y),int(x)]

for _ in range(25):
    b = []
    for i in range(len(a)):
        b.extend(stone(a[i]))
    a = b
print(len(a))