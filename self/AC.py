#5430번

import sys
input = sys.stdin.readline

testcase = int(input())
for i in range(testcase):
    pointer = 0
    inst = input()
    n = int(input())
    if n == 0:
        input()
        array = list()
    else:
        array = list(map(int,input().strip('[]\n').split(',')))
    for j in inst:
        if j == 'R':
            if pointer == 0:
                pointer = -1
            else:
                pointer = 0
        elif j == 'D':
            if len(array) == 0:
                print("error")
                break
            else:
                del array[pointer]
    else:
        if pointer == 0:
            print('[', end = "")
            for i in range(len(array)):
                if i == len(array) - 1:
                    print(array[len(array)-1], end="")
                else:
                    print(array[i], end = ",")
            print(']')
        else:
            print('[', end = "")
            for i in range(len(array)-1,-1,-1):
                if i == 0:
                    print(array[0], end="")
                else:
                    print(array[i], end = ",")
            print(']')