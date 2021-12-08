#5525번

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

target = "I" + ("OI" * N)
idx = 0
answer = 0

while idx < M and S[idx:].find(target) != -1:
    answer += 1
    idx += S[idx:].find(target) + 2*N + 1
    while True:
        if idx + 1 < M and S[idx] == "O" and S[idx+1] == "I":
            answer += 1
            idx += 2
        else:
            break

print(answer)