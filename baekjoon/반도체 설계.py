# 2352번

import sys
input = sys.stdin.readline

def bin_search(arr, s, e, target):
    if s == e:
        return s
    m = (s+e) // 2
    if target < arr[m]:
        return bin_search(arr, s, m, target)
    elif target == arr[m]:
        return m
    else:
        return bin_search(arr, m+1, e, target)

n = int(input())
ports = list(map(int, input().split()))

dp = [ports[0]]

for i in range(1, len(ports)):
    if dp[-1] < ports[i]:
        dp.append(ports[i])
    else:
        idx = bin_search(dp, 0, len(dp)-1, ports[i])
        dp[idx] = ports[i]

print(len(dp))