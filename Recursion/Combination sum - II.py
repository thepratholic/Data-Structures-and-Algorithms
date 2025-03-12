class Solution:
    def helper(self, i, nums, sum, ans, current, n):
        if sum == 0:
            ans.append(current[:])
            return

        if sum < 0 or i == n: return

        current.append(nums[i])
        self.helper(i+1, nums, sum - nums[i], ans, current, n)
        current.pop()

        for j in range(i+1, len(nums)):
            if nums[j] != nums[i]:
                self.helper(j, nums, sum, ans, current, n)
                break


    def combinationSum2(self, candidates, target):
        #your code goes here
        candidates.sort()
        ans = []
        self.helper(0, candidates, target, ans, [], len(candidates))
        return ans