class Solution:
    def f(self, nums, pages):
        countStudents = 1
        PagesOfStudent = 0
        for i in range(len(nums)):
            if nums[i] + PagesOfStudent <= pages:
                PagesOfStudent += nums[i]
            else:
                countStudents += 1
                PagesOfStudent = nums[i]
        return countStudents

    def findPages(self, nums, m):
        n = len(nums)
        if n < m: return -1
        ans = None
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) // 2
            
            if self.f(nums, mid) > m:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
        