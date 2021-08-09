def solution(citations):
    citations.sort(reverse = True)
    num = max(citations)
    i = 0
    while(i <= len(citations)):
        if i == len(citations) or num > citations[i]:
            if num <= i:
                return num
            else:
                num -= 1
                i -= 1
                
        i += 1