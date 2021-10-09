import sys
input = sys.stdin.readline

queue = list()

for i in range(int(input())):
    inst = input().split()
    if inst[0] == "push":
        queue.append(inst[1])
    elif inst[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif inst[0] == "size":
        print(len(queue))
    elif inst[0] == "empty":
        print(int(len(queue) == 0))
    elif inst[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif inst[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])