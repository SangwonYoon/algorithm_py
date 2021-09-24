#1003번

def fibonacci(N):
    if len(fibo)-1 >= N:
        return fibo[N]
    else:
        fibo.append([fibonacci(N-1)[0] + fibonacci(N-2)[0], fibonacci(N-1)[1] + fibonacci(N-2)[1]])
        return fibo[N]

import sys
input = sys.stdin.readline

fibo = [[1,0], [0,1]]

T = int(input())
for i in range(T):
    N = int(input())
    arr = fibonacci(N)
    print(arr[0], arr[1])