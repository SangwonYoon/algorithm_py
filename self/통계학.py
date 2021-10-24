#2108번

import sys
input = sys.stdin.readline

N = int(input())
nums = list()
nums_dic = dict()
for i in range(N):
    num = int(input())
    nums.append(num)
    if(num in nums_dic):
        nums_dic[num] += 1
    else:
        nums_dic[num] = 1

nums.sort()

print(round(sum(nums) / N))
print(nums[N//2])

M = -1
M_list = list()
for (key,value) in nums_dic.items():
    if value > M:
        M = value
        M_list = [key]
    elif value == M:
        M_list.append(key)
print(sorted(M_list)[1]) if len(M_list) != 1 else print(M_list[0])

print(nums[-1] - nums[0])