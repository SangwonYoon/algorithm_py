# 14503번

import sys
input = sys.stdin.readline

answer = 0
rotation = [[0, -1], [-1, 0], [0, 1], [1, 0]]
reverse = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def clean_up(cell, x, y, d):
    global answer, rotation, reverse
    cell[x][y] = -1 # clean up
    answer += 1
    d_mem = d

    while True:
        dx = x + rotation[d][0]
        dy = y + rotation[d][1]
        if cell[dx][dy] == 0: # 왼쪽 방향에 청소하지 않은 공간 존재
            d = (d-1) % 4
            clean_up(cell, dx, dy, d)
            break
        else:
            d = (d-1) % 4
            if d_mem == d:
                dx = x + reverse[d][0]
                dy = y + reverse[d][1]
                if cell[dx][dy] == 1:
                    break
                else: # 후진
                    x = dx
                    y = dy

N, M = map(int, input().split())
r, c, d = map(int, input().split())
cell = []
for _ in range(N):
    cell.append(list(map(int, input().split())))

clean_up(cell, r, c, d)
print(answer)