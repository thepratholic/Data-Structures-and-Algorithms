class Solution:
    def recursiveSum(self,n):
        #code here
        if n <= 0:
            return 0
        return self.recursiveSum(n-1) + n