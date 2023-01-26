# 15686번

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
home = []
chicken = []


for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            home.append([i, j])
        elif temp[j] == 2:
            chicken.append([i, j])

answer = 1000000

for c in combinations(chicken, M):
    chicken_distance = 0
    for h in home:
        min_distance = 1000000
        for store in c:
            temp = abs(h[0] - store[0]) + abs(h[1] - store[1])
            if temp < min_distance:
                min_distance = temp
        chicken_distance += min_distance
    if answer > chicken_distance:
        answer = chicken_distance

print(answer)
