# 1197번

import sys

input = sys.stdin.readline

def get_parent(num):
    if num == parent[num]:
        return num
    parent[num] = get_parent(parent[num])
    return parent[num]

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edge = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append([A, B, C])

edge.sort(key=lambda x: x[2])

cnt = 0
total = 0
while cnt < V-1:
    A, B, C = edge.pop(0)
    p_A = get_parent(A)
    p_B = get_parent(B)
    if p_A != p_B:
        if p_A < p_B:
            parent[p_B] = p_A
        else:
            parent[p_A] = p_B
        total += C
        cnt += 1

print(total)