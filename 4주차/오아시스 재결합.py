import sys 

people = int(sys.stdin.readline())
height = list()
cnt = 0

for i in range(people):
    temp = int(sys.stdin.readline())
    while(len(height) != 0 and height[-1][0] < temp):
        cnt += height.pop()[1]
    if len(height) == 0:
        height.append([temp,1])
    elif(height[-1][0] == temp):
        if len(height) == 1:
            cnt += height[-1][1]
        else:
            cnt += height[-1][1] + 1
        height[-1][1] += 1
    else:
        cnt += 1
        height.append([temp,1])
print(cnt)