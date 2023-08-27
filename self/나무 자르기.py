# 2805번

import sys

input = sys.stdin.readline

def get_wood(height):
    total = 0
    for t in tree:
        if t > height:
            total += (t-height)
    return total

N, M = map(int, input().split())
tree = list(map(int, input().split()))
highest = max(tree)
lowest = 0
result = highest

while highest >= lowest:
    middle = (highest+lowest)//2
    if get_wood(middle) >= M:
        result = middle
        lowest = middle+1
    else:
        highest = middle-1

print(result)