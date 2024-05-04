# 2503번

import sys

input = sys.stdin.readline

def compare(num_a, num_b):
    a = list(num_a)
    b = list(num_b)

    strike = 0
    ball = 0

    for i in range(3):
        if a[i] == b[i]:
            strike += 1
            continue
        else:
            for j in range(3):
                if a[i] == b[j]:
                    ball += 1
                    break

    return (strike, ball)


nums = []

for n in range(100, 1000):
    nums.append(str(n))

for idx in range(len(nums)-1, -1, -1):
    if "0" in nums[idx] or len(set(nums[idx])) < 3:
        nums.pop(idx)

N = int(input())

for _ in range(N):
    query_num, strike, ball = map(int, input().split())
    for idx in range(len(nums)-1, -1, -1):
        s, b = compare(nums[idx], str(query_num))
        if s != strike or b != ball:
            nums.pop(idx)

print(len(nums))