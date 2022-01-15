#11652번

import sys
input = sys.stdin.readline

N = int(input())
nums = dict()
max = 0
idx = -1

for i in range(N):
    temp = int(input())
    if temp in nums:
        nums[temp] += 1
    else:
        nums[temp] = 1
    if nums[temp] > max:
        max = nums[temp]
        idx = temp
    elif nums[temp] == max and temp < idx:
        idx = temp

print(idx)