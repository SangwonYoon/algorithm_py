# 11052번

import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

cost = [[0] * (N+1) for _ in range(N)]

for i in range(N):
    for j in range(1, N+1):
        if i == 0:
            cost[i][j] = cost[i][j-(i+1)] + p[i]
        else:
            if j <= i:
                cost[i][j] = cost[i-1][j]
            else:
                cost[i][j] = max(cost[i-1][j], cost[i][j-(i+1)] + p[i])

print(cost[-1][-1])