from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    br = deque(bridge)
    tr = deque(truck_weights)
    answer = 0
    cnt = 0
    number_of_trucks = len(tr)
    wt = 0
    
    while(cnt != number_of_trucks):
        answer += 1
        passed = br.pop()
        if(passed != 0):
            cnt += 1
            wt -= passed
        if(len(tr) > 0):
            if(tr[0] + wt <= weight):
                new_truck = tr.popleft()
                br.appendleft(new_truck)
                wt += new_truck
            else:
                br.appendleft(0)
        else:
            br.appendleft(0)
            
    return answer