class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class Deque:
    def __init__(self):
        self.front = self.rear = None
        self.sz = 0

    def insertRear(self, d):
        temp = Node(d)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz += 1

    def deleteRear(self):
        if self.rear.prev is None: return None
        else:
            res = self.rear.data
            self.rear = self.rear.prev
            self.rear.next = None
            return res
    
    def insertFront(self, d):
        temp = Node(d)
        if self.front is None:
            self.rear = temp
        else:
            temp.next = self.front
            self.front = self.front.prev
        self.front = temp
        self.sz += 1

    def deleteFront(self):
        if self.front is None: return None
        else:
            res = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res
    
    def getFront(self):
        if self.front:
            return self.front.data

    def getRear(self):
        if self.rear:
            return self.rear.data
    
    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0
    
dq = Deque()
dq.insertRear(10)
dq.insertRear(20)
dq.insertFront(5)
print(dq.deleteFront())
print(dq.getFront())
print(dq.getRear())