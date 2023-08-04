from heapq import heappop, heappush

def solution(jobs):
    try:
        answer = 0
        t = 0
        jobs.sort(key = lambda x : x[0])
        idx = 0
        heap = []

        while heap or idx < len(jobs):
            while idx < len(jobs) and jobs[idx][0] <= t:
                heappush(heap, [jobs[idx][1], jobs[idx][0]])
                idx += 1
            if heap:
                temp = heappop(heap)
                t += temp[0]
                answer += t - temp[1]
            else:
                if idx < len(jobs):
                    t = jobs[idx][0]

        return answer // len(jobs)
    except IndexError as e:
        print(e)