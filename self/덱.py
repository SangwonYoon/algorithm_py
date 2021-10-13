#10866번

import sys
input = sys.stdin.readline

deque = []

for i in range(int(input())):
    inst = input().split()
    if inst[0] == "push_front":
        deque.insert(0,inst[1])
    elif inst[0] == "push_back":
        deque.append(inst[1])
    elif inst[0] == "pop_front":
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif inst[0] == "pop_back":
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)
    elif inst[0] == "size":
        print(len(deque))
    elif inst[0] == "empty":
        print(int(len(deque) == 0))
    elif inst[0] == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif inst[0] == "back":
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)