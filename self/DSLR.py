# 9019번

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    queue = deque([])
    visited = [0] * 10000
    visited[A] = ""
    queue.append(A)
    while not visited[B]:
        temp = queue.popleft()
        command = visited[temp]

        #D
        temp_D = (2*temp)%10000
        if not visited[temp_D]:
            visited[temp_D] = command + "D"
            queue.append(temp_D)

        #S
        temp_S = (temp-1) % 10000
        if not visited[temp_S]:
            visited[temp_S] = command + "S"
            queue.append(temp_S)

        #L
        temp_L = (temp*10)%10000 + temp//1000
        if not visited[temp_L]:
            visited[temp_L] = command + "L"
            queue.append(temp_L)

        #R
        temp_R = temp//10 + (temp%10) * 1000
        if not visited[temp_R]:
            visited[temp_R] = command + "R"
            queue.append(temp_R)

    print(visited[B])