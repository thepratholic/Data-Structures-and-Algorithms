from queue import LifoQueue

class Stack:
    def __init__(self):
        self.stack = LifoQueue(maxsize=3)
        self.top = -1
        self.size = self.stack.qsize()

    def push(self, data):
        if self.size == 3:
            return
        self.stack.put(data)
        self.top += 1

    def isEmpty(self):
        return self.stack.empty()
    
    def pop(self):
        if self.isEmpty() == True: return -1
        popped = self.stack.get()
        self.top -= 1
        return popped


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.isEmpty())
