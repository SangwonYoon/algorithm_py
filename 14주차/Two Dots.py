#16929번

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dots = [[j for j in input().rstrip()] for i in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]

dx, dy = [-1,1,0,0], [0,0,-1,1]
n = 1

def isCycle(x,y):
    cnt = 0
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == n:
            cnt += 1
    if cnt >= 2:
        print('Yes')
        return True
    return False

def search(x,y):
    if isCycle(x,y):
        sys.exit()
    visited[y][x] = n
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and dots[y][x] == dots[ny][nx] and visited[ny][nx] == 0:
            search(nx,ny)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            search(j,i)
            n += 1

print('No')