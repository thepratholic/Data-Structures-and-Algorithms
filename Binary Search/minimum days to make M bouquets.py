class Solution:
    def possible(self, nums, mid, k, m):
        count = 0
        noOfB = 0
        for i in range(len(nums)):
            if nums[i] <= mid:
                count += 1
            else:
                noOfB += (count // k)
                count = 0
        noOfB += (count // k)
        return noOfB >= m

    def roseGarden(self, n, nums, k, m):
        ans = -1
        low, high = min(nums), max(nums)

        if n < (m * k): return -1

        while low <= high:
            mid = (low + high) // 2

            if self.possible(nums, mid, k, m):
                ans = mid 
                high = mid - 1

            else:
                low = mid + 1

        return ans