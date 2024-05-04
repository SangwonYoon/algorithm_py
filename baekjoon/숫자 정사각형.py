# 1051번

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []

for _ in range(N):
    row = list(map(int, list(input().rstrip())))
    matrix.append(row)

size = min([N, M])

while size >= 1:
    for i in range(N-size+1):
        for j in range(M-size+1):
            if matrix[i][j] == matrix[i+size-1][j] == matrix[i][j+size-1] == matrix[i+size-1][j+size-1]:
                print(size**2)
                sys.exit(0)

    size -= 1