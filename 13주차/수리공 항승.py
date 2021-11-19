#1449번

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

points = list(map(int,input().split()))
points.sort()
points = deque(points)

cnt = 0
taped = 0
while len(points) > 0:
    temp = points.popleft()
    if temp > taped:
        taped = temp - 0.5 + L
        cnt += 1

print(cnt)