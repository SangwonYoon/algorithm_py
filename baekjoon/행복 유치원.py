# 13164번

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
childs = list(map(int, input().split()))

delta = []
for i in range(1, N):
    delta.append(childs[i]- childs[i-1])

delta.sort(reverse = True)
print(sum(delta[K-1:]))