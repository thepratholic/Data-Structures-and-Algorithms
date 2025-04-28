class Solution:
    def kthBit(self, n, k):
        if n & (1 << (k)):
            return True
        else: return False

s = Solution()
print(s.kthBit(4, 2))