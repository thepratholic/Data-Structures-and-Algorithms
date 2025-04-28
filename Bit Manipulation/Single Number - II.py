class Solution:
    def singleNumber(self, nums):
        #your code goes here
        ones, twos = 0, 0
        n = len(nums)

        for i in range(n):

            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones