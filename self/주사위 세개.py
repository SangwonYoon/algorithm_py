# 2480번

import sys

input = sys.stdin.readline

inputs = list(map(int, input().split()))
nums = [0] * 7

for n in inputs:
    nums[n] += 1

if max(nums) == 3:
    print(nums.index(3) * 1000 + 10000)
elif max(nums) == 2:
    print(nums.index(2) * 100 + 1000)
else:
    print(sorted(inputs)[-1] * 100)