#1339번

import sys
input = sys.stdin.readline

nums = []
max = 0
for i in range(int(input())):
    a = input().rstrip()
    if len(a) > max:
        max = len(a)
    nums.append(a)

digit = [[] for i in range(max)]
for i in nums:
    for j in range(len(i)-1,-1,-1):
        digit[len(i)-1-j].append(i[j])

weight = dict()
for i in range(len(digit)-1,-1,-1):
    while len(digit[i]) > 0:
        temp = digit[i].pop()
        if temp not in weight:
            weight[temp] = 10**i
        else:
            weight[temp] += 10**i

x = list(weight.values())
x.sort(reverse = True)
n = 9
total = 0
for i in x:
    total += i*n
    n -= 1

print(total)