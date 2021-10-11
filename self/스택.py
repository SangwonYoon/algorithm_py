#10828번

import sys
input = sys.stdin.readline
stack = []

for i in range(int(input())):
    inst = input().split()
    if inst[0] == "push":
        stack.append(inst[1])
    elif inst[0] == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif inst[0] == "size":
        print(len(stack))
    elif inst[0] == "empty":
        print(int(len(stack) == 0))
    elif inst[0] == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)