#1912번

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
sum = [nums[0]]

for i in range(1,n):
    if sum[i-1] > 0:
        sum.append(sum[i-1] + nums[i])
    else:
        sum.append(nums[i])

print(max(sum))