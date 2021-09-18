#1027번

N = int(input())
view = list()
building = list(map(int,input().split()))

for i in range(N):
    cnt = 0
    if i != N-1:
        temp = building[i+1] - building[i]
        cnt += 1
        for j in range(i+2,N):
            if (building[j] - building[i]) / (j - i) > temp:
                temp = (building[j] - building[i]) / (j - i)
                cnt += 1
    if i != 0:
        temp = building[i] - building[i-1]
        cnt += 1
        for j in range(i-2,-1,-1):
            if (building[j] - building[i]) / (j - i) < temp:
                temp = (building[j] - building[i]) / (j - i)
                cnt += 1
    view.append(cnt)

print(max(view))