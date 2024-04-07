# 20057번

import sys

input = sys.stdin.readline

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
tornado = [[0, -2, 0.02], [1, -1, 0.1], [0, -1, 0.07], [-1, -1, 0.01], [2, 0, 0.05], [1, 1, 0.1], [0, 1, 0.07], [-1, 1, 0.01], [0, 2, 0.02]]

N = int(input())
sand = [[0] * (N+4) for _ in range(2)]
pos = [N//2 + 2, N//2 + 2] # [x, y]

for _ in range(N):
    temp_sand = [0, 0]
    temp_sand += list(map(int, input().split()))
    temp_sand += [0, 0]
    sand.append(temp_sand)

sand += [[0] * (N+4) for _ in range(2)]

offset = 0.5

while pos[0] != 2 or pos[1] != 2:
    offset += 0.5

    if int(offset) % 2 == 1 and int(offset) == offset:
        d = direction[0]
    elif int(offset) % 2 == 1 and int(offset) != offset:
        d = direction[1]
    elif int(offset) % 2 == 0 and int(offset) == offset:
        d = direction[2]
    else:
        d = direction[3]

    for _ in range(int(offset)):
        pos[0] += d[0]
        pos[1] += d[1]
        # print(f"{pos=}")
        
        amount = sand[pos[1]][pos[0]]

        for t in tornado:
            if d[0] == 0:
                dy, dx, perc = t
            else:
                dx, dy, perc = t
            
            if sum(d) == -1:
                dy *= -1
                dx *= -1

            moving_sand = int(sand[pos[1]][pos[0]] * perc)
            amount -= moving_sand

            sand[pos[1] + dy][pos[0] + dx] += moving_sand

        sand[pos[1] + d[1]][pos[0] + d[0]] += amount
        sand[pos[1]][pos[0]] = 0

        if pos[0] == 2 and pos[1] == 2:
            break

    # print()

result = 0

for i in range(N+4):
    for j in range(N+4):
        if i < 2 or i > N+1 or j < 2 or j > N+1:
            result += sand[i][j]

# print(sand)
print(result)
