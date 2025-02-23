import math as m

class Solution:
    def helper(self, nums, mid):
        total_hours = 0
        for i in range(len(nums)):
            total_hours += m.ceil(nums[i] / mid)

        return total_hours

    def minimumRateToEatBananas(self, nums, h):
        result, low, high = float("inf"), 1, max(nums)

        while low <= high:
            mid = (low + high) // 2

            if self.helper(nums, mid) <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result