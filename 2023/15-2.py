import re

boxes = [{} for _ in range(256)]
for s in input().split(','):
    label, n = re.split(r'[=-]+', s)
    cur = 0
    for c in label:
        cur += ord(c)
        cur *= 17
        cur %= 256
    if len(n):
        boxes[cur][label] = int(n)
    elif label in boxes[cur]:
        del boxes[cur][label]

ans = 0
for i, slot in enumerate(boxes):
    for j, (k, val) in enumerate(slot.items()):
        ans += (i + 1) * (j + 1) * val
print(ans)