#3190번

import math
import sys
from collections import deque

input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # (dy, dx)

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]  # 0 빈공간, 1 뱀, 2 사과
board[0][0] = 1
apples = []

for _ in range(K):
    apple_y, apple_x = map(int, input().split())
    apples.append((apple_y, apple_x))
    board[apple_y-1][apple_x-1] = 2

L = int(input())

movements = deque([])

for _ in range(L):
    time, turn = input().split()
    movements.append((int(time), turn))

temp_direction_idx = 0
temp_time = 0
temp_pos = [0, 0]
snake_pos = deque([[0, 0]])

while True:
    die_flag = False
    if movements:
        time, turn = movements.popleft()
    else:
        time = math.inf
    dy, dx = directions[temp_direction_idx]
    while temp_time < time:
        temp_time += 1
        temp_y, temp_x = snake_pos[0]
        new_y, new_x = temp_y+dy, temp_x+dx

        if not (0 <= new_y < N and 0 <= new_x < N) or board[new_y][new_x] == 1:
            die_flag = True
            break
        elif board[new_y][new_x] == 2:
            board[new_y][new_x] = 1
            snake_pos.appendleft([new_y, new_x])
        else:
            board[new_y][new_x] = 1
            snake_pos.appendleft([new_y, new_x])
            tail_y, tail_x = snake_pos.pop()
            board[tail_y][tail_x] = 0

    if die_flag:
        break

    if turn == "L":
        temp_direction_idx = (temp_direction_idx - 1) % 4
    else:
        temp_direction_idx = (temp_direction_idx + 1) % 4

print(temp_time)