class Solution:
    def moveZeroes(self, nums):
        j = -1
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                j = i
                break

        if j == -1: return

        for i in range(j + 1, n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums