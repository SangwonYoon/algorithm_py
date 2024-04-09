# 20055번

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
durability = list(map(int, input().split()))
robots = [0] * (N*2)
belt = deque(map(list, zip(robots, durability)))

turn = 0
broken = 0

while broken < K: # phase 4
    turn += 1

    # phase 1
    belt.rotate(1)
    belt[N-1][0] = 0 # 로봇 내림

    # phase 2
    for i in range(N-2, -1, -1):
        if belt[i][0] == 1 and belt[i+1][0] == 0 and belt[i+1][1] > 0:
            belt[i][0] = 0
            belt[i+1][0] = 1
            belt[i+1][1] -= 1
            if belt[i+1][1] == 0:
                broken += 1
    
    belt[N-1][0] = 0 # 로봇 내림

    # phase 3
    if belt[0][1] > 0:
        belt[0][0] = 1
        belt[0][1] -= 1
        if belt[0][1] == 0:
            broken += 1

print(turn)
