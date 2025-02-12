class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def rotateArray(self, nums, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        self.reverse(nums, 0, n - 1)
        return nums