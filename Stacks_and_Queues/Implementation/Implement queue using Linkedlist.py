class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.start = self.end = None
        self.curSize = 0

    def push(self, x):
        newNode = Node(x)
        if self.start is None:
            self.start = self.end = newNode
        else:
            self.end.next = newNode
            self.end = newNode
        self.curSize += 1


    def pop(self):
        if self.start is None:
            return -1

        if self.start.next is None:
            popped = self.start.data
            temp = self.start
            self.start = self.end = None
            del temp
            self.curSize -= 1
            return popped
        else:
            popped = self.start.data
            temp = self.start
            self.start = self.start.next
            del temp
            self.curSize -= 1
            return popped

    def peek(self):
        if self.start is None:
            return -1
        return self.start.data
     

    def isEmpty(self):
        return self.curSize == 0