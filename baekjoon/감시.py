# 15683번

import sys

input = sys.stdin.readline

def observe():
    global matrix, cctv_direction, cctv, answer
    blind = [[1] * M for _ in range(N)]
    for i, (row, col, type) in enumerate(cctv):
        for dir_x, dir_y in direction[type][cctv_direction[i]]:
            k = 0
            while True:
                dx, dy = dir_x * k, dir_y * k
                if 0 <= row+dy < N and 0 <= col+dx < M and matrix[row+dy][col+dx] != 6:
                    blind[row+dy][col+dx] = 0
                    k += 1
                else:
                    break
    blind_spot = sum([sum(b) for b in blind]) - sum([m.count(6) for m in matrix])
    answer = min(answer, blind_spot)

def rotate():
    global cctv_direction, cctv
    if len(cctv_direction) == len(cctv):
        observe()
    else:
        for i in range(len(direction[cctv[len(cctv_direction)][2]])):
            cctv_direction.append(i)
            rotate()
            cctv_direction.pop()
        

cctv_1_direction = [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]]
cctv_2_direction = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
cctv_3_direction = [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]]
cctv_4_direction = [[(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)]]
cctv_5_direction = [[(0, 1), (1, 0), (0, -1), (-1, 0)]]
direction = [cctv_1_direction, cctv_2_direction, cctv_3_direction, cctv_4_direction, cctv_5_direction]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= matrix[i][j] <= 5:
            cctv.append((i, j, matrix[i][j]-1)) # (row, col, cctv_type)

cctv_direction = []
answer = 64

rotate()
print(answer)