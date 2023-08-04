# 7568번 
import sys

input = sys.stdin.readline

N = int(input())

info = [list(map(int,input().split())) for _ in range(N)]

for i in info:
    cnt = 1
    for j in info:
        if j[0] > i[0] and j[1] > i[1]:
            cnt += 1
    print(cnt, end = " ")