#11725번

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree(i):
    temp = memo[i]
    for k in temp:
        if tree[k] == 0:
            tree[k] = i
            makeTree(k)

N = int(input())
tree = [0 for _ in range(N+1)] #부모의 노드 번호 저장
tree[1] = -1

memo = dict()

for _ in range(N-1):
    a, b = map(int,input().split())
    if a in memo:
        memo[a].append(b)
    else:
        memo[a] = [b]
    if b in memo:
        memo[b].append(a)
    else:
        memo[b] = [a]

makeTree(1)

for i in range(2, N+1):
    print(tree[i])