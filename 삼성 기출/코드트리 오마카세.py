import bisect
import sys

input = sys.stdin.readline

class Query:
    def __init__(self, cmd, time, name):
        self.cmd = cmd
        self.time = time
        self.name = name

# 명령 집합
queries = []

# 초밥들  name: [(time, x), ...]
sushies = {}

# 사람들  name: [x, last_sushi_time]
people = {}

L, Q = map(int, input().split())

for _ in range(Q):
    command = input().split()
    x, n = -1, -1
    name = ""

    if command[0] == "100": # 초밥 추가
        cmd, time, x, name = command
        time, x = map(int, [time, x])
        if name in people: # 이미 사람이 들어와 있는 경우
            seat = people[name][0]
            time_to_eat = time + (seat - x) % L
            queries.append(Query("111", time_to_eat, name)) # 초밥 제거
            if people[name][1] < time_to_eat: # 마지막으로 초밥을 먹은 시간 기록
                    people[name][1] = time_to_eat
        else: # 사람이 아직 안 들어온 경우
            if name in sushies:
                sushies[name].append((time, x))
            else:
                sushies[name] = [(time, x)]

    elif command[0] == "200": # 사람 들어옴
        cmd, time, x, name, n = command
        time, x, n = map(int, [time, x, n])
        people[name] = [x, -1]
        if name in sushies: # 초밥 벨트 위에 본인의 초밥이 있는 경우
            for prev_t, prev_x in sushies[name]:
                time_to_eat = time + (x - (prev_x + time - prev_t) % L) % L
                queries.append(Query("111", time_to_eat, name)) # 초밥 제거
                if people[name][1] < time_to_eat: # 마지막으로 초밥을 먹은 시간 기록
                    people[name][1] = time_to_eat
    
    else: # 사진 찍기
        cmd, time = command
        time = int(time)

    queries.append(Query(cmd, time, name))

for name, (_, last_sushi_time) in people.items():
    queries.append(Query("222", last_sushi_time, name)) # 사람 나감

queries.sort(key = lambda x : (x.time, x.cmd))

num_of_person = 0
num_of_sushi = 0

for q in queries:
    cmd = q.cmd
    if cmd == "100":
        num_of_sushi += 1
    elif cmd == "111":
        num_of_sushi -= 1
    elif cmd == "200":
        num_of_person += 1
    elif cmd == "222":
        num_of_person -= 1
    else:
        print(num_of_person, num_of_sushi)