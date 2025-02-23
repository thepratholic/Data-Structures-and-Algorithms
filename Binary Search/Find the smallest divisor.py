import math as m
class Solution:
    def helper(self, nums, mid):
        sum_val = 0
        for i in nums:
            sum_val += m.ceil(i / mid)
        return sum_val

    def smallestDivisor(self, nums, limit):
        n = len(nums)

        if n > limit: return -1

        low, high = 1, max(nums)

        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if self.helper(nums, mid) <= limit:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
