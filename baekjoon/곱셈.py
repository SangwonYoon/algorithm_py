#1629번

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def power(num, exp, div):
    num %= div
    if exp == 1:
        return num
        
    if exp % 2 == 1:
        return (power(num, exp-1, div) * num) % div
    else:
        result = power(num, exp//2, div)
        return (result**2) % div

A, B, C = map(int, input().split())
print(power(A, B, C))