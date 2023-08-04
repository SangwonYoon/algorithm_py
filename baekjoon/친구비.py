# 16562번

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, temp, friends, i):
    if i not in graph:
        return
    neighbor = graph[i]
    for j in range(len(neighbor)):
        if friends[neighbor[j]] == 1:
            friends[neighbor[j]] = -1
            temp.append(costs[neighbor[j]])
            dfs(graph, temp, friends, neighbor[j])


N, M, k = map(int, input().split())
costs = list(map(int, input().split()))
costs.insert(0, 0)

graph = {}

for _ in range(M):
    v, w = map(int, input().split())
    if v not in graph:
        graph[v] = [w]
    else:
        graph[v].append(w)
    if w not in graph:
        graph[w] = [v]
    else:
        graph[w].append(v)

friends = [1 for _ in range(N+1)]
friends[0] = -1
total = 0
while 1 in friends:
    target = friends.index(1)
    friends[target] = -1
    temp = [costs[target]]
    dfs(graph, temp, friends, target)
    total += min(temp)
    if total > k:
        print("Oh no")
        break
else:
    print(total)