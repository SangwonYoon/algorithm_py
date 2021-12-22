def check(i): #퀸이 서로 공격할 수 없는 위치인지 확인
    for k in range(i):
        if (chess[i] == chess[k] or chess[i] + (k-i) == chess[k] or chess[i] + (i-k) == chess[k]):
            return False
    return True

def queen(n): # 체스판의 n번째 행에 queen을 놓는 함수
    global cnt

    if n == N: # 여기까지 도착하면 체스판에 N개의 퀸을 놓는데 성공
        cnt += 1
    else:
        for i in range(N):
            chess[n] = i
            if check(n):
                queen(n+1) # 다음 행에 퀸을 놓는다.

N = int(input())
chess = [0 for i in range(N)] # 퀸의 위치 : (index, 해당 index의 값)
cnt = 0

queen(0) # 0번째 행부터 퀸을 놓기 시작

print(cnt)