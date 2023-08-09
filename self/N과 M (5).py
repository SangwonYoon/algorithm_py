# 15654번

def solution(nums, m, visited, result):
    if len(result) == m:
        print(*result)
    
    else:
        for idx in range(len(nums)):
            if not visited[idx]:
                result.append(nums[idx])
                visited[idx] = 1
                solution(nums, m, visited, result)
                result.pop()
                visited[idx] = 0

_, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0] * len(nums)
solution(nums, M, visited, [])