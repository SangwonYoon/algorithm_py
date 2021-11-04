def solution(n):
    tri = [[0 for i in range(j)] for j in range(1,n+1)]
    form = 1
    i,j = 0,0
    num = 1
    while num <= n*(n+1)/2:
        tri[i][j] = num
        num += 1
        if form == 1:
            if i+1 < n and tri[i+1][j] == 0:
                i += 1
            else:
                form = 2
                j += 1
                
        elif form == 2:
            if j+1 < n and tri[i][j+1] == 0:
                j += 1
            else:
                form = 3
                i -= 1
                j -= 1
                
        elif form == 3:
            if tri[i-1][j-1] == 0:
                i -= 1
                j -= 1
            else:
                form = 1
                i += 1
                
    return sum(tri,[])