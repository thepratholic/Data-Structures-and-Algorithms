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
    
    def update(self, idx, l, r, u_idx, u_val): # this is for single point update
        if l == r:
            self.tree[idx] = u_val
            return
        
        mid = (l + r) >> 1
        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_idx, u_val)

        else:
            self.update(2 * idx + 2, mid + 1, r, u_idx, u_val)

        self.tree[idx] = self.tree[2 * idx + 1] +  self.tree[2 * idx + 2]
        return
            