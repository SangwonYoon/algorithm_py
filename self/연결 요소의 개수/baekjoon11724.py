#11724번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def travel(i,cnt):
    if points[i] != cnt:
        points[i] = cnt
    else:
        return
    for j in range(len(graph[i])):
        travel(graph[i][j],cnt)

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
points = [0 for i in range(N+1)]
cnt = 1

for i in range(1,N+1):
    if points[i] == 0:
        travel(i,cnt)
        cnt += 1

print(cnt-1)