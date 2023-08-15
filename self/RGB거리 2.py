# 17404번

import sys
from math import inf

input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

total = [
    [inf, cost[0][0] + cost[1][1], cost[0][0] + cost[1][2]],
    [cost[0][1] + cost[1][0], inf, cost[0][1] + cost[1][2]],
    [cost[0][2] + cost[1][0], cost[0][2] + cost[1][1], inf]
]

for i in range(3, N+1):
    R = cost[i-1][0]
    G = cost[i-1][1]
    B = cost[i-1][2]
    new_total = [[0] * 3 for _ in range(3)] 
    new_total[0][0] = min(total[0][1] + R, total[0][2] + R)
    new_total[0][1] = min(total[0][0] + G, total[0][2] + G)
    new_total[0][2] = min(total[0][0] + B, total[0][1] + B)
    new_total[1][0] = min(total[1][1] + R, total[1][2] + R)
    new_total[1][1] = min(total[1][0] + G, total[1][2] + G)
    new_total[1][2] = min(total[1][0] + B, total[1][1] + B)
    new_total[2][0] = min(total[2][1] + R, total[2][2] + R)
    new_total[2][1] = min(total[2][0] + G, total[2][2] + G)
    new_total[2][2] = min(total[2][0] + B, total[2][1] + B)
    total = new_total

print(min(total[0][1], total[0][2], total[1][0], total[1][2], total[2][0], total[2][1]))