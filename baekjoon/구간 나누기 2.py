#  13397번

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
while left < right:
    mid = (left+right) // 2
    cnt = 0
    s = 0
    for i in range(len(arr)):
        if max(arr[s:i+1]) - min(arr[s:i+1]) > mid:
            cnt += 1
            s = i
    cnt += 1
    if cnt <= M:
        right = mid
    else:
        left = mid + 1

print(left)