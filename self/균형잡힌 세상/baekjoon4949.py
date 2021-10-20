#4949번

import sys
input = sys.stdin.readline

while(True):
    stack = list()
    str = input().rstrip()
    if str == ".":
        break
    for i in str:
        if i == "(":
            stack.append("(")
        elif i == "[":
            stack.append("[")
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break;
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break;
    else:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")