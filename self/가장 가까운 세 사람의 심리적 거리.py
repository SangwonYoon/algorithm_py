# 20529번

import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbti = input().split()
    if N >= 33:
        print(0)
    else:
        distance = [[10] * N for _ in range(N)]
        for i in range(N):
            for j in range(i):
                dist = 0
                for idx in range(4):
                    if mbti[i][idx] != mbti[j][idx]:
                        dist += 1
                distance[i][j] = dist
                distance[j][i] = dist

        min = 100
        people = list(range(N))
        for comb in list(combinations(people, 3)):
            a, b, c = comb
            total_distance = distance[a][b] + distance[b][c] + distance[a][c]
            if min > total_distance:
                min = total_distance

        print(min)
