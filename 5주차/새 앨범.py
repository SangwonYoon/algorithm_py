from math import ceil

N = int(input()) #노래의 개수
L = int(input()) #노래의 길이
C = int(input()) #시디의 용량

num = 1
while(C >= ((L+1) * num - 1)):
    num += 1
num -= 1

if num % 13 == 0:
    num -= 1

if (N - N // num * num) % 13 == 0 and (num - 1) == (N - N // num * num) and N - N // num * num != 0:
    print(ceil(N / num)+1)
else:
    print(ceil(N / num))