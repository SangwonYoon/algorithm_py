# 1032번

import sys

input = sys.stdin.readline

def change_char(word, idx, char):
    if idx == 0:
        return char + word[1:]
    elif idx == len(word)-1:
        return word[:-1] + char
    else:
        return word[:idx] + char + word[idx+1:]

N = int(input())

pattern = ""
for _ in range(N):
    temp = input().strip()
    if pattern == "":
        pattern = temp
    else:
        for idx in range(len(pattern)):
            if pattern[idx] != "?" and pattern[idx] != temp[idx]:
                pattern = change_char(pattern, idx, "?")

print(pattern)