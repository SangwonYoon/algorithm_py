#9461번

import sys
input = sys.stdin.readline

memo = [1,1,1,2,2]
for i in range(int(input())):
    N = int(input())
    for j in range(len(memo),N):
        memo.append(memo[j-1] + memo[j-5])
    print(memo[N-1])