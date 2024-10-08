class MyHash:
    def __init__(self, x) -> None:
        self.table = [[] for i in range(x)]
        self.BUCKET = x

    def insert(self, x):
        i = x % self.BUCKET
        self.table[i].append(x)

    def remove(self, x):
        i = x % self.BUCKET
        if x in self.table[i]:
            self.table[i].remove(x)

    def search(self, x):
        i = x % self.BUCKET
        return x in self.table[i]
h = MyHash(7)
h.insert(50)
h.insert(21)
h.insert(17)
h.insert(58)
print(h.search(21))
h.remove(58)