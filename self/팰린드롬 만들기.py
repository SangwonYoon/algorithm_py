#1213번

import sys
input = sys.stdin.readline

str = input().rstrip()
alphabet = dict()
answer = ""
memo = ""

for i in str:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1

for i in range(ord('A'), ord('Z')+1):
    c = chr(i)
    if c in alphabet:
        while alphabet[c] > 0:
            if alphabet[c] >= 2:
                answer += c
                alphabet[c] -= 2
            else:
                if memo == "":
                    memo = c
                    alphabet[c] -= 1
                else:
                    print("I'm Sorry Hansoo")
                    sys.exit()

print(answer + memo + answer[::-1])
