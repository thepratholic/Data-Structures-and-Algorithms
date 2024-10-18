
from heapq import heappush, heappop, heapify
# A class for Min Heap
class MinHeap:

    def __init__(self):
        self.heap = []
    def parent(self, i):
        return self.heap[(i-1)/2]

    def leftChild(self, i):
        return self.heap[(2 * i) + 1]
    def rightChild(self, i):
        return self.heap[(2 * i) + 2]

    def insertKey(self, k):
        heappush(self.heap, k)

    def extractMin(self):
        return heappop(self.heap)


    def getMin(self):
        return self.heap[0]

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin())
print(heapObj.getMin())
print(heapObj.getMin())