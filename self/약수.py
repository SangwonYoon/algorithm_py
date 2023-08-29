# 1037번

import sys

input = sys.stdin.readline

_ = input()
divisors = list(map(int, input().split()))
divisors.sort()
print(divisors[0] * divisors[-1])