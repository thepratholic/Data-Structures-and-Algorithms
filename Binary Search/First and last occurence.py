class Solution:
    def firstOccurrence(self, nums, n, x):
        first = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == x:
                first = mid
                high = mid - 1

            elif nums[mid] < x:
                low = mid + 1
            else: high = mid - 1
        return first

    def lastOccurrence(self, nums, n, x):
        last = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == x:
                last = mid
                low = mid + 1
            elif nums[mid] < x:
                low = mid + 1
            else: high = mid - 1
        return last

    def searchRange(self, nums, target):
        n = len(nums)
        first = self.firstOccurrence(nums, n, target)
        if first == -1: 
            return [-1, -1]
        last = self.lastOccurrence(nums, n, target)
        return [first, last]