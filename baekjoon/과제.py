# 13904번

import sys
input = sys.stdin.readline

N = int(input())
assign = {}

for _ in range(N):
    d, w = map(int, input().split())
    if d not in assign:
        assign[d] = [w]
    else:
        assign[d].append(w)

result = []
days = max(assign.keys())

for i in range(1, days + 1):
    if i not in assign:
        result.append(0)
    else:
        assign[i].sort(reverse = True)
        result.append(assign[i][0])
        for j in range(1, len(assign[i])):
            if min(result) < assign[i][j]:
                result[result.index(min(result))] = assign[i][j]
            else:
                break

print(sum(result))