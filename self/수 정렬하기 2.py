#2751번

import sys
input = sys.stdin.readline

def quickSort(arr,s,e):
    if s >= e:
        return
    pivot = arr[(s+e) // 2]
    low = s
    high = e
    while(low <= high):
        while(arr[low] < pivot):
            low += 1
        while(arr[high] > pivot):
            high -= 1
        if(low <= high):
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    quickSort(arr,s,low-1)
    quickSort(arr,low,e)
    return arr

N = int(input())
arr = list()

for i in range(N):
    arr.append(int(input()))

arr = quickSort(arr,0,N-1)
for i in range(len(arr)):
    print(arr[i])