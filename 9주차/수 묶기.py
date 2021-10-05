#1744번

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort(reverse = True)
answer = 0
for j in range(0,len(nums),2):
    if j != len(nums)-1 and nums[j+1] > 1:
        answer += nums[j] * nums[j+1]
    else:
        if nums[j] > 0:
            answer += nums[j]
        if j != len(nums)-1 and nums[j+1] == 1:
            answer += nums[j+1]

for k in range(len(nums)-1,-1,-2):
    if k != 0 and nums[k-1] <= 0:
        answer += nums[k] * nums[k-1]
    else:
        if nums[k] <= 0:
            answer += nums[k]

print(answer)