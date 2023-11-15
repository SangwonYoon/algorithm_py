# 2636번

import sys
from collections import deque
input = sys.stdin.readline

def diffusion(cheese):
    num = cheese[0][0] - 1
    cheese[0][0] = num
    queue = deque([[0, 0]])
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            new_y, new_x = y+delta[i][0], x+delta[i][1]
            if new_y >= 0 and new_y < row and new_x >= 0 and new_x < column:
                if cheese[new_y][new_x] == num+1 or cheese[new_y][new_x] == 0:
                    queue.append([new_y, new_x])
                    cheese[new_y][new_x] = num

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

row, column = map(int, input().split())

cheese = list()

for _ in range(row):
    cheese.append(list(map(int, input().split())))

time = 0
finish_flag = False

while not finish_flag:
    time += 1
    cnt = 0
    finish_flag = True

    diffusion(cheese)

    for i in range(row):
        for j in range(column):
            if cheese[i][j] == 1:
                for k in range(4):
                    new_i, new_j = i+delta[k][0], j+delta[k][1]
                    if new_i >= 0 and new_i < row and new_j >= 0 and new_j < column:
                        if cheese[new_i][new_j] < 0:
                            cnt += 1
                            cheese[i][j] = 0
                            break
                else:
                    finish_flag = False

print(time)
print(cnt)