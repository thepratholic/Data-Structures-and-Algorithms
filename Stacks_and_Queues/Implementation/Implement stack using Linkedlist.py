class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.topp = None
        self.curSize = 0

    def push(self, x):
        newNode = Node(x)

        newNode.next = self.topp
        self.topp = newNode
        self.curSize += 1

    def pop(self):
        if self.topp is None:
            return -1
        popped = self.topp.data
        temp = self.topp
        self.topp = self.topp.next
        del temp
        self.curSize -= 1
        return popped

    def top(self):
        if self.topp is None:
            return -1
        return self.topp.data     

    def isEmpty(self):
        return self.curSize == 0
