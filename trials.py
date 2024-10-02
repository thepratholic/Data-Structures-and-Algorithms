
class Solution:
    cnt = 0
    def f(self):
        if self.cnt == 3: return 
        print(self.cnt)
        self.cnt+=1
        self.f()


s = Solution()
print(s.f())