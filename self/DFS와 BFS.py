# 1260번

import sys
from collections import deque

input = sys.stdin.readline

def BFS(graph, start):
    visited = [0] * (N+1)

    queue = deque([])
    queue.append(start)
    visited[start] = 1

    while queue:
        temp = queue.popleft()
        print(temp, end = " ")
        for i in range(len(graph[temp])):
            if not visited[graph[temp][i]]:
                queue.append(graph[temp][i])
                visited[graph[temp][i]] = 1


def DFS(graph, visited, node):
    visited[node] = 1
    print(node, end = " ")
    for i in range(len(graph[node])):
        if not visited[graph[node][i]]:
            DFS(graph, visited, graph[node][i])


N, M, V = map(int, input().split())
graph = [set() for _ in range(1001)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

graph = list(map(sorted, list(map(list, graph))))
visited = [0] * (N+1)
DFS(graph, visited, V)
print()
BFS(graph, V)