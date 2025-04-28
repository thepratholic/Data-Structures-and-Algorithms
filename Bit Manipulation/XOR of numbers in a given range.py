class Solution:   
    def helper(self, n):
        if n%4 == 1: return 1
        if n%4 == 2: return n+1
        if n%4 == 3: return 0
        if n%4 == 0: return n 
       
    def findRangeXOR(self, l, r):
        #your code goes here
        return self.helper(l-1) ^ self.helper(r)