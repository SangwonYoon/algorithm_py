# 3896번

import sys
input = sys.stdin.readline

def binarySearch(s,e,num):
    if s > e:
        return -1
    m = (s+e)//2
    if prime[m-1] < num < prime[m]:
        return m
    elif num > prime[m]:
        return binarySearch(m+1,e,num)
    elif num < prime[m-1]:
        return binarySearch(s,m-1,num)
    else:
        return -1

prime = []

bit = [1 for i in range(1299710)]
for i in range(2,1299710): #에라토스테네스의 체
    if bit[i]:
        prime.append(i)
        for j in range(i*2,1299710,i):
            bit[j] = 0

T = int(input())
for i in range(T):
    num = int(input())

    idx = binarySearch(0,len(prime)-1,num)
    if idx != -1:
        print(prime[idx]-prime[idx-1])
    else:
        print(0)