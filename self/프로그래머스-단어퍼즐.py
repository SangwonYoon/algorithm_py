def solution(strs, t):
    memo = [30000 for i in range(len(t)+1)] #문자열 길이 20000 이하 -> result도 20000 이하
    memo[0] = 0
    
    for i in range(1,len(memo)):
        for j in range(1,6): #단어 조각 길이
            if i - j < 0:
                break
            if t[i-j:i] in strs:
                memo[i] = min(memo[i],memo[i-j]+1)
                
    if memo[-1] != 30000:
        return memo[-1]
    else:
        return -1