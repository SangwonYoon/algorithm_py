# 11053번

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1]

for i in range(1, len(arr)):
    dp.append(1)
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j]+1

print(max(dp))