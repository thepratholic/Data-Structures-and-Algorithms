from queue import LifoQueue

class StackQueue:
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


    def peek(self):
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())

        return self.output.queue[-1]
     

    def isEmpty(self):
        return self.input.empty() and self.output.empty()
