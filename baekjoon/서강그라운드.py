# 14938번

import sys
input = sys.stdin.readline

def find_near_node(graph, s, m):
    result = [s]
    while True:
        closest_distance = min(list(filter(lambda x : x >= 0, graph[s])))
        if closest_distance > m:
            break
        closest_node = graph[s].index(closest_distance)
        graph[s][closest_node] *= -1
        result.append(closest_node)
        for i in range(len(graph[closest_node])):
            if i != s and graph[s][i] > closest_distance + abs(graph[closest_node][i]):
                graph[s][i] = closest_distance + abs(graph[closest_node][i])

    return result


answer = []

n, m ,r = map(int, input().split())
items = list(map(int, input().split()))

temp = [1000] * n
graph = [temp[:] for _ in range(n)]

for _ in range(r):
    s, e, w = map(int, input().split())
    graph[s-1][e-1] = w
    graph[e-1][s-1] = w

for i in range(n):
    near_node = find_near_node(graph, i, m)
    total = 0
    for node in near_node:
        total += items[node]

    answer.append(total)
print(max(answer))