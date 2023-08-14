import sys
from math import sqrt

input = sys.stdin.readline

def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return round(sqrt((x1-x2)**2 + (y1-y2)**2), 2)

def find_parent(a):
    while p[a] != a:
        a = p[a]
    return a

n = int(input())
position = []
for _ in range(n):
    a, b = map(float, input().split())
    position.append([a, b])

distance = []
for i in range(n):
    for j in range(i):
        distance.append([i, j, get_distance(position[i], position[j])])

distance.sort(key=lambda x : x[2])

total = 0
cnt = 0
p = [i for i in range(n)]

while cnt < n-1 and distance:
    a, b, dist = distance.pop(0)
    if find_parent(a) == find_parent(b):
        continue
    p[find_parent(b)] = a
    total += dist
    cnt += 1

print(total)