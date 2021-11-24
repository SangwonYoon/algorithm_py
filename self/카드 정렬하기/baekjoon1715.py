import sys
input = sys.stdin.readline
import heapq

N = int(input())
cards = [int(input()) for i in range(N)]
heapq.heapify(cards)

total = 0
while len(cards) > 1:
    target = heapq.heappop(cards) + heapq.heappop(cards)
    total += target
    heapq.heappush(cards,target)

print(total)