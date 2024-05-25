# 2563번

import sys

input = sys.stdin.readline

N = int(input());

matrix = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    for row in range(y, y+10):
        for col in range(x, x+10):
            if matrix[row][col] == 0:
                matrix[row][col] = 1
                result += 1

print(result)