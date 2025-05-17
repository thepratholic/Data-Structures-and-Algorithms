class Solution:
    def canJump(self, nums):
        #your code goes here
        max_jump = 0
        n = len(nums)

        for i in range(n):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])

        return True