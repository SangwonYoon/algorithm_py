import sys
input = sys.stdin.readline
from collections import deque

def check(arr):
    for i in range(len(arr)):
        if 0 in arr[i]:
            return False # 다 안익음
    return True # 다 익음

def day_after():
    x, y = -1, -1
    while position:
        x, y = position.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                position.append([nx,ny])
    return x, y

M, N = map(int, input().split())
tomato = [list(map(int,input().split())) for i in range(N)]
position = deque([])
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            position.append([j,i])

dx, dy = [-1,1,0,0], [0,0,-1,1]

x, y = day_after()

if check(tomato):
    print(tomato[y][x] - 1)
else:
    print(-1)