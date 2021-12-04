#16953번

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
while(B > A):
    if(B % 10 == 1):
        B = (B-1)//10
        cnt += 1
    elif(B % 2 == 0):
        B /= 2
        cnt += 1
    else:
        break
if B == A: print(cnt)
else : print(-1)