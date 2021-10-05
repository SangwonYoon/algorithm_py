paper = int(input())
covered = list()
answer = 0

for i in range(102):
    covered.append([0] * 102)

for i in range(paper):
    x, y = map(int, input().split())
    for a in range(x+1,x+11):
        for b in range(y+1,y+11):
            covered[a][b] = 1

for i in range(1,101):
    for j in range(1,101):
        if covered[i][j] == 1:
            if covered[i-1][j] == 0:
                answer += 1
            if covered[i+1][j] == 0:
                answer += 1
            if covered[i][j-1] == 0:
                answer += 1
            if covered[i][j+1] == 0:
                answer += 1

print(answer)