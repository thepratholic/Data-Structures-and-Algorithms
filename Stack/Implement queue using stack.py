from queue import LifoQueue

class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, x):
        self.input.put(x)

    def pop(self):
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        popped = self.output.get()
        return popped
    
    def getFront(self):
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        return self.output.queue[-1]

    def size(self):
        return len(self.input) + len(self.output)
    
q = Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
print(q.pop())
print(q.getFront())