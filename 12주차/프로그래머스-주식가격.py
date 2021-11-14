from collections import deque

def solution(prices):
    answer = []
    p = deque(prices)
    while len(p) > 0:
        temp = p.popleft()
        cnt = 1
        for i in p:
            if temp > i:
                answer.append(cnt)
                break
            cnt += 1
        else:
            answer.append(cnt-1)
    return answer