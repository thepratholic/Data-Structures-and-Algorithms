import math as m
class MyMaxHeap:
    def __init__(self):
        self.heap = []
        i = 0
        while i >= 0:
            self.maxHeapify(i)
            i-=1

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return (2 * i) + 1

    def rightChild(self, i):
        return (2 * i) + 2

    def extract_max(self):
        if len(self.heap) == 0: return m.inf
        res = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.maxHeapify(0)
        return res

    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def maxHeapify(self, index):
        leftChild = self.leftChild(index)
        rightChild = self.rightChild(index)
        largest = index
        n = len(self.heap)
        if leftChild < n and self.heap[leftChild] > self.heap[largest]:
            largest = leftChild
        if rightChild < n and self.heap[rightChild] > self.heap[largest]:
            largest = rightChild
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxHeapify(largest)

    def deleteKey(self, index):
        n = len(self.heap)
        if index >= n: return
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        if index < len(self.heap):
            self.maxHeapify(index)

max_heap = MyMaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(15)
max_heap.insert(30)
max_heap.insert(25)
print("\nExtracted max:", max_heap.extract_max())