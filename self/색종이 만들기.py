#2630번

import sys
input = sys.stdin.readline

def divide_paper(arr,x,y,n):
    result = []
    for i in range(x,x+n):
        temp = []
        for j in range(y,y+n):
            temp.append(arr[i][j])
        result.append(temp)
    return result

def divide(arr):
    n = len(arr[0]) // 2
    result = []
    result.append(divide_paper(arr,0,0,n))
    result.append(divide_paper(arr,n,0,n))
    result.append(divide_paper(arr,0,n,n))
    result.append(divide_paper(arr,n,n,n))
    return result

def check(arr):
    n = len(arr[0])
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[0][0]:
                return False
    return True


N = int(input())
blue = 0
white = 0
paper = [[list(map(int,input().split())) for i in range(N)]]

while len(paper) > 0:
    for i in range(len(paper)-1,-1,-1):
        if check(paper[i]):
            if paper[i][0][0] == 0:
                white += 1
            else:
                blue += 1
            paper.pop(i)
        else:
            result = divide(paper.pop(i))
            paper.insert(i,result[3])
            paper.insert(i,result[2])
            paper.insert(i,result[1])
            paper.insert(i,result[0])

print(white)
print(blue)