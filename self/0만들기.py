# 7490번

import sys
input = sys.stdin.readline

def concat(op):
    num = 2
    exp = "1"
    for i in range(len(op)):
        exp += operations[op[i]] + str(num)
        num += 1

    return exp

def base_3(n):
    for i in range(len(n)-1, -1, -1):
        if n[i] + 1 == 3:
            n[i] = 0
        else:
            n[i] += 1
            break
    return n

operations = [" ", "+", "-"]

T = int(input())

for _ in range(T):
    n = int(input())

    op = [0] * (n-1)

    while True:
        result = concat(op)
        if eval(result.replace(" ", "")) == 0:
            print(result)

        op = base_3(op)
        if op == [0] * (n-1):
            print()
            break