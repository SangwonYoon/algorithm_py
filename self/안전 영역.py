#2468번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
height = [list(map(int,input().split())) for i in range(N)]
safe_area = [1]

dx, dy = [-1,1,0,0], [0,0,-1,1]

def search(x,y):
    visited[y][x] = n
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and height[ny][nx] > water and not visited[ny][nx]:
            search(nx,ny)

M = max(max(height))
for water in range(1,M):
    n = 1
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if height[i][j] > water and not visited[i][j]:
                search(j,i)
                n += 1
    safe_area.append(n-1)

print(max(safe_area))