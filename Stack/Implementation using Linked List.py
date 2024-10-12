import math as m

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.sizeOfStack = 0

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.sizeOfStack += 1

    def size(self):
        return self.sizeOfStack

    def top(self):
        if self.head is None:
            return m.inf
        return self.head.data

    def pop(self):
        if self.head is None:
            return m.inf
        res = self.head.data
        self.head = self.head.next
        self.sizeOfStack -= 1
        return res

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.top())
print(s.size())