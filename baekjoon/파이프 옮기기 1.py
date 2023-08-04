# 17070번

import sys
input = sys.stdin.readline

N = int(input())

cell = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if cell[i][j] != 1:
            if i == 0 and (j == 0 or j == 1):
                pass
            elif i == 0:
                dp[i][j][0] = dp[i][j-1][0]
            elif j == 0:
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
                if cell[i][j-1] == 0 and cell[i-1][j] == 0:
                    dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))
