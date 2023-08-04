# 2239번

import sys

def is_valid(cell, x, y, num):
    for i in range(9):
        if cell[i][y] == num:
            return False
        if cell[x][i] == num:
            return False

    if x < 3:
        for i in range(3):
            if y < 3:
                for j in range(3):
                    if cell[i][j] == num:
                        return False
            elif y < 6:
                for j in range(3, 6):
                    if cell[i][j] == num:
                        return False
            else:
                for j in range(6, 9):
                    if cell[i][j] == num:
                        return False
    elif x < 6:
        for i in range(3, 6):
            if y < 3:
                for j in range(3):
                    if cell[i][j] == num:
                        return False
            elif y < 6:
                for j in range(3, 6):
                    if cell[i][j] == num:
                        return False
            else:
                for j in range(6, 9):
                    if cell[i][j] == num:
                        return False
    else:
        for i in range(6, 9):
            if y < 3:
                for j in range(3):
                    if cell[i][j] == num:
                        return False
            elif y < 6:
                for j in range(3, 6):
                    if cell[i][j] == num:
                        return False
            else:
                for j in range(6, 9):
                    if cell[i][j] == num:
                        return False
    return True

def printcell(cell):
    for i in range(9):
        for j in range(9):
            print(cell[i][j], end = "")
        print("")
    sys.exit()


def sudoku(cell, x, y):
    if cell[x][y] != 0:
        if x == 8 and y == 8:
            printcell(cell)
        elif y == 8:
            sudoku(cell, x+1, 0)
        else:
            sudoku(cell, x, y+1)
    else:
        for i in range(1, 10):
            if is_valid(cell, x, y, i):
                cell[x][y] = i
                if x == 8 and y == 8:
                    printcell(cell)
                elif y == 8:
                    sudoku(cell, x+1, 0)
                else:
                    sudoku(cell, x, y+1)
                cell[x][y] = 0

cell = []
for i in range(9):
    temp = list(map(int, list(input().strip())))
    cell.append(temp)

sudoku(cell, 0, 0)