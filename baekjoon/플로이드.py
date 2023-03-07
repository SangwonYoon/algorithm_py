import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [[100000000 if i != j else 0 for i in range(n)] for j in range(n)] # i번 도시에서 j번 도시로 가는 최소 비용
graph = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] < 0 or c < graph[a-1][b-1]:
        graph[a-1][b-1] = c

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0: # i번 도시에서 j번 도시로 향하는 버스가 존재하는 경우
            cost[i][j] = graph[i][j]

    for _ in range(n-1):
        min = 100000001
        idx = -1
        for j in range(n):
            if cost[i][j] > 0 and cost[i][j] < min:
                min = cost[i][j]
                idx = j

        for j in range(n):
            if cost[i][j] > 0 and graph[idx][j] > 0 and cost[i][j] > min + graph[idx][j]:
                cost[i][j] = min + graph[idx][j]

        cost[i][idx] = -min

for i in range(n):
    for j in range(n):
        print(abs(cost[i][j]), end = " ") if abs(cost[i][j]) != 100000000 else print(0, end = " ")
    print()