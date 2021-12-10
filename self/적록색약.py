#10026번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx, dy = [-1,1,0,0], [0,0,-1,1]

def search(x, y):
    visited[y][x] = cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and paint[y][x] == paint[ny][nx] and visited[ny][nx] == 0:
            search(nx,ny)

def search_weakness(x,y):
    visited[y][x] = cnt_weakness
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
            if (paint[y][x] == 'B' and paint[ny][nx] == 'B') or ((paint[y][x] == 'R' or paint[y][x] == 'G') and (paint[ny][nx] == 'R' or paint[ny][nx] == 'G')):
                search_weakness(nx,ny)

N = int(input())
paint = [[i for i in input().rstrip()] for j in range(N)]

visited = [[0 for i in range(N)] for j in range(N)]
cnt = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            search(j,i)
            cnt += 1

visited = [[0 for i in range(N)] for j in range(N)]
cnt_weakness = 1

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            search_weakness(j,i)
            cnt_weakness += 1

print(cnt - 1, cnt_weakness - 1)
