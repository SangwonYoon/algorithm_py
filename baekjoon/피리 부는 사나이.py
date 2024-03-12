# 16724번

import sys

input = sys.stdin.readline


def find_parent(i, j):
    n = j+i*M+1
    if p[i][j] == n:
        return n
    else:
        parent_n = p[i][j]
        p_i, p_j = (parent_n-1) // M, (parent_n-1) % M
        real_parent = find_parent(p_i, p_j)
        p[i][j] = real_parent
        return real_parent


def merge(i, j, m):
    d_i, d_j = i+move[m][0], j+move[m][1]
    p[i][j] = find_parent(d_i, d_j)


move = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

N, M = map(int, input().split())

zone = []

for _ in range(N):
    zone.append(list(input().rstrip()))

p = [[j+i*M+1 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        merge(i, j, zone[i][j])

for i in range(N):
    for j in range(M):
        p[i][j] = find_parent(i, j)

print(len(set([n for l in p for n in l])))
