import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def find_attacker():
    global matrix, attack_history
    weakest_turret = []
    weakest_damage = 5001
    for r in range(N):
        for c in range(M):
            if matrix[r][c] <= 0:
                continue
            if matrix[r][c] == weakest_damage:
                weakest_turret.append((r, c))
            elif matrix[r][c] < weakest_damage:
                weakest_damage = matrix[r][c]
                weakest_turret = [(r, c)]

    if len(weakest_turret) == 1:
        return weakest_turret[0]
    
    for turret in attack_history[::-1]:
        if turret in weakest_turret:
            return turret
    
    weakest_turret.sort(key = lambda x : (x[0] + x[1], x[1]))
    return weakest_turret[-1]


def find_target():
    global matrix, attack_history
    strongest_turret = []
    strongest_damage = 1
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == strongest_damage:
                strongest_turret.append((r, c))
            elif matrix[r][c] > strongest_damage:
                strongest_damage = matrix[r][c]
                strongest_turret = [(r, c)]

    if len(strongest_turret) == 1:
        return strongest_turret[0]

    for turret in attack_history[::-1]:
        if turret in strongest_turret:
            strongest_turret.remove(turret)
            if len(strongest_turret) == 1:
                break

    if len(strongest_turret) == 1:
        return strongest_turret[0]

    strongest_turret.sort(key = lambda x : (x[0] + x[1], x[1]))
    return strongest_turret[0]


def find_route(source_row, source_col, dest_row, dest_col):
    queue = deque([(source_row, source_col, [])])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0] * M for _ in range(N)]
    visited[source_row][source_col] = 1
    while queue:
        temp_row, temp_col, d = queue.popleft()
        if temp_row == dest_row and temp_col == dest_col:
            return d
        for i, (dy, dx) in enumerate(directions):
            new_row = (temp_row+dy)%N
            new_col = (temp_col+dx)%M
            if matrix[new_row][new_col] > 0 and visited[new_row][new_col] == 0:
                queue.append((new_row, new_col, d+[directions[i]]))
                visited[new_row][new_col] = 1

    return []


attack_history = []
for _ in range(K):
    alive_turret = sum([1 if matrix[r][c] > 0 else 0 for r in range(N) for c in range(M)])
    if alive_turret == 1:
        break

    visited = [[0] * M for _ in range(N)]
    
    # 1. 공격자 선정
    attack_turret = find_attacker()
    a_row, a_col = attack_turret

    # 2. 공격자의 공격
    target_turret = find_target()
    t_row, t_col = target_turret
    visited[t_row][t_col] = 1

    attack_history.append((a_row, a_col))
    matrix[a_row][a_col] += N+M
    damage = matrix[a_row][a_col]
    visited[a_row][a_col] = 1

    # (1) 레이저 공격
    route = find_route(a_row, a_col, t_row, t_col)
    if len(route) > 0:
        temp_row, temp_col = a_row, a_col
        for dy, dx in route:
            temp_row, temp_col = (temp_row+dy)%N, (temp_col+dx)%M
            if temp_row == t_row and temp_col == t_col:
                matrix[temp_row][temp_col] -= damage
            else:
                matrix[temp_row][temp_col] -= damage // 2
                visited[temp_row][temp_col] = 1
    else: # (2) 포탄 공격
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = (t_row+i)%N
                new_col = (t_col+j)%M
                if i == 0 and j == 0:
                    deal = damage
                elif new_row == a_row and new_col == a_col:
                    deal = 0
                else:
                    deal = damage // 2
                    visited[new_row][new_col] = 1
                
                if matrix[new_row][new_col] > 0:
                    matrix[new_row][new_col] -= deal

    for r in range(N):
        for c in range(M):
            if matrix[r][c] > 0 and visited[r][c] == 0:
                matrix[r][c] += 1

print(max([max(row) for row in matrix]))