class Solution:
    def RecursivePower(self,n,p):
        '''
        return value of n^p recursively;
        '''
        # code here

        if n==0: return 1
        if p % 2 == 0:
            half_pow = pow(n, p//2)
            return half_pow * half_pow
        else:
            return n * self.RecursivePower(n, p-1)