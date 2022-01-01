# 1780번

import sys
input = sys.stdin.readline

def slice(i,j,n):
    global cnt
    p = paper[i][j]
    for y in range(i,i+n):
        for x in range(j,j+n):
            if p != paper[y][x]:
                new_n = n // 3
                for dy in range(3):
                    for dx in range(3):
                        slice(i+dy*new_n,j+dx*new_n,new_n)
                return
    cnt[p] += 1

N = int(input())
paper = [list(map(int,input().split())) for i in range(N)]
cnt = [0,0,0]

slice(0,0,N)

print(cnt[-1])
print(cnt[0])
print(cnt[1])