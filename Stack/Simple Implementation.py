class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.sizeStack = 0

    def size(self):
        return self.sizeStack
    
    def push(self, val):
        self.stack.append(val)
        self.top += 1
        self.sizeStack += 1

    def pop(self):
        if self.isEmpty() == False: return -1
        popped = self.stack[self.top]
        self.top -= 1
        self.sizeStack -= 1
        return popped

    def isEmpty(self):
        return True if self.stack else False

    def display(self):
        for i in range(self.sizeStack):
            print(self.stack[i], end=" ")

    
s = Stack()
s.push(1)
s.push(2)
s.push(5)
s.push(10)
print(s.pop())
print(s.isEmpty())
s.display()