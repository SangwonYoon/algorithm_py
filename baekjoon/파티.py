# 1238번

import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[10000000] * N for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s-1][e-1] = w

go = [(0, X-1)] # weight, node
come = [(0, X-1)]

for _ in range(N-1):
    closest_distance = min(list(filter(lambda x : x >= 0, graph[X-1])))
    closest_node = graph[X-1].index(closest_distance)
    go.append((closest_distance, closest_node))
    graph[X-1][closest_node] *= -1
    for i in range(N):
        if i != X-1 and closest_distance + graph[closest_node][i] < graph[X-1][i]:
            graph[X-1][i] = closest_distance + graph[closest_node][i]

to_dest = []
for i in range(N):
    to_dest.append(graph[i][X-1])

for _ in range(N-1):
    closest_distance = min(list(filter(lambda x : x >= 0, to_dest)))
    closest_node = to_dest.index(closest_distance)
    come.append((closest_distance, closest_node))
    to_dest[closest_node] *= -1
    for i in range(N):
        if i != X-1 and closest_distance + graph[i][closest_node] < to_dest[i]:
            to_dest[i] = closest_distance + graph[i][closest_node]

result = []
go.sort(key = lambda x : x[1])
come.sort(key = lambda x : x[1])

for i in range(N):
    result.append(go[i][0] + come[i][0])

print(max(result))