#11403번

def route(source, temp):
    for i in range(N):
        if matrix[temp][i] == 1 and answer[source][i] == 0:
            answer[source][i] = 1
            route(source,i)

N = int(input())
matrix = list()
for i in range(N):
    array = list(map(int,input().split()))
    matrix.append(array)

answer = list()
for i in range(N):
    answer.append([0]*N)

for i in range(N):
    route(i,i)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end = " ")
    print("")