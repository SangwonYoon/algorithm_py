#1012번

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(x,y):
    farm.remove([x,y])
    if x != 0 and [x-1,y] in farm:
        search(x-1,y)
    if x != M-1 and [x+1,y] in farm:
        search(x+1,y)
    if y != 0 and [x,y-1] in farm:
        search(x,y-1)
    if y != N-1 and [x,y+1] in farm:
        search(x,y+1)

T = int(input())

for i in range(T):
    M, N, K = map(int,input().split())
    farm = [list(map(int,input().split())) for j in range(K)]
    farm.sort(key = lambda x : x[1])
    farm.sort(key = lambda x : x[0])

    cnt = 0
    while len(farm) > 0:
        x, y = farm[0]
        search(x,y)
        cnt += 1

    print(cnt)