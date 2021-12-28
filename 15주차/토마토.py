#7569번

import sys
input = sys.stdin.readline
from collections import deque

def search():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return False #토마토가 다 익지 않았음
    return True #토마토가 다 익었음

def day_after():
    global q
    new_q = deque([])
    while len(q) > 0:
        h, y, x = q.popleft()
        for i in range(6):
            nx, ny, nh = x + dx[i], y + dy[i], h + dh[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nh < H and tomato[nh][ny][nx] == 0:
                new_q.append([nh,ny,nx])
                tomato[nh][ny][nx] = day
    q = new_q

M, N, H = map(int,input().split())
tomato = [[list(map(int,input().split())) for i in range(N)] for j in range(H)]

dx, dy, dh = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
day = 1
q = deque([])
for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    q.append([i,j,k])

while len(q) > 0:
    if search():
        print(day-1)
        break
    day += 1
    day_after()

if not search():
    print(-1)