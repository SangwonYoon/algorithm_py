# bfs 알고리즘

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    q = [[0,0,1]]
    
    while len(q):
        x, y, cnt = q.pop(0)
        for i in range(4):
            dx = x + movement[i][0]
            dy = y + movement[i][1]
            if dx >= 0 and dx < m and dy >= 0 and dy < n and maps[dy][dx] == 1:
                if dx == m-1 and dy == n-1:
                    return cnt+1
                maps[dy][dx] = 0
                q.append([dx, dy, cnt+1])
                
    return -1