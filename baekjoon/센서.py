# 2212번

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

if N <= K:
    print(0)
    sys.exit(0)

sensors = list(map(int, input().split()))
sensors = sorted(list(set(sensors)))
dist = []

for i in range(len(sensors)-1):
    dist.append(sensors[i+1] - sensors[i])
dist.sort()

if K == 1:
    print(sum(dist))
else:
    print(sum(dist[:-(K-1)]))