from typing import List


class NumArray:


    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segment_tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, nums)

    def build(self, i, l, r, nums):
        if l == r:
            self.segment_tree[i] = nums[l]
            return

        mid = (l + r) >> 1
        self.build(2 * i + 1, l, mid, nums)
        self.build(2 * i + 2, mid + 1, r, nums)
        self.segment_tree[i] = self.segment_tree[2 * i + 1] + self.segment_tree[2 * i + 2]

    def updatePoint(self, index, val, i, l, r):
        if l == r:
            self.segment_tree[i] = val
            return

        mid = (l + r) >> 1
        if index <= mid:
            self.updatePoint(index, val, 2 * i + 1, l, mid)

        else:
            self.updatePoint(index, val, 2 * i + 2, mid + 1, r)

        self.segment_tree[i] = self.segment_tree[2 * i + 1] + self.segment_tree[2 * i + 2]

    def query(self, start_range, end_range, i, l, r):
        if l > end_range or r < start_range:
            return 0

        elif l >= start_range and r <= end_range:
            return self.segment_tree[i]

        else:
            mid = (l + r) >> 1
            return self.query(start_range, end_range, 2 * i + 1, l, mid) + self.query(start_range, end_range, 2 * i + 2, mid + 1, r)

    def update(self, index: int, val: int) -> None:
        self.updatePoint(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(left, right, 0, 0, self.n - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)