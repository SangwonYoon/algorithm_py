#14500번

import sys
input = sys.stdin.readline

def tet(i,j): #ㅡ
    lst = list()
    total = 0
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i][j+3]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅣ
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅁ
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #7412 L
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+2][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #6321 」
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i-1][j+2]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #8963 ㄱ
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #4789 「
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #2369 」
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i-1][j+1] + matrix[i-2][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #6987 ㄱ
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+2]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #8741 「
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+2][j]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #4123 ㄴ
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #오른쪽 번개
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+2][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #1256
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i-1][j+1] + matrix[i-1][j+2]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #왼쪽 번개
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j-1] + matrix[i+2][j-1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #z
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+1][j+2]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅜ
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅏ
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+1][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅗ
    try:
        total = matrix[i][j] + matrix[i+1][j] + matrix[i+1][j-1] + matrix[i+1][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    total = 0 #ㅓ
    try:
        total = matrix[i][j] + matrix[i][j+1] + matrix[i-1][j+1] + matrix[i+1][j+1]
    except:
        pass
    finally:
        if total:
            lst.append(total)

    return lst



N, M = map(int,input().split())

matrix = list()

for i in range(N):
    matrix.append(list(map(int,input().split())))

array = list()
for i in range(N):
    for j in range(M):
        array += tet(i,j)

print(max(array))