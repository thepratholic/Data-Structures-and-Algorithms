class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Queue:
    def __init__(self):
        self.rear = self.front = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def getRear(self):
        return self.rear.data
    def getFront(self):
        return self.front.data
    
    def enqueue(self, d):
        temp = Node(d)
        if self.rear is None:
            self.rear = self.front = temp
            return 
        else:
            self.rear.next = temp
            self.rear = temp
        self.size += 1

    def dequeue(self):
        if self.isEmpty(): return None
        temp = self.front
        self.front = self.front.next
        if self.front is None: self.rear = None
        self.size -= 1

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.getFront())
print(q.getRear())
