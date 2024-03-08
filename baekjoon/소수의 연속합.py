# 1644번

import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(0)
    sys.exit(0)

arr = [True] * (N+1)
arr[0] = False
arr[1] = False

for i in range(2, N+1):
    if arr[i]:
        j = 2
        while (i*j <= N):
            arr[i*j] = False
            j += 1

prime = [n for n in range(N+1) if arr[n]]

ptr1 = len(prime)-1
ptr2 = len(prime)-1

cnt = 0
total = prime[-1]

while ptr1 >= 0:
    if total == N:
        cnt += 1
        ptr1 -= 1
        total += prime[ptr1]
    elif total < N:
        ptr1 -= 1
        total += prime[ptr1]
    else:
        total -= prime[ptr2]
        ptr2 -= 1

print(cnt)
