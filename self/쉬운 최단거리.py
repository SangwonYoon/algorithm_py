# 14940번

import sys
input = sys.stdin.readline

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

n, m = map(int, input().split())
map_input = [list(map(int, input().split())) for _ in range(n)]

queue = []
map_output = []
for i in range(n):
    temp = []
    for j in range(m):
        if map_input[i][j] == 2:
            queue.append((i, j))
            temp.append(0)
        else:
            temp.append(map_input[i][j] * (-1))
    map_output.append(temp)

while queue:
    y, x = queue.pop(0)
    for dy, dx in direction:
        new_y, new_x = y+dy, x+dx
        if new_y >= 0 and new_y < n and new_x >= 0 and new_x < m and map_output[new_y][new_x] == -1:
            map_output[new_y][new_x] = map_output[y][x] + 1
            queue.append((new_y, new_x))

for i in range(n):
    for j in range(m):
        print(map_output[i][j], end = " ")
    print()