#1517번

import sys
input = sys.stdin.readline

def merge_sort(s,e):
    global cnt, nums
    if s < e:
        result = []
        mid = (s + e) // 2
        merge_sort(s,mid)
        merge_sort(mid + 1,e)
        left, right = s, mid + 1
        while left <= mid and right <= e:
            if nums[left] > nums[right]:
                result.append(nums[right])
                right += 1
                cnt += mid - left + 1
            else:
                result.append(nums[left])
                left += 1
        if right <= e:
            result += nums[right:e + 1]
        else:
            result += nums[left:mid + 1]
        nums[s:e + 1] = result

N = int(input())
nums = list(map(int,input().split()))
cnt = 0
merge_sort(0, N-1)
print(cnt)