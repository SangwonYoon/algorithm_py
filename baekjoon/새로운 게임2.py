# 17837번

import sys

input = sys.stdin.readline

def move_chess(row, col, dy, dx, i, type):
    global grid, chess

    target_chess_index = grid[row][col].index(i) # 옮기는 체스 말이 몇 번째 위치에 있는지 확인
    moving_chess = grid[row][col][target_chess_index:] # 옮기는 체스 말 위에 있는 말을 함께 이동
    grid[row][col] = grid[row][col][:target_chess_index]
    row += dy
    col += dx
    for c in moving_chess:
        chess[c][0], chess[c][1] = row, col

    if type == 0:
        grid[row][col] += moving_chess
    elif type == 1:
        grid[row][col] += moving_chess[::-1]

    if len(grid[row][col]) >= 4:
        return True

    return False

def reverse_direction(row, col, i):
    global chess, direction

    chess[i][2] = chess[i][2] // 2 * 2 + (chess[i][2] + 1) % 2 # 방향 뒤집기
    dx, dy = direction[chess[i][2]]

    if not (0 <= row+dy < N and 0 <= col+dx < N) or matrix[row+dy][col+dx] == 2:
        return False
    else:
        return move_chess(row, col, dy, dx, i, matrix[row+dy][col+dx])


direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

N, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)] # 체스 판의 상태 표시

chess = [] # 체스 말의 상태 표시
for _ in range(K):
    row, col, d = map(int, input().split())
    chess.append([row-1, col-1, d-1])

grid = [[[] for _ in range(N)] for _ in range(N)] # 체스 말이 체스 판의 어느 위치에 있는지 표시
for i, (row, col, _) in enumerate(chess):
    grid[row][col].append(i)

turn = 0

while turn < 1000:
    turn += 1
    for i, (row, col, d) in enumerate(chess):
        dx, dy = direction[d]
        if not (0 <= row+dy < N and 0 <= col+dx < N) or matrix[row+dy][col+dx] == 2:
            finish = reverse_direction(row, col, i)
        else:
            finish = move_chess(row, col, dy, dx, i, matrix[row+dy][col+dx])

        if finish:
            break
    else:
        continue

    break
else:
    print(-1)
    sys.exit(0)

print(turn)
