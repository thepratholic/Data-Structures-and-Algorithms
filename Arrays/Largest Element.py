class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]

        return largest