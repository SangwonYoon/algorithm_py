#1865번

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())

    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append([S, E, -T])

    distance = [0] * (N+1)
    neg_loop_flag = False
    
    for i in range(N):
        for j in range(len(edges)):
            start, end, cost = edges[j]
            if distance[end] > distance[start] + cost:
                if i == N-1:
                    neg_loop_flag = True
                distance[end] = distance[start] + cost
    
    if neg_loop_flag:
        print("YES")
    else:
        print("NO")