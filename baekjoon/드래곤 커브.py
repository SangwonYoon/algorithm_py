# 15685번

import sys

input = sys.stdin.readline

direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]

N = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    way = [d]

    for _ in range(g):
        temp_way = []
        for w in way[::-1]:
            temp_way.append((w+1) % 4)
        way += temp_way

    grid[y][x] = 1
    pos = [x, y]
    for w in way:
        pos[0] += direction[w][0]
        pos[1] += direction[w][1]
        grid[pos[1]][pos[0]] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
            answer += 1

print(answer)
