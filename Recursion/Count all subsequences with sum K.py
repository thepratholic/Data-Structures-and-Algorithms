class Solution:
    def helper(self, i, nums, k, n):
        if k == 0: return 1
        if k < 0 or i == n: return 0

        path1 = self.helper(i+1, nums, k - nums[i], n)
        path2 = self.helper(i+1, nums, k, n)

        return path1 + path2
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here

        n = len(nums)
        return self.helper(0, nums, k, n)