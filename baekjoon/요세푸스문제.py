# 1158번

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]
order = []
n = 1

for _ in range(N):
    n += K-1
    n = (n-1) % len(nums) + 1
    order.append(nums.pop(n-1))

print("<", end = "")
print(", ".join(list(map(str, order))), end = "")
print(">")