class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        preSumMap = {}
        s, maxLen = 0, 0

        for i in range(n):
            s += nums[i]

            if s == k:
                maxLen = max(maxLen, i + 1)

            rem = s - k

            if rem in preSumMap:
                maxLen = max(maxLen, i - preSumMap[rem])

            if s not in preSumMap:
                preSumMap[s] = i 

        return maxLen