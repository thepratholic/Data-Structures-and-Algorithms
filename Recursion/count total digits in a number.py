class Solution:

    def countDigits(self, n):
        # code here
        if n == 0: return 0
        return self.countDigits(n//10) + 1