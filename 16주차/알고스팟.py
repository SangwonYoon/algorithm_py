#1261번

import sys
input = sys.stdin.readline
from collections import deque

dx, dy = [-1,1,0,0], [0,0,-1,1]

N, M = map(int,input().split())
map = [list(int(j) for j in input().rstrip()) for i in range(M)]
visited = [[float("inf") for i in range(N)] for j in range(M)]
visited[0][0] = 0

q = deque([[0,0]])
while q:
    y, x = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[y][x] + map[ny][nx] < visited[ny][nx]:
            q.append([ny,nx])
            visited[ny][nx] = visited[y][x] + map[ny][nx]

print(visited[M-1][N-1])