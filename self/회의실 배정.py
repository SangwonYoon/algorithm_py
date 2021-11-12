#1931번

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
time = [list(map(int,input().split())) for i in range(N)]
time.sort(key = lambda x : x[0])
time.sort(key = lambda x : x[1])
time = deque(time)

cnt = 0
end_t = 0
while len(time) > 0:
    if time[0][0] < end_t:
        time.popleft()
    else:
        end_t = time.popleft()[1]
        cnt += 1

print(cnt)
