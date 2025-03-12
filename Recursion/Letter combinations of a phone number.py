class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno","pqrs", "tuv", "wxyz"]

    def helper(self, i, digits, ans, n, current):
        if i == n:
            ans.append(current)
            return

        s = self.map[int(digits[i])]

        for char in s:
            self.helper(i+1, digits, ans, n, current + char)
        


    def letterCombinations(self, digits):
        #your code goes here
        ans = []
        if not digits:
            return ans

        self.helper(0, digits, ans, len(digits), "")
        return ans