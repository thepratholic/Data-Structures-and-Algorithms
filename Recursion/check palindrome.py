class Solution:
    def rev(self, s, start, end):
        if start >= end: return True
        if s[start] != s[end]: return False
        return self.rev(s, start+1, end-1)
    

    def isPalin(self,n):
        #code here
        str_n = str(n)
        return self.rev(str_n, 0, len(str_n)-1)
    

s = Solution()
print(s.isPalin(100))