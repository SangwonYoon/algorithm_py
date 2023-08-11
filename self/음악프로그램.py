# 2623번

import sys
# from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

cnt = [0] * (N+1)
next = {}

for _ in range(M):
    priority = list(map(int, input().split()))[1:]
    for idx in range(len(priority)-1):
        temp = priority[idx]
        temp_next = priority[idx+1]
        cnt[temp_next] += 1
        if temp in next:
            next[temp].append(temp_next)
        else:
            next[temp] = [temp_next]

queue = []
for i in range(1, N+1):
    if cnt[i] == 0:
        queue.append(i)

idx = 0
while idx < len(queue):
    temp = queue[idx]
    if temp in next:
        next_list = next[temp]
        for n in next_list:
            cnt[n] -= 1
            if cnt[n] == 0:
                queue.append(n)
    idx += 1

if sum(cnt) == 0:
    for k in queue:
        print(k)
else:
    print(0)