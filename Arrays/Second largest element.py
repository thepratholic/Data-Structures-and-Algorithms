class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        largest, secondLargest = nums[0], -1
        for i in range(n):
            if nums[i] > largest:
                secondLargest = largest
                largest = nums[i]
            elif nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]
        return secondLargest