answer = -1
a = 0
b = 0
visited = []

def travel(node, graph, num):
    global a, b, visited
    visited[node] = 1
    if num == 1:
        a += 1
    else:
        b += 1
        
    temp = graph[node]
    for i in range(len(temp)):
        if not visited[temp[i]]:
            travel(temp[i], graph, num)
    

def solution(n, wires):
    global a, b, visited, answer
    for i in range(n-1):
        a = 0
        b = 0
        temp = wires[:i] + wires[i+1:]
        graph = [[] for _ in range(n)]
        for wire in temp:
            graph[wire[0]-1].append(wire[1]-1)
            graph[wire[1]-1].append(wire[0]-1)

        visited = [0] * n
        travel(0, graph, 1)

        idx = visited.index(0)
        travel(idx, graph, 2)

        if answer == -1 or abs(a-b) < answer:
            answer = abs(a-b)
            
    return answer
        