#2579번

import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(int(input()))
else:
    stairs = [int(input()) for i in range(N)]

    point = [[stairs[0], 0], [stairs[0]+stairs[1], stairs[1]]]

    for i in range(2,N):
        temp = list()
        temp.append(point[i-1][1]+stairs[i])
        temp.append(max(point[i-2][0],point[i-2][1])+stairs[i])
        point.append(temp)

    print(max(point[-1]))