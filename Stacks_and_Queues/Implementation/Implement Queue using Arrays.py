class ArrayQueue:
    def __init__(self):
        self.queue = [0] * 10
        self.start = self.end = -1
        self.curSize = 0
        self.capacity = 10

    def push(self, x):
        if self.curSize == self.capacity:
            print("Queue is full\nExiting")
            exit(1)

        if self.end == -1:
            self.start = self.end = 0
        
        else:
            self.end = (self.end + 1) % self.capacity
        self.queue[self.end] = x
        self.curSize += 1

    def pop(self):
        if self.curSize == 0:
            print("Queue is Empty\nExiting")
            exit(1)

        popped = self.queue[self.start]
        if self.curSize == 1:
            self.start = self.end = -1

        else:
            self.start = (self.start + 1) % self.capacity

        self.curSize -= 1
        return popped


    def peek(self):
        if self.curSize == 0:
            print("Queue is Empty\nExiting")
            exit(1)

        return self.queue[self.start]

     

    def isEmpty(self):
        return self.curSize == 0