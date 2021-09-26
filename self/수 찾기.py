#1920번

import sys
input = sys.stdin.readline

def search(s,e,target):
    if s > e: return 0
    mid = (s+e) // 2
    if arr[mid] == target: 
        return 1
    elif arr[mid] > target: 
        return search(s,mid-1,target)
    else: 
        return search(mid+1,e,target)

N = int(input())
arr = list(map(int,input().split()))
M = int(input())
check = list(map(int,input().split()))

arr.sort()
for i in check:
    print(search(0,len(arr)-1,i))