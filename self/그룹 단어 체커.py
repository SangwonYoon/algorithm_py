# 1316번
import sys

input = sys.stdin.readline

N = int(input())
cnt = N

for _ in range(N):
    word = input().rstrip()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)