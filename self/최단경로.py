#1753번

import sys
from math import inf
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

distance = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    distance[u].append((v, w))

result = [inf] * (V+1)
result[start] = 0
heap = []
for i in range(len(distance[start])):
    heapq.heappush(heap, (distance[start][i][1], distance[start][i][0]))

while heap:
    while heap:
        min, idx = heapq.heappop(heap)
        if result[idx] == inf:
            result[idx] = min
            break

    for j in range(len(distance[idx])):
        dest, weight = distance[idx][j]
        if result[dest] == inf:
            heapq.heappush(heap, (min + weight, dest))

for i in range(1, len(result)):
    if result[i] == inf:
        print("INF")
    else:
        print(result[i])