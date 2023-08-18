# 9465번

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == 1:
        print(max(a[0], b[0]))
        continue
    
    score = list(zip(a, b))
    dp = [(score[0][0], score[0][1]), (score[0][1] + score[1][0], score[0][0] + score[1][1])]
    
    for i in range(2, len(score)):
        up = max(dp[i-2][1], dp[i-1][1]) + score[i][0]
        down = max(dp[i-2][0], dp[i-1][0]) + score[i][1]
        dp.append((up, down))

    print(max(dp[-1][0], dp[-1][1]))