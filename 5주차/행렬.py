def flip(arr,a,b):
    for i in range(a,a+3):
        for j in range(b,b+3):
            arr[i][j] = 1 - arr[i][j]

N, M = map(int, input().split())

arr1 = list()
arr2 = list()

for i in range(N):
    arr1.append(list(map(int,input().rstrip())))
for i in range(N):
    arr2.append(list(map(int,input().rstrip())))

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if arr1[i][j] != arr2[i][j]:
            flip(arr1,i,j)
            cnt += 1

if arr1 == arr2:
    print(cnt)
else:
    print(-1)