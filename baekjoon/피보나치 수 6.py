# 11444번

import sys
input = sys.stdin.readline

def fibo(n):
    if n == 1:
        return [[1,1], [1,0]]
    if n % 2 != 0:
        return matmul(fibo(n-1), [[1,1], [1,0]])
    else:
        mat = fibo(n//2)
        return matmul(mat, mat)

def matmul(mat1, mat2):
    result = [[0,0], [0,0]]
    result[0][0] = (mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % 1000000007
    result[0][1] = (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % 1000000007
    result[1][0] = (mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % 1000000007
    result[1][1] = (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % 1000000007

    return result

n = int(input())

result = fibo(n)
print(result[1][0] % 1000000007)