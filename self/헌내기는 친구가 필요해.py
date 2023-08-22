# 21736번

import sys
from collections import deque

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([])
map_info = []
for n in range(N):
    temp = list(input())
    if "I" in temp:
        queue.append([n, temp.index("I")])
    map_info.append(temp)

cnt = 0 
while queue:
    x, y = queue.popleft()
    for i in direction:
        dx, dy = x+i[0], y+i[1]
        if dx >= 0 and dx < N and dy >= 0 and dy < M:
            if map_info[dx][dy] == "O":
                queue.append([dx, dy])
                map_info[dx][dy] = "X"
            elif map_info[dx][dy] == "P":
                cnt += 1
                queue.append([dx, dy])
                map_info[dx][dy] = "X"

if cnt == 0:
    print("TT")
else:
    print(cnt)