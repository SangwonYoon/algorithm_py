# 1719번

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[-1] * (n+1) for _ in range(n+1)]
result = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a][b] = dist
    graph[b][a] = dist

for i in range(1, n+1):
    temp_result = [[-1, -1]] * (n+1)
    for seq in range(n):
        if seq == 0:
            target = i
            min_dist = 0
        else:
            min_dist = 1000001
            for j in range(1, n+1):
                if temp_result[j][0] > 0 and temp_result[j][0] < min_dist:
                    min_dist = temp_result[j][0]
                    target = j
            temp_result[target][0] *= -1

        for node in range(1, n+1):
            if graph[target][node] > 0:
                if temp_result[node][1] == -1 or (temp_result[node][0] > 0 and graph[target][node] + min_dist < temp_result[node][0]):  # noqa: E501
                    temp_result[node] = [graph[target][node] + min_dist, target]  # noqa: E501

    for j in range(1, n+1):
        if j != i:
            result[j][i] = temp_result[j][1]
        else:
            result[j][i] = "-"

for i in range(1, n+1):
    for j in range(1, n+1):
        print(result[i][j], end=" ")
    print()
