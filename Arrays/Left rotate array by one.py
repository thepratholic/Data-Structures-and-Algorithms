class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        temp = nums[0]
        for i in range(n-1):
            nums[i] = nums[i+1]

        nums[n - 1] = temp
        return nums