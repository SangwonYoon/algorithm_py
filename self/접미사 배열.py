#11656번

import sys
input = sys.stdin.readline

str = input().rstrip()
words = []

for i in range(len(str)):
    words.append(str[i:])

for i in sorted(words):
    print(i)