import sys, math

w, h = 101, 103
g = [[0]*w for _ in range(h)]
ans = [0]*4
for line in sys.stdin:
    p, v = line.split()
    p = tuple(map(int,p.strip('p=').split(',')))
    v = tuple(map(int,v.strip('v=').split(',')))
    x, y = (p[0]+v[0]*100)%w,(p[1]+v[1]*100)%h
    if x<w//2 and y<h//2:
        ans[0]+=1
    if x<w//2 and y>h//2:
        ans[1]+=1
    if x>w//2 and y<h//2:
        ans[2]+=1
    if x>w//2 and y>h//2:
        ans[3]+=1
print(math.prod(ans))