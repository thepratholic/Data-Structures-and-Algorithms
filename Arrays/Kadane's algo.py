class Solution:
    def maxSubArray(self, nums):
        maxi, current = float("-inf"), 0
        n = len(nums)
        for i in range(n):
            current += nums[i]
            maxi = max(maxi, current)
            if current < 0:
                current = 0


        return maxi