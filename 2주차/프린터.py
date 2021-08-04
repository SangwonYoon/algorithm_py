from collections import deque

def solution(prior, location):
    pr = deque(prior)
    cnt = 0
    while(True):
        if pr[0] == max(pr):
            pr.popleft()
            cnt += 1
            if location == 0:
                return cnt
            else:
                location -= 1
        else:
            pr.append(pr.popleft())
            if location == 0:
                location = len(pr) - 1
            else:
                location -= 1