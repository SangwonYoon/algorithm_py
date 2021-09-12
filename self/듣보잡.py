#1764번

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr1 = set()
for i in range(N):
    arr1.add(input().rstrip())

arr2 = set()
for j in range(M):
    arr2.add(input().rstrip())

answer = list(arr1 & arr2)
answer.sort()
print(len(answer))
for i in answer:
    print(i)