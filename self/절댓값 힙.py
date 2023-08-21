# 11286번

import sys

input = sys.stdin.readline

class Heap:
    h = []

    def pop(self):
        if self.h:
            self.h[0], self.h[-1] = self.h[-1], self.h[0]
            output = self.h.pop()
            if len(self.h) > 1:
                self.heapify()
            return output
        else:
            return 0

    def push(self, num):
        self.h.append(num)
        if len(self.h) > 1:
            child = len(self.h)-1
            while child > 0:
                parent = (child-1) // 2
                if abs(self.h[child]) < abs(self.h[parent]) or (abs(self.h[child]) == abs(self.h[parent]) and self.h[child] < self.h[parent]):
                    self.h[child], self.h[parent] = self.h[parent], self.h[child]
                    child = parent
                else:
                    break

    def heapify(self):
        parent = 0
        while len(self.h) > (parent+1)*2-1:
            child = (parent+1)*2-1
            if len(self.h) > child+1:
                if abs(self.h[child]) > abs(self.h[child+1]) or (abs(self.h[child]) == abs(self.h[child+1]) and self.h[child] > self.h[child+1]):
                    child = child+1
            if abs(self.h[child]) < abs(self.h[parent]) or (abs(self.h[child]) == abs(self.h[parent]) and self.h[child] < self.h[parent]):
                self.h[parent], self.h[child] = self.h[child], self.h[parent]
                parent = child
            else:
                break

            

N = int(input())
heap = Heap()
for _ in range(N):
    n = int(input())
    if n == 0:
        print(heap.pop())
    else:
        heap.push(n)
