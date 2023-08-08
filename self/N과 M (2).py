# 15650번

def solution(n, m, result, last_num):
    if last_num == n-(m-(len(result)+1)):
        if result:
            last_num = result.pop()
            solution(n, m, result, last_num)
        else:
            return

    elif m == len(result):
        print(*result)
        last_num = result.pop()
        solution(n, m, result, last_num)
    
    else:
        result.append(last_num+1)
        solution(n, m, result, last_num+1)


N, M = map(int, input().split())

result = []
solution(N, M, result, 0)


# n, m = map(int, input().split())

# result = []
# def solution(num):
#     if len(result) == m:
#         print(*result)
#         return 
#     for i in range(num,n+1):
#         result.append(i)
#         solution(i+1)
#         result.pop()
            
# solution(1)