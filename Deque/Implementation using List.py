class Deque:
    def __init__(self, c):
        self.deque = [None] * c
        self.capacity = c
        self.sz = 0
        self.front = 0

    def insertRear(self, data):
        if self.sz == self.capacity: return
        rear = (self.front + self.sz) % self.capacity
        self.deque[rear] = data
        self.sz += 1

    def deleteRear(self):
        if self.sz == 0: return None  # Deque is empty
        rear = (self.front + self.sz - 1) % self.capacity
        res = self.deque[rear]
        # self.deque[rear] = None  # Optional: Clear the value
        self.sz -= 1
        return res

    def insertFront(self, d):
        if self.sz == self.capacity: return None
        else:
            self.front = (self.front - 1) % self.capacity
            self.deque[self.front] = d
            self.sz += 1

    def deleteFront(self):
        if self.sz == 0: return None
        else:
            res = self.deque[self.front]
            self.front = (self.front + 1) % self.capacity
            self.sz -= 1
            return res

    def size(self):
        return self.sz

    def getFront(self):
        if self.sz == 0: return None
        else: return self.deque[self.front]

    def getRear(self):
        if self.sz == 0: return None
        else:
            rear = (self.front + self.sz - 1) % self.capacity
            return self.deque[rear]

d = Deque(5)
d.insertRear(10)
d.insertRear(20)
d.insertRear(30)
d.insertFront(5)
print(d.deleteFront())
print(d.deleteRear())
print(d.getFront())
print(d.getRear())