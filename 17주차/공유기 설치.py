#2110번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def binarySearch(s,e):
    if s > e:
        return
    global answer
    distance = (s+e)//2
    cnt = 1
    temp = home[0]
    for i in range(1,len(home)):
        if home[i] >= temp + distance:
            cnt += 1
            temp = home[i]
    if cnt >= C:
        answer = distance
        binarySearch(distance+1,e)
    else:
        binarySearch(s,distance-1)

answer = 0
N, C = map(int,input().split())
home = [int(input()) for _ in range(N)]
home.sort()
start = 1
end = home[-1] - home[0]
binarySearch(start,end)
print(answer)