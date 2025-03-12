class Solution:
    def helper(self, sum, last, current, k, ans):
        if sum == 0 and len(current) == k:
            ans.append(current[:])
            return

        if sum <= 0: return

        for i in range(last, 10):
            if i <= sum:
                current.append(i)
                self.helper(sum - i, i+1, current, k, ans)
                current.pop()
            
        
        
    def combinationSum3(self, k, n):
        #your code goes here

        ans = []
        self.helper(n, 1, [], k, ans)
        return ans