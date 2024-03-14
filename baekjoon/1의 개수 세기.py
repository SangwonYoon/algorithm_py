# 9527번

import sys

input = sys.stdin.readline


def get_acc(num):
    if len(num) < 4:
        return int(num, 2)

    new_num = num[:2] + num[3:]
    if num[2] == "0":
        return get_acc(new_num)
    else:
        return get_acc(new_num) + acc[len(num)-3] + int(new_num, 2) + 1


A, B = map(int, input().split())

acc = [0]

length = len(bin(B)) - 2

for i in range(1, length):
    val = acc[i-1] * 2 + 2**(i-1)
    acc.append(val)

print(get_acc(bin(B)) - get_acc(bin(A-1)))
