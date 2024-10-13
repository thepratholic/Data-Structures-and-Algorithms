from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()

    def push(self, d):
        s = len(self.q1)
        self.q1.append(d)
        for i in range(s):
            self.q1.append(self.q1.popleft())


    def pop(self):
        if self.q1:
            return self.q1.popleft()

    def top(self):
        if self.q1:
            return self.q1[0]

    def size(self):
        return len(self.q1)

    def display(self):
        if self.q1:
            for i in range(self.size()):
                print(self.q1[i], end=" ")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.top())
s.display()