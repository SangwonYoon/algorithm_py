# 17779번

import sys

input = sys.stdin.readline

def calculate(x, y, d1, d2):
    global grid, total
    election = [0] * 5

    col1 = y+1
    for r in range(x+d1):
        if r >= x:
            col1 -= 1
        election[0] += sum(grid[r][:col1])

    col2 = y+1
    for r in range(x+d2+1):
        if r > x:
            col2 += 1
        election[1] += sum(grid[r][col2:])

    col3 = y-d1
    for r in range(x+d1, N):
        election[2] += sum(grid[r][:col3])
        if r < x+d1+d2:
            col3 += 1

    col4 = y+d2
    for r in range(x+d2+1, N):
        election[3] += sum(grid[r][col4:])
        if r <= x+d1+d2:
            col4 -= 1

    election[4] = total - sum(election)

    return max(election) - min(election)


N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

total = sum([sum(g) for g in grid])
answer = 40000

for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, y+1):
            for d2 in range(1, N-y-1):
                if x+d1+d2 >= N:
                    continue

                diff = calculate(x, y, d1, d2)
                answer = min(diff, answer)

print(answer)
