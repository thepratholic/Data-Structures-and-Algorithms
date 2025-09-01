class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_val = val
            return
        
        if val > self.min_val:
            self.stack.append(val)
        else:
            self.stack.append(2 * val - self.min_val)
            self.min_val = val


    def pop(self) -> None:
        if not self.stack:
            return 

        popped = self.stack.pop()

        if popped < self.min_val:
            self.min_val = (2 * self.min_val - popped)

    def top(self) -> int:
        if not self.stack:
            return

        if self.min_val > self.stack[-1]:
            return self.min_val
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
       