#1543번

import sys
input = sys.stdin.readline

str = input().rstrip()
target = input().rstrip()

idx = 0
answer = 0
while str[idx:].find(target) != -1:
    answer += 1
    idx += str[idx:].find(target) + len(target)

print(answer)