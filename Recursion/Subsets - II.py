class Solution:
    def helper(self, i, nums, current, ans, n):
        if i == n:
            ans.append(current[:])
            return 

        current.append(nums[i])
        self.helper(i+1, nums, current, ans, n)
        current.pop()

        for j in range(i+1, n):
            if nums[j] != nums[i]:
                self.helper(j, nums, current, ans, n)
                return

        self.helper(n, nums, current, ans, n)


    def subsetsWithDup(self, nums):
        #your code goes here
        nums.sort()
        ans = []
        self.helper(0, nums, [], ans, len(nums))
        return ans