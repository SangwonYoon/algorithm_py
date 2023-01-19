def convert(char):
    if ord(char) <= 78:
        return ord(char) - 65
    else:
        return 91 - ord(char)

def solution(name):
    answer = 0
    lr = 19
    
    for idx, char in enumerate(name):
        answer += convert(char)
        lr = min(lr, idx*2 + len(name[idx+1:].lstrip("A")), len(name[idx+1:].lstrip("A"))*2 + idx)
    
    return answer + lr