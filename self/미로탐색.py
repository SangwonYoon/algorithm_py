#2178번

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
maze = [[int(i) for i in input().rstrip()] for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
visited[0][0] = 1
q = deque([[0,0]])
dx, dy = [-1,1,0,0], [0,0,-1,1]

while(True):
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1 and visited[ny][nx] == 0:
            q.append([nx,ny])
            visited[ny][nx] = visited[y][x] + 1
            if nx == M-1 and ny == N-1:
                print(visited[ny][nx])
                sys.exit()