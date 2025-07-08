class Solution:
    def helper(self, nums, k):
        n = len(nums)
        l, r = 0, 0
        count = 0
        sum = 0
        while r < n:
            sum += (nums[r] % 2)
            while sum > k:
                sum -= (nums[l] % 2)
                l += 1
            count += (r - l + 1)
            r += 1
        return count

    def numberOfOddSubarrays(self, nums, k):
        #your code goes here
        return self.helper(nums, k) - self.helper(nums, k - 1)