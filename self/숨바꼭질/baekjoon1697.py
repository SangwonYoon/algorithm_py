import sys
N, K = map(int,input().split())

if(N >= K):
    print(N-K)
    sys.exit()
else:
    pos = [-1] * (K*2)
    pos[N] = 0
    prev = [N]
    while True:
        temp = list()
        for i in prev:
            if(2*i <= 2*K and pos[2*i] == -1):
                pos[2*i] = pos[i] + 1
                temp.append(2*i)
            if(i+1 <= 2*K and pos[i+1] == -1):
                pos[i+1] = pos[i] + 1
                temp.append(i+1)
            if(i-1 >= 0 and pos[i-1] == -1):
                pos[i-1] = pos[i] + 1
                temp.append(i-1)
        if K in temp:
            break
        prev = temp
    print(pos[K])