#1620번

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

pokemon_name = {}
pokemon_num = {}

for i in range(N):
    name = input().rstrip()
    pokemon_name[name] = i+1
    pokemon_num[i+1] = name

for i in range(M):
    question = input().rstrip()
    if ord(question[0]) >= 48 and ord(question[0]) <= 57:
        print(pokemon_num[int(question)])
    else:
        print(pokemon_name[question])