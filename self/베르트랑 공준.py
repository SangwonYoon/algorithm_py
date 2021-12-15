#4948번

import sys
input = sys.stdin.readline
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

memo = [True for i in range(123456 * 2 + 1)]
memo[1] = False

for i in range(2,123456 * 2 + 1):
    if not isPrime(i):
        memo[i] = False

while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(n+1, 2*n+1):
        if memo[i]:
            answer += 1
    print(answer)