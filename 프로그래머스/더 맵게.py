from heapq import heappush, heappop, heapify

# def heapify(heap, idx):
#     while 2*idx < len(heap):
#         if 2*idx+1 <= len(heap)-1:
#             if heap[2*idx] < heap[2*idx+1]:
#                 smaller = 2*idx
#             else:
#                 smaller = 2*idx+1
#         else:
#             smaller = 2*idx
#         if heap[idx] > heap[smaller]:
#             heap[idx], heap[smaller] = heap[smaller], heap[idx]
#             idx = smaller
#         else:
#             break
            
def bubbleup(heap, idx):
    while idx > 1:
        if heap[idx] < heap[int(idx/2)]:
            heap[idx], heap[int(idx/2)] = heap[int(idx/2)], heap[idx]
            idx = int(idx/2)
        else:
            break

def solution(scovil, K):
    answer = 0
    heapify(scovil)
    while len(scovil):
        a = heappop(scovil)
        if a >= K:
            return answer
        elif not len(scovil):
            return -1
        b = heappop(scovil)
        heappush(scovil, a + 2*b)
        answer += 1
        