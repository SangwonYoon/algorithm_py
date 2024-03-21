# 17471번

import sys
from itertools import combinations


def is_connected(selected_locations, adjacent, visited):
    location1 = selected_locations[0]
    visited[location1-1] = 1
    dfs(selected_locations, location1, adjacent, visited, 1)

    location2 = visited.index(-1) + 1
    if location2 in selected_locations:
        return False

    visited[location2-1] = 2
    dfs(selected_locations, location2, adjacent, visited, 2)

    if -1 in visited:
        return False

    return True


def dfs(selected_locations, n, adjacent, visited, mark):
    visited[n-1] = mark
    adj = adjacent[n]

    if mark == 1:
        for location in adj:
            if visited[location-1] == -1 and location in selected_locations:
                dfs(selected_locations, location, adjacent, visited, 1)
    elif mark == 2:
        for location in adj:
            if visited[location-1] == -1 and location not in selected_locations:
                dfs(selected_locations, location, adjacent, visited, 2)


input = sys.stdin.readline

N = int(input())

answer = 100000

people = list(map(int, input().split()))
people.insert(0, -1)

adjacent = [[-1]]
for _ in range(N):
    temp = list(map(int, input().split()))
    temp.pop(0)
    adjacent.append(temp)

locations = [i for i in range(1, N+1)]
for n in range(1, N//2+1):
    for selected_locations in combinations(locations, n):
        visited = [-1 for _ in range(N)]
        if is_connected(selected_locations, adjacent, visited):
            a = 0
            b = 0
            for location in range(1, N+1):
                if location in selected_locations:
                    a += people[location]
                else:
                    b += people[location]
            if abs(a-b) < answer:
                answer = abs(a-b)

print(answer) if answer != 100000 else print(-1)
