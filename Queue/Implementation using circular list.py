class Queue:
    def __init__(self, c):
        self.q = []
        self.capacity = c
        self.front = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity: return
        else:
            rear = (self.front + self.size - 1) % self.capacity
            rear = (rear + 1) % self.capacity
            self.q.append(x)
            self.size += 1

    def dequeue(self):
        if self.size == 0: return
        else:
            res = self.q[self.front]
            self.front += 1 % self.capacity
            self.size -= 1
            return res

    def getFront(self):
        if self.size == 0: return None
        return self.q[self.front]
    def getRear(self):
        if self.size == 0: return None
        rear = (self.front + self.size - 1) % self.capacity
        return self.q[rear]


q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.getFront())
print(q.getRear())