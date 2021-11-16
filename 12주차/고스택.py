#3425번

import sys
input = sys.stdin.readline

command = list()

while True:
    a = input().rstrip()
    if a == "QUIT":
        break
    if a != "END":
        command.append(a)
    else:
        for i in range(int(input())):
            stack = [int(input())]
            try:
                for j in command:
                    if j == "POP":
                        stack.pop()
                    elif j == "INV":
                        stack.append(-stack.pop())
                    elif j == "DUP":
                        stack.append(stack[-1])
                    elif j == "SWP":
                        stack[-1], stack[-2] = stack[-2], stack[-1]
                    elif j == "ADD":
                        stack.append(stack.pop() + stack.pop())
                    elif j == "SUB":
                        stack.append(-stack.pop() + stack.pop())
                    elif j == "MUL":
                        stack.append(stack.pop() * stack.pop())
                    elif j == "DIV":
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(-(abs(y) // abs(x))) if x * y < 0 else stack.append(abs(y) // abs(x))
                    elif j == "MOD":
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(abs(y) % abs(x)) if y >= 0 else stack.append(-(abs(y) % abs(x)))
                    else:
                        stack.append(int(j.split()[1]))
                if len(stack) != 1 or stack[0] > 10**9:
                    print("ERROR")
                else:
                    print(stack[0])
            except:
                print("ERROR")
                continue

        command = list()
        blank = input()
        print()