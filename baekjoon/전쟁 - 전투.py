# 1303번

import sys

mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(id, army, board, y, x):
    global cnt
    for dx, dy in mv:
        new_x = x + dx
        new_y = y + dy
        if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M:
            if board[new_y][new_x] == 0 and army[new_y][new_x] == id:
                board[new_y][new_x] = 1
                cnt += 1
                dfs(id, army, board, new_y, new_x)


input = sys.stdin.readline

N, M = map(int, input().split())

army = []
board = []
for _ in range(M):
    temp = list(input())
    army.append(temp)
    board.append([0] * N)

w = 0
b = 0

for i in range(N):
    for j in range(M):
        if board[j][i] == 0:
            board[j][i] = 1
            cnt = 1
            dfs(army[j][i], army, board, j, i)
            if army[j][i] == "W":
                w += cnt**2
            else:
                b += cnt**2

print(f"{w} {b}")
