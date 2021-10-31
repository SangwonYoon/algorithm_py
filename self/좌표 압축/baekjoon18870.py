import sys
input = sys.stdin.readline

N = int(input())
pos = list(map(int,input().split()))
sorted_pos = sorted(list(set(pos)))

dict = {sorted_pos[i]:i for i in range(len(sorted_pos))}

for i in range(N):
    print(dict[pos[i]], end=" ")