class ArrayStack:
    def __init__(self, size = 1000):
        self.array_stack = [0] * size
        self.topp = -1
        self.capacity = size

    def push(self, x):
        if self.topp == self.capacity - 1:
            print("Stack overflow")
            return
        self.topp += 1
        self.array_stack[self.topp] = x

    def pop(self):
        if self.topp == -1:
            print("Stack is empty")
            return -1
        popped = self.array_stack[self.topp]
        self.topp -= 1
        return popped

    def top(self):
        if self.topp == -1:
            print("Stack is empty")
            return -1 
        return self.array_stack[self.topp]

    def isEmpty(self):
        return self.topp == -1
