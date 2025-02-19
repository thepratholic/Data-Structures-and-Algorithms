class Solution:
    def findCeil(self, nums, x):
        n = len(nums)
        ans = n 
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                ans = nums[mid]
                high = mid - 1
            else: low = mid + 1

        return ans

    def findFloor(self, nums, x):
        ans = -1 
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= x:
                ans = nums[mid]
                low = mid + 1
            else:
                high = mid - 1

        return ans

    def getFloorAndCeil(self, nums, x):
       floor = self.findFloor(nums, x)
       ceil = self.findCeil(nums, x)

       return [floor, ceil]
