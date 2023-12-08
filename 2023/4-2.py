mul = [1] * 1000
i = 0
while True:
    i += 1
    try:
        a, c = input().split(' | ')
        a, b = a.split(': ')
        b = list(map(int,b.split()))
        cnt = sum(x in b for x in map(int,c.split()))
        if cnt:
            for j in range(i, i + cnt):
                mul[j] += mul[i-1]
    except EOFError:
        break

print(sum(mul[:i-1]))