# 2342번

import sys

input = sys.stdin.readline


def update(key, value, new_dp):
    if key in new_dp:
        if new_dp[key] > value:
            new_dp[key] = value
    else:
        new_dp[key] = value


adjacent = {1: (2, 4), 2: (1, 3), 3: (2, 4), 4: (1, 3)}

commands = list(map(int, input().split()))[:-1]
dp = {0: 0}

for command in commands:
    new_dp = {}
    for key in dp.keys():
        l, r = key // 10, key % 10
        if l == command or r == command:
            update(key, dp[key] + 1, new_dp)
            continue

        if l == 0:
            new_key = command * 10 + r if command < r else r * 10 + command
            update(new_key, dp[key] + 2, new_dp)

            if r == 0:
                continue

            new_key = command
            if command in adjacent[r]:
                update(new_key, dp[key] + 3, new_dp)
            else:
                update(new_key, dp[key] + 4, new_dp)
        else:
            new_key = command * 10 + r if command < r else r * 10 + command
            if command in adjacent[l]:
                update(new_key, dp[key] + 3, new_dp)
            else:
                update(new_key, dp[key] + 4, new_dp)

            new_key = command * 10 + l if command < l else l * 10 + command
            if command in adjacent[r]:
                update(new_key, dp[key] + 3, new_dp)
            else:
                update(new_key, dp[key] + 4, new_dp)

    dp = new_dp

print(min(dp.values()))
