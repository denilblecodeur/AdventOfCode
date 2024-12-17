A = int(input().split(': ')[-1])
B = int(input().split(': ')[-1])
C = int(input().split(': ')[-1])
input()
program = input().split()[1]
P = list(map(int,program.split(',')))
n = len(P)
ptr = 0
ans = []
while ptr < n:
    opcode, operand = P[ptr], P[ptr+1]
    combo = [0,1,2,3,A,B,C][operand]
    if opcode in (0,6,7):
        res = A // (1 << combo)
        if opcode == 0: A = res
        elif opcode == 6: B = res
        else: C = res
    elif opcode == 1:
        B ^= operand
    elif opcode == 2:
        B = combo % 8
    elif opcode == 3:
        if A != 0:
            ptr = operand
            continue
    elif opcode == 4:
        B ^= C
    elif opcode == 5:
        ans.append(combo % 8)
    ptr += 2
print(','.join(map(str,ans)))