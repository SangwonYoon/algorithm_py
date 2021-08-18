def visitable(city):
    for i in range(N):
        if conn[city][i] and visit[i] == 0:
            visit[i] = 1
            visitable(i)

N = int(input())
M = int(input())

conn = list()
for i in range(N):
    conn.append(list(map(int,input().split())))

plan = list(map(int,input().split()))

visit = [0]*N
visit[plan[0]-1] = 1
visitable(plan[0]-1)

for i in range(M):
    if visit[plan[i]-1] == 0:
        print("NO")
        break
else:
    print("YES") 