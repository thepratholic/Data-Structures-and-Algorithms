class Solution:    
    def myPow(self, x, n):
        #your code goes here

        if n == 0: 
            return 1

        if n < 0:
            x = 1/x
            n = -n
        
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x * x, n//2)