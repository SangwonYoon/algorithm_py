#13305번

import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int,input().split()))
price = list(map(int,input().split()))

total = price[0] * length[0]
temp = price[0]
for i in range(1,N-1):
    if price[i] < temp:
        temp = price[i]
    total += temp * length[i]

print(total)