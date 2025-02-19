class Solution:
    def search(self, nums, k):
        n = len(nums)

        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == k: return mid
            # left half sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= k and k <= nums[mid]:
                    high = mid - 1
                else: low = mid + 1

            # right half sorted
            else:
                if nums[mid] <= k and k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

