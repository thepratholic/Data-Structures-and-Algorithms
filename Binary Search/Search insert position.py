class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)

        ans = n 
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans