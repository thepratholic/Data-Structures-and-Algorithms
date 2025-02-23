class Solution:
    def f(self, a, mid):
        n = len(a)
        partitions = 1
        subarraySum = 0
        for i in range(n):
            if a[i] + subarraySum <= mid:
                subarraySum += a[i]
            else:
                partitions += 1
                subarraySum = a[i]
        return partitions

    def largestSubarraySumMinimized(self, a, k):
        ans = None 
        low, high = max(a), sum(a)

        while low <= high:
            mid = (low + high) // 2

            if self.f(a, mid) > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans