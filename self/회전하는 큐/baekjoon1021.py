from collections import deque

N, M = map(int, input().split())
nums = list(map(int,input().split()))

q = deque([i for i in range(1,N+1)])
exist = [1 for i in range(1,N+1)]

cnt = 0
for i in nums:
    if q[0] == i:
        exist[q.popleft()-1] = 0
    elif i < q[0]:
        offset = sum(exist[i:q[0]])
        if offset <= len(q) // 2:
            cnt += offset
            q.rotate(offset)
            exist[q.popleft()-1] = 0
        else:
            cnt += len(q) - offset
            q.rotate(-len(q) + offset)
            exist[q.popleft()-1] = 0
    elif q[0] < i:
        offset = sum(exist[q[0]:i])
        if offset <= len(q) // 2:
            cnt += offset
            q.rotate(-offset)
            exist[q.popleft()-1] = 0
        else:
            cnt += len(q) - offset
            q.rotate(len(q) - offset)
            exist[q.popleft()-1] = 0

print(cnt)