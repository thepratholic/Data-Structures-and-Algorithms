class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)

        S = 0
        SN = (n * (n + 1)) // 2
        S2 = 0
        S2N = (n * (n + 1) * (2 * n + 1)) // 6
        
        for num in nums:
            S += num
            S2 += num * num

        val1 = S - SN
        val2 = S2 - S2N

        val2 = val2 // val1

        x = (val1 + val2) // 2
        y = val2 - x 

        return [int(x), int(y)]