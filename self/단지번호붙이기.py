#2667번

import sys
input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

def search(x, y):
    global cnt
    visited[y][x] = num
    cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and map[ny][nx] == 1 and visited[ny][nx] == 0:
            search(nx, ny)

N = int(input())
map = [[int(i) for i in input().rstrip()] for j in range(N)]

visited = [[0 for i in range(N)] for j in range(N)]
num = 1
complex = []
cnt = 0

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            search(j, i)
            complex.append(cnt)
            num += 1

complex.sort()
print(num-1)
for i in range(len(complex)):
    print(complex[i])