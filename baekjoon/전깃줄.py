# 2565번

import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(list(map(int, input().split())))
l.sort(key = lambda x : x[0])

arr = []
for i in range(N):
    arr.append(l[i][1])

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(N-max(dp))