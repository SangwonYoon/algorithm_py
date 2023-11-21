#14499번

import sys
input = sys.stdin.readline

def roll(position, command):
    if command == 1:
        return [position[2], position[1], position[5], position[3], position[0], position[4]]
    elif command == 2:
        return [position[4], position[1], position[0], position[3], position[5], position[2]]
    elif command == 3:
        return [position[3], position[0], position[2], position[5], position[4], position[1]]
    elif command == 4:
        return [position[1], position[5], position[2], position[0], position[4], position[3]]

delta = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]

N, M, x, y, K = map(int, input().split())
area = []
dice = [0] * 7
position = [1, 2, 4, 5, 3, 6]

for _ in range(N):
    area.append(list(map(int, input().split())))

commands = list(map(int, input().split()))
for command in commands:
    dx, dy = x + delta[command][0], y + delta[command][1]
    if dx >= 0 and dx < N and dy >= 0 and dy < M:
        x, y = dx, dy
        position = roll(position, command)
        if area[dx][dy] == 0:
            area[dx][dy] = dice[position[5]]
        else:
            dice[position[5]] = area[dx][dy]
            area[dx][dy] = 0
        
        print(dice[position[0]])
