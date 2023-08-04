# 11066번

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    acc = [0]
    for i in range(len(files)):
        acc.append(acc[i] + files[i])

    dp = [[0] * K for _ in range(K)]
    diag = 1
    
    while diag <= K-1:
        for i in range(K-diag):
            j = i + diag
            for k in range(i, j):
                if dp[i][j] == 0 or dp[i][j] > dp[i][k] + dp[k+1][j] + acc[j+1] - acc[i]:
                    dp[i][j] = dp[i][k] + dp[k+1][j] + acc[j+1] - acc[i]
        diag += 1

    print(dp[0][K-1])