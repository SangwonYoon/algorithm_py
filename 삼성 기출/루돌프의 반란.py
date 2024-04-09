import sys

input = sys.stdin.readline


def calc_distance(loc1, loc2):
    y1, x1 = loc1
    y2, x2 = loc2
    return (y2-y1)**2 + (x2-x1)**2


def find_rudolf_direction(rudolf, santa):
    y_diff = santa[0] - rudolf[0]
    x_diff = santa[1] - rudolf[1]
    if y_diff == 0:
        return (0, int(x_diff/abs(x_diff)))
    elif x_diff == 0:
        return (int(y_diff/abs(y_diff)), 0)
    else:
        return (int(y_diff/abs(y_diff)), int(x_diff/abs(x_diff)))


def knock_back(santa_loc_row, santa_loc_col, direction, santa_num):
    if not(0 <= santa_loc_row < N and 0 <= santa_loc_col < N):
        score[santa_num-1][1] = -1 # 산타 아웃
        return

    if matrix[santa_loc_row][santa_loc_col] > 0:
        knock_back_row = santa_loc_row + direction[0]
        knock_back_col = santa_loc_col + direction[1]
        knock_back(knock_back_row, knock_back_col, direction, matrix[santa_loc_row][santa_loc_col])
    matrix[santa_loc_row][santa_loc_col] = santa_num
    santa[santa_num-1][1] = santa_loc_row
    santa[santa_num-1][2] = santa_loc_col


def discount(x):
    if x[1] > 0:
        x[1] -= 1
    return x


def find_santa_direction(santa, rudolf):
    y_diff = rudolf[0] - santa[0]
    x_diff = rudolf[1] - santa[1]

    if abs(y_diff) > abs(x_diff):
        dy = int(y_diff/abs(y_diff))
        if not is_santa_exist(santa[0]+dy, santa[1]):
            return (dy, 0)
        
        if x_diff == 0:
            return (0, 0)
        
        dx = int(x_diff/abs(x_diff))
        if not is_santa_exist(santa[0], santa[1]+dx):
            return (0, dx)
        
    elif abs(y_diff) < abs(x_diff):
        dx = int(x_diff/abs(x_diff))
        if not is_santa_exist(santa[0], santa[1]+dx):
            return (0, dx)
        
        if y_diff == 0:
            return (0, 0)
        
        dy = int(y_diff/abs(y_diff))
        if not is_santa_exist(santa[0]+dy, santa[1]):
            return (dy, 0)
        
    else:
        if y_diff < 0:
            dy = -1
            if not is_santa_exist(santa[0]+dy, santa[1]):
                return (dy, 0)

        if x_diff > 0:
            dx = 1
            if not is_santa_exist(santa[0], santa[1]+dx):
                return (0, dx)

        if y_diff > 0:
            dy = 1
            if not is_santa_exist(santa[0]+dy, santa[1]):
                return (dy, 0)
        
        if x_diff < 0:
            dx = -1
            if not is_santa_exist(santa[0], santa[1]+dx):
                return (0, dx)
        
    return (0, 0)
        
        
def is_santa_exist(row, col):
    global matrix
    if matrix[row][col] > 0:
        return True
    return False


N, M, P, C, D = map(int, input().split())
matrix = [[0] * N for _ in range(N)] # 0은 빈 공간, -1은 루돌프, 자연수 n은 산타 번호
rudolf = list(map(int, input().split()))
rudolf[0] -= 1
rudolf[1] -= 1
matrix[rudolf[0]][rudolf[1]] = -1

santa = [] # [[santa_num, row, col], ...]
for _ in range(P):
    santa_num, row, col = list(map(int, input().split()))
    santa.append([santa_num, row-1, col-1])
    matrix[row-1][col-1] = santa_num

santa.sort(key = lambda x : x[0])
# santa = [[row, col] for _, row, col in santa]
score = [[0, 0] for _ in range(P)] # [[score, stun_turn], ...]

turn = 0
while turn < M:
    turn += 1

    # rudolf's turn
    santa_sorted = sorted(santa, key=lambda x:x[2], reverse=True)
    santa_sorted = sorted(santa_sorted, key=lambda x:x[1], reverse=True)
    target_santa = [-1, 2*N**2] # [santa_num, distance]

    for n, row, col in santa_sorted:
        if score[n-1][1] == -1: # 기절한 산타는 거리 계산 스킵
            continue
        dist = calc_distance(rudolf, (row, col))
        if target_santa[1] > dist:
            target_santa = [n, dist]
    
    target_santa_loc = santa[target_santa[0]-1][1:]
    d = find_rudolf_direction(rudolf, target_santa_loc)
    matrix[rudolf[0]][rudolf[1]] = 0
    rudolf[0] += d[0]
    rudolf[1] += d[1]

    if rudolf == target_santa_loc: # 충돌
        score[target_santa[0]-1][0] += C
        score[target_santa[0]-1][1] = 2 # 현재 턴과 다음 턴 동안 기절

        santa_y = target_santa_loc[0] + d[0] * C
        santa_x = target_santa_loc[1] + d[1] * C

        knock_back(santa_y, santa_x, d, target_santa[0])

    matrix[rudolf[0]][rudolf[1]] = -1

    # santa's turn
    for santa_num in range(1, P+1):
        if score[santa_num-1][1] == 0: # 살아있는 산타
            temp_santa_loc = santa[santa_num-1][1:]
            d = find_santa_direction(temp_santa_loc, rudolf)
            matrix[temp_santa_loc[0]][temp_santa_loc[1]] = 0
            temp_santa_loc[0] += d[0]
            temp_santa_loc[1] += d[1]

            if rudolf == temp_santa_loc: # 충돌
                score[santa_num-1][0] += D
                score[santa_num-1][1] = 2 # 현재 턴과 다음 턴 동안 기절

                santa_y = temp_santa_loc[0] + d[0] * -D
                santa_x = temp_santa_loc[1] + d[1] * -D

                knock_back_d = [d[0] * -1, d[1] * -1]

                knock_back(santa_y, santa_x, knock_back_d, santa_num)
            else:
                matrix[temp_santa_loc[0]][temp_santa_loc[1]] = santa_num
                santa[santa_num-1][1] = temp_santa_loc[0]
                santa[santa_num-1][2] = temp_santa_loc[1]

    if [stun for _, stun in score].count(-1) == P: # 모든 산타가 기절
        break

    for i in range(P):
        if score[i][1] >= 0: # 산타가 아웃되지 않았으면
            score[i][0] += 1

    score = list(map(discount, score)) # 기절을 1턴씩 품

print(" ".join([str(s[0]) for s in score]))