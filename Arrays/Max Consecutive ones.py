class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maximum_ones = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
                maximum_ones = max(maximum_ones, count)
            else:
                count = 0

        return maximum_ones
