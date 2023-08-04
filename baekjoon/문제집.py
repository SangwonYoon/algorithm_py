# 1766번

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}
in_degree = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    in_degree[e] += 1
    if s not in graph:
        graph[s] = [e]
    else:
        graph[s].append(e)

q = []
result = []

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        heappush(q, i)

while q:
    target = heappop(q)
    result.append(target)
    if target in graph:
        neighbor = graph[target]
        for i in range(len(neighbor)):
            in_degree[neighbor[i]] -= 1
            if in_degree[neighbor[i]] == 0:
                heappush(q, neighbor[i])

for k in result:
    print(k, end=" ")