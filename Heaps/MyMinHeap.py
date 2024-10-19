import math
class MyMinHeap:
    def __init__(self):
        self.heap = []
        i = len(self.heap) - 2 // 2
        while i >= 0:
            self.minHeapify(i)
            i -= 1

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
        self.minHeapify(0)
        return mini

    def minHeapify(self, index):
        leftChild = self.leftChild(index)
        rightChild = self.rightChild(index)
        smallest = index
        n = len(self.heap)
        if leftChild < n and self.heap[leftChild] < smallest:
            smallest = leftChild
        if rightChild < n and self.heap[rightChild] < smallest:
            smallest = rightChild
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.minHeapify(smallest)

    def insert(self, data):
        self.heap.append(data)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def decreaseKey(self, index, data):
        self.heap[index] = data
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            p = self.parent(index)
            self.heap[p], self.heap[index] = self.heap[index], self.heap[p]
            index = p

    def deleteKey(self, index):
        n = len(self.heap)
        if index >= n: return
        else:
            self.decreaseKey(index, -math.inf)
            self.extract_min()
