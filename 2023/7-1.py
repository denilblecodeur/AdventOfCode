cards = []
while True:
    try:
        a, b = input().split()
        cards.append((a, b))
    except EOFError:
        break

rank = [[] for _ in range(7)]
order = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(', ')

from collections import Counter

for i in range(len(cards)):
    card = cards[i][0]
    C = Counter(card).most_common()
    if len(C) == 1:
        rank[0].append(i)
    elif len(C) == 2:
        if C[0][1] == 4:
            rank[1].append(i)
        else:
            rank[2].append(i)
    elif len(C) == 3:
        if C[0][1] == 3:
            rank[3].append(i)
        else:
            rank[4].append(i)
    elif len(C) == 4:
        rank[5].append(i)
    else:
        rank[6].append(i)

def f(card):
    score = 0
    for i, c in enumerate(card):
        score *= len(order)
        score += len(order) - order.index(c)
    return score

ans = 0
tot = len(cards)
for run in rank:
    run.sort(key=lambda i:-f(cards[i][0]))
    for i in run:
        ans += int(cards[i][1]) * tot
        tot -= 1
print(ans)