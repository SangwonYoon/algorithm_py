import math

def solution(progresses, speeds):
    date = list()
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i]) / speeds[i]))

    result = list()
    idx = 0

    while(idx < len(date)):
        temp = date[idx]
        cnt = 1
        while(idx+1 < len(date) and date[idx+1] <= temp):
            idx += 1
            cnt += 1
        result.append(cnt)
        idx += 1
    
    return result

