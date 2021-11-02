def solution(n, t, m, timetable):
    new_tt = list()
    for i in timetable:
        a,b = map(int,i.split(":"))
        new_tt.append(a*60+b)
    new_tt.sort()

    bus = [(540+t*i) for i in range(n)]
    for i in range(len(bus)):
        if i != len(bus) - 1:
            seat = m
            while(seat > 0):
                if len(new_tt) > 0 and new_tt[0] <= bus[i]:
                    new_tt.pop(0)
                    seat -= 1
                else:
                    break
        else:
            seat = m
            last = bus[i]
            while(seat > 0):
                if len(new_tt) > 0 and new_tt[0] <= bus[i]:
                    last = new_tt.pop(0)
                    seat -= 1
                else:
                    break
            if seat == 0:
                answer = last-1
            else:
                answer = bus[i]

    hour = answer//60
    answer -= hour*60
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    minute = answer
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)


    return hour + ":" + minute