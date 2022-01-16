#1916번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dijkstra(idx):
    visited.append(idx)

    for i in range(len(route[idx])):
        node[route[idx][i][0]] = min(node[route[idx][i][0]], node[idx] + route[idx][i][1])

    temp = node[:]
    for i in visited:
        temp[i] = float("inf")

    target = temp.index(min(temp))
    if target == e:
        print(node[target])
    else:
        dijkstra(target)

N = int(input())
M = int(input())

route = [[] for i in range(N+1)]

for i in range(M):
    a, b, cost = map(int,input().split())
    route[a].append([b, cost])

s, e = map(int,input().split())

visited = []

node = [float("inf") for i in range(N+1)] #s번 노드부터 각 노드까지의 최소 비용을 저장하는 리스트
node[s] = 0
dijkstra(s)