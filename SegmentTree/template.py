class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, arr)
        
    def build(self, i, l, r, arr):
        if l == r:
            self.tree[i] = arr[l]
            return
        
        mid = (l + r) >> 1
        self.build(2 * i + 1, l, mid, arr)
        self.build(2 * i + 2, mid + 1, r, arr)
        
        self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]
        
    def query(self, i, l, r, start, end):
        if r < start or end < l:
            return 0
            
        if l >= start and r <= end:
            return self.tree[i]
            
        mid = (l + r) >> 1
        
        return self.query(2 * i + 1, l, mid, start, end) + self.query(2 * i + 2, mid + 1, r, start, end)
        