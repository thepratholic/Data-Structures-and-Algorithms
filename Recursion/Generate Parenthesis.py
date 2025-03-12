class Solution:
    def generate(self, open_count, close_count, ans, n, current):
        if open_count == close_count == n:
            ans.append(current)
            return 

        if open_count < n:
            self.generate(open_count + 1, close_count, ans, n, current + "(")

        if close_count < open_count:
            self.generate(open_count, close_count+1, ans, n, current+")")
            
    def generateParenthesis(self, n):
        ans = []
        self.generate(0, 0, ans, n, "")
        return ans