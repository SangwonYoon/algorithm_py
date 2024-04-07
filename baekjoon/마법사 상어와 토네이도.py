# 20057번

import sys

input = sys.stdin.readline

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
tornado_right = [[0, -2, 0.02], [1, -1, 0.1], [0, -1, 0.07], [-1, -1, 0.01], [2, 0, 0.05], [1, 1, 0.1], [0, 1, 0.07], [-1, 1, 0.01], [0, 2, 0.02]]
tornado_down = [[y, x, perc] for x, y, perc in tornado_right]
tornado_left = [[-x, -y, perc] for x, y, perc in tornado_right]
tornado_up = [[-y, -x, perc] for x, y, perc in tornado_right]

N = int(input())
sand = [[0] * (N+4) for _ in range(2)]
pos = [N//2 + 2, N//2 + 2] # [x, y]

for _ in range(N):
    temp_sand = [0, 0]
    temp_sand += list(map(int, input().split()))
    temp_sand += [0, 0]
    sand.append(temp_sand)

sand += [[0] * (N+4) for _ in range(2)]

distance = 0.5

while pos[0] != 2 or pos[1] != 2:
    distance += 0.5

    if int(distance) % 2 == 1 and int(distance) == distance:
        d = direction[0]
        tornado = tornado_left
    elif int(distance) % 2 == 1 and int(distance) != distance:
        d = direction[1]
        tornado = tornado_down
    elif int(distance) % 2 == 0 and int(distance) == distance:
        d = direction[2]
        tornado = tornado_right
    else:
        d = direction[3]
        tornado = tornado_up

    for _ in range(int(distance)):
        pos[0] += d[0]
        pos[1] += d[1]
        
        amount = sand[pos[1]][pos[0]]

        for dx, dy, perc in tornado:
            moving_sand = int(sand[pos[1]][pos[0]] * perc)
            amount -= moving_sand

            sand[pos[1] + dy][pos[0] + dx] += moving_sand

        sand[pos[1] + d[1]][pos[0] + d[0]] += amount
        sand[pos[1]][pos[0]] = 0

        if pos[0] == 2 and pos[1] == 2:
            break

result = 0

for i in range(N+4):
    for j in range(N+4):
        if i < 2 or i > N+1 or j < 2 or j > N+1:
            result += sand[i][j]

print(result)
