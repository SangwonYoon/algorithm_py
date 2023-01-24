# 12738번

import sys
input = sys.stdin.readline

def bin_search(dp, s, e, target):
    if s == e:
        return s
    m = (s+e) // 2
    if dp[m] == target:
        return m
    elif dp[m] > target:
        return bin_search(dp, s, m, target)
    else:
        return bin_search(dp, m+1, e, target)

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bin_search(dp, 0, len(dp)-1, arr[i])
        dp[idx] = arr[i]

print(len(dp))