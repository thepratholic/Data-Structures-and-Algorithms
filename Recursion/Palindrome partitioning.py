class Solution:
    def check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def helper(self, i, curr, ans, n, s):
        if i == n:
            ans.append(curr[:])
            return

        for j in range(i, n):
            if self.check(s, i, j):
                curr.append(s[i:j+1])
                self.helper(j+1, curr, ans, n, s)
                curr.pop()
                
    def partition(self, s: str):
        #your code goes here
        ans = []
        self.helper(0, [], ans, len(s), s)
        return ans
