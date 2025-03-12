class Solution:
    def Backtrack(self, i, nums, sum, ans, current, n):
        if sum == 0:
            ans.append(current[:])
            return 

        if sum < 0 or i == n: return

        self.Backtrack(i+1, nums, sum, ans, current, n)

        current.append(nums[i])
        self.Backtrack(i, nums, sum - nums[i], ans, current, n)
        current.pop()

    def combinationSum(self, candidates, target):
        ans = []
        self.Backtrack(0, candidates, target, ans, [], len(candidates))
        return ans