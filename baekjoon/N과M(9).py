# 15663번

from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int,input().split()))
nums.sort()

result = list(set(permutations(nums, M)))
result.sort()

for i in range(len(result)):
    for j in range(M):
        print(result[i][j], end = " ")
    print()