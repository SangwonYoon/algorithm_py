# 17144번

import sys
input = sys.stdin.readline

movement = [[1,0], [0,1], [-1,0], [0,-1]]

def spread(cell):
    R = len(cell)
    C = len(cell[0])
    new_cell = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if cell[i][j] > 0:
                cnt = 0
                for k in range(4):
                    di = i + movement[k][0]
                    dj = j + movement[k][1]
                    if di >= 0 and di < R and dj >= 0 and dj < C and cell[di][dj] != -1:
                        new_cell[di][dj] += cell[i][j] // 5
                        cnt += 1
                new_cell[i][j] -= (cell[i][j] // 5) * cnt

    for i in range(R):
        for j in range(C):
            cell[i][j] += new_cell[i][j]

def air_movement(cell, air_cleaner):
    R = len(cell)
    C = len(cell[0])

    u = air_cleaner[0]
    d = air_cleaner[1]

    for i in range(u-1, 0, -1):
        cell[i][0] = cell[i-1][0]

    for j in range(d+1, R-1):
        cell[j][0] = cell[j+1][0]

    for i in range(C-1):
        cell[0][i] = cell[0][i+1]
        cell[R-1][i] = cell[R-1][i+1]

    for i in range(u):
        cell[i][C-1] = cell[i+1][C-1]

    for j in range(R-1, d, -1):
        cell[j][C-1] = cell[j-1][C-1]

    for i in range(C-2, 0, -1):
        cell[u][i+1] = cell[u][i]
        cell[d][i+1] = cell[d][i]

    cell[u][1] = 0
    cell[d][1] = 0

R, C, T = map(int, input().split())
cell = [list(map(int, input().split())) for _ in range(R)]

air_cleaner = []

for i in range(R):
    if cell[i][0] == -1:
        air_cleaner.append(i)
        air_cleaner.append(i+1)
        break

for i in range(T):
    spread(cell)
    air_movement(cell, air_cleaner)
    print(cell)

total = 2
for i in range(len(cell)):
    total += sum(cell[i])

print(total)