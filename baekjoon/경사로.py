# 14890번

import sys

input = sys.stdin.readline


def is_passable(road, N, L):
    climbs = [0] * N
    for j in range(N-1):
        if road[j] != road[j+1]:
            if road[j] + 1 == road[j+1] and j-L+1 >= 0:
                for k in range(L):
                    if road[j-k] != road[j] or climbs[j-k] != 0:
                        return False
                    else:
                        climbs[j-k] = 1
            elif road[j] == road[j+1] + 1 and j+L < N:
                for k in range(L):
                    if road[j+1+k] != road[j+1] or climbs[j+1+k] != 0:
                        return False
                    else:
                        climbs[j+1+k] = 1
            else:
                return False
    return True


N, L = map(int, input().split())

roads = []

for _ in range(N):
    road = list(map(int, input().split()))
    roads.append(road)

climbs_row = [[0] * N for _ in range(N)]
climbs_col = [[0] * N for _ in range(N)]
answer = 0

for i in range(N):
    temp_row_road = roads[i]
    temp_col_road = [roads[n][i] for n in range(N)]

    if is_passable(temp_row_road, N, L):
        answer += 1

    if is_passable(temp_col_road, N, L):
        answer += 1

print(answer)
