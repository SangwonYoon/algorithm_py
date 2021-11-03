import sys
input = sys.stdin.readline

N, K = map(int,input().split())
things = [[0,0]]
for i in range(N):
    things.append(list(map(int,input().split())))
memo = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1,N+1):
    weight = things[i][0]
    value = things[i][1]
    for j in range(1,K+1):
        if j < weight:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(memo[i-1][j],memo[i-1][j-weight] + value)

print(memo[N][K])