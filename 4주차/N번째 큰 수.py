import heapq

N = int(input())
nums = list()

for i in map(int,input().split()):
    heapq.heappush(nums,i)

for i in range(N-1):
    for j in map(int,input().split()):
        heapq.heappush(nums,j)
        heapq.heappop(nums)

print(heapq.heappop(nums))