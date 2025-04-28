class Solution:   
    def singleNumber(self, nums):
        #your code goes here

        xorr = 0
        for i in nums:
            xorr ^= i 

        rightmost = (xorr & xorr-1) ^ xorr
        b1, b2 = 0, 0

        for k in nums:
            if k & rightmost:
                b1 ^= k

            else:
                b2 ^= k 
        return [b1, b2] if b1 < b2 else [b2, b1]