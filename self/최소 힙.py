#1927번

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for i in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,x)