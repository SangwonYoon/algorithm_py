def solution(n, arr1, arr2):
    answer = list()
    for i in range(n):
        answer.append(" "*n)
    for i in range(len(arr1)):
        temp = n-1
        while(temp >= 0):
            if(arr1[i] // 2**temp == 1):
                arr1[i] -= 2**temp
                answer[i] = answer[i][:n-1-temp] + '#' + answer[i][n-temp:]
            temp -= 1
    for i in range(len(arr2)):
        temp = n-1
        while(temp >= 0):
            if(arr2[i] // 2**temp == 1):
                arr2[i] -= 2**temp
                answer[i] = answer[i][:n-1-temp] + '#' + answer[i][n-temp:]
            temp -= 1
            
    return answer