arr = [5,4,3,2,1]

for i in range(1,len(arr)): # 2번째 값부터 시작
    for j in range(i,0,-1): # 이전 값들과 비교
        if arr[j] < arr[j-1]: # 이전 값보다 작을시
            arr[j], arr[j-1] = arr[j-1], arr[j] # 한칸 이동
        else:
            break

print(arr)