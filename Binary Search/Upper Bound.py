class Solution:
    def upperBound(self, nums, x):
        n = len(nums)
        low, high = 0, n - 1
        ans = n 

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > x:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans