# 10942번

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = []

for _ in range(M):
    questions.append(list(map(int, input().split())))

dp = [0 if i % 2 == 0 else 0.5 for i in range(N*2)]

for q in questions:
    s, e = q
    mid = (s+e) / 2

    offset = e - mid

    i = dp[(s+e)-2]
    while i <= offset and mid-i >= 0:
        if nums[int(mid+i)-1] != nums[int(mid-i)-1]:
            if i-1 >= 0:
                dp[(s+e)-2] = i-1
            print(0)
            break
        i += 1
    else:
        dp[(s+e)-2] = i
        print(1)
