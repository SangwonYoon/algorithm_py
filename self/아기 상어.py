#16236번

import sys
input = sys.stdin.readline
from collections import deque

dx, dy = [0,-1,1,0], [-1,0,0,1]

def bfs():
    global q
    new_q = deque([])
    eatable = list()
    while len(q) > 0:
        y, x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if matrix[ny][nx] == shark_size or matrix[ny][nx] == 0:
                    new_q.append([ny,nx])
                elif matrix[ny][nx] < shark_size:
                    print([ny,nx])
                    eatable.append([ny,nx])
    if len(eatable) > 0:
        eatable.sort(key= lambda x : x[1])
        eatable.sort(key= lambda x : x[0])
        ny, nx = eatable[0]
        matrix[ny][nx] = 0
        q = deque([[ny,nx]])
        return True
    else:
        q = new_q
        return False

N = int(input())
matrix = [list(map(int,input().split())) for i in range(N)]
shark_size = 2
eat = 0
answer = 0

q = deque([])
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            q.append([i,j])
            matrix[i][j] = 0

time = 0
visited = [[0 for i in range(N)] for j in range(N)]

while len(q) > 0:
    if bfs():
        answer += time + 1
        time = 0
        visited = [[0 for i in range(N)] for j in range(N)]
        eat += 1
        if eat == shark_size:
            shark_size += 1
            eat = 0
    else:
        time += 1

print(answer)