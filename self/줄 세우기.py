# 2252번

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
shorter_than_me = [0] * (N+1)
queue = deque([])
taller_than_me = {}

for _ in range(M):
    A, B = map(int, input().split())
    shorter_than_me[B] += 1
    if A in taller_than_me:
        taller_than_me[A].append(B)
    else:
        taller_than_me[A] = [B]

for idx in range(1, N+1):
    if shorter_than_me[idx] == 0:
        queue.append(idx)

while queue:
    temp = queue.popleft()
    print(temp, end = " ")
    if temp in taller_than_me:
        taller_list = taller_than_me.pop(temp)
        for taller in taller_list:
            shorter_than_me[taller] -= 1
            if shorter_than_me[taller] == 0:
                queue.append(taller)