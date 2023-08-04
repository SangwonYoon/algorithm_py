# 3020번

import sys
import bisect
input = sys.stdin.readline

N, H = map(int, input().split())
N = N//2

up = []
down = []

for _ in range(N):
    down.append(int(input()))
    up.append(int(input()))

up.sort()
down.sort()

result = []

for k in range(1, H+1):
    d = bisect.bisect_left(down, k)
    u = bisect.bisect_left(up, H-k+1)
    result.append(2 * N - d - u)

result.sort(reverse=True)
print(result[-1], H - result.index(result[-1]))