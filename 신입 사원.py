# 1946번

import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    rank = list()
    for j in range(N):
        rank.append(list(map(int,input().split())))
    rank.sort(key = lambda x : x[0])
    answer = 1
    highest = rank[0][1]
    for j in range(1,N):
        if highest > rank[j][1]:
            highest = rank[j][1]
            answer += 1
    print(answer)