# 11659번

import sys
input = sys.stdin.readline

total = 0
nums_total = list()
N, M = map(int,input().split())
nums = list(map(int,input().split()))
for i in nums:
    total += i 
    nums_total.append(total)

for i in range(M):
    a, b = map(int,input().split())
    if a == 1:
        print(nums_total[b-1])
    else:
        print(nums_total[b-1]-nums_total[a-2])