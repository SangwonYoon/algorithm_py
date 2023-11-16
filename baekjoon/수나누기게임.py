#27172번

from math import sqrt
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = max(nums)
scores = [0] * (M+1)

card_exist = [False] * (M+1)
for n in nums:
    card_exist[n] = True

for num in nums:
    k = 2
    while k * num <= M:
        target = k * num
        if card_exist[target]:
            scores[num] += 1
            scores[target] -= 1
        k += 1

for num in nums:
    print(scores[num], end = " ")