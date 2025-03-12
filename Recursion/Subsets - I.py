class Solution:
    def helper(self, i, sum, ans, nums, n):
        if i == n:
            ans.append(sum)
            return

        self.helper(i+1, sum + nums[i], ans, nums, n)
        self.helper(i+1, sum, ans, nums, n)

    def subsetSums(self, nums):
        #your code goes here
        ans = []
        self.helper(0, 0, ans, nums, len(nums))
        return ans