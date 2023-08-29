# 2822번

import sys

input = sys.stdin.readline

scores = []
for i in range(8):
    scores.append([i+1, int(input())])

scores.sort(key=lambda x : -x[1])
total = 0
order = []

for i in range(5):
    total += scores[i][1]
    order.append(scores[i][0])

print(total)
print(*sorted(order))
