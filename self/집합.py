#11723번

import sys
input = sys.stdin.readline

S = [0 for i in range(21)]

for i in range(int(input())):
    op = input().split()
    if op[0] == "add":
        S[int(op[1])] = 1
    elif op[0] == "remove":
        S[int(op[1])] = 0
    elif op[0] == "check":
        print(S[int(op[1])])
    elif op[0] == "toggle":
        S[int(op[1])] = 1 - S[int(op[1])]
    elif op[0] == "all":
        S = [1 for i in range(21)]
    elif op[0] == "empty":
        S = [0 for i in range(21)]