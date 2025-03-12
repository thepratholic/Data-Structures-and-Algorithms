class Solution:
    def backtrack(self, index, nums, n, current, ans):
        if index == n:
            ans.append(current[:])
            return

        self.backtrack(index + 1, nums, n, current, ans)

        current.append(nums[index])
        self.backtrack(index + 1, nums, n, current, ans)
        current.pop()

    def powerSet(self, nums):
        #your code goes here
        n = len(nums)
        ans = []
        current = []

        self.backtrack(0, nums, n, current, ans)
        return ans