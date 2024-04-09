# 17140번

import sys

input = sys.stdin.readline

def operation():
    global matrix
    max_len = -1
    for i in range(len(matrix)):
        rows = []
        for num in set(matrix[i]):
            if num == 0:
                continue
            rows.append((num, matrix[i].count(num)))
        rows.sort(key = lambda x : x[0])
        rows.sort(key = lambda x : x[1])
        matrix[i] = []
        for row in rows:
            matrix[i] += row
        if len(matrix[i]) > max_len:
            max_len = len(matrix[i])

    for i in range(len(matrix)):
        diff = max_len - len(matrix[i])
        matrix[i] += [0] * diff

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

turn = 0

while len(matrix) < r or len(matrix[0]) < c or matrix[r-1][c-1] != k:
    if turn >= 100:
        break
    turn += 1

    if len(matrix) >= len(matrix[0]): # R operation
        operation()

    else: # C operation
        matrix = list(zip(*matrix))
        operation()
        matrix = list(zip(*matrix))
else:
    print(turn)
    sys.exit(0)

print(-1)