answer = 0

def permutation(dungeons, i, k):
    if i+1 == len(dungeons):
        global answer
        explore = exp(k, dungeons)
        if explore > answer:
            answer = explore
            
    for j in range(i, len(dungeons)):
        swap(dungeons, i, j)
        permutation(dungeons, i+1, k)
        swap(dungeons, i, j)

def swap(dungeons, i, j):
    dungeons[i], dungeons[j] = dungeons[j], dungeons[i]
    
def exp(k, dungeons):
    cnt = 0
    for dungeon in dungeons:
        if k >= dungeon[0]:
            cnt += 1
            k -= dungeon[1]
    return cnt

def solution(k, dungeons):
    permutation(dungeons, 0, k)
    return answer
    