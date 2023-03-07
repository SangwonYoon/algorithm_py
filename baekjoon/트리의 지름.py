import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(total, source, graph, cost):
    for i in range(len(graph[source])):
        dest, weight = graph[source][i]
        if cost[dest] == -1:
            cost[dest] = total + weight
            dfs(total + weight, dest, graph, cost)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = (map(int, input().split()))
    graph[p].append((c, w))
    graph[c].append((p, w))

cost = [-1 if i != 1 else 0 for i in range(n+1)]
dfs(0, 1, graph, cost)

farthest = cost.index(max(cost))
cost = [-1 if i != farthest else 0 for i in range(n+1)]
dfs(0, farthest, graph, cost)

print(max(cost))