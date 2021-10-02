#11650번
N = int(input())

pos = [list(map(int,input().split())) for _ in range(N)]

pos.sort(key = lambda x : x[1])
pos.sort(key = lambda x : x[0])

for i in pos:
    print(i[0], i[1])