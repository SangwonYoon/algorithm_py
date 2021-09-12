#1389번
import sys
input = sys.stdin.readline

def Kevin(person):
    arr = [-1] * N
    arr[person-1] = 0
    cnt = 1
    while(-1 in arr):
        for i in range(len(arr)):
            if arr[i] == cnt - 1:
                for j in range(len(relation[i])):
                    if arr[relation[i][j]-1] == -1:
                        arr[relation[i][j]-1] = cnt
        cnt += 1
    return sum(arr)

N, M = map(int,input().split())
relation = list()
for i in range(N):
    relation.append(list())
for i in range(M):
    temp = list(map(int,input().split()))
    relation[temp[0]-1].append(temp[1])
    relation[temp[1]-1].append(temp[0])

Bacon = list()
for i in range(N):
    Bacon.append(Kevin(i+1))

for i in range(len(Bacon)):
    if Bacon[i] == min(Bacon):
        print(i+1)
        break