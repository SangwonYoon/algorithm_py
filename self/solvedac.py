# 18110번

import sys

input = sys.stdin.readline

def round_func(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
difficulty = []
for _ in range(n):
    difficulty.append(int(input()))

difficulty.sort()
offset = round_func(n * 0.15)

if n == 0:
    print(0)
elif offset == 0:
    print(round_func(sum(difficulty)/len(difficulty)))
else:
    print(round_func(sum(difficulty[offset:-offset])/len(difficulty[offset:-offset])))