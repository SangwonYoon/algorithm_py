# 2206번

from collections import deque
import sys
input = sys.stdin.readline

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
if N == 1 and M == 1:
    print(1)
    sys.exit(0)

maze = []

for _ in range(N):
    maze.append(list(map(int, list(input().rstrip()))))

visited_1 = [[0] * M for _ in range(N)]
visited_0 = [[0] * M for _ in range(N)]

queue = deque([[0, 0, 1]])
visited_1[0][0] = 1

while queue:
    i, j, life = queue.popleft()
    if life == 1:
        cnt = visited_1[i][j]
    else:
        cnt = visited_0[i][j]

    for k in range(4):
        di, dj = i+delta[k][0], j+delta[k][1]
        if di >= 0 and di < N and dj >= 0 and dj < M:
            if di == N-1 and dj == M-1:
                print(cnt+1)
                sys.exit(0)
            if life == 1:
                if maze[di][dj] == 0 and visited_1[di][dj] == 0:
                    queue.append([di, dj, 1])
                    visited_1[di][dj] = cnt+1
                elif maze[di][dj] == 1 and visited_0[di][dj] == 0:
                    queue.append([di, dj, 0])
                    visited_0[di][dj] = cnt+1
            else:
                if maze[di][dj] == 0 and visited_1[di][dj] == 0 and visited_0[di][dj] == 0:
                    queue.append([di, dj, 0])
                    visited_0[di][dj] = cnt+1

print(-1)