#1167번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(dist, node, tree):
    for i in range(len(tree[node])):
        other, weight = tree[node][i]
        if dist[other] == -1:
            dist[other] = dist[node] + weight
            dfs(dist, other, tree)

V = int(input())

tree = [[] for _ in range(V+1)]

for _ in range(V):
    weights = list(map(int, input().split()))[:-1]
    n = weights.pop(0)
    for i in range(0, len(weights), 2):
        tree[n].append([weights[i], weights[i+1]])

dist = [-1] * (V+1)
dist[1] = 0
dfs(dist, 1, tree)

target = dist.index(max(dist))

dist = [-1] * (V+1)
dist[target] = 0
dfs(dist, target, tree)
print(max(dist))