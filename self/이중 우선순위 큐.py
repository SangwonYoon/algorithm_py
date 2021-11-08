#7662번

import sys
import heapq
input = sys.stdin.readline

def sync(Q): # 두 힙을 동기화시켜주는 함수, 해당 값이 반대편 힙에서 존재하지 않으면 이쪽 힙에서도 삭제
    while Q and not id[Q[0][1]]:
        heapq.heappop(Q)

for i in range(int(input())):
    maxQ = list() # 최대 힙
    minQ = list() # 최소 힙
    id = [False] * 1000001 # 최소힙과 최대힙을 서로 동기화시켜 주기 위해 반대편 힙에서 존재하는지 저장하는 배열
    for j in range(int(input())):
        op, num = input().split()
        num = int(num)
        if op == "I":
            heapq.heappush(maxQ,(-num, j)) # heapq 모듈은 기본적으로 최소힙을 지원하므로 최대힙을 만들기 위해서는 튜플을 힙에 넣으면 튜플의 첫 원소를 기준으로 최소힙을 만든다는 부분을 이용해 집어넣는 값에 -를 붙인다.
            heapq.heappush(minQ,(num, j)) # 두 힙을 동기화 하기 위해 튜플의 두번째 원소는 고유한 아이디값을 집어넣는다.
            id[j] = True 
        elif num == 1:
            sync(maxQ) # 힙에서 값을 제거하기 전에 제거하려는 값이 이미 반대편 힙에서 삭제됐을 수 있으므로 동기화를 진행한다. 삭제한 후 동기화를 하는 경우에는 선형 탐색으로 아이디 값을 가진 원소를 찾아야하는 것에 비해, 삭제하려는 값이 반대편 힙에서 삭제되었는지 확인만 해주는 경우가 훨씬 빠르다.
            if maxQ:
                id[heapq.heappop(maxQ)[1]] = False # 값을 삭제해준 뒤 해당 값이 삭제되었음을 id 배열의 값을 False로 바꿔줘서 알린다.
            
        else:
            sync(minQ)
            if minQ:
                id[heapq.heappop(minQ)[1]] = False

    sync(maxQ) # 출력하기 전 출력하려는 값들이 반대편 힙에서 삭제된 값일 수 있으므로 동기화해준다.
    sync(minQ)
           

    if len(maxQ) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(maxQ)[0], heapq.heappop(minQ)[0])
