class Solution:
    def numSubarraysWithSum(self, nums, goal):
        #your code goes here
        return self.helper(nums, goal) - self.helper(nums, goal - 1)


    def helper(self, nums, goal):
        if goal < 0: 
            return 0
        l, r = 0, 0
        n = len(nums)
        count = 0
        sum_val = 0
        while r < n:
            sum_val += nums[r]
            while sum_val > goal:
                sum_val -= nums[l]
                l += 1
            count += (r - l + 1)
            r += 1
        return count