# 16928

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

ladder = dict()
for _ in range(N+M):
    u, v = map(int, input().split())
    ladder[u] = v

visited = [0] * 101
visited[1] = 1

queue = deque([[1, 0]])

while queue:
    temp, cnt = queue.popleft()
    for i in range(1,7):
        if not visited[temp+i]:
            visited[temp+i] = 1
            if temp+i in ladder.keys():
                new_pos = ladder[temp+i]
                if not visited[new_pos]:
                    if temp + i == 100:
                        print(cnt + 1)
                        queue = []
                        break
                    else:
                        visited[new_pos] = 1
                        queue.append([new_pos, cnt+1])
            else:
                if temp + i == 100:
                    print(cnt+1)
                    queue = []
                    break
                else:
                    queue.append([temp+i, cnt+1])