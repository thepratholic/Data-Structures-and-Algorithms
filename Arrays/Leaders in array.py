class Solution:
    def leaders(self, nums):
        ans = []
        n = len(nums)
        maxi = float("-inf")

        for i in range(n-1, -1, -1):
            if nums[i] > maxi:
                ans.append(nums[i])
                maxi = max(maxi, nums[i])

        ans.reverse()
        return ans
        