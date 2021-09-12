#17219

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pwd = dict()
for i in range(N):
    site, word = input().split()
    pwd[site] = word

for i in range(M):
    print(pwd[input().rstrip()])