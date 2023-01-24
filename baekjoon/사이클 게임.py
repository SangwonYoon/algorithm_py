# 20040번

import sys
input = sys.stdin.readline

def find_root(points, a):
    while points[a] != a:
        a = points[a]
    return a

n, m = map(int, input().split())
points = [i for i in range(n)]
inp = []

for _ in range(m):
    inp.append(list(map(int, input().split())))

for i in range(m):
    a, b = inp[i]
    A = find_root(points, a)
    B = find_root(points, b)
    if A == B:
        print(i+1)
        break
    points[B] = A
else:
    print(0)