#11651번

import sys
input = sys.stdin.readline

point = list()
N = int(input())
for i in range(N):
    point.append(list(map(int,input().split())))

point.sort(key = lambda x : x[0])
point.sort(key = lambda x : x[1])

for i in point:
    print(str(i[0]) + " " + str(i[1]))

