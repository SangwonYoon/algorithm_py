# 11660번
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cell = []
for i in range(N):
    temp = list(map(int, input().split()))
    cell.append(temp)

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            cell[i][j] += cell[i][j-1]
        elif j == 0:
            cell[i][j] += cell[i-1][j]
        else:
            cell[i][j] += cell[i-1][j] + cell[i][j-1] - cell[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        answer = cell[x2-1][y2-1]
    elif x1 == 1:
        answer = cell[x2-1][y2-1] - cell[x2-1][y1-2]
    elif y1 == 1:
        answer = cell[x2-1][y2-1] - cell[x1-2][y2-1]
    else:
        answer = cell[x2-1][y2-1] - cell[x2-1][y1-2] - cell[x1-2][y2-1] + cell[x1-2][y1-2]

    print(answer)