#2407번

memo = [1,1,2]

def factorial(n):
    if len(memo) - 1 >= n:
        return memo[n]
    else:
        memo.append(factorial(n-1) * n)
        return memo[n]

n, m = map(int,input().split())
answer = factorial(n) // (factorial(m) * factorial(n-m))

print(answer)