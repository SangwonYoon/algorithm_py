# 14719번

import sys
input = sys.stdin.readline

H, W = map(int, input().split())

cell = list(map(int, input().split()))
answer = 0

for i in range(1, H+1):
    s = 0
    e = W-1

    while s < W and cell[s] < i: s += 1
    while e >= 0 and cell[e] < i: e -= 1
    if s >= e:
        break
    for j in range(s+1, e):
        if cell[j] < i:
            answer += 1

print(answer)