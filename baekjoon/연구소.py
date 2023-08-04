# 14502번
import sys
input = sys.stdin.readline
import copy

answer = 0
movement = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def spread(cell, x, y):
    N = len(cell)
    M = len(cell[0])
    for i in range(4):
        dx, dy = x + movement[i][0], y + movement[i][1]
        if dx >= 0 and dx < N and dy >= 0 and dy < M and cell[dx][dy] == 0:
            cell[dx][dy] = 2
            spread(cell, dx, dy)

def wall(cell, cnt, x, y, virus):
    global answer
    N = len(cell)
    M = len(cell[0])
    for i in range(x, N):
        for j in range(M):
            #print(cnt, j)
            if cell[i][j] == 0:
                cell[i][j] = 1
                if cnt == 1:
                    cell_cp = copy.deepcopy(cell)
                    for v in virus:
                        vx, vy = v
                        spread(cell, vx, vy)
                    safe = cnt_safe(cell)
                    if answer < safe:
                        answer = safe
                    cell = cell_cp
                else:
                    cell_cp = copy.deepcopy(cell)
                    wall(cell, cnt-1, i, j, virus)
                    cell = cell_cp
                cell[i][j] = 0

def cnt_safe(cell):
    N = len(cell)
    total = 0
    for i in range(N):
        total += cell[i].count(0)
    return total

N, M = map(int, input().split())

cell = []
virus = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 2:
            virus.append([i, j])
    cell.append(temp)

wall(cell, 3, 0, 0, virus)
print(answer)

