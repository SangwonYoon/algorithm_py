#2638번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())
matrix = []

dx, dy = [-1,1,0,0], [0,0,-1,1]

def outside(y,x):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 0:
            matrix[ny][nx] = -1
            outside(ny,nx)

def checkoutside():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == -1:
                outside(y,x)

def melt():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if matrix[ny][nx] == -1:
                        cnt += 1
                        if cnt >= 2:
                            matrix[y][x] = 0
                            break

def search():
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                return True
    return False

for i in range(N):
    if i == 0 or i == N-1:
        input()
        matrix.append([-1 for _ in range(M)])
    else:
        temp = list(map(int,input().split()))
        temp[0] = -1
        temp[-1] = -1
        matrix.append(temp)

answer = 0
while search():
    checkoutside()
    melt()
    answer += 1

print(answer)