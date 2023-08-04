# 1516번

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
cost = [0]
graph = {}
in_degree = [0]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    cost.append(temp[0])
    in_degree.append(len(temp) - 2)
    for j in range(1, len(temp)-1):
        if temp[j] not in graph:
            graph[temp[j]] = [i]
        else:
            graph[temp[j]].append(i)

q = []
result = [-1] * (N+1)

for i in range(1, N+1):
    if in_degree[i] == 0:
        result[i] = cost[i]
        heappush(q, (result[i], i))

while q:
    target = heappop(q)[1]
    if target in graph:
        neighbor = graph[target]
        for i in range(len(neighbor)):
            in_degree[neighbor[i]] -= 1
            if in_degree[neighbor[i]] == 0:
                result[neighbor[i]] = result[target] + cost[neighbor[i]]
                heappush(q, (result[neighbor[i]], neighbor[i]))

for i in range(1, N+1):
    print(result[i])