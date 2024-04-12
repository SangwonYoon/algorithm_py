import sys

input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # (dy, dx)

def is_knight_movable(row, col, height, width, direction): # (이동 가능 여부, damage)
    global matrix, chess, knock_back_knights, L
    if direction == 0: # 위로 움직이는 경우
        if row+dy < 0:
            return False
        for w in range(width):
            if matrix[row+dy][col+w] == 2: # 이동하는 곳에 벽이 있는 경우
                return False
            
            if chess[row+dy][col+w] >= 0: # 이동하는 곳에 다른 기사가 있는 경우
                target_knight = chess[row+dy][col+w]
                if target_knight not in knock_back_knights:
                    knock_back_knights.append(target_knight)
    elif direction == 1: # 오른쪽으로 움직이는 경우
        if col+dx+width-1 >= L:
            return False
        for h in range(height):
            if matrix[row+h][col+dx+width-1] == 2: # 이동하는 곳에 벽이 있는 경우
                return False
            
            if chess[row+h][col+dx+width-1] >= 0: # 이동하는 곳에 다른 기사가 있는 경우
                target_knight = chess[row+h][col+dx+width-1]
                if target_knight not in knock_back_knights:
                    knock_back_knights.append(target_knight)
    elif direction == 2: # 아래쪽으로 움직이는 경우
        if row+dy+height-1 >= L:
            return False
        for w in range(width):
            if matrix[row+dy+height-1][col+w] == 2: # 이동하는 곳에 벽이 있는 경우
                return False
            
            if chess[row+dy+height-1][col+w] >= 0: # 이동하는 곳에 다른 기사가 있는 경우
                target_knight = chess[row+dy+height-1][col+w]
                if target_knight not in knock_back_knights:
                    knock_back_knights.append(target_knight)
    else: # 왼쪽으로 움직이는 경우
        if col+dx < 0:
            return False
        for h in range(height):
            if matrix[row+h][col+dx] == 2: # 이동하는 곳에 벽이 있는 경우
                return False
            
            if chess[row+h][col+dx] >= 0: # 이동하는 곳에 다른 기사가 있는 경우
                target_knight = chess[row+h][col+dx]
                if target_knight not in knock_back_knights:
                    knock_back_knights.append(target_knight)
    
    return True


def knock_back(knight, direction): # 넉백 중 벽에 부딪히면 False를 반환
    global knock_back_knights, knights, directions, damages
    row, col, height, width, _ = knights[knight]
    movable = is_knight_movable(row, col, height, width, direction)
    if not movable:
        return False
    
    # 데미지 계산
    dy, dx = directions[direction]
    damages[knight] = calc_damage(row+dy, col+dx, height, width)
    return True


def calc_damage(row, col, height, width):
    global matrix
    total_damage = 0
    for r in range(row, row+height):
        for c in range(col, col+width):
            if matrix[r][c] == 1:
                total_damage += 1
    
    return total_damage


def move_knight(row, col, height, width, direction, knight):
    global directions, knights
    dy, dx = directions[direction]
    knights[knight][0], knights[knight][1] = row+dy, col+dx

    if direction == 0:
        for w in range(width):
            if chess[row+height-1][col+w] == knight:
                chess[row+height-1][col+w] = -1
            chess[row+dy][col+w] = knight
    elif direction == 1:
        for h in range(height):
            if chess[row+h][col] == knight:
                chess[row+h][col] = -1
            chess[row+h][col+dx+width-1] = knight
    elif direction == 2:
        for w in range(width):
            if chess[row][col+w] == knight:
                chess[row][col+w] = -1
            chess[row+dy+height-1][col+w] = knight
    elif direction == 3:
        for h in range(height):
            if chess[row+h][col+width-1] == knight:
                chess[row+h][col+width-1] = -1
            chess[row+h][col+dx] = knight


def remove_knight(row, col, height, width, knight):
    for h in range(height):
        for w in range(width):
            if chess[row+h][col+w] == knight:
                chess[row+h][col+w] = -1

L, N, Q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(L)]
knights = [] # [r, c, h, w, k]
for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    knights.append([r-1, c-1, h, w, k])
commands = [list(map(int, input().split())) for _ in range(Q)] # [knight, direction]

life = [k for _, _, _, _, k in knights] # 기사들의 체력 정보
chess = [[-1] * L for _ in range(L)] # 체스판 위 기사들의 위치
for knight, (row, col, height, width, _) in enumerate(knights):
    for h in range(height):
        for w in range(width):
            chess[row+h][col+w] = knight

for knight, direction in commands:
    knight -= 1
    row, col, height, width, _ = knights[knight]

    if life[knight] <= 0: # 기사의 체력이 없으면 명령 스킵
        continue

    dy, dx = directions[direction]
    block_flag = False # 이동 중 벽에 가로 막히는지
    knock_back_knights = [] # 밀려나는 기사 정보
    movable = is_knight_movable(row, col, height, width, direction)
    if not movable: # 명령 받은 기사 이동 가능 여부 확인
        continue

    damages = {} # 기사들이 입은 피해 정보
    for knock_back_knight in knock_back_knights:
        if not knock_back(knock_back_knight, direction): # 밀려난 기사 이동 가능 여부 확인
            block_flag = True
            break

    if block_flag:
        continue

    # 기사 이동
    move_knight(row, col, height, width, direction, knight)
    for knock_back_knight in knock_back_knights:
        life[knock_back_knight] -= damages[knock_back_knight]
        t_row, t_col, t_height, t_width, _ = knights[knock_back_knight]
        if life[knock_back_knight] > 0: # 살아 있는 기사
            move_knight(t_row, t_col, t_height, t_width, direction, knock_back_knight)
        else: # 사라진 기사
            remove_knight(t_row, t_col, t_height, t_width, knock_back_knight)

answer = 0
for idx in range(len(life)):
    if life[idx] > 0:
        answer += knights[idx][4] - life[idx]

print(answer)