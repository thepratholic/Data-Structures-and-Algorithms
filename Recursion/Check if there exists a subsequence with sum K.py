class Solution:
    def helper(self, index, nums, k, n):
        if k < 0: return False
        if k == 0: return True
        if index == n: return k == 0

        path1 = self.helper(index + 1, nums, k - nums[index], n)
        path2 = self.helper(index + 1, nums, k, n)

        return path1 or path2

    def checkSubsequenceSum(self, nums, k):
        #your code goes here
        n = len(nums)
        return self.helper(0, nums, k, n)