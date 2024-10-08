class MyHash:
    def __init__(self, cap):
        self.capacity = cap
        self.table = [-1 for i in range(cap)]
        self.size = 0

    def hash(self, val):
        return val % self.capacity
    
    def insert(self, val):
        if self.size == self.capacity: return False
        if self.search(val) == True: return False
        h = self.hash(val)
        i = h
        while self.table[i] not in (-1, -2):
            i = (i+1) % self.capacity
        self.table[h] = val
        self.size += 1
        return True

    
    def search(self, x):
        h = self.hash(x)
        i = h
        while self.table[i] != -1:
            if self.table[i] == x:
                return True
            i = (i+1) % self.capacity
            if i == h: return False
        return False
    
    def remove(self, val):
        if self.search(val) == False: return False
        h = self.hash(val)
        i = h
        while self.table[i] != -1:
            if self.table[i] == val:
                self.table[i] = -2
                return True
            i = (i+1) % self.capacity
        return False
h = MyHash(7)
h.insert(70)
h.insert(56)
print(h.search(56))
print(h.remove(56))
print(h.search(56))