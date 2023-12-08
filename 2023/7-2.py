cards = []
while True:
    try:
        a, b = input().split()
        cards.append((a, b))
    except EOFError:
        break

rank = [[] for _ in range(7)]
order = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(', ')

from collections import Counter

for i in range(len(cards)):
    card = cards[i][0]
    J = card.count('J')
    C = Counter(card).most_common()
    if len(C) == 1:
        rank[0].append(i)
    elif len(C) == 2:
        if J > 0:
            rank[0].append(i)
        elif C[0][1] == 4:
            rank[1].append(i)
        else:
            assert C[0][1] == 3
            rank[2].append(i)
    elif len(C) == 3:
        if J > 0:
            baz = [c for c in C if c[0] != 'J']
            if baz[0][1] + J == 4:
                rank[1].append(i)
            else:
                assert baz[0][1] + J == 3
                rank[2].append(i)
        elif C[0][1] == 3:
            rank[3].append(i)
        else:
            assert C[0][1] == 2
            rank[4].append(i)
    elif len(C) == 4:
        if J > 0:
            rank[3].append(i)
        else:
            rank[5].append(i)
    else:
        if J > 0:
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