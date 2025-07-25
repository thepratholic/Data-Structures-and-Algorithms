from queue import Queue

class QueueStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        length = self.q.qsize()
        self.q.put(x)

        for i in range(length):
            self.q.put(self.q.get())

        

    def pop(self):
        if self.q.empty():
            return -1

        popped = self.q.queue[0]
        self.q.get()
        return popped


    def top(self):
        if self.q.empty():
            return -1
        return self.q.queue[0]
     

    def isEmpty(self):
        return self.q.empty()