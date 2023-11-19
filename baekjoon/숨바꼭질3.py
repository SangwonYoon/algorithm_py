# 13549번

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([])
visited = [-1] * 100001

queue.append(N)
visited[N] = 0

while queue:
    pos = queue.popleft()
    if pos == K:
        print(visited[pos])
        break
    if pos < K and pos*2 <= 100000 and visited[pos*2] == -1:
        queue.appendleft(pos*2)
        visited[pos*2] = visited[pos]
    if pos-1 >= 0 and visited[pos-1] == -1:
        queue.append(pos-1)
        visited[pos-1] = visited[pos] + 1
    if pos+1 <= 100000 and visited[pos+1] == -1:
        queue.append(pos+1)
        visited[pos+1] = visited[pos] + 1