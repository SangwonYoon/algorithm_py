# 1138번

N = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(len(arr)-1, -1, -1):
    result.insert(arr[i], i+1)

for i in result:
    print(i, end = " ")