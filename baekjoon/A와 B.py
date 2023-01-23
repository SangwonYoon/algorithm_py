# 12904번

import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
stack = list(T)

flag = -1

while len(S) < len(stack):
    if flag == -1:
        if stack[-1] == "A":
            stack.pop()
        else: # stack[-1] == "B"
            stack.pop()
            flag *= -1
    elif flag == 1:
        if stack[0] == "A":
            stack.pop(0)
        else: # stack[0] == "B"
            stack.pop(0)
            flag *= -1

if flag == 1:
    stack.reverse()

if S == "".join(stack):
    print(1)
else:
    print(0)