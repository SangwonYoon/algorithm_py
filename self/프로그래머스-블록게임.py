def form(arr):
    i = arr[0][0]
    j = arr[0][1]
    
    if arr[1] == [i+1,j] and arr[2] == [i+1,j+1] and arr[3] == [i+1,j+2]:
        return 1
    elif arr[1] == [i+1,j] and arr[2] == [i+2,j-1] and arr[3] == [i+2,j]:
        return 2
    elif arr[1] == [i+1,j] and arr[2] == [i+2,j] and arr[3] == [i+2,j+1]:
        return 3
    elif arr[1] == [i+1,j-2] and arr[2] == [i+1,j-1] and arr[3] == [i+1,j]:
        return 4
    elif arr[1] == [i+1,j-1] and arr[2] == [i+1,j] and arr[3] == [i+1,j+1]:
        return 5
    else:
        return 0
    

def solution(board):
    answer = 0
    block = [[] for i in range(201)]
    check = list()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                num = board[i][j]
                block[num].append([i,j])
                if len(block[num]) == 4 and form(block[num]):
                    check.append((num,form(block[num])))
                    
    #print(block)
    print(check)
                    
    for i in range(len(check)):
        flag = True
        if check[i][1] == 1:
            for j in range(block[check[i][0]][2][0]):
                if board[j][block[check[i][0]][2][1]] != 0:
                    flag = False
                    break
                if board[j][block[check[i][0]][3][1]] != 0:
                    flag = False
                    break
            if flag:
                answer += 1
                for i in block[check[i][0]]:
                    board[i[0]][i[1]] = 0
                    
        elif check[i][1] == 2:
            for j in range(block[check[i][0]][2][0]):
                if board[j][block[check[i][0]][2][1]] != 0:
                    flag = False
                    break
            if flag:
                answer += 1
                for i in block[check[i][0]]:
                    board[i[0]][i[1]] = 0
                    
        elif check[i][1] == 3:
            for j in range(block[check[i][0]][2][0]):
                if board[j][block[check[i][0]][3][1]] != 0:
                    flag = False
                    break
            if flag:
                answer += 1
                for i in block[check[i][0]]:
                    board[i[0]][i[1]] = 0
                    
        elif check[i][1] == 4:
            for j in range(block[check[i][0]][2][0]):
                if board[j][block[check[i][0]][1][1]] != 0:
                    flag = False
                    break
                if board[j][block[check[i][0]][2][1]] != 0:
                    flag = False
                    break
            if flag:
                answer += 1
                for i in block[check[i][0]]:
                    board[i[0]][i[1]] = 0
                    
        elif check[i][1] == 5:
            for j in range(block[check[i][0]][2][0]):
                if board[j][block[check[i][0]][1][1]] != 0:
                    flag = False
                    break
                if board[j][block[check[i][0]][3][1]] != 0:
                    flag = False
                    break
            if flag:
                answer += 1
                for i in block[check[i][0]]:
                    board[i[0]][i[1]] = 0
                    
    print(board)
    return answer