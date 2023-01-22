# 9935번

import sys
input = sys.stdin.readline

str = input().strip()
bomb = input().strip()
target_c = bomb[-1]
l = len(bomb)

stack = []

for c in str:
    stack.append(c)
    if c == target_c and len(stack) >= l and "".join(stack[-l:]) == bomb:
        for _ in range(l):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")