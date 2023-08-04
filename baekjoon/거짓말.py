# 1043번

import sys
input = sys.stdin.readline

def spread(graph, person):
    for i in range(len(graph[person])):
        if graph[person][i] == 1 and i not in fact:
            fact.append(i)
            spread(graph, i)

N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

tmp = list(map(int, input().split()))
f = tmp[0]
fact = list(map(lambda x : x-1, tmp[1:]))
party = []

for i in range(M):
    temp = list(map(int, input().split()))
    p = temp[0]
    people = list(map(lambda x: x-1, temp[1:]))
    party.append(people[0])
    for a in range(p):
        for b in range(a):
            graph[people[a]][people[b]] = 1
            graph[people[b]][people[a]] = 1

for person in fact:
    spread(graph, person)

answer = 0
for k in party:
    if k not in fact:
        answer += 1

print(answer)