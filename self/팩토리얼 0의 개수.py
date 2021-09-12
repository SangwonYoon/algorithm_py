#1676번

N = int(input())

cnt_5 = 0
cnt_2 = 0
for i in range(2,N+1):
    while(i % 5 == 0):
        cnt_5 += 1
        i /= 5
    while(i % 2 == 0):
        cnt_2 += 1
        i /= 2

print(min(cnt_5,cnt_2))