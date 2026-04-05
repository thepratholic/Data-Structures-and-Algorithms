from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[0] * 6 for _ in range(4 * self.n)]
        self.build(0, 0, self.n - 1, arr)

    def get_depth(self, x):
        d = 0
        while x > 1:
            d += 1
            x = bin(x).count('1')
        return d

    def build(self, idx, l, r, arr):
        if l == r:
            d = self.get_depth(arr[l])
            self.tree[idx][d] = 1
            return

        mid = (l + r) >> 1
        self.build(2 * idx + 1, l, mid, arr)
        self.build(2 * idx + 2, mid + 1, r, arr)

        for j in range(6):
            self.tree[idx][j] = self.tree[2 * idx + 1][j] + self.tree[2 * idx + 2][j]


    def query(self, idx, l, r, start, end, k):
        if r < start or end < l:
            return 0

        if l >= start and r <= end:
            return self.tree[idx][k]

        mid = (l + r) >> 1
        return self.query(2 * idx + 1, l, mid, start, end, k) + self.query(2 * idx + 2, mid + 1, r, start, end, k)
        
    def update(self, idx, l, r, update_val, update_idx):
        if l == r:
            self.tree[idx] = [0] * 6
            update_val_depth = self.get_depth(update_val)
            self.tree[idx][update_val_depth] = 1
            return

        mid = (l + r) >> 1
        if update_idx <= mid:
            self.update(2 * idx + 1, l, mid, update_val, update_idx)

        else:
            self.update(2 * idx + 2, mid + 1, r, update_val, update_idx)

        for j in range(6):
            self.tree[idx][j] = self.tree[2 * idx + 1][j] + self.tree[2 * idx + 2][j]

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        res = []
        seg = SegmentTree(nums)

        for q in queries:
            if q[0] == 1:
                l, r, k = q[1], q[2], q[3]
                res.append(seg.query(0, 0, seg.n - 1, l, r, k))
            else:
                idx, val = q[1], q[2]
                seg.update(0, 0, seg.n - 1, val, idx)
                
        return res