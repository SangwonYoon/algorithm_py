#9576번

import sys
input = sys.stdin.readline

for i in range(int(input())):
    N, M = map(int,input().split())
    books = [1 for j in range(N)]
    student = list()
    for j in range(M):
        student.append(list(map(int,input().split())))
    student.sort(key = lambda x : x[0])
    student.sort(key = lambda x : x[1])
    answer = 0
    for j in student:
        for k in range(j[0],j[1]+1):
            if books[k-1] == 1:
                books[k-1] = 0
                answer += 1
                break
    print(answer)