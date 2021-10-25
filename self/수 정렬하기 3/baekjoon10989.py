import sys
input = sys.stdin.readline

nums = [0 for i in range(10001)]
for i in range(int(input())):
    n = int(input())
    nums[n] += 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)