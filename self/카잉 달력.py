#6064번

import sys
input = sys.stdin.readline

for i in range(int(input())):
    M, N, x, y = map(int, input().split())
    base = M
    year = x
    while year <= M * N:
        if y == N:
            y = 0
        if year % N == y:
            print(year)
            break
        else:
            year += M
    else:
        print(-1)