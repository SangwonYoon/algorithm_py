def solution(clothes):
    c = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in c:
            c[clothes[i][1]] = [clothes[i][0]]
        else:
            c[clothes[i][1]].append(clothes[i][0])
    
    answer = 1
    for v in c.values():
        answer *= len(v)+1
    return answer-1