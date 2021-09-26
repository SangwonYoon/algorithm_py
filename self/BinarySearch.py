# 정렬된 배열 arr에서 사용 가능

arr = list()
arr.sort()

def search(s,e,target):
    if s > e: return 0
    mid = (s+e) // 2
    if arr[mid] == target: 
        return 1
    elif arr[mid] > target: 
        return search(s,mid-1,target)
    else: 
        return search(mid+1,e,target)