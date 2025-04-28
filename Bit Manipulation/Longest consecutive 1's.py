class Solution:
    ##Complete this function

    def maxConsecutiveOnes(self, n):
        ##Your code here
        maxi, curr = 0, 0
        while n > 0:
            n = n & (n << 1)
            curr += 1
            maxi = max(curr, maxi)
        return maxi