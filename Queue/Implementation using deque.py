from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
        self.front = self.rear = 0
        self.size = 0
    def enqueue(self, d):
        self.queue.append(d)
        self.rear += 1
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty\n")
        else:
            popped = self.queue[self.front]
            self.front += 1
            self.size -= 1
            return popped

    def Size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def getFront(self):
        if self.front == self.rear:
            print("Queue is empty\n")
        else:
            return self.queue[self.front]

    def getRear(self):
        if self.front == self.rear:
            print("Queue is empty\n")
        else:
            return self.queue[self.rear-1]

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.getFront())
print(q.getRear())
print(q.Size())