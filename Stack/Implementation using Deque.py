from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
        self.top = -1
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.top += 1
        self.size += 1

    def pop(self):
        if self.isEmpty() == True: return -1
        popped = self.stack[-1]
        self.top -= 1
        self.size -= 1
        return popped
    
    def isEmpty(self):
        return self.size == 0
    
    def display(self):
        for i in range(self.size):
            print(self.stack[i], end=" ")

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.isEmpty())
s.display()