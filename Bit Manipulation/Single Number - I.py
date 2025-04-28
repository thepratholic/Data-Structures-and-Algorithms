class Solution:
    def singleNumber(self, nums):
        #your code goes here
        xor = 0

        for i in nums:
            xor ^= i 

        return xor