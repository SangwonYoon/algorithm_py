#1647번

from collections import deque
import sys
input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] == a:
        return a
    p = find_parent(parent, parent[a])
    parent[a] = p
    return p

def is_cycle(parent, a, b):
    return find_parent(parent, a) == find_parent(parent, b)

def merge(parent, a, b):
    p_a = find_parent(parent, a)
    p_b = find_parent(parent, b)

    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b
    

N, M = map(int, input().split())

cost = []

for _ in range(M):
    A, B, weight = map(int, input().split())
    cost.append([A, B, weight])

cost.sort(key = lambda x:x[2])
cost = deque(cost)

answer = 0
parent = [i for i in range(N+1)]
cnt = 0

while cnt < N-2:
    a, b, weight = cost.popleft()
    if not is_cycle(parent, a, b):
        answer += weight
        cnt += 1
        merge(parent, a, b)

print(answer)