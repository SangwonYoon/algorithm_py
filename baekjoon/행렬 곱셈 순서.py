# 11049번

import sys
input = sys.stdin.readline

N = int(input())
size = []
r, c = map(int ,input().split())
size.append(r)
size.append(c)

for _ in range(N-1):
    size.append(list(map(int, input().split()))[1])

dp = [[0] * N for _ in range(N)]
diag = 1

while diag <= N-1:
    for i in range(N-diag):
        j = i + diag
        m = dp[i+1][j] + size[i]*size[i+1]*size[j+1]
        for k in range(i+1, j):
            m = min(m, dp[i][k] + dp[k+1][j] + size[i]*size[k+1]*size[j+1])
        dp[i][j] = m
    diag += 1

print(dp[0][N-1])