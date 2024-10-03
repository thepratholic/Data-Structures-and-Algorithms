class Solution:
    def sumOfDigits(self, n):
        # code here

        if n == 0: return 0
        else:
            return self.sumOfDigits(n//10) + (n % 10)