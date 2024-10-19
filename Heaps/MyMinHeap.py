import math
class MyMinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return i-1 // 2
    def leftChild(self, i):
        return 2*i + 1
    def rightChild(self, i):
        return 2*i + 2
    def extract_min(self):
        if len(self.heap) == 0: return math.inf
        mini = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        # self.minHeapify(0)
        return mini
    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap)

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
