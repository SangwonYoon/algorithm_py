#2606번

import sys
input = sys.stdin.readline

def V(source):
    for i in range(len(conn[source-1])):
        if virus[conn[source-1][i]-1] == False:
            virus[conn[source-1][i]-1] = True
            V(conn[source-1][i])

N = int(input())
M = int(input())
conn = [list() for _ in range(N)]
virus = [False] * N
for i in range(M):
    a,b = map(int,input().split())
    conn[a-1].append(b)
    conn[b-1].append(a)

V(1)

cnt = 0
for i in range(1,len(virus)):
    if(virus[i]):
        cnt += 1

print(cnt)