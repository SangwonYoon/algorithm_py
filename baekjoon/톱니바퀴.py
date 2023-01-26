# 14891번

import sys
input = sys.stdin.readline

state = [0, 0, 0, 0]

def rotate(gear, n, d):
    global state
    if n == 1:
        state[0] = 1
        if state[1] == 0 and gear[0][2] != gear[1][-2]:
            rotate(gear, 2, d*(-1))
        target = gear[0] # target : list
        if d == 1:
            target.insert(0, target.pop())
        else:
            target.append(target.pop(0))

    elif n == 2:
        state[1] = 1
        if state[0] == 0 and gear[1][-2] != gear[0][2]:
            rotate(gear, 1, d*(-1))
        if state[2] == 0 and gear[1][2] != gear[2][-2]:
            rotate(gear, 3, d*(-1))
        target = gear[1]
        if d == 1:
            target.insert(0, target.pop())
        else:
            target.append(target.pop(0))

    elif n == 3:
        state[2] = 1
        if state[1] == 0 and gear[2][-2] != gear[1][2]:
            rotate(gear, 2, d*(-1))
        if state[3] == 0 and gear[2][2] != gear[3][-2]:
            rotate(gear, 4, d*(-1))
        target = gear[2]
        if d == 1:
            target.insert(0, target.pop())
        else:
            target.append(target.pop(0))
    else:
        state[3] = 1
        if state[2] == 0 and gear[2][2] != gear[3][-2]:
            rotate(gear, 3, d*(-1))
        target = gear[3]
        if d == 1:
            target.insert(0, target.pop())
        else:
            target.append(target.pop(0))

gear = []
for _ in range(4):
    gear.append(list(map(int, list(input().strip()))))

k = int(input())
for _ in range(k):
    state = [0, 0, 0, 0]
    n, d = map(int, input().split())
    rotate(gear, n, d)

answer = 0
for i in range(4):
    answer += gear[i][0] * (2**i)

print(answer)