# 11054번

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

dp_inc = [1] * N
dp_dec = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and dp_inc[i] < dp_inc[j] + 1:
            dp_inc[i] = dp_inc[j] + 1
        if arr[N-1-i] > arr[N-1-j] and dp_dec[N-1-i] < dp_dec[N-1-j] + 1:
            dp_dec[N-1-i] = dp_dec[N-1-j] + 1

result = []
for i in range(N):
    result.append(dp_inc[i] + dp_dec[i])

print(max(result)-1)