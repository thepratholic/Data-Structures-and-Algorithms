class Queue:
    def __init__(self, c):
        self.queue = []
        self.rear = 0
        self.front = -1
        self.qsize = 0
        self.capacity = c

    def enqueue(self, data):
        if self.capacity == self.rear: print("Queue is full\n")
        self.queue.append(data)
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear: print("Queue is empty\n")
        else:
            d = self.queue.pop(0)
            self.front += 1
            return d

    def queueDisplay(self):
        if self.front == self.rear: print("Queue is empty\n")
        for i in self.queue:
            print(i, end=" ")

    def getFront(self):
        if self.front == self.rear: print("Queue is empty\n")
        return self.queue[0]
    
    
q = Queue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
# q.queueDisplay()
print(q.getFront())
