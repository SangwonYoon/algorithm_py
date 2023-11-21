#4485번

import heapq
from math import inf
import sys
input = sys.stdin.readline

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

case = 1
while True:
    N = int(input())
    if N == 0:
        break

    cave = []

    for _ in range(N):
        cave.append(list(map(int, input().split())))

    distance = [[inf] * N for _ in range(N)]
    distance[0][0] = cave[0][0]

    queue = []
    heapq.heappush(queue, (cave[0][0] + cave[0][1], 0, 1))
    heapq.heappush(queue, (cave[0][0] + cave[1][0], 1, 0))

    while distance[-1][-1] == inf:
        min_dist, min_i, min_j = heapq.heappop(queue)
        if distance[min_i][min_j] != inf:
            continue

        distance[min_i][min_j] = min_dist

        for k in range(4):
            di, dj = min_i + delta[k][0], min_j + delta[k][1]
            if di >= 0 and di < N and dj >= 0 and dj < N:
                heapq.heappush(queue, (min_dist + cave[di][dj], di, dj))

    print(f"Problem {case}: {distance[-1][-1]}")
    case += 1