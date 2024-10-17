# A Python program to demonstrate common binary heap operations
  
# Import the heap functions from python library
from heapq import heappush, heappop, heapify 
  
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time
  
# A class for Min Heap
class MinHeap:
      
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return self.heap[(i-1)/2]
      
    def leftChild(self, i):
        return self.heap[(2 * i) + 1]
    def rightChild(self, i):
        return self.heap[(2 * i) + 2]
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]
  
# Driver pgoratm to test above function
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