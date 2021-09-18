#11727번

def solution(n):
    sol.append(sol[n-1] + 2 * sol[n-2])

n = int(input())

sol = [0, 1, 3, 5]
for i in range(4,n+1):
    solution(i)
print(sol[n] % 10007)